This guide covers how to setup and manage prefixes, suffixes and meta with LuckPerms.

If you are already familiar with these concepts, and just want to view how the commands work, then you should read the [Command Usage: Meta](Meta-Commands) page.

# Key Definitions
### Prefix / Suffix
Prefixes and suffixes on Minecraft servers relate to the text that comes before and after your username in chat.

For example, given the chat message:
```
[Admin] Luck the great: Hello!
```
The prefix is the `"[Admin] "` part, and the suffix is `" the great"` part.

### Meta
Also sometimes referred to as "options" or "variables", meta is just a general term for extra data associated with a user or group. Unlike permissions, meta is split up into two parts, the "key" and the "value". The key is the name of the meta, and the value is whatever the key is set to.

For example, my user might have the following meta, to indicate that I can have a maximum of 5 homes, and that my username should be colored blue.
```
max-homes = 5
username-color: blue
```

## Who provides what?
Generally, plugins which provide and manage permissions on your server will also have functionality to allow you to set, manage and store prefixes/suffixes/meta. This is true of LuckPerms.

Occasionally, permissions plugins will also provide the means to apply this data to the chat. This is not the case for LuckPerms, and you'll need an additional plugin to apply chat formatting for you. More on this later.

## How do prefixes/suffixes/meta get stored
Prefixes and suffixes in LuckPerms are converted and stored as permission nodes. You'll notice that when you add a prefix or suffix to a user/group, that a new entry will appear in their permissions data which relates to the value you set. Why do it this way? Well, it makes things much easier from a programming point of view to have everything stored in the same place, and in similar formats. It also means you can easily manipulate prefix and suffix data in the same way you do for permissions.

Prefixes and suffixes are split up into two parts
* **Weight** - this is just a number which determines the priority of the prefix/suffix. A higher number = a higher weight and a higher priority. 
* **Value** - what the actual value of the prefix is.

A prefix of `"[Admin] "`, set with a weight of 100 translates into the permission: `prefix.100.[Admin] `.

A similar system is used for meta. A meta pair, `favourite-color = red` would translate into the permission: `meta.favourite-color.red`.

## How does prefix/suffix weight work
Prefixes and suffixes can be inherited in the same way as permissions. This means that LuckPerms needs to determine which prefix/suffix to actually use for a player, when it gets requested.

When another plugin asks for a Users prefix/suffix, LuckPerms will:
* Collect all of the prefixes/suffixes the user has and inherits together
* Sorts them according to their weight, where a higher weight number = a higher priority
* Then selects the prefix/suffix with the highest weight to go on to represent the player.

If two entries with the same weight are found, the one closest to the user is used first. Closest meaning the one that was discovered first by the plugin when searching the inheritance tree for data.

## How do I actually set prefixes and suffixes for a user
For example, if I want people in the admin group to have the "&c[Admin] " prefix, and people in the mod group to have the "&d[Mod] " prefix, I would run:

* /lp creategroup admin
* /lp creategroup mod
* /lp group admin parent add mod
* /lp group admin meta addprefix 100 "&c[Admin] "
* /lp group mod meta addprefix 90 "&d[Mod] "

If I then decided I wanted to change admins prefix to use the "&4" color, to remove the previously set value, I'd run:
* /lp group admin meta removeprefix 100

This would remove all prefixes set to admin with a weight of 100. I could then re-set the new prefix value.

The command usage for setting prefixes/suffixes temporarily follows the same format as the commands for adding temporary permissions, or parent groups.

The full command usages can be found [**here**](Meta-Commands). The commands for adding and removing meta are also documented there.

## How do I see the prefixes/suffixes a user or group has
The easiest way to debug issues with prefixes/suffixes is to use the info command.

For example: `/lp user Luck meta info`. This will list all of the prefixes, suffixes and meta a user has and inherits, and will order the entries by weight, so you can easily see which values are being applied.

Another useful command is the general user info command: `/lp user Luck info`. If the player is online on the server, this will show you which of their prefixes is currently being provided to plugins looking to read data from LuckPerms.

## Displaying prefixes and suffixes
As mentioned earlier, LuckPerms does not handle any of the chat formatting for you. You will need to install an external plugin to do it for you.

