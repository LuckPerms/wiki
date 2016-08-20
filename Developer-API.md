LuckPerms has an extensive API, allowing for easy integration with other projects. To use the API, you need to obtain an instance of the `LuckPermsApi` interface. This can be done in a number of ways.

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
All of the available methods can be seen in the various interfaces in the `luckperms-api` module.

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
        <version>2.5</version>
    </dependency>
</dependencies>
````

### Events
LuckPerms exposes a full read/write API, as well as an event listening system. Due to the multi-platform nature of the project, an internal Event system is used, as opposed to the systems already in place on each platform. (the Bukkit Event api, for example). This means that simply registering your listener with the platform is not sufficient.

All events are **fired asynchronously**. This means you should not interact with or call any non-thread safe methods from within listeners.

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
    LuckPermsApi api;
    api.registerListener(new TestListener());
}
```

## Versioning
As of version 2.0, LuckPerms roughly follows the standards set out in Semantic Versioning.

The only difference is that the patch number is not included anywhere within the pom, and is calculated each build, based upon how may commits have been made since the last tag. (A new tag is made every minor version)

This means that API versions do not have a patch number (as no API changes are made in patches). API versions will be x.y, and each individual build of LuckPerms will follow x.y.z.
