This page shows some sample usages of the LuckPerms API, which is introduced [here](https://github.com/lucko/LuckPerms/wiki/Developer-API).

___

### Index

* [Checking if a player is in a group](#checking-if-a-player-is-in-a-group)
* [Finding a players group](#finding-a-players-group)
* [Listening to LuckPerms events](#listening-to-luckperms-events)
* [Obtaining a User instance](#obtaining-a-user-instance)
* [Obtaining a Group/Track instance](#obtaining-a-grouptrack-instance)
* [Adding a permission/parent/prefix/suffix/metadata to a user/group](#adding-a-permissionparentprefixsuffixmetadata-to-a-usergroup)
* [Using UserData](#using-userdata)
* [Searching for a permission](#searching-for-a-permission)

___

### Checking if a player is in a group
Checking for group membership can be done directly via hasPermission checks.

```java
public static boolean isPlayerInGroup(Player player, String group) {
    return player.hasPermission("group." + group);
}
```

However, remember that anyone with server operator status or `*` permissions will also have these permissions.

___

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

___

### Listening to LuckPerms events
All event interfaces can be found in the [`me.lucko.luckperms.api.event`](https://github.com/lucko/LuckPerms/tree/master/api/src/main/java/me/lucko/luckperms/api/event) package. They all extend [`LuckPermsEvent`](https://github.com/lucko/LuckPerms/blob/master/api/src/main/java/me/lucko/luckperms/api/event/LuckPermsEvent.java).

To listen to events, you need to obtain the [`EventBus`](https://github.com/lucko/LuckPerms/blob/master/api/src/main/java/me/lucko/luckperms/api/event/EventBus.java) instance, using `LuckPermsApi#getEventBus`.

It's usually a good idea to create a separate class for your listeners. Here's a short example class you can reference.

```java
import me.lucko.luckperms.api.event.EventBus;
import me.lucko.luckperms.api.event.log.LogPublishEvent;
import me.lucko.luckperms.api.event.user.UserLoadEvent;
import me.lucko.luckperms.api.event.user.track.UserPromoteEvent;

public class TestListener {
    private final MyPlugin plugin;

    public TestListener(MyPlugin plugin, LuckPermsApi api) {
        this.plugin = plugin;

        // get the LuckPerms event bus
        EventBus eventBus = api.getEventBus();

        // subscribe to an event using a lambda
        eventBus.subscribe(LogPublishEvent.class, e -> e.getCancellationState().set(true));

        eventBus.subscribe(UserLoadEvent.class, e -> {
            System.out.println("User " + e.getUser().getName() + " was loaded!");
            if (e.getUser().hasPermission("some.perm", true)) {
                // Do something
            }
        });

        // subscribe to an event using a method reference
        eventBus.subscribe(UserPromoteEvent.class, this::onUserPromote);
    }

    private void onUserPromote(UserPromoteEvent event) {
        // as we want to access the Bukkit API, we need to use the scheduler to jump back onto the main thread.
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

`EventBus#subscribe` returns an [`EventHandler`](https://github.com/lucko/LuckPerms/blob/master/api/src/main/java/me/lucko/luckperms/api/event/EventHandler.java) instance, which can be used to unregister the listener when your plugin disables.

___

### Obtaining a User instance
A `User` in LuckPerms is simply an object which represents a player on the server, and their associated permission data. In order to conserve memory usage, LuckPerms will only load User data when it absolutely needs to. 

Meaning:
* **Online players** are guaranteed to have an associated User object loaded in memory.
* **Offline players** MAY have an associated User object loaded, but they most likely will not.

This makes getting a User instance a little complicated, depending on if the Player is online or not.

If you need to interact with the `User` on the main thread, then you need to be sure that the player is online.

```java
UUID playerUuid = ....?
User user = api.getUser(playerUuid);
if (user == null) {
    // user isn't already loaded.. :(
} else {
    // great, the user is loaded!
}
```

Handling this can be tricky, but it's slightly easier if you don't need to get a result back to the same thread immediately.

If you're not sure if the `User` you want to obtain is online, you can setup a method to help with the process.
```java
public void getUserAndApply(UUID playerUuid, Consumer<User> action) {
    User user = api.getUser(playerUuid);
    if (user != null) {
        // user is already loaded, just apply the action
        action.accept(user);
        return;
    }

    // ok, user isn't online, so we need to load them.
    // once the user is loaded, this callback will be executed on the main thread.
    api.getStorage().loadUser(playerUuid)
            .thenAcceptAsync(wasSuccessful -> {

                // for whatever reason, the user could not be loaded.
                // this might be because the database is not accessible, or because
                // there was some other unexpected error.
                if (!wasSuccessful) {
                    return;
                }

                // ok, so the user *should* be loaded now!
                User loadedUser = api.getUser(playerUuid);
                if (loadedUser == null) {
                    // nope, still not loaded.
                    return;
                }

                // apply the action now they're loaded.
                action.accept(loadedUser);

                // tell LuckPerms that you're finished with the user, and that
                // it can unload them.

                api.cleanupUser(loadedUser);
            }, api.getStorage().getSyncExecutor());
}
```

This then allows you to do something like this.
```java
getUserAndApply(playerUuid, user -> {
    // do something with the user.
    user.doSomething(...);
});
```

Alternatively, you can forcefully load the user. However, this is only safe to do from an async thread.
```java
public void doSomethingToUser(UUID playerUuid) {
    User user = api.getUser(playerUuid);
    if (user == null) {
        // user not loaded, we need to load them from the storage.
        // this is a blocking call.
        api.getStorage().loadUser(playerUuid).join();

        // then grab a new instance
        user = api.getUser(playerUuid);
    }

    // still null, despite our efforts to load them.
    if (user == null) {
        throw new RuntimeException("Unable to load user for " + playerUuid);
    }

    // now we have a user, and can apply whatever action we want.
    user.doSomething(...);

    // remember that once you're finished with a user, you need to tell
    // LuckPerms to cleanup that instance.
    api.cleanupUser(loadedUser);
}
```

As you can see, this process can get fairly complex. What you decide to do will greatly depend on what you're trying to achieve with the API. If you know the player is online, it's simple. 😄 

### Obtaining a Group/Track instance
Grabbing a `Group` or `Track` is much more simple, as they are always kept loaded in memory.

Simply...
```java
Group group = api.getGroup(groupName);
if (group == null) {
    // group doesn't exist.
    return;
}

// now we have a group, and can apply whatever action we want.
group.doSomething(...);
```

You can do exactly the same for `Track`s using the `#getTrack` method.

### Adding a permission/parent/prefix/suffix/metadata to a user/group
In LuckPerms, group inheritances, chat meta (prefixes/suffixes) and metadata are all stored inside permission `Node`s, represented in the API by the `Node` interface.

To obtain a `Node`, you use the `NodeFactory`, which can be obtained using `LuckPermsApi#getNodeFactory`.

```java
// build a permission node
Node node = api.getNodeFactory().newBuilder(permission).build();

// build a group node
Node node = api.getNodeFactory().makeGroupNode(group).build();

// build a prefix node
Node node = api.getNodeFactory().makePrefixNode(100, "[Some Prefix]").build();

// build a suffix node
Node node = api.getNodeFactory().makeSuffixNode(150, "[Some Suffix]").build();

// build a metadata node
Node node = api.getNodeFactory().makeMetaNode("some-key", "some-value").build();
```

Then, you can set the node onto the user/group.

**IMPORTANT:** Whenever you make changes to User/Group/Track data, you need to save your changes using the `Storage` interface.

```java
public boolean addPermission(User user, String permission) {

    // build the permission node
    Node node = api.getNodeFactory().newBuilder(permission).build();

    // set the permission
    DataMutateResult result = user.setPermission(node);

    // wasn't successful.
    // they most likely already have the permission
    if (result != DataMutateResult.SUCCESS) {
        return false;
    }

    // now, before we return, we need to have the user to storage.
    // this method will save the user, then run the callback once complete.
    api.getStorage().saveUser(user)
            .thenAcceptAsync(wasSuccessful -> {
                if (!wasSuccessful) {
                    return;
                }

                System.out.println("Successfully set permission!");

                // refresh the user's permissions, so the change is "live"
                user.refreshCachedData();

            }, api.getStorage().getAsyncExecutor());

    return true;
}
```

### Using UserData
All `User`s also have an extra object attached to them called `UserData`. This is the name of the caching class used by LuckPerms to store easily query-able data for all users.

This class is **very fast**, and is actually what is used to respond to all permission check requests made by other plugins on the server. If you're doing frequent data lookups, it is highly recommended that if possible, you use `UserData` over the methods in `User`.

Everything in `UserData` is indexed by `Contexts`, as this is how LuckPerms processes all lookups internally.

Contexts are explained in detail [here](https://github.com/lucko/LuckPerms/wiki/Command-Usage#what-is-context), and are represented in the API by the `Contexts` class.

The API exposes methods to obtain instances of `Contexts` using the internal LuckPerms calculation, however, these methods only work for online players. This is because, by their very nature, Contexts depend on the players state.

If you have a `Player` or `ProxiedPlayer` instance handy for the User you're querying, you can use
```java
Contexts contexts = api.getContextsForPlayer(player);
```
to get a "current" instance.

Otherwise, you can use
```java
Optional<Contexts> contexts = api.getContextForUser(user);
```
but be aware this will only return an instance for Users where the corresponding player is online.

You can fallback to the platforms static content instance using `ContextManager#getStaticContexts`.

Finally, as a last result, you can either construct your own custom `Contexts` instance using your own values, or use `Contexts.global()` or `Contexts.allowAll()`.

Once you have a `Contexts` instance, you can start using the `UserData` object. 😄 

The containing data is split into two separate sections, 'Permission' and 'Meta' data.
```java
UserData cachedData = user.getCachedData();
Contexts contexts = ...;

PermissionData permissionData = cachedData.getPermissionData(contexts);
MetaData metaData = cachedData.getMetaData(contexts);
```

`PermissionData` contains information about a users "active" permission nodes, and allows you to run permission checks, in exactly the same way as you would using the Player/ProxiedPlayer object.

`MetaData` contains information about a users "active" prefixes, suffixes, and meta values.

For example...
```java
// run a permission check!
Tristate checkResult = permissionData.getPermissionValue("some.permission.node");

// the same as what Player#hasPermission would return
boolean checkResultAsBoolean = checkResult.asBoolean();

// get their current prefix
String prefix = metaData.getPrefix();

// get some random meta value
String metaResult = metaData.getMeta().getOrDefault("some-key", "default-value");
```

Since v4.0, these queries and lookups can also be performed for groups! The methods are identical for performing group based checks.

### Searching for a permission
You can use Java 8 streams to easily filter and return permissions applied to a user.
```java
public boolean hasPermissionStartingWith(User user, String startingWith) {
    return user.getPermissions().stream()
            .filter(Node::getValue)
            .filter(Node::isPermanent)
            .filter(n -> !n.isServerSpecific())
            .filter(n -> !n.isWorldSpecific())
            .anyMatch(n -> n.getPermission().startsWith(startingWith));
}
```