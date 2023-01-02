This page shows some sample usages of the LuckPerms API, which is introduced [here](Developer-API).

As well as this documentation, we also have the [api-cookbook](https://github.com/LuckPerms/api-cookbook). This is an example Bukkit plugin which uses the API to perform certain common functions.

___

### Index

* [Player group membership check](#checking-if-a-player-is-in-a-group)
* [Player group membership lookup](#finding-a-players-group)
* [Getting a LuckPerms `User` object](#obtaining-a-user-instance)
  * [Distinction between online & offline players](#distinction-between-online--offline-players)
  * [Loading data for players](#loading-data-for-players)
* [Getting a LuckPerms `Group` or `Track` object](#obtaining-a-grouptrack-instance)
* [Saving changes](#saving-changes)
* [The `Node` object](#the-basics-of-node)
  * [Creating new nodes](#creating-new-node-instances)
  * [Modifying existing nodes](Developer-API-Usage#modifying-existing-nodes)
* [Reading user/group data](#reading-usergroup-data)
* [Modifying user/group data](#modifying-usergroup-data)
* [Context](#the-basics-of-context)
  * [Important classes](#important-classes)
  * [Registering ContextCalculators](#registering-contextcalculators)
  * [Querying active contexts/query options](#querying-active-contextsquery-options)
* [CachedData](#the-basics-of-cacheddata)
  * [Performing permission checks](#performing-permission-checks)
  * [Getting prefixes and suffixes](#retrieving-prefixessuffixes)
  * [Getting metadata](#retrieving-metadata)
* [Store and query custom metadata](#store-and-query-custom-metadata)
* [Events](#events)
  * [Event listeners](#event-listeners)
  * [Listening for changes to user cached data](#listening-for-changes-to-user-cached-data)
  * [Listening for changes to permissions/parent groups/etc](#listening-for-changes-to-permissionsparent-groupsetc)

___

### Checking if a player is in a group

Checking for group membership can be most easily achieved using hasPermission checks.

```java
public static boolean isPlayerInGroup(Player player, String group) {
    return player.hasPermission("group." + group);
}
```

However, keep in mind that anyone with server operator status or `*` permissions will also have these permissions.

___

### Finding a players group

We can use the method above with a list of "possible" groups in order to find a player's group.

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

Remember to order your `possibleGroups` list by priority. e.g. owner first, member last.

___

### Obtaining a User instance

A `User` in LuckPerms is simply an object which represents a player on the server, and their associated permission data.

#### Distinction between online & offline players

In order to conserve memory usage, LuckPerms will only load User data when it absolutely needs to. 

Meaning:

* **Online** players are guaranteed to have an associated User object loaded already.
* **Offline** players *may* have an associated User object loaded, but they most likely will not.

This makes getting a User instance a little complicated, depending on if the Player is online or not.

#### Loading data for players

##### If the player is already online

If we know the player is connected, LuckPerms will already have data in memory for them.

It's as simple as...

```java
Player player = ...;
User user = luckPerms.getPlayerAdapter(Player.class).getUser(player);
```

Or if you only have a `UUID`...

```java
User user = luckPerms.getUserManager().getUser(uuid);
```

However, remember that this instance *may* not represent the user's most up-to-date state. If you want to make changes, it's a good idea to request for the user's data to be loaded again (read on...).

##### If the player isn't (or might not be) online

Let's assume we want to load some data about a user - but we only have their unique id.

The first thing we need to do is obtain the `UserManager`. This object is responsible for handling all operations relating to `User`s. The user manager provides a method which lets us load a `User` instance, appropriately named `loadUser`.

The method returns a `CompletableFuture` (explained [here](Developer-API#using-completablefutures)).

We can simply attach a callback onto the future to apply the action.

```java
UserManager userManager = luckPerms.getUserManager();
CompletableFuture<User> userFuture = userManager.loadUser(uniqueId);

userFuture.thenAcceptAsync(user -> {
    // Now we have a user which we can query.
    // ...
});
```

##### If the player isn't (or might not be) online & we want to return something

The callback approach works well if you don't need to actually "return" anything. It performs all of the nasty i/o away from the main server thread, and handles everything in the background.

But what if we need data *now*? Well, that's where it gets fun. Unfortunately, there's no straightforward answer - but you effectively have two options.

* Define a blocking method, which will be (kind of) simple, but will lag the server if it's not called async
* Embrace CompletableFutures and callbacks

The first option effectively comes down to this...

```java
public User giveMeADamnUser(UUID uniqueId) {
    UserManager userManager = luckPerms.getUserManager();
    CompletableFuture<User> userFuture = userManager.loadUser(uniqueId);

    return userFuture.join(); // ouch! (block until the User is loaded)
}
```

You can then do whatever you want with the user instance - but remember, this should only ever be called from an async task!

The other option is to embrace callbacks.

In an ideal world, we'd be able to do something like this, without any consequences.

```java
public boolean isAdmin(UUID who) {
    User user = luckPerms.getUserManager().loadUser(who);

    Collection<Group> inheritedGroups = user.getInheritedGroups(user.getQueryOptions());
    return inheritedGroups.stream().anyMatch(g -> g.getName().equals("admin"));
}

public void informIfAdmin(CommandSender sender, UUID who) {
    if (isAdmin(who)) {
        sender.sendMessage("Yes! That player is an admin!");
    } else {
        sender.sendMessage("No, that player isn't an admin.");
    }
}
```

However, we can't, because `#loadUser` returns a CompletableFuture - as it performs lots of expensive database queries to produce a result.

The solution? More futures!

```java
public CompletableFuture<Boolean> isAdmin(UUID who) {
    return luckPerms.getUserManager().loadUser(who)
        .thenApplyAsync(user -> {
            Collection<Group> inheritedGroups = user.getInheritedGroups(user.getQueryOptions());
            return inheritedGroups.stream().anyMatch(g -> g.getName().equals("admin"));
        });
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

* Using `UserManager#getUser` or `PlayerAdapter#getUser`
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
Group group = luckPerms.getGroupManager().getGroup(groupName);
if (group == null) {
    // group doesn't exist.
    return;
}

// now we have a group, and can apply whatever action we want.
group.doSomething(...);
```

You can do exactly the same for `Track`s using the `TrackManager#getTrack` method.

If you need to get up-to-date data (a good idea if you're making changes), then just call `loadGroup` or `loadTrack` instead, respectively.

___

### Saving changes

After making changes to a user/group/track, you have to save the changes back to the storage provider. It's pretty easy.

```java
public void addPermission(User user, String permission) {
    // Add the permission
    user.data().add(Node.builder(permission).build());

    // Now we need to save changes.
    luckPerms.getUserManager().saveUser(user);
}
```

There is also a handy `modify*` method which handles loading and saving for you.

```java
public void addPermission(UUID userUuid, String permission) {
    // Load, modify, then save
    luckPerms.getUserManager().modifyUser(userUuid, user -> {
        // Add the permission
        user.data().add(Node.builder(permission).build());
    });
}
```

The same methods also exist for groups and tracks.

___

### The basics of Node

The `Node` interface is the core data class in LuckPerms.

Most simply, it represents a "permission node". However, it actually encapsulates far more than just permission assignments. Nodes are used to store data about inherited groups, as well as assigned prefixes, suffixes and meta values.

Combining these various states into one object (a "node") means that a holder only has to have one type of data set (a set of nodes) in order to take on various properties.

The `Node` interface provides a number of methods to read the attributes of the node, as well as methods to query and extract additional state and properties from these settings.

Nodes have the following attributes:

* key - the key of the node
* value - the value of the node (false for negated)
* context - the contexts required for this node to apply
* expiry - the time when this node should expire

There are a number of node types, all of which are extensions of the base `Node` class.

* `PermissionNode` - represents an assigned permission
* `RegexPermissionNode` - represents an assigned regex permission
* `InheritanceNode` - marks that the holder should inherit data from another group
* `PrefixNode` - represents an assigned prefix
* `SuffixNode` - represents an assigned suffix
* `MetaNode` - represents an assigned meta option
* `WeightNode` - marks the weight of the object holding the node
* `DisplayNameNode` - marks the display name of the object holding the node

___

### Creating new node instances

To obtain a `Node`, you use `NodeBuilder`s.

If you just have a "key" and are unsure which category of node it falls into, you can simply use `Node.builder()`.

```java
// build any type of node
Node node = Node.builder("some.node.key").build();

// and with extra properties!
Node node = Node.builder("some.node.key")
        .value(false)
        .expiry(Duration.ofHours(1))
        .withContext(DefaultContextKeys.SERVER_KEY, "survival")
        .build();

// note: all of the following classes extend from Node

// build a permission node
PermissionNode node = PermissionNode.builder("my.permission").build();

// build a regex permission node
RegexPermissionNode node = RegexPermissionNode.builder(pattern).build();

// build an inheritance node
InheritanceNode node = InheritanceNode.builder(group).build();

// build a prefix node
PrefixNode node = PrefixNode.builder("[Some Prefix]", 100).build();

// build a suffix node
SuffixNode node = SuffixNode.builder("[Some Suffix]", 150).build();

// build a metadata node
MetaNode node = MetaNode.builder("some-key", "some-value").build();

// build a weight node
WeightNode node = WeightNode.builder(25).build();

// build a display name node
DisplayNameNode node = DisplayNameNode.builder("SeniorModerator").build();
```

___

### Modifying existing nodes

`Node`s are immutable - meaning their attributes cannot be changed. However, we can easily create a *new* node based upon the properties of an existing one.

e.g.

```java
Node negated = node.toBuilder().value(false).build();
```

___

### Reading user/group data

`User`s and `Group`s both inherit from a super interface called `PermissionHolder`. This interface defines most of the shared permission functionality in users and groups.

As explained above, most data held by users/groups are contained within `Node` instances. This means that there are only a few methods to think about. However, they all do slightly different things!

Importantly, all of the methods below return **immutable collections**. You cannot make changes to the returned connections. 

#### `.getNodes()`

The method signature is:

```java
Collection<Node> getNodes()
```

* This method returns an un-flattened (or squashed) collection of the user/groups nodes. 
* Entries nearer the start of the collection (index zero) have priority over nodes at the end.
* This view does **not** consider inherited data.

It's a relatively cheap call, and will return quite quickly.

You can use the Stream API to easily filter the returned data to find what you need. For example, if you wanted to get a list of groups a holder inherits from, you could use something like this:

```java
Set<String> groups = user.getNodes().stream()
    .filter(NodeType.INHERITANCE::matches)
    .map(NodeType.INHERITANCE::cast)
    .map(InheritanceNode::getGroupName)
    .collect(Collectors.toSet());
```

You can make this a bit simpler by passing the node type as a parameter!

```java
Set<String> groups = user.getNodes(NodeType.INHERITANCE).stream()
    .map(InheritanceNode::getGroupName)
    .collect(Collectors.toSet());
```

Or even more complicated queries, like finding the max priority of a temporary prefix held on a specific server.

```java
int maxWeight = user.getNodes(NodeType.PREFIX).stream()
    .filter(Node::hasExpiry)
    .filter(n -> n.getContexts().getAnyValue(DefaultContextKeys.SERVER_KEY)
        .map(v -> v.equals("factions")).orElse(false))
    .mapToInt(ChatMetaNode::getPriority)
    .max()
    .orElse(0);
```

If you need to do a more specific lookup or check, prefer using one of the other methods (described later) to avoid iterating over the whole collection of nodes.

#### `.getDistinctNodes()`

The method signature is:

```java
SortedSet<Node> getDistinctNodes();
```

* This method returns a sorted view of `#getNodes`. If you are not worried about ordering, it's faster to use `#getNodes`.
* The nodes are sorted according to "priority order". As the returned type is a set, duplicate elements may be missing.
* This view does **not** consider inherited data.

#### `.resolveInheritedNodes()`

The method signature is:

```java
Collection<Node> resolveInheritedNodes(QueryOptions queryOptions)
```

* This method returns an un-flattened (or squashed) list of the user/groups nodes, and all nodes they inherit from their parents.
* Entries nearer the start of the list (index zero) have priority over nodes at the end.
* This view **does** consider inherited data. If you don't need this, use the `getNodes` method instead.

The `QueryOptions` parameter encapsulates the lookup settings for the query. This class is explained in a later section. If you're not worried particularly about filtering by context, simply use `QueryOptions.nonContextual()`.

___

### Modifying user/group data

User/group data can be modified by adding and removing `Node`s from the holders data. This can be done by calling `#data` and calling the methods on the returned `NodeMap`.

Here is an example of adding a permission to a user:
```java
DataMutateResult result = user.data().add(Node.builder("your.node.here").build());
```
Don't forget to [save](#saving-changes) your changes!

___

### The basics of Context

Contexts are an important concept in LuckPerms, and are introduced [here](Context). They are encapsulated within the API by a few important classes.

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

ImmutableContextSet set2 = ImmutableContextSet.of("world", "world_nether");

ImmutableContextSet set3 = ImmutableContextSet.builder()  
    .add("world", "world_nether")
    .add("server", "survival")
    .build();

Map<String, String> map = new HashMap<>();
map.put("region", "something");

ImmutableContextSet.Builder builder = ImmutableContextSet.builder();
map.forEach(builder::add);

ImmutableContextSet set4 = builder.build();
```

You can of course also create an `ImmutableContextSet` by first creating (or obtaining) a `MutableContextSet` and converting it.

```java
MutableContextSet set = MutableContextSet.create();
set.add("something", "something");

ImmutableContextSet immutableSet = set.immutableCopy();
```

#### `MutableContextSet`

A *mutable* implementation of ContextSet. You can obtain an instance in a number of ways.

```java
MutableContextSet set1 = MutableContextSet.create();
set1.add("world", "text");

MutableContextSet set2 = MutableContextSet.of("world", "world_nether");

Map<String, String> map = new HashMap<>();
map.put("region", "something");

MutableContextSet set3 = MutableContextSet.create();
map.forEach(set3::add);

set3.removeAll("region");
```

To edit an `ImmutableContextSet`, you can make a "mutable copy" of it.

```java
ImmutableContextSet set = ImmutableContextSet.of("something", "something");

MutableContextSet mutableCopy = set.mutableCopy();
mutableCopy.add("something", "something-else");
```

#### Registering ContextCalculators

A "subject" (a player in most cases) is just an object which can have contexts applied to them.

In other words, a "subject" is an object which has an **active context set**. A `ContextCalculator` is an object which determines the "active" contexts for a given type of Subject.

The subject type varies between platforms.

| Platform   | Subject type                                       |
| ---------- | -------------------------------------------------- |
| Bukkit     | `org.bukkit.entity.Player`                         |
| BungeeCord | `net.md_5.bungee.api.connection.ProxiedPlayer`     |
| Sponge     | `org.spongepowered.api.service.permission.Subject` |
| Fabric     | `net.minecraft.server.network.ServerPlayerEntity`  |
| Forge      | `net.minecraft.server.level.ServerPlayer`          |
| Nukkit     | `cn.nukkit.Player`                                 |
| Velocity   | `com.velocitypowered.api.proxy.Player`             |

In order to provide your own context, you need to create and register a `ContextCalculator`.

For example, if I wanted to provide a context for the player's gamemode, in order to set permissions for players only when they are in creative, I'd create a calculator as follows.
The `estimatePotentialContexts` method can be added, but is not necessary, to show context suggestions in the tab completion.

```java
public class CustomCalculator implements ContextCalculator<Player> {

    @Override  
    public void calculate(Player target, ContextConsumer contextConsumer) {
        contextConsumer.accept("gamemode", target.getGameMode().name());
    }
    
    @Override
    public ContextSet estimatePotentialContexts() {
        ImmutableContextSet.Builder builder = ImmutableContextSet.builder();
        for (GameMode gameMode : GameMode.values()) {
            builder.add("gamemode", gameMode.name().toLowerCase());
        }
        return builder.build();
    }
    
}
```

Then register it using

```java
luckPerms.getContextManager().registerCalculator(new CustomCalculator());
```

#### Querying active contexts/query options

You can query the "active" contexts/query options of a Subject using the `ContextManager`.

If you already have an instance of the subject type, you can query directly using this.

```java
Player player = ...;

ImmutableContextSet contextSet = luckPerms.getContextManager().getContext(player);
QueryOptions queryOptions = luckPerms.getContextManager().getQueryOptions(player);
```

If you only have a `User`, you can still perform a lookup, however, a result will only be returned if the corresponding subject (player) is online.

```java
Optional<ImmutableContextSet> contextSet = luckPerms.getContextManager().getContext(user);
Optional<QueryOptions> queryOptions = luckPerms.getContextManager().getQueryOptions(user);
```

If you absolutely need to obtain an instance, you can fallback to the server's "static" context/query option. (these are formed using calculators which provide contexts/query options regardless of the passed subject.)

```java
User user = ...;

// This is the easy way...
ImmutableContextSet contextSet = user.getQueryOptions().context();
QueryOptions queryOptions = user.getQueryOptions();

// But is equivalent to this...
ContextManager cm = luckPerms.getContextManager();
ImmutableContextSet contextSet = cm.getContext(user).orElse(cm.getStaticContext());
QueryOptions queryOptions = cm.getQueryOptions(user).orElse(cm.getStaticQueryOptions());
```

___

### The basics of CachedData

All `User`s and `Group`s also have an extra object attached to them called `CachedData`. This is the name of the caching class used by LuckPerms to store easily query-able data for all permission holders. The lookup methods provided by this class are very fast. If you're doing frequent data lookups, it is highly recommended that you use `CachedData` over the methods in `User` and `Group`.

Everything in `CachedData` is indexed by `QueryOptions`, as this is how LuckPerms processes all lookups internally.

The contained data is split into two separate sections: `CachedPermissionData` and `CachedMetaData`.

* `CachedPermissionData` contains the user/groups fully resolved map of permissions, and allows you to run permission checks in exactly the same way as you would using the Player class provided by the platform.
* `CachedMetaData` contains information about a user/groups prefixes, suffixes, and meta values.

#### Obtaining `CachedPermissionData` and `CachedMetaData`

You need either:

* A platform `Player` instance
* A LuckPerms `User` or `Group` instance + optionally some `QueryOptions` (see above for how to obtain this)

If you have a `Player` platform instance (like *org.bukkit.entity.Player*), you can use the `PlayerAdapter` to obtain cached data.

```java
Player player = ...;
PlayerAdapter<Player> adapter = luckperms.getPlayerAdapter(Player.class);

CachedPermissionData permissionData = adapter.getPermissionData(player);
CachedMetaData metaData = adapter.getMetaData(player);
```

If you already have a LuckPerms `User` or `Group` instance, you can use the following methods to obtain cached data.
```java
// Will attempt to use the most appropriate currect query options for the User
CachedPermissionData permissionData = user.getCachedData().getPermissionData();
CachedMetaData metaData = user.getCachedData().getMetaData();

// You can also manually specify which query options to use
CachedPermissionData permissionData = user.getCachedData().getPermissionData(queryOptions);
CachedMetaData metaData = user.getCachedData().getMetaData(queryOptions);
```

Once you have a cached data instance, you can perform lots of different queries.

#### Performing permission checks

```java
// run a permission check!
Tristate checkResult = permissionData.checkPermission("some.permission.node");

// the same as what Player#hasPermission would return
boolean checkResultAsBoolean = checkResult.asBoolean();
```

We can put all of this together to create a method that can run a "normal" permission check when passed a `User` and a `String` (the permission).

```java
public boolean hasPermission(User user, String permission) {
    return user.getCachedData().getPermissionData().checkPermission(permission).asBoolean();
}
```

#### Retrieving prefixes/suffixes

```java
String prefix = user.getCachedData().getMetaData().getPrefix();
String suffix = user.getCachedData().getMetaData().getSuffix();
```

#### Retrieving metadata

```java
String metaValue = user.getCachedData().getMetaData().getMetaValue("some-key");
```

These methods work with `Group`s too!

___

### Store and query custom metadata

The metadata stored by LuckPerms isn't limited to only a few types. You use the API to easily store any sort of data about players, whilst also taking advantage of the storage / caching systems built into LP.

#### Setting metadata

You can set metadata by creating & adding a `MetaNode` to a user.

To illustrate this, let's store a player "level" meta value.

```java
public void setLevel(Player player, int level) {
    // obtain a User instance (by any means! see above for other ways)
    User user = luckPerms.getPlayerAdapter(Player.class).getUser(player);

    // create a new MetaNode holding the level value
    // of course, this can have context/expiry/etc too!
    MetaNode node = MetaNode.builder("level", Integer.toString(level)).build();

    // clear any existing meta nodes with the same key - we want to override
    user.data().clear(NodeType.META.predicate(mn -> mn.getMetaKey().equals("level")));
    // add the new node
    user.data().add(node);

    // save!
    luckPerms.getUserManager().saveUser(user);
}
```

#### Querying metadata

Once the metadata is set, querying it is easy!

```java
public int getLevel(Player player) {
    // obtain CachedMetaData - the easiest way is via the PlayerAdapter
    // of course, you can get it via a User too if the player is offline.
    CachedMetaData metaData = luckPerms.getPlayerAdapter(Player.class).getMetaData(player);

    // query & parse the meta value
    return metaData.getMetaValue("level", Integer::parseInt).orElse(0);
}
```

___

### Events

LuckPerms uses it's own event system, completely separate from the event systems used by platforms (e.g. Bukkit or Sponge). This means that instead of registering your listener with the server, you must register it directly with LuckPerms.

The events supported by LuckPerms are defined as `interface`s that extend from [`LuckPermsEvent`](https://github.com/LuckPerms/LuckPerms/blob/master/api/src/main/java/net/luckperms/api/event/LuckPermsEvent.java). They can be found in the [`net.luckperms.api.event`](https://github.com/LuckPerms/LuckPerms/tree/master/api/src/main/java/net/luckperms/api/event) package.

#### Event listeners

To listen to events, you first need to obtain the [`EventBus`](https://github.com/LuckPerms/LuckPerms/blob/master/api/src/main/java/net/luckperms/api/event/EventBus.java) instance using `LuckPerms#getEventBus`, then register each listener using the `subscribe` method.

The `subscribe` method accepts a `java.util.function.Consumer` object - which allows listeners to be defined as:

1. [Expression lambdas](https://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html#syntax)
2. [Statement lambdas](https://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html#syntax)
3. [Method references](https://docs.oracle.com/javase/tutorial/java/javaOO/methodreferences.html)

It's usually a good idea to create a separate class for your listeners. Here's a short example class demonstrating how to subscribe to events.

```java
import net.luckperms.api.event.EventBus;
import net.luckperms.api.event.log.LogPublishEvent;
import net.luckperms.api.event.user.UserLoadEvent;
import net.luckperms.api.event.user.track.UserPromoteEvent;

public class MyListener {
    private final MyPlugin plugin;

    public MyListener(MyPlugin plugin, LuckPerms luckPerms) {
        this.plugin = plugin;

        EventBus eventBus = luckPerms.getEventBus();

        // 1. Subscribe to an event using an expression lambda
        eventBus.subscribe(this.plugin, LogPublishEvent.class, e -> /* ... */);

      	// 2. Subscribe to an event using a statement lambda
        eventBus.subscribe(this.plugin, UserLoadEvent.class, e -> {
            // ...
        });

        // 3. Subscribe to an event using a method reference
        eventBus.subscribe(this.plugin, UserPromoteEvent.class, this::onUserPromote);
    }

    private void onUserPromote(UserPromoteEvent event) {
        // ...
    }
}
```

If your listener is simple, then an expression or statement lambda is best. If your listener is complex, then method references are probably going to be more organised.

#### Listening for changes to user cached data

If you have a system that depends on a users cached data (e.g. their prefix or permission state), then you may find it necessary to perform some action in your plugin when the data changes (e.g. invalidate or update a cache). The best & most simple event to use to achieve this is the [`UserDataRecalculateEvent`](https://github.com/LuckPerms/LuckPerms/blob/master/api/src/main/java/net/luckperms/api/event/user/UserDataRecalculateEvent.java).

This is a simple event that is "called when a User's cached data is refreshed". It doesn't give any information about what caused the refresh - just that it happened!

#### Listening for changes to permissions/parent groups/etc

Recall from earlier that [all user/group data is stored as `Node`s](#the-basics-of-node) - introducing:

* the [`NodeAddEvent`](https://github.com/LuckPerms/LuckPerms/blob/master/api/src/main/java/net/luckperms/api/event/node/NodeAddEvent.java) - called when a node is added to a user/group
* the [`NodeRemoveEvent`](https://github.com/LuckPerms/LuckPerms/blob/master/api/src/main/java/net/luckperms/api/event/node/NodeRemoveEvent.java) - called when a node is removed from a user/group
* the [`NodeClearEvent`](https://github.com/LuckPerms/LuckPerms/blob/master/api/src/main/java/net/luckperms/api/event/node/NodeClearEvent.java) - called when a user/group has all/some their existing nodes removed

All of these events extend from [`NodeMutateEvent`](https://github.com/LuckPerms/LuckPerms/blob/master/api/src/main/java/net/luckperms/api/event/node/NodeMutateEvent.java) which defines the base properties.

These events cover all possible changes that could be made to a user/groups LuckPerms data. The trick is to figure out which event you need, and how to filter down to only catch the desired changes.

For example, to catch *prefixes* being added to *groups*, you would need to listen to the `NodeAddEvent`, then check if `e.isGroup() && e.getNode().getType() == NodeType.PREFIX`. Of course, afterwards, you could then cast `((Group) e.getTarget())` and `((PrefixNode) node)` to extract further information.

To catch both additions and removals, you can either subscribe to the generic `NodeMutateEvent`, or to both the add and remove events separately.

There is an [example listener in the API Cookbook](https://github.com/LuckPerms/api-cookbook/blob/master/src/main/java/me/lucko/lpcookbook/listener/PlayerNodeChangeListener.java) which demonstrates this nicely.

