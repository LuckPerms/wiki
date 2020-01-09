# Frequently Asked Questions
These are some of the questions that are asked quite frequently. Please check to see if your question has already been answered here before seeking support.

**Tip: Always check your console for any errors during start up or whenever something goes wrong!**

***

### Why are permissions not working?
First, *make sure LuckPerms is your only permission plugin!* We have had many issues where people will install LuckPerms and not remove another permission manager like PermissionsEx. You *must* remove any other permission plugins otherwise LuckPerms will not be used for permission checking. The only exception is when you are performing a migration, in which case you must have both permission plugins installed but please remember to remove the old plugin afterwards.

If LuckPerms is your only permission plugin, then the issue could be that you have not added the correct permissions for what you require. Always make sure to consult the documentation of the plugins you are using to see what the available permissions are. If the documentation is incomplete, then you can use [Verbose mode](https://github.com/lucko/LuckPerms/wiki/Verbose) to see which permissions are being checked in real time and what value LuckPerms returns for the user that is being checked.

***

### Why are prefixes not working?
Most of the time this isn't actually an issue with LuckPerms itself but here are a few troubleshooting tips:

- LuckPerms is *not* a chat formatter and another plugin is required to format the chat or tab list to include prefixes and suffixes.
  - If you are running a Bukkit based server (CraftBukkit, Spigot, Paper) then you also need to install [Vault](https://dev.bukkit.org/bukkit-plugins/vault/).
  - Some popular chat formatting plugins are listed [here](https://github.com/lucko/LuckPerms/wiki/Prefixes,-Suffixes-&-Meta#displaying-prefixes-and-suffixes).
- Firstly, you should check if a prefix/suffix is actually set with LuckPerms - run `/lp user <user> info` and see if the prefix/suffix is displayed correctly. If so, great! LuckPerms has done its job and now it's up to your chat/tab/whatever formatter to display it correctly. If not, you need to [set a prefix or suffix](https://github.com/lucko/LuckPerms/wiki/Prefixes,-Suffixes-&-Meta).
- If you are using Essentials, make sure you are running [EssentialsX and EssentialsXChat](https://ci.ender.zone/job/EssentialsX/). The X is important! Other versions of Essentials may not work correctly with LuckPerms.
  - Run `/ess version` for a quick rundown on your Essentials setup, this also reports whether Vault is installed and which permission plugin you are running - preferably LuckPerms!
  - Essentials provides the `{DISPLAYNAME}` placeholder to its chat formats which will combine the prefix, nickname and suffix into one. If you do not like this behaviour then you can change the `add-prefix-suffix` option to `false` in the Essentials config.
- Are your prefixes/suffixes displaying, but not the right ones? You most likely need to set the priority/weight correctly. If you type `/lp user <user> meta info` and see a bunch of zeroes, or some/all of the numbers (priorities) are the same, LuckPerms will take the first highest one and use that as that user's prefix/suffix. To change these, you will need to [set the prefix again using the correct command](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta#lp-usergroup-usergroup-meta-setprefix-priority-prefix-context) - or you can easily edit the number using the web editor. Prefixes and suffixes are stored as permissions, just like everything else, they look similar to this: `prefix.100.[Admin]` - the `100` there is the priority and this is the number you would change to edit it.
- Lastly, the `meta-formatting` section of the LuckPerms config is very important and you should make sure you only change it when necessary (e.g. [prefix/suffix stacking](https://github.com/lucko/LuckPerms/wiki/Prefix-&-Suffix-Stacking)). It's possible your prefixes/suffixes are not working because this section has been tampered with. If you want to set it back to default, make sure the `format` looks like this:
```
    format:
      - "highest"
```

***

### How do I get permissions to sync across multiple servers?
This is explained in detail on the [Network Installation](https://github.com/lucko/LuckPerms/wiki/Network-Installation) page. You should also read [Syncing data between servers](https://github.com/lucko/LuckPerms/wiki/Syncing-data-between-servers). Here is a brief rundown:

- You need the Bungeecord version of LuckPerms installed on your proxy.
- You need LuckPerms installed on each of your backend (Spigot, Sponge) servers.
- You must ensure IP forwarding is enabled on Bungeecord and that the Spigot servers have `bungeecord: true`.
- You must use the same [remote storage method](https://github.com/lucko/LuckPerms/wiki/Storage-types#remote-databases) (such as MySQL) on ALL of your LuckPerms installations. This requires the `storage-method` property to be set as well as the database credentials on all servers.
- Ensure your servers are all connected to the correct database by running `/lp info` and checking if the storage method is correct. Use `/lpb info` for Bungeecord (run it from the console if you run into permission errors).
- If you are using MySQL or MariaDB, set the [`messaging-service`](https://github.com/lucko/LuckPerms/wiki/Configuration#messaging-service) to `sql` on all servers. This will enable syncing for all of your servers when a change is made to the database.

***

### MySQL errors

Such as:

* LuckPerms cannot connect to my MySQL server
* I'm getting an annoying SSL warning message
* "No operations allowed after connection closed" error

Please see [here](https://github.com/lucko/LuckPerms/wiki/Storage-system-errors).

***

### I use SpongeForge and when I install LuckPerms I lose all my permissions, why?
This is an intentional behaviour of SpongeForge. As soon as a permission plugin is installed it will disable the OP system.  
To fix this, give the groups and users the required permissions for the plugins. If you want OP-like permissions, you can use the wildcard `*` but this is considered [bad practice](https://nucleuspowered.org/docs/configuration/permissions.html#nucleus-is-not-a-permissions-management-plugin).

***

### What versions does LuckPerms support?
The latest version of LuckPerms supports MC versions from 1.8.8 up to the latest release which is currently 1.15.1.  
For the version 1.7.10 will you need to use the Legacy version of LuckPerms, which can be found on [Jenkins](https://ci.lucko.me/view/LuckPerms/job/LuckPerms/).  
Even older versions are not supported.
