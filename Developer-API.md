## Intro
The LuckPerms API allows you to change a huge amount of the plugins internals programmatically, and easily integrate LuckPerms deeply into your existing plugins and systems.

Most other permissions plugins either don't have APIs, have bad APIs, or have APIs with poor documentation and methods and classes that disappear or move randomly between versions. The Vault project is a great interface and a great way to integrate with lots of plugins at once, but its functionality is very limited.

LuckPerms follows Semantic Versioning, meaning whenever a non-backwards compatible API change is made, the major version will increment. You can rest assured knowing your integration will not break between versions, providing the major version remains the same.

## How to use the API in your project
The API package in LuckPerms is [`me.lucko.luckperms.api`](https://github.com/lucko/LuckPerms/tree/master/api/src/main/java/me/lucko/luckperms).

My Nexus Server can be found at [https://nexus.lucko.me/](https://nexus.lucko.me/). The repository you need for your build scripts is [https://repo.lucko.me/](https://repo.lucko.me/).

#### Other useful links
* [JavaDocs](https://jd.lucko.me/LuckPerms/)
* [CI Server](https://ci.lucko.me/job/LuckPerms/)

### Maven
````xml
<repositories>
    <repository>
        <id>luck-repo</id>
        <url>http://repo.lucko.me/</url>
    </repository>
</repositories>

<dependencies>
    <dependency>
        <groupId>me.lucko.luckperms</groupId>
        <artifactId>luckperms-api</artifactId>
        <version>2.17</version>
        <scope>provided</scope>
    </dependency>
</dependencies>
````

### Gradle
```gradle
repositories {
    maven {
        name "luck-repo"
        url "http://repo.lucko.me/"
    }
}

dependencies {
    compile ("me.lucko.luckperms:luckperms-api:2.17")
}
```

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

### A warning about thread safety
All LuckPerms internals are thread-safe, including the API. You can call API methods from async threads without incurring issues.

However, please be aware that some operations, (especially in the Storage class) are blocking. [CompletableFuture](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/CompletableFuture.html)s are used in these situations to prevent accidental issues, where the main server thread waits for I/O to execute. Care should be taken to specify the correct executor when adding callbacks to these futures.

### I want to depend on LuckPerms
On Bukkit/Bungee, you need to add the following to your plugins `plugin.yml`.
```yml
depend: [LuckPerms]
```

On Sponge, add the following to your plugins declaration.
```java
@Plugin(
        id = "myplugin",
        dependencies = {
                @Dependency(id = "luckperms")
        }
)
public class MyPlugin {
    ...
}
```

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

## Group Lookups
If you just want to find out which group a player is in, I **highly** recommend the following method.

```java
public static String getPlayerGroup(Player player, List<String> possibleGroups) {
    for (String group : possibleGroups) {
        if (player.hasPermission("group." + group)) {
            return group;
        }
    }
    return null;
}
```
Remember to order your group list in order of priority. e.g. Owner first, member last. 