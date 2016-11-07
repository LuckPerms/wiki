# Frequently Asked Questions
These are some of the questions I get asked quite frequently. I'd appreciate it if you check to see if your question has already been answered here before asking me directly. 😄 

### I'm using EssentialsChat and it's not working
Please make sure you are using the latest version of [EssentialsX](https://www.spigotmc.org/resources/essentialsx.9089/) and you have [Vault](https://dev.bukkit.org/bukkit-plugins/vault/) installed on your server. The "**X**" part of Essentials**X** is important - the older versions of Essentials do not work.

### Where do I install LuckPerms?
If you run a network of servers, you should install LuckPerms into the plugin folder of every server you want to use LuckPerms on.

If you also want to use LuckPerms to apply permissions on your BungeeCord proxy, you should place LuckPermsBungee.jar into your BungeeCord plugins folder.

If you choose to only install LuckPerms on your BungeeCord proxy, it will have no impact on any permission checks performed by plugins on any backend Spigot/Sponge servers. If you want that functionality, you need to install LuckPerms on those servers too.

### How do I get permissions to sync across multiple servers
Connect each LuckPerms installation to the same MySQL/MongoDB server. You can use `/luckperms sync` to pull the latest changes from the database. If you're also using Redis, you can use `/luckperms networksync` to push changes to other connected servers.
