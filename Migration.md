LuckPerms has built in support to allow easy migration of permissions data from existing permissions plugins into LuckPerms.

### Currently Supported:
* **GroupManager** (if you're using this currently, you should urgently switch to something else, even if it isn't LuckPerms. GroupManager is old, buggy and bad.)
* **zPermissions**
* **PermissionsEx**
* **PowerfulPerms**

The migration process is fairly simple, however it varies slightly for each platform.

# How to

1. Place the LuckPerms jar file, as well as the jar of zPermissions, etc... in your servers plugin folder.

## zPermissions, PermissionsEx & GroupManager
These all follow a similar process.

4. Execute the following command:

**/luckperms migration [plugin name] [list of worlds]**

Where the plugin name is the plugin you are importing from.

The list of worlds is required to migrate per-world permission data.

Example:
I have my existing permissions system on zPermissions, and have 3 worlds. world, world_nether and world_end.

I would therefore type into Console: /luckperms migration zpermissions world world_nether world_end

## PowerfulPerms
The process for PowerfulPerms is more complicated.

Users are only loaded into the plugin when they join the server, and the plugins API does not expose a way to get all players from its backend.

This means that during the import process, we have to query the PowerfulPerms MySQL tables to get a list of all users.

The command usage is therefore different.

**/luckperms migration powerfulperms <address> <database> <username> <password> <db table>**

Where:

* address = the address and port of your MySQL server e.g. 127.0.0.1:3306
* database = the name of the database where your PowerfulPerms data is stored
* username = the username to login to the SQL server
* password = the password to login to the SQL server
* db table = the name of the table where player data is stored (or technically a list of UUIDs).

The default db table is "players", however if you have an added table prefix, you will need to include that too.
e.g. if my table prefix is "pp_", the db table should = "pp_players".

# Continuation
If it seems that the command does not exist, check your servers startup log to see that the plugin you are importing from loaded correctly.

The process will start, and give you logging output about the process of the operation in the console. Be patient, it may take some time.

When the process has finished, stop the server, and remove the other jar file, and then start your server again.

# Errors
When writing the migration system, I had to code in most cases against poorly written APIs, APIs that change randomly with almost every release (what's the point in the API!), or in some cases no API whatsoever.

This makes it firstly very hard to design a perfect, bug free solution, and secondly very hard to test. Additionally, everyones dataset is different, and I may not have accounted for errors thrown by the other plugins.

If the process doesn't complete and prints an error message, please submit an Issue on GitHub or drop me a PM on Spigot. The chances are it's a small oversight or bug that I can fix quite easily.