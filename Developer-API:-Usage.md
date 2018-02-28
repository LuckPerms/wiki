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

### Reading user/group data

`User`s and `Group`s both inherit from a super interface called `PermissionHolder`. This interface defines most of the shared permission functionality in users and groups.

As explained above, most data held by users/groups are contained within `Node` instances. This means that there are only a few methods to think about. However, they all do slightly different things!

Importantly, all of the methods below return **immutable collections**. You cannot make changes to the returned connections. 

#### `.getOwnNodes()`
The method signature is:
```java
List<Node> getOwnNodes()
```

* This method returns an un-flattened (or squashed) list of the user/groups permission nodes. 
* Entries nearer the start of the list (index zero) have priority over nodes at the end.
* This view does **not** consider inherited data.

It's a relatively cheap call, and will return quite quickly.

You can use the Stream API to easily filter the returned data to find what you need. For example, if you wanted to get a list of groups a holder inherits from, you could use something like this:
```java
Set<String> groups = user.getAllNodes().stream()
    .filter(Node::isGroupNode)
    .map(Node::getGroupName)
    .collect(Collectors.toSet());
```

Or even more complicated queries, like finding the max weight of a temporary prefix held on a specific server.
```java
OptionalInt maxWeight = user.getAllNodes().stream()
    .filter(Node::isTemporary)
    .filter(Node::isPrefix)
    .filter(Node::isServerSpecific)
    .filter(n -> n.getServer().get().equals("factions"))
    .map(Node::getPrefix)
    .mapToInt(Map.Entry::getKey)
    .max();
```

#### `.getNodes()`
The method signature is:
```java
ImmutableSetMultimap<ImmutableContextSet, Node> getNodes();
```

* This method is similar to `#getOwnNodes`, but differs in the way the data is presented.
* Nodes are mapped to the value of their context - obtained using `Node#getFullContexts`
* This is how data is stored internally (at the moment) - so again this method should return quickly.
* You should use this method if you want to query data in a specific set of contexts - otherwise it's probably better to use one of the other options.
* This view does **not** consider inherited data.

#### `.getPermissions()`
The method signature is:
```java
SortedSet<? extends Node> getPermissions();
```

Note that despite the name, this method will still return all types of node - not just plain permissions.

* This method returns a sorted view of `#getOwnNodes`. If you are not worried about ordering, it's faster to use `#getOwnNodes`.
* The nodes are sorted according to "priority order". As the returned type is a set, duplicate elements may be missing.
* This view does **not** consider inherited data.

#### `.getAllNodes()`
The method signature is:
```java
SortedSet<LocalizedNode> getAllNodes();
```

* Unlike the other methods, this method **does** return inherited data.
* This method is quite slow - if you need to query inherited data, consider using `CachedData` (explained below)
* Users/Groups also define a version of this method which accepts a `Contexts` instance - to filter results based upon on the encapsulated lookup settings in the contexts.

___

### Modifying user/group data

User/group data can be modified by adding and removing `Node`s from the holders data. This can be done in a number of ways.

#### `.setPermission(Node)`

* Effectively "adds" a node to the user/group.
* Note that despite the name, this method will work for all types of node.
	* Meaning, this method is also used for
		* Adding prefixes
		* Adding suffixes
		* Adding metadata
		* Adding inheritances to other groups
* This method adds the node to the holder's permanent permission store, and when saved, this data will be written to the storage provider.

The method returns a `DataMutateResult`. This enum encapsulates the status of the operation, and will return a value depending on if the operation was performed successfully.

In the case of `#setPermission`, it will return `ALREADY_HAS` if the user/group already has the permission set.

You can check for generic success/failure using `DataMutateResult#wasSuccess` and `DataMutateResult#wasFailure`.

#### `.setTransientPermission(Node)`

Same as the above method, except this method adds the node to the holders "transient" data store.

A transient node is a permission that does not persist. Whenever a user logs out of the server, or the server restarts, this permission will disappear. It is never saved to the storage, and therefore will not apply on other servers.

This is useful if you want to temporarily set a permission for a user while they're online, but don't want it to persist, and have to worry about removing it when they log out.

#### `.unsetPermission(Node)`

* Effectively "removes" a node from the user/group.
* Note that despite the name, this method will work for all types of node.
	* Meaning, this method is also used for
		* Removing prefixes
		* Removing suffixes
		* Removing metadata
		* Removing inheritances from other groups
