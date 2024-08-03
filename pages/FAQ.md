# Frequently Asked Questions
These are some of the questions that are asked quite frequently. Please check to see if your question has already been answered here before seeking support.

**Tip: Always check your console for any errors during start up or whenever something goes wrong!**

***

### Why are permissions not working?
First, *make sure LuckPerms is your only permission plugin!* We have had many issues where people will install LuckPerms and not remove another permission manager like PermissionsEx. You *must* remove any other permission plugins otherwise LuckPerms will not be used for permission checking. The only exception is when you are performing a migration, in which case you must have both permission plugins installed but please remember to remove the old plugin afterwards.

If LuckPerms is your only permission plugin, then the issue could be that you have not added the correct permissions for what you require. Always make sure to consult the documentation of the plugins you are using to see what the available permissions are. If the documentation is incomplete or you're unable to find any, then you can use [Verbose mode](Verbose) to see which permissions are being checked in real-time and what value LuckPerms returns for the user that is being checked.

If you are running a Fabric server with LuckPerms, you **cannot use permissions with vanilla commands**. Unlike Bukkit/Spigot and Sponge, Fabric does not add permission checks for vanilla commands. This is not an issue with LuckPerms. However, since Fabric supports modifying the base game, you may install an additional mod to add those permission checks, such as [Minecraft Command Permissions](https://github.com/lucko/minecraft-command-permissions-fabric) or [Command Hider](https://github.com/LoganDark/fabric-command-hider).

Also note that individual mods may not support permissions either, as permissions in Fabric are not yet as standardized as they are in Bukkit/Spigot or Sponge.

***

### Why are prefixes/suffixes not working?
Most of the time this isn't actually an issue with LuckPerms itself but here are a few troubleshooting tips:

- LuckPerms is *not* a chat formatter and another plugin is required to format the chat or tab list to include prefixes and suffixes.
  - If you are running a Bukkit based server (CraftBukkit, Spigot, Paper) then you also need to install [Vault](https://dev.bukkit.org/bukkit-plugins/vault/).
  - Some popular chat formatting plugins are listed [here](Prefixes,-Suffixes-&-Meta#displaying-prefixes-and-suffixes).
- Firstly, you should check if a prefix/suffix is actually set with LuckPerms - run `/lp user <user> info` and see if the prefix/suffix is displayed correctly. If so, great! LuckPerms has done its job and now it's up to your chat/tab/whatever formatter to display it correctly. If not, you need to [set a prefix or suffix](Prefixes,-Suffixes-&-Meta).
- If you are using Essentials, make sure you are running [EssentialsX and EssentialsXChat](https://ci.ender.zone/job/EssentialsX/). The X is important! Other versions of Essentials may not work correctly with LuckPerms.
  - Run `/ess version` for a quick rundown on your Essentials setup, this also reports whether Vault is installed and which permission plugin you are running - preferably LuckPerms! If the command only returns a message like "Reloaded Essentials [version]" then you are using an unsupported version of Essentials and should update to EssentialsX (linked above).
  - Essentials provides the `{DISPLAYNAME}` placeholder to its chat formats which will combine the prefix, nickname and suffix into one. If you do not like this behaviour then you can change the `add-prefix-suffix` option to `false` in the Essentials config.
- Are your prefixes/suffixes displaying, but not the right ones? You most likely need to set the priority/weight correctly. If you type `/lp user <user> meta info` and see a bunch of zeroes, or some/all of the numbers (priorities) are the same, LuckPerms will take the first highest one and use that as that user's prefix/suffix. To change these, you will need to [set the prefix again using the correct command](Meta-Commands#lp-usergroup-usergroup-meta-setprefix-priority-prefix-context) - or you can easily edit the number using the web editor. Prefixes and suffixes are stored as permissions, just like everything else, they look similar to this: `prefix.100.[Admin]` - the `100` there is the priority and this is the number you would change to edit it.
- Lastly, the `meta-formatting` section of the LuckPerms config is very important and you should make sure you only change it when necessary (e.g. [prefix/suffix stacking](Prefix-&-Suffix-Stacking)). It's possible your prefixes/suffixes are not working because this section has been tampered with. If you want to set it back to default, make sure the `format` looks like this:
```
    format:
      - "highest"
```

***

### How do I get permissions to sync across multiple servers?
This is explained in detail on the [Network Installation](Network-Installation) page. You should also read [Syncing data between servers](Syncing-data-between-servers). Here is a brief rundown:

- You need the Bungeecord version of LuckPerms installed on your proxy if:
  - you want to manage Bungeecord permissions (in most cases, you do), or
  - you set your messaging-service to `pluginmsg` (not recommended when using a SQL database).
- You need LuckPerms installed on each of your backend (Spigot, Sponge) servers.
- You must ensure IP forwarding is enabled on Bungeecord and that the Spigot servers have `bungeecord: true` set in their spigot.yml file.
- You must use the same [remote storage method](Storage-types#remote-databases) (such as MySQL) on ALL of your LuckPerms installations. This requires the `storage-method` property to be set as well as the database credentials to be identical on all servers.
- Ensure your servers are all connected to the correct database by running `/lp info` and checking if the storage method is correct. Use `/lpb info` for Bungeecord (run it from the console if you run into permission errors).
- If you are using MySQL or MariaDB, set the [`messaging-service`](Configuration#messaging-service) to `sql` on all servers. This will enable syncing for all of your servers when a change is made to the database.

***

### MySQL errors

Such as:

* LuckPerms cannot connect to my MySQL server
* I'm getting an annoying SSL warning message
* "No operations allowed after connection closed" error

Please see [here](Storage-system-errors).

***

### I use SpongeForge and when I install LuckPerms I lose all my permissions, why?
This is intentional behaviour of SpongeForge. As soon as a permission plugin is installed, it will disable the OP system.  
To fix this, you need to give your groups and users the required permissions. If you want OP-like permissions, you can use the wildcard `*` but this is [not recommended](https://nucleuspowered.org/docs/nowildcard.html).

***

### What versions does LuckPerms support?
LuckPerms supports Minecraft versions from 1.8.8 up to the latest release.  

If you want to use LuckPerms on a Bukkit 1.7.10 server, you will need to use the Bukkit-Legacy jar, available [here](https://luckperms.net/download).

***

### When I install LuckPerms my server shuts down
LuckPerms will never shut down your server.  

If you use AuthMe, make sure to check your console for the following lines:  
```
[AuthMe] Aborting initialization of AuthMe: [InjectorReflectionException]: Could not invoke method 'setup' for fr.xephi.authme.permission.PermissionsManager@xxxxxxxx
[AuthMe] THE SERVER IS GOING TO SHUT DOWN AS DEFINED IN THE CONFIGURATION!
```

If those lines are shown, the server was shut down by AuthMe, due to a configuration setting it has by default.

To fix, open the AuthMe config.yml and change `forceVaultHook` from false to true.

***

### LuckPerms cannot download dependencies 
LuckPerms requires an internet connection to be able to download its dependencies. If LuckPerms does not have a connection or a host is blocking it, the plugin will **not** work.

> me.lucko.luckperms.common.dependencies.DependencyDownloadException: java.net.ConnectException: Connection refused (Connection refused)

An error like this either means that **a)** the server doesn't have an internet connection or **b)** your host is blocking the connection.

Do either of the following to resolve this:

- You can install LP locally (where you do have an internet connection), and then copy the content of the `/LuckPerms/libs/` directory to your other server, into the folder `/LuckPerms/libs/`.

- Contact your server host to allow connections from [libraries.luckperms.net](https://libraries.luckperms.net/) and [repo1.maven.org](https://repo1.maven.org/maven2/).


