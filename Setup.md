## Initial Setup

1. Download the `LuckPerms-???-x.x.x.jar` file that corresponds to your platform. You can find the latest versions [here](https://ci.lucko.me/job/LuckPerms/).
2. Navigate to your mods/plugins directory. This is usually either `/server/plugins/` or `/server/mods/`. Then place the LuckPerms jar in this directory.
3. Fully stop & start your server, and allow the default configuration to be generated.
4. Fully stop your server, and open the config file. It will be located at `/plugins/LuckPerms/config.yml` or `/config/luckperms/luckperms.conf`.
5. Read through the config file, and change the options to suit your server, especially taking note of the **Storage** settings.
6. Start your server again.

## Requirements
LuckPerms has a few requirements. The *vast* majority of servers will meet these requirements already.

#### tl;dr
* You need Java 8 or higher
* Your server needs access to the internet the first time you load the plugin

### Java 8
Your server must be running **Java 8** or higher. LuckPerms does not work on older versions of Java.

Most MC shared hosting companies have updated by now, but if your provider still doesn't run Java 8, ask them nicely to update. If you control your own server, the update process is very simple. There are plenty of guides available online.

### Internet Connection
LuckPerms uses a number of [external libraries](https://github.com/lucko/LuckPerms/wiki/External-connections-and-3rd-party-software), some of which are [downloaded automatically at runtime](https://github.com/lucko/LuckPerms/wiki/External-connections-and-3rd-party-software#external-services).

If your server does not have an internet connection, you can install LP locally (where you do have an internet connection), and then copy the content of the `/LuckPerms/libs/` directory to your other server.

### CraftBukkit and Offline Mode
If your server is using CraftBukkit and running in Offline or Cracked mode, LuckPerms (and a number of other plugins, for that matter) will not work. This is due to a [CraftBukkit bug regarding the AsyncPlayerPreLoginEvent](https://hub.spigotmc.org/jira/browse/SPIGOT-3541). 

Your options are:

1. Switch to Spigot or [Paper](https://ci.destroystokyo.com/job/PaperSpigot/) [recommended]
2. Enable online mode

### Older MC versions
The main release of LuckPerms is not compatible with Bukkit versions earlier than 1.8.8.

A LuckPerms release for 1.7.10 can be found on [Jenkins](https://ci.lucko.me/job/LuckPerms/), under "Bukkit-Legacy".