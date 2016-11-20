Command usage is printed to the console/chat whenever invalid arguments are provided. **Simply typing /perms** will list all commands a user has permission to use.

### Aliases
A list of aliases for each platform are listed below. Each command works in exactly the same manner, so you can use whichever you prefer.

| Bukkit / Sponge  | Bungee           |
|------------------|------------------|
| /luckperms       | /luckpermsbungee |
| /perms           | /bperms          |
| /permissions     | /bpermissions    |
| /lp              | /lpb             |
| /perm            | /bperm           |

**Important**: Commands are different on BungeeCord. This is so you can choose where your command gets directed to. If commands were the same, you would never be able to control LuckPerms on a backend server.

If you are using Bukkit/Spigot, by default, all OPed users have access to LuckPerms commands. You can change this in the config.

# Overview
Arguments Key: \<required\> [optional]

### General
*  [/perms](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms)
*  [/perms `sync`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-sync)
*  [/perms `networksync`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-networksync)
*  [/perms `info`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-info)
*  [/perms `verbose` \<true|false\> [filters...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-verbose)
*  [/perms `import` \<file\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-import)
*  [/perms `creategroup` \<group\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-creategroup)
*  [/perms `deletegroup` \<group\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-deletegroup)
*  [/perms `listgroups`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-listgroups)
*  [/perms `createtrack` \<track\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-createtrack)
*  [/perms `deletetrack` \<track\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-deletetrack)
*  [/perms `listtracks`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-listtracks)

### Super Secret Console Commands
*  [/perms `export` \<file\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-export)
*  [/perms `migration`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-migration)
*  [/perms `queuecommand` \<command args...\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-queuecommand)

### User   (/lp user \<user\> ...)
*  [/perms user \<user\> `info`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-user-user-info)
*  [/perms user \<user\> `permission`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#permission---lp-user-user-permission---lp-group-group-permission-)
*  [/perms user \<user\> `parent`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#parent---lp-user-user-parent---lp-group-group-parent-)
*  [/perms user \<user\> `meta`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#meta---lp-user-user-meta---lp-group-group-meta-)
*  [/perms user \<user\> `switchprimarygroup` \<group\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-user-user-switchprimarygroup)
*  [/perms user \<user\> `promote` \<track\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-user-user-promote)
*  [/perms user \<user\> `demote` \<track\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-user-user-demote)
*  [/perms user \<user\> `showtracks`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-user-user-showtracks)
*  [/perms user \<user\> `bulkchange` \<server|world\> \<from\> \<to\>](https://github.com/lucko/LuckPerms/wiki/Bulk-Editing#perms-groupuser--bulkchange-serverworld-from-to)
*  [/perms user \<user\> `clear`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-user-user-clear)

### Group   (/lp group \<group\> ...)
*  [/perms group \<group\> `info`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-group-group-info)
*  [/perms group \<group\> `permission`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#permission---lp-user-user-permission---lp-group-group-permission-)
*  [/perms group \<group\> `parent`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#parent---lp-user-user-parent---lp-group-group-parent-)
*  [/perms group \<group\> `meta`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#meta---lp-user-user-meta---lp-group-group-meta-)
*  [/perms group \<group\> `showtracks`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-group-group-showtracks)
*  [/perms group \<group\> `bulkchange` \<server|world\> \<from\> \<to\>](https://github.com/lucko/LuckPerms/wiki/Bulk-Editing#perms-groupuser--bulkchange-serverworld-from-to)
*  [/perms group \<group\> `clear`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-group-group-clear)
*  [/perms group \<group\> `rename` \<new name\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-group-group-rename)
*  [/perms group \<group\> `clone` \<name of clone\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-group-group-clone)

### Permission   (/lp user \<user\> permission ... | /lp group \<group\> permission ...)
*  [`info`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-usergroup-usergroup-permission-info)
*  [`set` \<node\> \<true/false\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-usergroup-usergroup-permission-set)
*  [`unset` \<node\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-usergroup-usergroup-permission-unset)
*  [`settemp` \<node\> \<true/false\> \<duration\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-usergroup-usergroup-permission-settemp)
*  [`unsettemp` \<node\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-usergroup-usergroup-permission-unsettemp)
*  [`check` \<node\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-usergroup-usergroup-permission-check)
*  [`checkinherits` \<node\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-usergroup-usergroup-permission-checkinherits)

###[ Parent   (/lp user \<user\> parent ... | /lp group \<group\> parent ...)
*  [`info`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-usergroup-usergroup-parent-info)
*  [`set` \<group\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-usergroup-usergroup-parent-set)
*  [`add` \<group\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-usergroup-usergroup-parent-add)
*  [`remove` \<group\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-usergroup-usergroup-parent-remove)
*  [`addtemp` \<group\> \<duration\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-usergroup-usergroup-parent-addtemp)
*  [`removetemp` \<group\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-usergroup-usergroup-parent-removetemp)

### Meta   (/lp user \<user\> meta ... | /lp group \<group\> meta ...)
*  [`info`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-usergroup-usergroup-meta-info)
*  [`set` \<key\> \<value\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-usergroup-usergroup-meta-set)
*  [`unset` \<key\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-usergroup-usergroup-meta-unset)
*  [`settemp` \<key\> \<value\> \<duration\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-usergroup-usergroup-meta-settemp)
*  [`unsettemp` \<key\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-usergroup-usergroup-meta-unsettemp)
*  [`addprefix` \<priority\> \<prefix\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-usergroup-usergroup-meta-addprefix)
*  [`addsuffix` \<priority\> \<suffix\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-usergroup-usergroup-meta-addsuffix)
*  [`removeprefix` \<priority\> \<prefix\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-usergroup-usergroup-meta-removeprefix)
*  [`removesuffix` \<priority\> \<suffix\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-usergroup-usergroup-meta-removesuffix)
*  [`addtempprefix` \<priority\> \<prefix\> \<duration\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-usergroup-usergroup-meta-addtempprefix)
*  [`addtempsuffix` \<priority\> \<suffix\> \<duration\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-usergroup-usergroup-meta-addtempsuffix)
*  [`removetempprefix` \<priority\> \<prefix\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-usergroup-usergroup-meta-removetempprefix)
*  [`removetempsuffix` \<priority\> \<suffix\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-usergroup-usergroup-meta-removetempsuffix)
*  [`clear` [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-usergroup-usergroup-meta-clear)

### Track
*  /perms track \<track\> `info`
*  /perms track \<track\> `append` \<group\>
*  /perms track \<track\> `insert` \<group\> \<position\>
*  /perms track \<track\> `remove` \<group\>
*  /perms track \<track\> `clear`
*  /perms track \<track\> `rename` \<new name\>
*  /perms track \<track\> `clone` \<name of clone\>

### Log
*  /perms log `recent` [user] [page]
*  /perms log `search` \<query\> [page]
*  /perms log `notify` [on|off]
*  /perms log `export` \<file\>
*  /perms log `userhistory` \<user\> [page]
*  /perms log `grouphistory` \<group\> [page]
*  /perms log `trackhistory` \<track\> [page]

### User Bulk Edit
(see the wiki page for details)
*  /perms usersbulkedit `group` \<group|null\> \<server|world\> \<from\> \<to\>
*  /perms usersbulkedit `permission` \<node|null\> \<server|world\> \<from\> \<to\>

# Command Detail

### General
___
#### `/perms`  
**Permission**: n/a  
Prints a list of the LuckPerms commands a user has permission to use.  

___
#### `/perms sync`  
**Permission**: luckperms.sync  
Refreshes all cached data with the storage provider.

___
#### `/perms networksync`  
**Permission**: luckperms.sync  
Refreshes all cached data with the storage provider, and then uses Redis (if configured) to "ping" all other connected servers and request that they sync too.

___
#### `/perms info`  
**Permission**: luckperms.info  
Lists data about LuckPerms, including debug output, statistics, settings, and values from the configuration. 

___
#### `/perms verbose`  
**Permission**: luckperms.verbose  
**Arguments**:  
* `<true|false>` - whether to enable the feature
* `[filters...]` - the name of the user / start of the node to filter by

Enables verbose permission checking output for the sender executing the command. As a result, whenever a permission is checked for by a plugin, if the permission / user being checked match the filters provided, the sender will be notified.

___
#### `/perms import`  
**Permission**: luckperms.import  
**Arguments**:  
* `<file>` - the file to import from

Imports data into LuckPerms from a file. The file must be a list of commands, starting with "/luckperms". This file can be generated using the export command. The file is expected to be in the root plugin directory.

___
#### `/perms export`  
**Permission**: n/a (only usable by the console)  
**Arguments**:  
* `<file>` - the file to export to

Exports data from LuckPerms into a file. This file can either be used as a backup, or used to move data between LuckPerms installations. The file can be re-imported using the import command. The generated file will be in the root plugin directory.

___
#### `/perms queuecommand`  
**Permission**: n/a (only usable by the console)  
**Arguments**:  
* `<command args...>` - the command arguments

Queues a command for execution. This command should be used when you use LuckPerms in automated scripts. "/lp creategroup test" becomes "/lp queuecommand creategroup test".

___
#### `/perms creategroup`  
**Permission**: luckperms.creategroup  
**Arguments**:  
* `<name>` - the name of the group

Creates a new group.

___
#### `/perms deletegroup`  
**Permission**: luckperms.deletegroup  
**Arguments**:  
* `<name>` - the name of the group

Permanently deletes a group.

___
#### `/perms listgroups`  
**Permission**: luckperms.listgroups  
Displays a list of all current groups.

___
#### `/perms createtrack`  
**Permission**: luckperms.createtrack  
**Arguments**:  
* `<name>` - the name of the track

Creates a new track.

___
#### `/perms deletetrack`  
**Permission**: luckperms.deletetrack  
**Arguments**:  
* `<name>` - the name of the track

Permanently deletes a track.

___
#### `/perms listtracks`  
**Permission**: luckperms.listtracks  
Displays a list of all current tracks.

___
#### `/perms migration`  
**Permission**: n/a (only usable by the console)  
Lists commands availble to begin a migration process.

___

### User   (/lp user \<user\> ...)
___
#### `/perms user <user> info`  
**Permission**: luckperms.user.info  
Displays information about a user, including their username, primary group, parents, and current contexts.

___
#### `/perms user <user> switchprimarygroup`  
**Permission**: luckperms.user.switchprimarygroup  
**Arguments**:  
* `<group>` - the group to switch to

This command allows you to change a user's primary group. If they are not already a member of the specified group, they will be added to it. This should not be used as a replacement to the "parent set" command. Their existing primary group will not be removed as a parent. (a user can have multiple parent groups)

___
#### `/perms user <user> promote`  
**Permission**: luckperms.user.promote  
**Arguments**:  
* `<track>` - the track to promote along
* `[server]` - the server to promote in
* `[world]` - the world to promote in

This command will promote a user along a track. Firstly, the command will check to see if the user is on the track specified in the given server/world. If the user is not on the track, or on the track in more than one place, the command will fail. If not, the user will be promoted up the track, and will be removed from the existing group. If the track action affects their primary group, that will be updated too.

___
#### `/perms user <user> demote`  
**Permission**: luckperms.user.demote  
**Arguments**:  
* `<track>` - the track to demote along
* `[server]` - the server to demote in
* `[world]` - the world to demote in

This command will demote a user along a track. Firstly, the command will check to see if the user is on the track specified in the given server/world. If the user is not on the track, or on the track in more than one place, the command will fail. If not, the user will be demoted down the track, and will be removed from the existing group. If the track action affects their primary group, that will be updated too.

___
#### `/perms user <user> showtracks`  
**Permission**: luckperms.user.showtracks  
Displays a list of all of the tracks a user is currently on.

___
#### `/perms user <user> clear`  
**Permission**: luckperms.user.clear  
**Arguments**:  
* `[server]` - the server to filter by
* `[world]` - the world to filter by

Clears the user's permissions, parent groups and meta.

___

### Group   (/lp group \<group\> ...)
___
#### `/perms group <group> info`  
**Permission**: luckperms.group.info  
Displays information about a group.

___
#### `/perms group <group> showtracks`  
**Permission**: luckperms.group.showtracks  
Displays a list of all of the tracks a group is currently on.

___
#### `/perms group <group> clear`  
**Permission**: luckperms.group.clear  
**Arguments**:  
* `[server]` - the server to filter by
* `[world]` - the world to filter by

Clears the group's permissions, parent groups and meta.

___
#### `/perms group <group> rename`  
**Permission**: luckperms.group.rename  
**Arguments**:  
* `<new name>` - the new name for the group

Changes a group's name. Note that any members of this group will not know about the change, and will still point to the old group name. If you wish to update this, please see the bulk edit commands.

___
#### `/perms group <group> clone`  
**Permission**: luckperms.group.clone  
**Arguments**:  
* `<new name>` - the name of the clone

Makes an exact copy of the group under a different name.

___

### Permission   (/lp user \<user\> permission ... | /lp group \<group\> permission ...)
___
#### `/perms user/group <user|group> permission info`  
**Permission**: luckperms.user.permission.info or luckperms.group.permission.info  
Displays a list of the permission nodes a user/group has.

___
#### `/perms user/group <user|group> permission set`  
**Permission**: luckperms.user.permission.set or luckperms.group.permission.set  
**Arguments**:  
* `<node>` - the permission node to set
* `<true|false>` - the value to set the permission to
* `[server]` - the server to set the permission on (specify "global" for all servers)
* `[world]` - the world to set the permission on

Sets a permission for a user/group. Giving a value of "false" will negate the permission.

___
#### `/perms user/group <user|group> permission unset`  
**Permission**: luckperms.user.permission.unset or luckperms.group.permission.unset  
**Arguments**:  
* `<node>` - the permission node to unset
* `[server]` - the server to unset the permission on (specify "global" for all servers)
* `[world]` - the world to unset the permission on

Unsets a permission for a user/group.

___
#### `/perms user/group <user|group> permission settemp`  
**Permission**: luckperms.user.permission.settemp or luckperms.group.permission.settemp  
**Arguments**:  
* `<node>` - the permission node to set
* `<true|false>` - the value to set the permission to
* `<duration>` - the duration until the permission will expire
* `[server]` - the server to set the permission on (specify "global" for all servers)
* `[world]` - the world to set the permission on

Sets a permission temporarily for a user/group. Giving a value of "false" will negate the permission. Duration should either be a time period, or a unix timestamp when the permission will expire. e.g. "3d13h45m" will set the permission to expire in 3 days, 13 hours and 45 minutes time. "1482694200" will set the permission to expire at 7:30PM on 25th December 2016.

___
#### `/perms user/group <user|group> permission unsettemp`  
**Permission**: luckperms.user.permission.unsettemp or luckperms.group.permission.unsettemp  
**Arguments**:  
* `<node>` - the permission node to unset
* `[server]` - the server to unset the permission on (specify "global" for all servers)
* `[world]` - the world to unset the permission on

Unsets a temproary permission for a user/group.

___
#### `/perms user/group <user|group> permission check`  
**Permission**: luckperms.user.permission.check or luckperms.group.permission.check  
**Arguments**:  
* `<node>` - the permission node to check for
* `[server]` - the server to check for the permission on (specify "global" for all servers)
* `[world]` - the world to check for the permission on

Checks to see if a user/group has a certain permission.

___
#### `/perms user/group <user|group> permission checkinherits`  
**Permission**: luckperms.user.permission.checkinherits or luckperms.group.permission.checkinherits  
**Arguments**:  
* `<node>` - the permission node to check for
* `[server]` - the server to check for the permission on (specify "global" for all servers)
* `[world]` - the world to check for the permission on

Checks to see if a user/group inherits a certain permission, and if so, where from.

___

### Parent   (/lp user \<user\> parent ... | /lp group \<group\> parent ...)
___
#### `/perms user/group <user|group> parent info`  
**Permission**: luckperms.user.parent.info or luckperms.group.parent.info  
Displays a list of a user/group's parent groups. (groups they inherit from)

___
#### `/perms user/group <user|group> parent set`  
**Permission**: luckperms.user.parent.set or luckperms.group.parent.set  
**Arguments**:  
* `<group>` - the group to set
* `[server]` - the server to set the group on (specify "global" for all servers)
* `[world]` - the world to set the group on

Sets a user/group's parent. Unlike the "parent add" command, this command will clear all existing groups set at the given context. The add command will simply "add" the group to the existing ones a user/group has. If the command is executed with no server or world arguments, this command will also update a user's primary group.

___
#### `/perms user/group <user|group> parent add`  
**Permission**: luckperms.user.parent.add or luckperms.group.parent.add  
**Arguments**:  
* `<group>` - the group to add
* `[server]` - the server to add the group on (specify "global" for all servers)
* `[world]` - the world to add the group on

Adds a parent to a user/group. Unlike the "parent set" command, this command will just accumulate the given parent with the ones the user/group already has. No existing parents will be removed from the user, and a user's primary group will be unaffected.

___
#### `/perms user/group <user|group> parent remove`  
**Permission**: luckperms.user.parent.remove or luckperms.group.parent.remove  
**Arguments**:  
* `<group>` - the group to remove
* `[server]` - the server to add remove group on (specify "global" for all servers)
* `[world]` - the world to add remove group on

Removes a parent from the user/group.

___
#### `/perms user/group <user|group> parent addtemp`  
**Permission**: luckperms.user.parent.addtemp or luckperms.group.parent.addtemp  
**Arguments**:  
* `<group>` - the group to add
* `<duration>` - the duration until the group will expire
* `[server]` - the server to add the group on (specify "global" for all servers)
* `[world]` - the world to add the group on

Adds a parent to a user/group temporarily. Duration should either be a time period, or a unix timestamp when the permission will expire. e.g. "3d13h45m" will set the permission to expire in 3 days, 13 hours and 45 minutes time. "1482694200" will set the permission to expire at 7:30PM on 25th December 2016.

___
#### `/perms user/group <user|group> parent removetemp`  
**Permission**: luckperms.user.parent.removetemp or luckperms.group.parent.removetemp  
**Arguments**:  
* `<group>` - the group to remove
* `[server]` - the server to add remove group on (specify "global" for all servers)
* `[world]` - the world to add remove group on

Removes a tempoary parent from the user/group.

___

### Meta   (/lp user \<user\> meta ... | /lp group \<group\> meta ...)
___
#### `/perms user/group <user|group> meta info`  
**Permission**: luckperms.user.meta.info or luckperms.group.meta.info  
Displays a list of a user/group's inherited meta (options), prefixes and suffixes.

___
#### `/perms user/group <user|group> meta set`  
**Permission**: luckperms.user.meta.set or luckperms.group.meta.set  
**Arguments**:  
* `<key>` - the key to set
* `<value>` - the value to set the key to
* `[server]` - the server to set the meta on (specify "global" for all servers)
* `[world]` - the world to set the meta on

Sets a meta key value pair for a user/group. These values can be read and modified by other plugins using Vault or the Sponge Permissions API. However, most users will never need to use them.

___
#### `/perms user/group <user|group> meta unset`  
**Permission**: luckperms.user.meta.unset or luckperms.group.meta.unset  
**Arguments**:  
* `<key>` - the key to unset
* `[server]` - the server to unset the meta on (specify "global" for all servers)
* `[world]` - the world to unset the meta on

Unsets a meta key value pair for a user/group.

___
#### `/perms user/group <user|group> meta settemp`  
**Permission**: luckperms.user.meta.settemp or luckperms.group.meta.settemp  
**Arguments**:  
* `<key>` - the key to set
* `<value>` - the value to set the key to
* `<duration>` - the duration until the meta will expire
* `[server]` - the server to set the meta on (specify "global" for all servers)
* `[world]` - the world to set the meta on

Sets a temporary meta key value pair for a user/group. Duration should either be a time period, or a unix timestamp when the permission will expire. e.g. "3d13h45m" will set the permission to expire in 3 days, 13 hours and 45 minutes time. "1482694200" will set the permission to expire at 7:30PM on 25th December 2016.

___
#### `/perms user/group <user|group> meta unsettemp`  
**Permission**: luckperms.user.meta.unsettemp or luckperms.group.meta.unsettemp  
**Arguments**:  
* `<key>` - the key to unset
* `[server]` - the server to unset the meta on (specify "global" for all servers)
* `[world]` - the world to unset the meta on

Unsets a temporary meta key value pair for a user/group.

___
#### `/perms user/group <user|group> meta addprefix`  
**Permission**: luckperms.user.meta.addprefix or luckperms.group.meta.addprefix  
**Arguments**:  
* `<priority>` - the priority to add the prefix at
* `<prefix>` - the actual prefix string
* `[server]` - the server to add the prefix on (specify "global" for all servers)
* `[world]` - the world to add the prefix on

Adds a prefix to a user/group. You can wrap the prefix in " " quotes to escape spaces. 

___
#### `/perms user/group <user|group> meta addsuffix`  
**Permission**: luckperms.user.meta.addsuffix or luckperms.group.meta.addsuffix  
**Arguments**:  
* `<priority>` - the priority to add the suffix at
* `<suffix>` - the actual suffix string
* `[server]` - the server to add the suffix on (specify "global" for all servers)
* `[world]` - the world to add the suffix on

Adds a suffix to a user/group. You can wrap the suffix in " " quotes to escape spaces. 

___
#### `/perms user/group <user|group> meta removeprefix`  
**Permission**: luckperms.user.meta.removeprefix or luckperms.group.meta.removeprefix  
**Arguments**:  
* `<priority>` - the priority to remove the prefix at
* `<prefix>` - the actual prefix string
* `[server]` - the server to remove the prefix on (specify "global" for all servers)
* `[world]` - the world to remove the prefix on

Removes a prefix from a user/group. You can wrap the prefix in " " quotes to escape spaces. If you simply specify "null" as the prefix, all registered prefixes at the given priority will be removed.

___
#### `/perms user/group <user|group> meta removesuffix`  
**Permission**: luckperms.user.meta.removesuffix or luckperms.group.meta.removesuffix  
**Arguments**:  
* `<priority>` - the priority to remove the suffix at
* `<suffix>` - the actual suffix string
* `[server]` - the server to remove the suffix on (specify "global" for all servers)
* `[world]` - the world to remove the suffix on

Removes a suffix from a user/group. You can wrap the suffix in " " quotes to escape spaces. If you simply specify "null" as the suffix, all registered suffixes at the given priority will be removed.

___
#### `/perms user/group <user|group> meta addtempprefix`  
**Permission**: luckperms.user.meta.addtempprefix or luckperms.group.meta.addtempprefix  
**Arguments**:  
* `<priority>` - the priority to add the prefix at
* `<prefix>` - the actual prefix string
* `<duration>` - the duration until the prefix will expire
* `[server]` - the server to add the prefix on (specify "global" for all servers)
* `[world]` - the world to add the prefix on

Adds a prefix to a user/group temporarily. You can wrap the prefix in " " quotes to escape spaces. Duration should either be a time period, or a unix timestamp when the permission will expire. e.g. "3d13h45m" will set the permission to expire in 3 days, 13 hours and 45 minutes time. "1482694200" will set the permission to expire at 7:30PM on 25th December 2016.

___
#### `/perms user/group <user|group> meta addtempsuffix`  
**Permission**: luckperms.user.meta.addtempsuffix or luckperms.group.meta.addtempsuffix  
**Arguments**:  
* `<priority>` - the priority to add the suffix at
* `<suffix>` - the actual suffix string
* `<duration>` - the duration until the suffix will expire
* `[server]` - the server to add the suffix on (specify "global" for all servers)
* `[world]` - the world to add the suffix on

Adds a suffix to a user/group temporarily. You can wrap the suffix in " " quotes to escape spaces. Duration should either be a time period, or a unix timestamp when the permission will expire. e.g. "3d13h45m" will set the permission to expire in 3 days, 13 hours and 45 minutes time. "1482694200" will set the permission to expire at 7:30PM on 25th December 2016.

___
#### `/perms user/group <user|group> meta removetempprefix`  
**Permission**: luckperms.user.meta.removetempprefix or luckperms.group.meta.removetempprefix  
**Arguments**:  
* `<priority>` - the priority to remove the prefix at
* `<prefix>` - the actual prefix string
* `[server]` - the server to remove the prefix on (specify "global" for all servers)
* `[world]` - the world to remove the prefix on

Removes a tempoary prefix from a user/group. You can wrap the prefix in " " quotes to escape spaces. If you simply specify "null" as the prefix, all registered prefixes at the given priority will be removed.

___
#### `/perms user/group <user|group> meta removetempsuffix`  
**Permission**: luckperms.user.meta.removetempsuffix or luckperms.group.meta.removetempsuffix  
**Arguments**:  
* `<priority>` - the priority to remove the suffix at
* `<suffix>` - the actual suffix string
* `[server]` - the server to remove the suffix on (specify "global" for all servers)
* `[world]` - the world to remove the suffix on

Removes a temporary suffix from a user/group. You can wrap the suffix in " " quotes to escape spaces. If you simply specify "null" as the suffix, all registered suffixes at the given priority will be removed.

___
#### `/perms user/group <user|group> meta clear`  
**Permission**: luckperms.user.meta.clear or luckperms.group.meta.clear  
**Arguments**:  
* `[server]` - the server to filter by
* `[world]` - the world to filter by

Removes all meta/prefixes/suffixes.

___

# Command Permissions

**Note**: You can use wildcards to grant users access to a selection of commands.
* **All commands** - luckperms.*
* **All user commands** - luckperms.user.*
* **All group commands** - luckperms.group.*
* **All track commands** - luckperms.track.*
* **All log commands** - luckperms.log.*

### General
*  luckperms.sync
*  luckperms.info
*  luckperms.debug
*  luckperms.import
*  luckperms.creategroup
*  luckperms.deletegroup
*  luckperms.listgroups
*  luckperms.createtrack
*  luckperms.deletetrack
*  luckperms.listtracks

### User
*  luckperms.user.info
*  luckperms.user.permission.info
*  luckperms.user.permission.set
*  luckperms.user.permission.unset
*  luckperms.user.permission.settemp
*  luckperms.user.permission.unsettemp
*  luckperms.user.parent.info
*  luckperms.user.parent.add
*  luckperms.user.parent.remove
*  luckperms.user.parent.addtemp
*  luckperms.user.parent.removetemp
*  luckperms.user.meta.info
*  luckperms.user.meta.set
*  luckperms.user.meta.unset
*  luckperms.user.meta.settemp
*  luckperms.user.meta.unsettemp
*  luckperms.user.meta.addprefix
*  luckperms.user.meta.addsuffix
*  luckperms.user.meta.removeprefix
*  luckperms.user.meta.removesuffix
*  luckperms.user.meta.addtempprefix
*  luckperms.user.meta.addtempsuffix
*  luckperms.user.meta.removetempprefix
*  luckperms.user.meta.removetempsuffix
*  luckperms.user.meta.clear
*  luckperms.user.getuuid
*  luckperms.user.haspermission
*  luckperms.user.inheritspermission
*  luckperms.user.setprimarygroup
*  luckperms.user.showtracks
*  luckperms.user.promote
*  luckperms.user.demote
*  luckperms.user.showpos
*  luckperms.user.bulkchange
*  luckperms.user.clear

### Group
*  luckperms.group.info
*  luckperms.group.permission.info
*  luckperms.group.permission.set
*  luckperms.group.permission.unset
*  luckperms.group.permission.settemp
*  luckperms.group.permission.unsettemp
*  luckperms.group.parent.info
*  luckperms.group.parent.add
*  luckperms.group.parent.remove
*  luckperms.group.parent.addtemp
*  luckperms.group.parent.removetemp
*  luckperms.group.meta.info
*  luckperms.group.meta.set
*  luckperms.group.meta.unset
*  luckperms.group.meta.settemp
*  luckperms.group.meta.unsettemp
*  luckperms.group.meta.addprefix
*  luckperms.group.meta.addsuffix
*  luckperms.group.meta.removeprefix
*  luckperms.group.meta.removesuffix
*  luckperms.group.meta.addtempprefix
*  luckperms.group.meta.addtempsuffix
*  luckperms.group.meta.removetempprefix
*  luckperms.group.meta.removetempsuffix
*  luckperms.group.meta.clear
*  luckperms.group.haspermission
*  luckperms.group.inheritspermission
*  luckperms.group.showtracks
*  luckperms.group.bulkchange
*  luckperms.group.clear
*  luckperms.group.rename
*  luckperms.group.clone

### Track
*  luckperms.track.info
*  luckperms.track.append
*  luckperms.track.insert
*  luckperms.track.remove
*  luckperms.track.clear
*  luckperms.track.rename
*  luckperms.track.clone

### Log
*  luckperms.log.recent
*  luckperms.log.search
*  luckperms.log.notify
*  luckperms.log.export
*  luckperms.log.userhistory
*  luckperms.log.grouphistory
*  luckperms.log.trackhistory
