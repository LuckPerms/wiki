# Intro
LuckPerms fully implements the [Vault](https://dev.bukkit.org/bukkit-plugins/vault/) Chat and Permission API, meaning most plugins that depend on Permissions or Chat integration will work seamlessly with LuckPerms, even if the plugin was made before LuckPerms was.

The Permissions part of the API simply hooks with LuckPerms, allowing other plugins to modify permissions. Even though it would make sense to have a separate plugin to handle the Chat part of Vault, it is most common that permissions plugins do this too.

LuckPerms stores all data about groups and players in the form of permission nodes. Vault Chat requires a way to store and read special "meta" about a player, as well as a prefix and suffix. These are stored within LuckPerms as special permission nodes.

## Chat (Prefix/Suffix)
Prefixes and suffixes are stored in two separate permission nodes. These permission nodes behave like any other permission you set in LuckPerms, and can therefore be inherited, or only apply in certain servers, worlds, etc.

The node for storing prefixes and suffixes follows the format: prefix.priority.the_prefix & suffix.priority.the_suffix

If a user/group has or inherits multiple prefixes, the one with the highest priority applies.

### Example:
I want people in the admin group to have the "&c[Admin]" prefix, and people in the mod group to have a "&d[Mod]" prefix. To achieve this, I would run the following commands:

* /luckperms creategroup admin
* /luckperms creategroup mod
* /luckperms group admin setinherit mod
* /luckperms group admin set prefix.100.&c[Admin] true
* /luckperms group mod set prefix.90.&d[Mod] true

### Displaying Prefixes and Suffixes
LuckPerms does **not** format the chat for you. It only provides a way to store this data. You will need a Vault compatible chat formatting plugin to actually change how the chat looks.

## Meta
For the most part, server admins will rarely ever need to touch the meta system. However, I'll provide some brief docs on it anyway.

Vault Chat requires that LuckPerms provides a way to store "meta". This "meta" could be an Integer, Double, Boolean or String (Text). Think of it as a key value store.

The key, or as Vault calls them, nodes, is what the values, or "meta" is stored under.

Meta is stored in a similar way to prefixes and suffixes, except they are not inherited.

### Example
* Vault wants to store a value of "3.3" against the node "something".
* LuckPerms will convert this into the permission node: meta.something.3{SEP}3

### More info
If you're interested in utilising the Meta system, I suggest you check out [the Vault Chat API class](https://github.com/MilkBowl/VaultAPI/blob/master/src/main/java/net/milkbowl/vault/chat/Chat.java) and the [LuckPerms implementation of it](https://github.com/lucko/LuckPerms/blob/master/bukkit/src/main/java/me/lucko/luckperms/api/vault/VaultChatHook.java). If you don't understand it, just forget you ever read this. :sweat_smile: 