## Initial Setup

1. Download the `LuckPerms-???-x.x.x.jar` file that corresponds to your platform. You can find the latest versions [here](https://ci.lucko.me/job/LuckPerms/).
2. Navigate to your mods/plugins directory. This is usually either `/plugins/` or `/mods/`. Then place the LuckPerms jar in this directory.
3. Fully stop & start your server, and allow the default configuration to be generated.
4. Fully stop your server, and open the config file. It will be located at `/plugins/LuckPerms/config.yml` or `/config/luckperms/luckperms.conf`.
5. Read through the config file, and change the options to suit your server, especially taking note of the Storage settings.
6. Start your server again.

## FAQ
### Where do I install LuckPerms?
* If you run a network of servers, you should install LuckPerms into the plugin folder of every server you want to use LuckPerms on.
* If you also want to use LuckPerms to apply permissions on your BungeeCord proxy, you should place LuckPermsBungee.jar into your BungeeCord plugins folder.
* If you choose to only install LuckPerms on your BungeeCord proxy, it will have no impact on any permission checks performed by plugins on any backend Spigot/Sponge servers. If you want that functionality, you need to install LuckPerms on those servers too.

### Can I just install LuckPerms on BungeeCord?
* The permissions system used on BungeeCord is completely separate from the systems used on the backend Spigot/Sponge server.
* If you want the permission checks performed by Spigot/Sponge plugins to be handled by LuckPerms, install LuckPerms on your Spigot/Sponge server.
* If you want the permission checks performed by BungeeCord plugins to be handled by LuckPerms, install LuckPerms on your proxy.
* You **can** just install it on the proxy, but any checks which are performed by Spigot/Sponge plugins will not be handled by LuckPerms.

## Requirements
LuckPerms has a few requirements. The *vast* majority of servers will meet these requirements already.

#### tl;dr
* You need Java 8 or higher
* Your server needs access to the internet the first time you load the plugin

---
### Java 8
Your server must be running **Java 8** or higher. LuckPerms does not work on older versions of Java.

Most MC shared hosting companies have updated by now, but if your provider still doesn't run Java 8, ask them nicely to update. If you control your own server, the update process is very simple. There are plenty of guides available online.

---
### Internet Connection
LuckPerms uses a number of [external libraries](https://github.com/lucko/LuckPerms/wiki/External-connections-and-3rd-party-software), some of which are [downloaded automatically at runtime](https://github.com/lucko/LuckPerms/wiki/External-connections-and-3rd-party-software#external-services).

If your server does not have an internet connection, you can install LP locally (where you do have an internet connection), and then copy the content of the `/LuckPerms/lib/` directory to your other server.

## Compatibility
Some known compatibility issues are outlined below. In all cases, these issues are out of my control - and there's nothing I can do to resolve them in LuckPerms itself. 🙁 

Some of the compatibility issues are resolved in newer releases of the server - but the fixes are not backdated.

### CraftBukkit and Offline Mode
If your server is using CraftBukkit and running in Offline or Cracked mode, LuckPerms (and a number of other plugins, for that matter) will not work. This is due to a [CraftBukkit bug regarding the AsyncPlayerPreLoginEvent](https://hub.spigotmc.org/jira/browse/SPIGOT-3541).

This issue is yet to be resolved. (as of writing on 11th Jan 18)

Your options are:

1. Switch to Spigot or [Paper](https://ci.destroystokyo.com/job/Paper/)
2. Enable online mode

---
### Older Minecraft versions
The main release of LuckPerms is not compatible with Bukkit versions earlier than 1.8.8. 

A LuckPerms release for 1.7.10 can be found on [Jenkins](https://ci.lucko.me/job/LuckPermsLegacy/).

1.7.10 is the earliest version supported by LuckPerms.

---
### Cauldron, Thermos, etc
If you're using Cauldron, Thermos or any other Bukkit-Forge hack, you may encounter errors when trying to load LuckPerms. This is **not** a LuckPerms issue - but rather due to a bug in the server.

These issues have been reported to the respective projects, however none are currently being maintained, so this issue will (most likely) never be fixed. In the meantime, you can hack around these problems using the steps outlined below.

(I offer absolutely **no support** for these fixes.)

1. Navigate to the `libraries/net/md-5/SpecialSource/1.7-SNAPSHOT` directory
2. Delete the `SpecialSource-1.7-SNAPSHOT.jar` file
3. Download SpecialSource v1.7.4 from `https://repo1.maven.org/maven2/net/md-5/SpecialSource/1.7.4/SpecialSource-1.7.4.jar`
4. Copy the jar file to the `libraries/net/md-5/SpecialSource/1.7-SNAPSHOT` directory
5. Rename the jar file you just copied to `SpecialSource-1.7-SNAPSHOT.jar`
6. Start up server. If it stops immediately, you have renamed the SpecialSource wrong.

---
### Essentials
If you're using the "Essentials" bukkit plugin on your server, you may have to perform some extra steps to get it to play nicely with LuckPerms.

#### If you want Essentials to read prefix, suffix & group data from LuckPerms...
You will need to update to **EssentialsX** - an updated version of the original Essentials plugin. The original maintainer of Essentials stopped working on the project in 2014 & recommends EssentialsX as a replacement.

EssentialsX can be found here: [[GitHub]](https://github.com/EssentialsX/Essentials) [[Download]](http://ci.ender.zone/job/EssentialsX/)

If you want to use LuckPerms prefix/suffix data within Essentials, you also need to install [Vault](https://www.spigotmc.org/resources/vault.34315/).

#### If you don't want Essentials to read prefix, suffix & group data from LuckPerms, but still want LuckPerms to handle permission checks from Essentials...
You either need to update to EssentialsX (as detailed above) or...

Delete the `player-commands` section of the Essentials config.

When Essentials cannot detect a "known" permission system (it doesn't recognise LuckPerms!) - it falls back to it's [own config based permission system](https://github.com/essentials/Essentials/blob/2.x/Essentials/src/config.yml#L137-L142) for Essentials commands.
