## Intro
The LuckPerms API allows you to change a huge amount of the plugins internals programmatically, and easily integrate LuckPerms deeply into your existing plugins and systems.

Most other permissions plugins either don't have APIs, have bad APIs, or have APIs with poor documentation and methods and classes that disappear or move randomly between versions. The Vault project is a great interface and a great way to integrate with lots of plugins at once, but its functionality is very limited.

LuckPerms follows Semantic Versioning, meaning whenever a non-backwards compatible API change is made, the major version will increment. You can rest assured knowing your integration will not break between versions, providing the major version remains the same.

## How to use the API in your project
The API package in LuckPerms is [`me.lucko.luckperms.api`](https://github.com/lucko/LuckPerms/tree/master/api/src/main/java/me/lucko/luckperms).

My Nexus Server can be found at [https://nexus.lucko.me/](https://nexus.lucko.me/). The repository you need for your build scripts is [https://repo.lucko.me/](https://repo.lucko.me/).

#### Other useful links
* [JavaDocs](https://luckperms.lucko.me/javadocs/)
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
        <version>3.1</version>
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
    compile ("me.lucko.luckperms:luckperms-api:3.1")
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

However, please be aware that some operations, (especially in the Storage class) are blocking. [CompletableFuture](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/CompletableFuture.html)s are used in these situations to prevent accidental issues whereby through poor handling, the main server thread waits for I/O to execute. Care should be taken to specify the correct executor when adding callbacks to these futures.

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

All events are **fired asynchronously**. This means you should not interact with or call any non-thread safe method from within listeners.

It is important to note that most of Bukkit/Sponge are **not** thread safe, and should only be interacted with using the main server thread. You should use the scheduler if you need to access these methods fron LuckPerms listeners.

### How do I listen to an event
All event interfaces can be found in the [`me.lucko.luckperms.api.event`](https://github.com/lucko/LuckPerms/tree/master/api/src/main/java/me/lucko/luckperms/api/event) package. They all extend [`LuckPermsEvent`](https://github.com/lucko/LuckPerms/blob/master/api/src/main/java/me/lucko/luckperms/api/event/LuckPermsEvent.java).

To listen to events, you need to obtain the [`EventBus`](https://github.com/lucko/LuckPerms/blob/master/api/src/main/java/me/lucko/luckperms/api/event/EventBus.java) instance, using [`LuckPermsApi#getEventBus`](https://github.com/lucko/LuckPerms/blob/master/api/src/main/java/me/lucko/luckperms/api/LuckPermsApi.java#L68).

It's usually a good idea to create a separate class for your listeners. Here's a short example class you can reference.

```java
package me.lucko.test;

import me.lucko.luckperms.api.event.EventBus;
import me.lucko.luckperms.api.event.log.LogPublishEvent;
import me.lucko.luckperms.api.event.user.UserLoadEvent;
import me.lucko.luckperms.api.event.user.track.UserPromoteEvent;

public class TestListener {
    private final MyPlugin plugin;

    public TestListener(MyPlugin plugin, LuckPermsApi api) {
        this.plugin = plugin;

        EventBus eventBus = api.getEventBus();

        // use a lambda
        eventBus.subscribe(LogPublishEvent.class, e -> e.getCancellationState().set(true));
        eventBus.subscribe(UserLoadEvent.class, e -> {
            System.out.println("User " + e.getUser().getName() + " was loaded!");
            if (e.getUser().hasPermission("some.perm", true)) {
                // Do something
            }
        });

        // use a method reference
        eventBus.subscribe(UserPromoteEvent.class, this::onUserPromote);
    }

    private void onUserPromote(UserPromoteEvent event) {
        Bukkit.getScheduler().runTask(plugin, () -> {
            Bukkit.broadcastMessage(event.getUser().getName() + " was promoted to" + event.getGroupTo().get() + "!");

            Player player = Bukkit.getPlayer(event.getUser().getUuid());
            if (player != null) {
                player.sendMessage("Congrats!");
            }
        });
    }

}
```

[`EventBus#subscribe`](https://github.com/lucko/LuckPerms/blob/master/api/src/main/java/me/lucko/luckperms/api/event/EventBus.java#L43) returns an [`EventHander`](https://github.com/lucko/LuckPerms/blob/master/api/src/main/java/me/lucko/luckperms/api/event/EventHandler.java) instance, which can be used to unregister the listener when your plugin disables.

## Example Usage
Below are some short examples which illustrate some basic API functions.

### Finding a players group
If you just want to find out which group a player is in, I **highly** recommend the following method. (you don't even need to use the API!)

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

### Adding a permission to a user
```java
LuckPermsApi api = null; // See above for how to get the API instance.

Optional<User> user = api.getUserSafe(uuid);
if (!user.isPresent()) {
    return false; // The user isn't loaded in memory.
}

// Build the permission node we want to set
Node node = api.getNodeFactory().newBuilder(permission).setValue(true).build();

// Set the permission, and return true if the user didn't already have it set.
try {
    user.get().setPermission(node);

    // Now we need to save the user back to the storage
    api.getStorage().saveUser(u);

    return true;
} catch (ObjectAlreadyHasException e) {
    return false;
}
```

### Adding a permission to a (potentially) offline user
The CompletionStage API can be used to easily interact with the plugins Storage backing. See [here](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/CompletionStage.html) and [here](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/CompletableFuture.html) for more details about these classes.

```java
LuckPermsApi api = null; // See above for how to get the API instance.

// load the user in from storage. we can specify "null" for their username,
// since it's unknown to us.
api.getStorage().loadUser(uuid, "null").thenComposeAsync(success -> {
    // loading the user failed, return straight away
    if (!success) {
        return CompletableFuture.completedFuture(false);
    }
    
    // get the user instance, they're now loaded in memory.
    User user = api.getUser(uuid);

    // Build the permission node we want to set
    Node node = api.getNodeFactory().newBuilder(permission).setValue(true).build();

    // Set the permission, and return true if the user didn't already have it set.
    try {
        user.setPermission(node);
        
        // not we've set the permission, but still need to save the user data
        // back to the storage.
        
        // first save the user
        return api.getStorage().saveUser(user)
                .thenCompose(b -> {
                    // then cleanup their user instance so we don't create
                    // a memory leak.
                    api.cleanupUser(user);
                    return CompletableFuture.completedFuture(b);
                });
        
    } catch (ObjectAlreadyHasException e) {
        return CompletableFuture.completedFuture(false);
    }
    
}, api.getStorage().getAsyncExecutor());
```

### Getting a players prefix
LuckPerms has a (somewhat complex) caching system which is used for super fast permission / meta lookups. These classes are exposed in the API, and should be used where possible.

```java
LuckPermsApi api = null; // See above for how to get the API instance.

// Get the user, or null if they're not loaded.
User user = api.getUserSafe(uuid).orElse(null);
if (user == null) {
    return Optional.empty(); // The user isn't loaded. :(
}

// Now get their UserData. This is only loaded for online players.
UserData userData = user.getUserDataCache().orElse(null);
if (userData == null) {
    return Optional.empty(); // Nope! Not loaded.
}

// Now get the users "Contexts". This is basically just data about the players current state.
// Don't worry about it too much, just know we need it to get their cached data.
Contexts contexts = api.getContextForUser(user).orElse(null);
if (contexts == null) {
    return Optional.empty();
}

// Ah, now we're making progress. We can use the Contexts to get the users "MetaData". This is their cached meta data.
MetaData metaData = userData.getMetaData(contexts);

// Now return an optional of their prefix, if they have one.
// MetaData#getPrefix returns null if they have no prefix, so we wrap the return in Optional#ofNullable to catch this.
return Optional.ofNullable(metaData.getPrefix());
```

### Getting a players applied permissions
We can also use this caching system to get a Map containing the users permissions. This map contains the data which backs their permission lookups.
```java
// All retrieved in the same way as shown above.
User user;
UserData userData;
Contexts contexts;

PermissionData permissionData = userData.getPermissionData(contexts);

Map<String, Boolean> data = permissionData.getImmutableBacking();
```

### Searching for a permission
You can use Java 8 streams to easily filter and return permissions applied to a user.
```java
public boolean hasPermissionStartingWith(UUID uuid, String startingWith) {
    // Get the user, if they're online.
    Optional<User> user = api.getUserSafe(uuid);

    // If they're online, perform the check, otherwise, return false.
    return user.map(u -> u.getPermissions().stream()
            .filter(Node::getValue)
            .filter(Node::isPermanent)
            .filter(n -> !n.isServerSpecific())
            .filter(n -> !n.isWorldSpecific())
            .anyMatch(n -> n.getPermission().startsWith(startingWith))
    ).orElse(false);
}
```

### Creating a new group and assigning a permission
This method is not blocking, so can be safely called on the main server thread. The callback will be ran async too, once the operation has finished.
```java
api.getStorage().createAndLoadGroup("my-new-group").thenAcceptAsync(success -> {
    if (!success) {
        return;
    }

    Group group = api.getGroup("my-new-group");
    if (group == null) {
        return;
    }

    Node permission = api.buildNode("test.permission").build();

    try {
        group.setPermission(permission);
    } catch (ObjectAlreadyHasException ignored) {}

    // Now save the group back to storage
    api.getStorage().saveGroup(group);
}, api.getStorage().getAsyncExecutor());
```

## Versioning
As of version 2.0, LuckPerms roughly follows the standards set out in Semantic Versioning.

The only difference is that the patch number is not included anywhere within the pom, and is calculated each build, based upon how may commits have been made since the last tag. (A new tag is made every minor version)

This means that API versions do not have a patch number (as no API changes are made in patches). API versions will be x.y, and each individual build of LuckPerms will follow x.y.z.

### Changelog
* Version 2.x remained stable for a number of months, without any backwards incompatible changes. However, a number of methods became deprecated in the later versions, and the event API really needed a rewrite.
* Version 3.x introduced the following backwards incompatible changes. https://gist.github.com/lucko/fdf6ae4b2d9e466d8103dd9c68e5db9e