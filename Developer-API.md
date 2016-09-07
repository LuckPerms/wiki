## Intro
I spent an huge amount of time and effort making LuckPerms great for developers.

Most other permissions plugins either don't have APIs, have bad APIs, or have APIs with poor documentation and methods and classes that disappear or move randomly between versions. The Vault project is a great interface and  a great way to integrate with lots of plugins at once, but it's functionality is limited.

The LuckPerms API allows you to change a huge amount of the plugins internals programmatically, and easily integrate LuckPerms deeply into your existing plugins and systems. There is a massive amount of documentation you can read if you're unsure about what something does.

LuckPerms follows Semantic Versioning, meaning whenever a non-backwards compatible API change is made, the major version will increment. You can rest assured knowing your integration will not break between versions, providing the major version remains the same.

The vast majority of operations in LuckPerms run asynchronously in separate threads. This shouldn't affect API users significantly, as the internals of LuckPerms are thread safe. However, take great care to not perform blocking operations in Callbacks (these are called in the server thread), and not call synchronous datastore methods on the main server thread (Your server will lag).

## Useful Links
* **Maven Repository** - <https://nexus.lucko.me/>
* **CI Server** - <https://ci.lucko.me/job/LuckPerms/>
* **JavaDocs** - <https://jd.lucko.me/LuckPerms/> (I spent a lot of time on these, please make sure you read them <3)
* **API Source Code** - <https://github.com/lucko/LuckPerms/tree/master/api> (Can be really useful if you don't like reading JavaDocs online.)

## Usage Instructions
To use the API, you need to obtain an instance of the `LuckPermsApi` interface. This can be done in a number of ways.

```java
// On all platforms (throws IllegalStateException if the API is not loaded)
final LuckPermsApi api = LuckPerms.getApi();

// Or with Optional
Optional<LuckPermsApi> provider = LuckPerms.getApiSafe();
if (provider.isPresent()) {
    final LuckPermsApi api = provider.get();
}

// On Bukkit/Spigot
ServicesManager manager = Bukkit.getServicesManager();
if (manager.isProvidedFor(LuckPermsApi.class)) {
    final LuckPermsApi api = manager.getRegistration(LuckPermsApi.class).getProvider();
}

// On Sponge
Optional<LuckPermsApi> provider = Sponge.getServiceManager().provide(LuckPermsApi.class);
if (provider.isPresent()) {
    final LuckPermsApi api = provider.get();
}
```

If you want to use LuckPerms in your onEnable method, you need to add the following to your plugins `plugin.yml`.
```yml
depend: [LuckPerms]
```

You can add LuckPerms as a Maven dependency by adding the following to your projects `pom.xml`.
````xml
<repositories>
    <repository>
        <id>luck-repo</id>
        <url>https://repo.lucko.me/</url>
    </repository>
</repositories>

<dependencies>
    <dependency>
        <groupId>me.lucko.luckperms</groupId>
        <artifactId>luckperms-api</artifactId>
        <version>2.8</version>
    </dependency>
</dependencies>
````

### Events
LuckPerms exposes a full read/write API, as well as an event listening system. Due to the multi-platform nature of the project, an internal Event system is used, as opposed to the systems already in place on each platform. (the Bukkit Event API, for example). This means that simply registering your listener with the platform will not work.

All events are **fired asynchronously**. This means you should not interact with or call any non-thread safe methods from within listeners. (Any part of the Bukkit API, for example, use the scheduler if you need access)

To listen to an event, you need to first make a class that implements `LPListener`. Then within this class, you can define all of your listener methods.

Each listener method must be annotated with `@Subscribe`. For example...

```java
package me.lucko.test;

import com.google.common.eventbus.Subscribe;
import me.lucko.luckperms.api.event.LPListener;
import me.lucko.luckperms.api.event.events.PermissionSetEvent;

public class TestListener implements LPListener {

    @Subscribe
    public void onPermissionSet(PermissionSetEvent event) {

    }

}
```

You also need to register your new Listener with the API.
```java
@Override
public void onEnable() {
    LuckPermsApi api; // Get the API. (See above)
    api.registerListener(new TestListener());
}
```

## Versioning
As of version 2.0, LuckPerms roughly follows the standards set out in Semantic Versioning.

The only difference is that the patch number is not included anywhere within the pom, and is calculated each build, based upon how may commits have been made since the last tag. (A new tag is made every minor version)

This means that API versions do not have a patch number (as no API changes are made in patches). API versions will be x.y, and each individual build of LuckPerms will follow x.y.z.
