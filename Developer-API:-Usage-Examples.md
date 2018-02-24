This page shows some sample usages of the LuckPerms API, which is introduced [here](https://github.com/lucko/LuckPerms/wiki/Developer-API).

___

### Index

* Simple queries
  * [Checking if a player is in a group](#checking-if-a-player-is-in-a-group)
  * [Finding a players group](#finding-a-players-group)
* I/O - loading & saving data
  * [Obtaining a User instance](#obtaining-a-user-instance)
    * [Distinction between online & offline players](#distinction-between-online--offline-players)
    * [Loading data for players](#loading-data-for-players)
  * [Obtaining a Group/Track instance](#obtaining-a-grouptrack-instance)
  * [Saving changes](#saving-changes)
* [The basics of Node](#the-basics-of-node)
  * [Creating new node instances](#creating-new-node-instances)
  * [Modifying existing nodes](https://github.com/lucko/LuckPerms/wiki/Developer-API:-Usage-Examples#modifying-existing-nodes)
* Reading user/group data (WIP)
* Modifying user/group data (WIP)
* The basics of Context (WIP)
  * Important classes (WIP)
  * Registering ContextCalculators (WIP)
  * Querying active contexts (WIP)
* The basics of CachedData (WIP)
  * Performing permission checks (WIP)
  * Retrieving prefixes and suffixes (WIP)
  * Retrieving meta data (WIP)
* [Using UserData](#using-userdata)
* [Listening to LuckPerms events](#listening-to-luckperms-events)

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
We can use the method used above alongside a list of defined "possible" groups in order to search for a player's group.

Remember to order your group list in order of priority. e.g. owner first, member last.

```java
public static String getPlayerGroup(Player player, Collection<String> possibleGroups) {
    for (String group : possibleGroups) {
        if (player.hasPermission("group." + group)) {
            return group;
        }
    }
    return null;
}
```

___

### Obtaining a User instance
A `User` in LuckPerms is simply an object which represents a player on the server, and their associated permission data.

#### Distinction between online & offline players
In order to conserve memory usage, LuckPerms will only load User data when it absolutely needs to. 

Meaning:
* Online players are guaranteed to have an associated User object loaded already.
* Offline players *may* have an associated User object loaded, but they most likely will not.

This makes getting a User instance a little complicated, depending on if the Player is online or not.

#### Loading data for players

##### If the player is already online
If we know the player is connected, LuckPerms will already have data in memory for them.

It's as simple as...
```java
public User loadUser(Player player) {
    // assert that the player is online
    if (!player.isOnline()) {
        throw new IllegalStateException("Player is offline");
    }
    
    return luckPermsApi.getUserManager().getUser(player.getUniqueId());
}
```

However, remember that this instance *may* not represent the user's most up-to-date state. If you want to make changes, it's a good idea to request for the user's data to be loaded again.

##### If the player isn't (or might not be) online
Let's assume we want to load some data about a user - but we only have their unique id.

For the purposes of explaining, assume we want to write an implementation for this method.

```java
public void giveAdminPermissions(UUID uuid) {...}
```

The first thing we need to do is obtain the `UserManager`. This object is responsible for handling all operations relating to `User`s. The user manager provides a method which lets us load a `User` instance, appropriately named `loadUser`.

The method returns a `CompletableFuture` (explained [here](https://github.com/lucko/LuckPerms/wiki/Developer-API#using-completablefutures)).

We can simply attach a callback onto the future to apply the action.

```java
public void giveAdminPermissions(UUID uuid) {
    UserManager userManager = luckPermsApi.getUserManager();
    CompletableFuture<User> userFuture = userManager.loadUser(uuid);

    userFuture.thenAcceptAsync(user -> {
        // TODO: apply the action to the User instance
        user.doSomething(...);
    });
}
```

##### How to query information for a (potentially) offline player
The callback approach works well if you don't need to actually "return" anything. It performs all of the nasty i/o away from the main server thread, and handles everything in the background.

But what if we need data *now*? Well, that's where it gets fun. Unfortunately, there's no straightforward answer - but you effectively have two options.

* Define a blocking method, which will be (kind of) simple, but will lag the server if it's not called async
* Embrace CompletableFutures and callbacks

The first option effectively comes down to this...

```java
public User giveMeADamnUser(UUID uuid) {
    UserManager userManager = luckPermsApi.getUserManager();
    CompletableFuture<User> userFuture = userManager.loadUser(uuid);

    return userFuture.join(); // ouch!
}
```

You can then do whatever you want with the user instance - but remember, this method should only ever be called from an async task!

The other option is to embrace callbacks.

In an ideal world, we'd be able to do something like this, without any consequences.

```java
public boolean isAdmin(UUID who) {
    User user = luckPermsApi.getUserManager().loadUser(who);
    return user.inheritsGroup("admin"); // not a real method, just used here as an example :p
}

public void informIfAdmin(CommandSender sender, UUID who) {
    if (isAdmin(who)) {
        sender.sendMessage("Yes! That player is an admin!");
    } else {
        sender.sendMessage("No, that player isn't an admin.");
    }
}
```

However, we can't, because `#loadUser` returns a Future - as it performs lots of expensive database queries to produce a result.

The solution? More futures!

```java
public CompletableFuture<Boolean> isAdmin(UUID who) {
    return luckPermsApi.getUserManager().loadUser(who)
            .thenApplyAsync(user -> user.inheritsGroup("admin"));
}

public void informIfAdmin(CommandSender sender, UUID who) {
    isAdmin(who).thenAcceptAsync(result -> {
        if (result) {
            sender.sendMessage("Yes! That player is an admin!");
        } else {
            sender.sendMessage("No, that player isn't an admin.");
        }
    });
}
```

To summarise, there are two ways to obtain a user.

* Using `UserManager#getUser`
  * Always returns a result for online players
  * Is "main thread friendly" (can be called sync)
  * Will sometimes (but usually not) return a result of offline players
* Using `UserManager#loadUser`
  * Returns a future
  * Can either be used alongside callbacks, or as part of a blocking method which is only ever called async
  * Always works for both offline/online users

___

### Obtaining a Group/Track instance
Grabbing a `Group` or `Track` is much more simple, as they are always kept loaded in memory.

Simply...
```java
Group group = api.getGroupManager().getGroup(groupName);
if (group == null) {
    // group doesn't exist.
    return;
}

// now we have a group, and can apply whatever action we want.
group.doSomething(...);
```

You can do exactly the same for `Track`s using the `TrackManager#getTrack` method.

___

### Saving changes
After making changes to a user/group/track, you have to save the changes back to the storage provider. It's pretty easy.

```java
public void addPermission(User user, String permission) {
    // TODO add the permission
    
    // Now we need to save changes.
    luckPermsApi.getUserManager().saveUser(user);
}
```

The same methods also exist for groups and tracks.

However, if we're making a change to the user's live data, we'll also need to refresh their caches for the change to apply. In order to do this, we can just add a call onto the end of the save method.

It becomes...

```java
luckPermsApi.getUserManager().saveUser(user).thenRunAsync(user::refreshCachedData);
```

For group changes, it's best to request a complete update task.

```java
luckPermsApi.getGroupManager().saveGroup(group).thenComposeAsync(v -> luckPermsApi.runUpdateTask());
```

___

### The basics of Node

The `Node` interface is the core data class in LuckPerms.

Most simply, it represents a "permission node". However, it actually encapsulates far more than just permission assignments. Nodes are used to store data about inherited groups, as well as assigned prefixes, suffixes and meta values.

Combining these various states into one object (a "node") means that a holder only has to have one type of data set (a set of nodes) in order to take on various properties.

The `Node` interface provides a number of methods to read the attributes of the node, as well as methods to query and extract additional state and properties from these settings.

Nodes have the following attributes:

* permission - the actual permission string
* value - the value of the node (false for negated)
* override - if the node is marked as having special priority over other nodes
* server - the specific server where this node should apply
* world - the specific world where this node should apply
* context - the additional contexts required for this node to apply
* expiry - the time when this node should expire

Nodes can also fall into the following sub categories.

* normal - just a regular permission
* group node - a "group node" marks that the holder should inherit data from another group
* prefix - represents an assigned prefix
* suffix - represents an assigned suffix
* meta - represents an assigned meta option

___

### Creating new node instances
To obtain a `Node`, you use the `NodeFactory`, which can be obtained using `LuckPermsApi#getNodeFactory`.

```java
// build a simple permission node
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

___

### Modifying existing nodes
`Node`s are immutable - meaning their attributes cannot be changed. However, we can easily create a *new* node based upon the properties of an existing one.

e.g.
```java
Node negated = node.toBuilder().setValue(false).build();
```

___

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