LuckPerms has built in support to allow easy migration of permissions data from existing permissions plugins to LuckPerms.

## Intro
It should be noted that this system is not perfect. It will do a pretty decent job at converting all of your existing data, and works perfectly in *most cases*. However, not all data is the same, and there are sometimes things I haven't accounted for.

LuckPerms has some similarities with other permission plugins, however, some parts are fundamentally different, and therefore sometimes automatic migration is tricky.

Additionally, letting the plugin migrate all of your data for you means you will not have a chance to learn any of the LuckPerms commands. This may become an issue later on. 😉 If you're migrating from PermissionsEx or GroupManager, you might [find this page useful](GM-&-PEX-Command-Equivalents).

If you have an old permissions setup, or a setup you're not completely happy with, now might be a great time to have a restructure and cleanup, and a chance to learn LuckPerms commands in the process!
   
   
### Supported plugins
* Bukkit / Spigot
  * GroupManager
  * PermissionsEx
  * zPermissions
  * PowerfulPerms
  * bPermissions
  * PermissionsBukkit
  * PowerRanks
* BungeeCord
  * BungeePerms
* Sponge
  * None!
    * Support for migration on Sponge was removed due to API compatibility issues. LuckPerms is now the only supported permissions plugin for Sponge servers, and most users had already migrated or were using LuckPerms already.

## The process
The migration process is fairly simple, however it varies slightly for each platform.

1. Firstly, you need to [install LuckPerms](Installation). Don't remove your old permissions plugin yet.
2. Ensure that your old permissions plugin is still enabling properly. The migration process won't work if your old setup is broken.
3. Start your server - **do not reload** - a full restart is needed when installing LP. 
4. (optional) If you intend to change your data [storage type](Storage-types), for instance, to mysql, it is easiest to do this now. If you decide to change storage types after the migration, follow the instructions in [Switching Storage Types](Switching-storage-types).

Then, open your server console and run the migration command to start the process:

`/lp migration <plugin name>` 

Some plugins also require you to specify extra options/flags. If any are needed, you will be notified in chat before the migration begins.

Then, just let LuckPerms handle the rest! You will be notified of the migration progress, and then notified again once it has finished.

When the process has finished, stop the server, remove the jar file for your old permissions plugin, and start your server again.

The console output during the migration process is purposely verbose and spammy. Messages starting with "(LP) LOG" can be ignored, however stack traces shouldn't be (they usually mention some sort of exception). If your migration output contains stack traces, please report them to me. More info at the bottom of this page. 

## PowerfulPerms
The process for PowerfulPerms is more complicated.

Users are only loaded into the plugin when they join the server, and the plugins API does not expose a way to get all players from its backend.

This means that during the import process, we have to query the PowerfulPerms MySQL tables to get a list of all users.

The command usage is therefore different.

`/luckperms migration powerfulperms [address] [database] [username] [password] [db table]`

Where:
* address = the address and port of your MySQL server e.g. 127.0.0.1:3306
* database = the name of the database where your PowerfulPerms data is stored
* username = the username to login to the SQL server
* password = the password to login to the SQL server
* db table = the name of the table where player data is stored (although we're only concerned about a list of uuids).

The default db table, as far as I know, is "players", however if you have an added table prefix, you will need to include that too.

e.g. if my table prefix is "pp_", the db table should = "pp_players". (without the quotes)

For example: `/luckperms migration powerfulperms 127.0.0.1:3306 minecraft root passw0rd players`

## Errors
If it seems that the migration command does not exist, check your server's startup log to check if the plugin you are importing from loaded correctly.

If the process doesn't complete and prints an error message, please submit an Issue on GitHub or [contact me here](https://github.com/lucko/LuckPerms/wiki#2-speech_balloon-discord). I'll try to reply to you ASAP.
