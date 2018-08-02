# Frequently Asked Questions
These are some of the questions I get asked quite frequently. I'd appreciate it if you check to see if your question has already been answered here before asking me directly. 😄 

### I'm using EssentialsChat and it's not working
Please make sure you are using the latest version of [EssentialsX](https://ci.ender.zone/job/EssentialsX/) and you have [Vault](https://dev.bukkit.org/bukkit-plugins/vault/) installed on your server. The "**X**" part of Essentials**X** is important - the older versions of Essentials do not work.

### How do I get permissions to sync across multiple servers
Connect each LuckPerms installation to the same MySQL/MongoDB server. You can use `/luckperms sync` to pull the latest changes from the database. You can also [setup a Messaging Service](https://github.com/lucko/LuckPerms/wiki/Network-Installation#messaging-service) to have your changes sync instantly between servers.

### MySQL errors

Such as:

* LuckPerms cannot connect to my MySQL server
* I'm getting an annoying SSL warning message
* "No operations allowed after connection closed" error

Please see [here](https://github.com/lucko/LuckPerms/wiki/Storage-system-errors).