* This method removes the node to the holder's permanent permission store, and when saved, this change will be written to the storage provider.

The method returns a `DataMutateResult`. This enum encapsulates the status of the operation, and will return a value depending on if the operation was performed successfully.

In the case of `#unsetPermission`, it will return `LACKS` if the user/group doesn't have the node set.

You can check for generic success/failure using `DataMutateResult#wasSuccess` and `DataMutateResult#wasFailure`.

#### `.unsetTransientPermission(Node)`

Same as the above method, except this method removes the node from the holders "transient" data store.

#### `.clearMatching(Predicate<Node>)`

This method removes any nodes from the user/group which pass the given predicate. It can be used to "bulk remove" nodes of a specific type. 

For example, if I wanted to remove all prefixes set with a weight of 10...
```java
user.clearMatching(n -> n.isPrefix() && n.getPrefix().getKey() == 10);
```

This method is less like a transaction, and more a way to easily remove data matching a given criteria.

`#clearMatchingTransient` works in the same way, but affects the transient data store.

#### `.clearNodes()`

Clears everything!

#### `.clearNodes(ContextSet)`

Clears all nodes which are set in the given context.

___

### The basics of Context

Contexts are an important concept in LuckPerms, and are introduced [here](https://github.com/lucko/LuckPerms/wiki/Context). They are encapsulated within the API by a few important classes.

A very basic overview is that:

> **Context** in the most basic sense simply means the **circumstances where something will apply**.
> 
> A single "context" consists of a key and a value, both strings. The key represents the type of context, and the value represents the setting of the context key.
> 
> Contexts can be combined with each other to form so called "context sets" - simply a collection of context pairs.
> 
> Context keys are case-insensitive, and will be converted to lowercase by all implementations. Values however are case-sensitive. Context keys and values may not be null or empty. A key/value will be deemed empty if it's length is zero, or if it consists of only space characters.

#### Important classes
#### `ContextSet`
A "context set" is simply a set of contexts.

Internally, a context set is effectively a `Multimap<String, String>`, or a `<Map<String, Collection<String>>`, but importantly, it is **not** a `Map<String, String>`.

Keys can be mapped to multiple values.

The `ContextSet` interface defines a number of methods which can be used to interact with context set implementations. These methods should be fairly self explanatory - and are sufficiently explained in the Javadocs.

#### `ImmutableContextSet`

An *immutable* implementation of ContextSet. You can obtain an instance in a number of ways.

```java
ImmutableContextSet set1 = ImmutableContextSet.empty();  

ImmutableContextSet set2 = ImmutableContextSet.singleton("world", "world_nether");  

ImmutableContextSet set3 = ImmutableContextSet.builder()  
    .add("world", "world_nether")
    .add("server", "survival")
    .build();

Map<String, String> map = new HashMap<>();
map.put("region", "something");

ImmutableContextSet set4 = ImmutableContextSet.fromMap(map);
```

You can of course also create an `ImmutableContextSet` by first creating (or obtaining) a `MutableContextSet` and converting it.

```java
MutableContextSet set = MutableContextSet.create();
set.add("something", "something");

ImmutableContextSet immutableSet = set.makeImmutable();
```

#### `MutableContextSet`

A *mutable* implementation of ContextSet. You can obtain an instance in a number of ways.

```java
MutableContextSet set1 = MutableContextSet.create();
set1.add("world", "text");

MutableContextSet set2 = MutableContextSet.singleton("world", "world_nether");

Map<String, String> map = new HashMap<>();
map.put("region", "something");

MutableContextSet set3 = MutableContextSet.fromMap(map);
set3.removeAll("region");
```

To edit an `ImmutableContextSet`, you can make a "mutable copy" of it.

```java
ImmutableContextSet set = ImmutableContextSet.singleton("something", "something");

MutableContextSet mutableCopy = set.mutableCopy();
mutableCopy.add("something", "something-else");
```

#### `Contexts`

The `Contexts` class encapsulates all of the options and settings for a permission or meta lookup.

It contains the `ContextSet` for the lookup and a set of `LookupSetting`s.

| `LookupSetting` | Description |
|---------|-------------|
| `IS_OP` | If the target subject is OP |
| `INCLUDE_NODES_SET_WITHOUT_SERVER` | If global or non-server-specific nodes should be applied |
| `INCLUDE_NODES_SET_WITHOUT_WORLD` | If global or non-world-specific nodes should be applied |
| `RESOLVE_INHERITANCE` | If parent groups should be resolved |
| `APPLY_PARENTS_SET_WITHOUT_SERVER` | If global or non-server-specific group memberships should be applied |
| `APPLY_PARENTS_SET_WITHOUT_WORLD` | If global or non-world-specific group memberships should be applied |

You can query the value of a setting using:

```java
boolean shouldResolveInheritance = contexts.hasSetting(LookupSetting.RESOLVE_INHERITANCE);
```

You can create a Contexts instance using `Contexts.of(...)`, `Contexts.global()`, or `Contexts.allowAll()`.

It is more likely that you'll wish to obtain an "active" instance from LuckPerms via the `ContextManager`.

#### Registering ContextCalculators

A "subject" (a player in most cases) is just an object which can have contexts applied to them.

In other words, a "subject" is an object which has an **active context set**. A `ContextCalculator` is an object which determines the "active" contexts for a given type of Subject.

The subject type varies between platforms.

| Platform | Subject type |
|----------|--------------|
| Bukkit | `org.bukkit.entity.Player` |
| BungeeCord | `net.md_5.bungee.api.connection.ProxiedPlayer` |
| Sponge | `org.spongepowered.api.service.permission.Subject` |
| Nukkit | `cn.nukkit.Player` |

In order to provide your own context, you need to create and register a `ContextCalculator`.

For example, if I wanted to provide a context for the player's gamemode, in order to set permissions for players only when they are in creative, I'd create a calculator as follows.

```java
public class CustomCalculator implements ContextCalculator<Player> {

    @Override  
    public MutableContextSet giveApplicableContext(Player subject, MutableContextSet accumulator) {
        accumulator.add("gamemode", subject.getGameMode().name());
        return accumulator;
    }
    
}
```

Then register it using
```java
api.getContextManager().registerCalculator(new CustomCalculator());
```

#### Querying active contexts
You can query the "active" contexts of a Subject using the `ContextManager`.

If you already have an instance of the subject type, you can query directly using this.
```java
Player player = ...;

ImmutableContextSet contextSet = api.getContextManager().getApplicableContext(player);
Contexts contexts = api.getContextManager().getApplicableContexts(player);
```

If you only have a `User`, you can still perform a lookup, however, a result will only be returned if the corresponding subject (player) is online.
```java
Optional<ImmutableContextSet> contextSet = api.getContextManager().lookupApplicableContext(user);
Optional<Contexts> contexts = api.getContextManager().lookupApplicableContexts(user);
```

If you absolutely need to obtain an instance, you can fallback to the server's "static" context. (these are formed using calculators which provide contexts regardless of the passed subject.)
```java
ContextManager cm = api.getContextManager();

ImmutableContextSet contextSet = cm.lookupApplicableContext(user).orElse(cm.getStaticContext());
Contexts contexts = cm.lookupApplicableContexts(user).orElse(cm.getStaticContexts());
```
___

### The basics of CachedData
All `User`s and `Group`s also have an extra object attached to them called `CachedData`. This is the name of the caching class used by LuckPerms to store easily query-able data for all permission holders.

The lookup methods provided by this class are very fast. If you're doing frequent data lookups, it is highly recommended that if possible, you use `CachedData` over the methods in `User` and `Group`.

Everything in `CachedData` is indexed by `Contexts`, as this is how LuckPerms processes all lookups internally.

The contained data is split into two separate sections: `PermissionData` and `MetaData`.

`PermissionData` contains the user/groups fully resolved map of permissions, and allows you to run permission checks in exactly the same way as you would using the Player class provided by the platform.

`MetaData` contains information about a user/groups prefixes, suffixes, and meta values.

#### Obtaining `PermissionData` and `MetaData`
You need:
* A `User` or `Group` instance
* The `Contexts` to get the data in (see above for how to obtain this)

Once you have those instances, it's as simple as:
```java
PermissionData permissionData = user.getCachedData().getPermissionData(contexts);
MetaData metaData = user.getCachedData().getMetaData(contexts);
```

#### Performing permission checks
```java
// run a permission check!
Tristate checkResult = permissionData.getPermissionValue("some.permission.node");

// the same as what Player#hasPermission would return
boolean checkResultAsBoolean = checkResult.asBoolean();
```

#### Retrieving prefixes/suffixes
```java
String prefix = metaData.getPrefix();
String suffix = metaData.getSuffix();
```
#### Retrieving meta data
```java
String metaResult = metaData.getMeta().getOrDefault("some-key", "default-value");
```

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