Some recommendations are listed below.

### Bukkit/Spigot
LuckPerms has support for **any** chat formatting plugin which can read data from [Vault](https://dev.bukkit.org/projects/vault). You need to have Vault installed on your server for this to work.

If you're having issues with a plugin not picking up data correctly, please make sure the output of `/vault-info` shows that data is being read from LuckPerms.

Some popular chat formatting plugins which work with LuckPerms + Vault include:
* [VaultChatFormatter](https://www.spigotmc.org/resources/49016/) - recommended if you just want something simple!
* [EssentialsX Chat](https://essentialsx.net/downloads.html) - recommended if you already have Essentials on your server.
* [ChatEx](https://dev.bukkit.org/projects/chatex)
* [VentureChat](https://www.spigotmc.org/resources/771/)
* [Stylizer](https://www.spigotmc.org/resources/stylizer.78327/) - includes chat formatting and tablist.
* [DisplayFormatter](https://github.com/MCMDEV/displayformatter) - includes chat formatting and tablist, specifically for LuckPerms.
* [CarbonChat](https://github.com/Hexaoxide/Carbon) (beta)
* [DeluxeChat](https://www.spigotmc.org/resources/1277/) (paid)
* [ChatControl](https://builtbybit.com/resources/18217) (paid)
* [CMI](https://www.spigotmc.org/resources/cmi-298-commands-insane-kits-portals-essentials-economy-mysql-sqlite-much-more.3742/) (paid)
* [BetterPrefix](https://www.spigotmc.org/resources/betterprefix-papi-support.18096/)

Some popular tab/nametag formatting plugins which work with LuckPerms + Vault include:
* [NametagEdit](https://www.spigotmc.org/resources/3836/)
* [TAB](https://github.com/NEZNAMY/TAB)
* [Tab](https://www.spigotmc.org/resources/1448/) (paid)
* [CMI](https://www.spigotmc.org/resources/cmi-298-commands-insane-kits-portals-essentials-economy-mysql-sqlite-much-more.3742/) (paid)
* [BetterPrefix](https://www.spigotmc.org/resources/betterprefix-papi-support.18096/)


This is by no means a definitive list. Anything that supports Vault also supports LuckPerms!


### BungeeCord

Some popular chat formatting plugins which work with LuckPerms on BungeeCord include:
* [gChat](https://github.com/lucko/gChat) - recommended if you just want something simple.
* [BungeeChat](https://www.spigotmc.org/resources/12592/)
* [MultiChat](https://www.spigotmc.org/resources/26204/)

Some popular tab/nametag formatting plugins which work with LuckPerms on BungeeCord include:
* [BungeeTabListPlus](https://www.spigotmc.org/resources/313/)
* [TAB](https://github.com/NEZNAMY/TAB)

### Sponge
* [Nucleus](https://nucleuspowered.org/) - an "essentials" like plugin, which also includes a [module for chat formatting](https://nucleuspowered.org/docs/modules/chat.html).

### Fabric
* [Styled Chat](https://modrinth.com/mod/styled-chat) - includes chat formatting, uses [Fabric TextPlaceholderAPI](https://placeholders.pb4.eu) - Note that manual configuration is required and you need to use the [LuckPerms __Fabric__ PlaceholderAPI Addon](https://luckperms.net/download) for this mod to work with LuckPerms.
* [Styled Player List](https://modrinth.com/mod/styledplayerlist) - includes tablist formatting, uses [Fabric TextPlaceholderAPI](https://placeholders.pb4.eu) - Note that manual configuration is required and you need to use the [LuckPerms __Fabric__ PlaceholderAPI Addon](https://luckperms.net/download) for this mod to work with LuckPerms.
* [GraphiXMod](https://github.com/lochnessdragon/GraphiXMod) - includes chat formatting, holograms, tablist and scoreboard.
* [Chatter](https://github.com/Axieum/Chatter) - includes chat formatting and Discord integration

### Forge
* [BetterForgeChat](https://www.curseforge.com/minecraft/mc-mods/betterforgechat-with-luckperms-support) - Includes chat formatting, tablist, ftbessentials nicknames, and markdown styling.
