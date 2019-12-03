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
  * [Modifying existing nodes](https://github.com/lucko/LuckPerms/wiki/Developer-API:-Usage#modifying-existing-nodes)
* [Reading user/group data](#reading-usergroup-data)
* [Modifying user/group data](#modifying-usergroup-data)
* [The basics of Context](#the-basics-of-context)
  * [Important classes](#important-classes)
  * [Registering ContextCalculators](#registering-contextcalculators)
  * [Querying active contexts/query options](#querying-active-contextsquery-options)
* [The basics of CachedData](#the-basics-of-cacheddata)
  * [Performing permission checks](#performing-permission-checks)
  * [Retrieving prefixes and suffixes](#retrieving-prefixessuffixes)
  * [Retrieving meta data](#retrieving-meta-data)
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
    
    return luckPerms.getUserManager().getUser(player.getUniqueId());
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
    UserManager userManager = luckPerms.getUserManager();
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
    UserManager userManager = luckPerms.getUserManager();
    CompletableFuture<User> userFuture = userManager.loadUser(uuid);

    return userFuture.join(); // ouch!
}
```

You can then do whatever you want with the user instance - but remember, this method should only ever be called from an async task!

The other option is to embrace callbacks.

In an ideal world, we'd be able to do something like this, without any consequences.

```java
public boolean isAdmin(UUID who) {
    User user = luckPerms.getUserManager().loadUser(who);
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
    return luckPerms.getUserManager().loadUser(who)
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
Group group = luckPerms.getGroupManager().getGroup(groupName);
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
    luckPerms.getUserManager().saveUser(user);
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
        .expiry(1, TimeUnit.HOURS)
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
PrefixNode node = PrefixNode.builder(100, "[Some Prefix]").build();

// build a suffix node
SuffixNode node = SuffixNode.builder(150, "[Some Suffix]").build();

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
List<Node> getNodes()
```

* This method returns an un-flattened (or squashed) list of the user/groups nodes. 
* Entries nearer the start of the list (index zero) have priority over nodes at the end.
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

Or even more complicated queries, like finding the max priority of a temporary prefix held on a specific server.

```java
int maxWeight = user.getNodes().stream()
        .filter(Node::hasExpiry)
        .filter(NodeType.PREFIX::matches)
        .map(NodeType.PREFIX::cast)
        .filter(n -> n.getContexts().getAnyValue(DefaultContextKeys.SERVER_KEY)
                .map(v -> v.equals("factions")).orElse(false))
        .mapToInt(ChatMetaNode::getPriority)
        .max()
        .orElse(0);
```

#### `.getDistinctNodes()`

The method signature is:

```java
SortedSet<Node> getDistinctNodes();
```

* This method returns a sorted view of `#getNodes`. If you are not worried about ordering, it's faster to use `#getNodes`.
* The nodes are sorted according to "priority order". As the returned type is a set, duplicate elements may be missing.
* This view does **not** consider inherited data.

___

### Modifying user/group data

User/group data can be modified by adding and removing `Node`s from the holders data. This can be done by calling `#data` and calling the methods on the returned `NodeMap`.

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

ImmutableContextSet set2 = ImmutableContextSet.of("world", "world_nether");

ImmutableContextSet set3 = ImmutableContextSet.builder()  
    .add("world", "world_nether")
    .add("server", "survival")
    .build();

Map<String, String> map = new HashMap<>();
map.put("region", "something");

ImmutableContextSet set4 = ImmutableContextSet.create();
map.forEach(set4::add);
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
| Nukkit     | `cn.nukkit.Player`                                 |

In order to provide your own context, you need to create and register a `ContextCalculator`.

For example, if I wanted to provide a context for the player's gamemode, in order to set permissions for players only when they are in creative, I'd create a calculator as follows.
The `estimatePotentialContexts` method can be added, but is not necessary, to show context suggestions in the tab completion.

```java
public class CustomCalculator implements ContextCalculator<Player> {

    @Override  
    public void calculate(Player t, ContextConsumer contextConsumer) {
        contextConsumer.add("gamemode", t.getGameMode().name());
    }
    
    @Override
    public ContextSet estimatePotentialContexts() {
        ImmutableContextSet.Builder builder = ImmutableContextSet.builder();
        for (GameMode gameMode : GameMode.values()) {
            builder.add(KEY, gameMode.name().toLowerCase());
        }
        return builder.build();
    }
    
}
```

Then register it using

```java
api.getContextManager().registerCalculator(new CustomCalculator());
```

#### Querying active contexts/query options

You can query the "active" contexts/query options of a Subject using the `ContextManager`.

If you already have an instance of the subject type, you can query directly using this.

```java
Player player = ...;

ImmutableContextSet contextSet = api.getContextManager().getContext(player);
QueryOptions queryOptions = api.getContextManager().getQueryOptions(player);
```

If you only have a `User`, you can still perform a lookup, however, a result will only be returned if the corresponding subject (player) is online.

```java
Optional<ImmutableContextSet> contextSet = api.getContextManager().getContext(user);
Optional<QueryOptions> queryOptions = api.getContextManager().getQueryOptions(user);
```

If you absolutely need to obtain an instance, you can fallback to the server's "static" context/query option. (these are formed using calculators which provide contexts/query options regardless of the passed subject.)

```java
ContextManager cm = api.getContextManager();

ImmutableContextSet contextSet = cm.getContext(user).orElse(cm.getStaticContext());
QueryOptions queryOptions = cm.getQueryOptions(user).orElse(cm.getStaticQueryOptions());
```

___

### The basics of CachedData

All `User`s and `Group`s also have an extra object attached to them called `CachedData`. This is the name of the caching class used by LuckPerms to store easily query-able data for all permission holders.

The lookup methods provided by this class are very fast. If you're doing frequent data lookups, it is highly recommended that if possible, you use `CachedData` over the methods in `User` and `Group`.

Everything in `CachedData` is indexed by `QueryOptions`, as this is how LuckPerms processes all lookups internally.

The contained data is split into two separate sections: `CachedPermissionData` and `CachedMetaData`.

`CachedPermissionData` contains the user/groups fully resolved map of permissions, and allows you to run permission checks in exactly the same way as you would using the Player class provided by the platform.

`CachedMetaData` contains information about a user/groups prefixes, suffixes, and meta values.

#### Obtaining `CachedPermissionData` and `CachedMetaData`

You need:

* A `User` or `Group` instance

* The `QueryOptions` to get the data in (see above for how to obtain this)

```java
PermissionData permissionData = user.getCachedData().getPermissionData(queryOptions);
MetaData metaData = user.getCachedData().getMetaData(queryOptions);
```

#### Performing permission checks

```java
// run a permission check!
Tristate checkResult = permissionData.checkPermission("some.permission.node");

// the same as what Player#hasPermission would return
boolean checkResultAsBoolean = checkResult.asBoolean();
```

We can put all of this together to create a method that can run a "normal" permission check with passed a `User` and a `String` (the permission).

```java
public boolean hasPermission(User user, String permission) {
    ContextManager contextManager = api.getContextManager();
    ImmutableContextSet contextSet = contextManager.getContext(user).orElseGet(contextManager::getStaticContext);

    PermissionData permissionData = user.getCachedData().getPermissionData(QueryOptions.contextual(contextSet));
    return permissionData.getPermissionValue(permission).asBoolean();
}
```

#### Retrieving prefixes/suffixes

```java
String prefix = metaData.getPrefix();
String suffix = metaData.getSuffix();
```

#### Retrieving meta data

```java
List<String> defaultValues = new ArrayList<>();
defaultValues.add("default-value");

String metaResult = metaData.getMeta().getOrDefault("some-key", defaultValues);
```

___

### Listening to LuckPerms events

All event interfaces can be found in the [`net.luckperms.api.event`](https://github.com/lucko/LuckPerms/tree/master/api/src/main/java/net/luckpermapi/event) package. They all extend [`LuckPermsEvent`](https://github.com/lucko/LuckPerms/blob/master/api/src/main/java/net/luckperms/api/event/LuckPermsEvent.java).

To listen to events, you need to obtain the [`EventBus`](https://github.com/lucko/LuckPerms/blob/master/api/src/main/java/net/luckperms/api/event/EventBus.java) instance, using `LuckPerms#getEventBus`.

It's usually a good idea to create a separate class for your listeners. Here's a short example class you can reference.

```java
import net.luckperms.api.event.EventBus;
import net.luckperms.api.event.log.LogPublishEvent;
import net.luckperms.api.event.user.UserLoadEvent;
import net.luckperms.api.event.user.track.UserPromoteEvent;

public class TestListener {
    private final MyPlugin plugin;

    public TestListener(MyPlugin plugin, LuckPerms api) {
        this.plugin = plugin;

        // get the LuckPerms event bus
        EventBus eventBus = api.getEventBus();

        // subscribe to an event using a lambda
        eventBus.subscribe(LogPublishEvent.class, e -> e.setCancelled(true));

        eventBus.subscribe(UserLoadEvent.class, e -> {
            System.out.println("User " + e.getUser().getUsername() + " was loaded!");
            if (e.getUser().hasPermission("some.perm", true)) { <!-- Has problems -->
                // Do something
            }
        });

        // subscribe to an event using a method reference
        eventBus.subscribe(UserPromoteEvent.class, this::onUserPromote);
    }

    private void onUserPromote(UserPromoteEvent event) {
        // as we want to access the Bukkit API, we need to use the scheduler to jump back onto the main thread.
        Bukkit.getScheduler().runTask(plugin, () -> {
            Bukkit.broadcastMessage(event.getUser().getUsername() + " was promoted to" + event.getGroupTo().get() + "!");

            Player player = Bukkit.getPlayer(event.getUser().getUniqueId());
            if (player != null) {
                player.sendMessage("Congrats!");
            }
        });
    }

}
```

`EventBus#subscribe` returns an [`EventSubscription`](https://github.com/lucko/LuckPerms/blob/master/api/src/main/java/net/luckperms/api/event/EventSubscription.java) instance, which can be used to unregister the listener when your plugin disables.
