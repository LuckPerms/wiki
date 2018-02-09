# Frequently Asked Questions
These are some of the questions I get asked quite frequently. I'd appreciate it if you check to see if your question has already been answered here before asking me directly. 😄 

### I'm using EssentialsChat and it's not working
Please make sure you are using the latest version of [EssentialsX](https://ci.drtshock.net/job/essentialsx/) and you have [Vault](https://dev.bukkit.org/bukkit-plugins/vault/) installed on your server. The "**X**" part of Essentials**X** is important - the older versions of Essentials do not work.

### Where do I install LuckPerms?
If you run a network of servers, you should install LuckPerms into the plugin folder of every server you want to use LuckPerms on.

If you also want to use LuckPerms to apply permissions on your BungeeCord proxy, you should place LuckPermsBungee.jar into your BungeeCord plugins folder.

If you choose to only install LuckPerms on your BungeeCord proxy, it will have no impact on any permission checks performed by plugins on any backend Spigot/Sponge servers. If you want that functionality, you need to install LuckPerms on those servers too.

### Can I just install LuckPerms on BungeeCord?
The permissions system used on BungeeCord is completely separate from the systems used on the backend Spigot/Sponge server.

If you want the permission checks performed by Spigot/Sponge plugins to be handled by LuckPerms, install LuckPerms on your Spigot/Sponge server.

If you want the permission checks performed by BungeeCord plugins to be handled by LuckPerms, install LuckPerms on your proxy.

You **can** just install it on the proxy, but any checks which are performed by Spigot/Sponge plugins will not be handled by LuckPerms.

### How do I get permissions to sync across multiple servers
Connect each LuckPerms installation to the same MySQL/MongoDB server. You can use `/luckperms sync` to pull the latest changes from the database. You can also [setup a Messaging Service](https://github.com/lucko/LuckPerms/wiki/Instant-Update-Propagation#messaging-services) to have your changes sync instantly between servers.

### MySQL errors

Such as:

* LuckPerms cannot connect to my MySQL server
* I'm getting an annoying SSL warning message
* "No operations allowed after connection closed" error

Please see [here](https://github.com/lucko/LuckPerms/wiki/Storage-system-errors).