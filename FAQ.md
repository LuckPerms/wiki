# Frequently Asked Questions
These are some of the questions I get asked quite frequently. I'd appreciate it if you check to see if your question has already been answered here before asking me directly. 😄 

### Prefixes/Suffixes don't show in chat, tab, ...
LuckPerms doesn't manage the chat, tab list or whereever you want to display the prefix/suffix.  
You need to use a separate plugin for this. A popular example for a chat plugin is [EssentialsX](https://ci.ender.zone/job/EssentialsX/) with EssentialsXChat, but you may use any plugin that either hooks into [Vault](https://dev.bukkit.org/bukkit-plugins/vault/) or the LuckPerms API.

BungeeCord and Sponge don't have a plugin similar to vault, meaning that the plugin has to hook into the LuckPerms API directly to retrieve and display the prefix/suffix.

A list of (known) supported plugins can be found [here](https://github.com/lucko/LuckPerms/wiki/Prefixes,-Suffixes-&-Meta#displaying-prefixes-and-suffixes).

### How do I get permissions to sync across multiple servers
Connect each LuckPerms installation to the same MySQL/MongoDB server. You can use `/luckperms sync` to pull the latest changes from the database. You can also [setup a Messaging Service](https://github.com/lucko/LuckPerms/wiki/Network-Installation#messaging-service) to have your changes sync instantly between servers.

### MySQL errors

Such as:

* LuckPerms cannot connect to my MySQL server
* I'm getting an annoying SSL warning message
* "No operations allowed after connection closed" error

Please see [here](https://github.com/lucko/LuckPerms/wiki/Storage-system-errors).

### I use SpongeForge and when I install LuckPerms do plugins no longer work for OPs
This is an intentional behaviour of SpongeForge. As soon as a permission plugin, in this case LuckPerms, is installed will it disable the OP system.  
To fix this give the groups and users the required permissions for the plugins.

### What versions does LuckPerms support?
The latest version of LuckPerms supports MC versions from 1.8.8 up to the latest release which is currently 1.15.1.  
For the version 1.7.10 will you need to use the Legacy version of LuckPerms, which can be found on [Jenkins](https://ci.lucko.me/view/LuckPerms/job/LuckPerms/).  
Even older versions are not supported.
