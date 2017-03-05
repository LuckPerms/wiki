Command usage is printed to the console/chat whenever invalid arguments are provided. **Simply typing /lp or /lpb** will list all commands a user has permission to use.

If the only thing returned when you type a command is the plugin version, you do not have permission to use any of the commands. You need to use the server console to give yourself access to LuckPerms commands first.

### Aliases
A list of aliases for each platform are listed below. Each command works in exactly the same manner, so you can use whichever you prefer.

| Bukkit / Sponge  | Bungee           |
|------------------|------------------|
| /luckperms       | /luckpermsbungee |
| /perms           | /bperms          |
| /permissions     | /bpermissions    |
| /perm            | /bperm           |
| /lp              | /lpb             |

**`Important:`** Commands are different on BungeeCord. This is so you can choose where your command gets directed to. If commands were the same, you would never be able to control LuckPerms on a backend server.

If you are using Bukkit/Spigot, by default, all OPed users have access to LuckPerms commands. You can change this in the config.

# Overview
#### Arguments Key:
* `<required>` - you *must* specify this argument when running the command
* `[optional]` - you do not need to specify this argument. a default will be used if not given.

If you want to include spaces in arguments, you must escape the argument with quotes. `"  "`

The alias used below (/lp) can be exchanged for any of the ones listed in the aliases section above.

### General
*  [/lp](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp)
*  [/lp `sync`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-sync)
*  [/lp `info`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-info)
*  [/lp `verbose` \<on | record | off | paste\> [filter]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-verbose)
*  [/lp `tree` [selection] [max level] [player]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-tree)
*  [/lp `search` \<permission\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-search)
*  [/lp `check` \<user\> \<permission\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-check)
*  [/lp `networksync`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-networksync)
*  [/lp `import` \<file\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-import)
*  [/lp `export` \<file\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-export)
*  [/lp `reloadconfig`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-reloadconfig)
*  [/lp `migration`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-migration)
*  [/lp `creategroup` \<group\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-creategroup)
*  [/lp `deletegroup` \<group\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-deletegroup)
*  [/lp `listgroups`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-listgroups)
*  [/lp `createtrack` \<track\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-createtrack)
*  [/lp `deletetrack` \<track\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-deletetrack)
*  [/lp `listtracks`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-listtracks)

### User   (/lp user \<user\> ...)
*  [/lp user \<user\> `info`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-user-user-info)
*  [/lp user \<user\> `permission`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#permission---lp-user-user-permission---lp-group-group-permission-)
*  [/lp user \<user\> `parent`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#parent---lp-user-user-parent---lp-group-group-parent-)
*  [/lp user \<user\> `meta`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#meta---lp-user-user-meta---lp-group-group-meta-)
*  [/lp user \<user\> `switchprimarygroup` \<group\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-user-user-switchprimarygroup)
*  [/lp user \<user\> `promote` \<track\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-user-user-promote)
*  [/lp user \<user\> `demote` \<track\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-user-user-demote)
*  [/lp user \<user\> `showtracks`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-user-user-showtracks)
*  [/lp user \<user\> `bulkchange` \<server|world\> \<from\> \<to\>](https://github.com/lucko/LuckPerms/wiki/Bulk-Editing#lp-groupuser--bulkchange-serverworld-from-to)
*  [/lp user \<user\> `clear`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-user-user-clear)

### Group   (/lp group \<group\> ...)
*  [/lp group \<group\> `info`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-group-group-info)
*  [/lp group \<group\> `permission`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#permission---lp-user-user-permission---lp-group-group-permission-)
*  [/lp group \<group\> `parent`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#parent---lp-user-user-parent---lp-group-group-parent-)
*  [/lp group \<group\> `meta`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#meta---lp-user-user-meta---lp-group-group-meta-)
*  [/lp group \<group\> `setweight`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-group-group-setweight)
*  [/lp group \<group\> `showtracks`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-group-group-showtracks)
*  [/lp group \<group\> `bulkchange` \<server|world\> \<from\> \<to\>](https://github.com/lucko/LuckPerms/wiki/Bulk-Editing#lp-groupuser--bulkchange-serverworld-from-to)
*  [/lp group \<group\> `clear`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-group-group-clear)
*  [/lp group \<group\> `rename` \<new name\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-group-group-rename)
*  [/lp group \<group\> `clone` \<name of clone\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-group-group-clone)

### Permission   (/lp user \<user\> permission ... | /lp group \<group\> permission ...)
*  [`info`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-usergroup-usergroup-permission-info)
*  [`set` \<node\> \<true/false\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-usergroup-usergroup-permission-set)
*  [`unset` \<node\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-usergroup-usergroup-permission-unset)
*  [`settemp` \<node\> \<true/false\> \<duration\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-usergroup-usergroup-permission-settemp)
*  [`unsettemp` \<node\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-usergroup-usergroup-permission-unsettemp)
*  [`check` \<node\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-usergroup-usergroup-permission-check)
*  [`checkinherits` \<node\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-usergroup-usergroup-permission-checkinherits)

### Parent   (/lp user \<user\> parent ... | /lp group \<group\> parent ...)
*  [`info`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-usergroup-usergroup-parent-info)
*  [`set` \<group\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-usergroup-usergroup-parent-set)
*  [`add` \<group\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-usergroup-usergroup-parent-add)
*  [`remove` \<group\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-usergroup-usergroup-parent-remove)
*  [`addtemp` \<group\> \<duration\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-usergroup-usergroup-parent-addtemp)
*  [`removetemp` \<group\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-usergroup-usergroup-parent-removetemp)

### Meta   (/lp user \<user\> meta ... | /lp group \<group\> meta ...)
*  [`info`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-usergroup-usergroup-meta-info)
*  [`set` \<key\> \<value\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-usergroup-usergroup-meta-set)
*  [`unset` \<key\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-usergroup-usergroup-meta-unset)
*  [`settemp` \<key\> \<value\> \<duration\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-usergroup-usergroup-meta-settemp)
*  [`unsettemp` \<key\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-usergroup-usergroup-meta-unsettemp)
*  [`addprefix` \<priority\> \<prefix\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-usergroup-usergroup-meta-addprefix)
*  [`addsuffix` \<priority\> \<suffix\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-usergroup-usergroup-meta-addsuffix)
*  [`removeprefix` \<priority\> [prefix] [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-usergroup-usergroup-meta-removeprefix)
*  [`removesuffix` \<priority\> [suffix] [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-usergroup-usergroup-meta-removesuffix)
*  [`addtempprefix` \<priority\> \<prefix\> \<duration\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-usergroup-usergroup-meta-addtempprefix)
*  [`addtempsuffix` \<priority\> \<suffix\> \<duration\> [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-usergroup-usergroup-meta-addtempsuffix)
*  [`removetempprefix` \<priority\> [prefix] [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-usergroup-usergroup-meta-removetempprefix)
*  [`removetempsuffix` \<priority\> [suffix] [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-usergroup-usergroup-meta-removetempsuffix)
*  [`clear` [server] [world]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-usergroup-usergroup-meta-clear)

### Track   (/lp track \<track\> ...)
*  [/lp track \<track\> `info`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-track-track-info)
*  [/lp track \<track\> `append` \<group\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-track-track-append)
*  [/lp track \<track\> `insert` \<group\> \<position\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-track-track-insert)
*  [/lp track \<track\> `remove` \<group\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-track-track-remove)
*  [/lp track \<track\> `clear`](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-track-track-clear)
*  [/lp track \<track\> `rename` \<new name\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-track-track-rename)
*  [/lp track \<track\> `clone` \<name of clone\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-track-track-clone)

### Log   (/lp log ...)
*  [/lp log `recent` [user] [page]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-log-recent)
*  [/lp log `search` \<query\> [page]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-log-search)
*  [/lp log `notify` [on|off]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-log-notify)
*  [/lp log `export` \<file\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-log-export)
*  [/lp log `userhistory` \<user\> [page]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-log-userhistory)
*  [/lp log `grouphistory` \<group\> [page]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-log-grouphistory)
*  [/lp log `trackhistory` \<track\> [page]](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-log-trackhistory)

### User Bulk Edit
*  [/lp usersbulkedit `group` \<group|null\> \<server|world\> \<from\> \<to\>](https://github.com/lucko/LuckPerms/wiki/Bulk-Editing#lp-usersbulkedit-group-groupnull-serverworld-from-to)
*  [/lp usersbulkedit `permission` \<node|null\> \<server|world\> \<from\> \<to\>](https://github.com/lucko/LuckPerms/wiki/Bulk-Editing#lp-usersbulkedit-permission-nodenull-serverworld-from-to)

# Command Detail

### General
___
#### `/lp`  
**Permission**: n/a  
Prints a list of the LuckPerms commands a user has permission to use.  

___
#### `/lp sync`  
**Permission**: luckperms.sync  
Refreshes all cached data with the storage provider.

___
#### `/lp info`  
**Permission**: luckperms.info  
Lists data about LuckPerms, including debug output, statistics, settings, and values from the configuration. 

___
#### `/lp verbose`  
**Permission**: luckperms.verbose  
**Arguments**:  
* `<on|record|off|paste>` - whether to enable/disable logging, or to paste the logged output
* `[filter]` - the filter to sort the output

Controls the LuckPerms verbose logging system. This allows you to listen for all permission checks against players on the server. Whenever a permission is checked by a plugin, the check is passed onto the verbose handler.    

If your filters match the permission check, you will be notified.    

`on` will enable the system, and will send you an alert in chat when the filter is matched. `record` will do the same, however you will not be notified of checks in the chat. `off` will simply disable the checking, and `paste` will upload the first 500 results to GitHub's pastebin, and provide you with a link.    

Filters match the start of permissions or the user being checked. You can use `&` (and) and `|` (or) symbols, and `!` to negate a match. Parenthesis `( )` are also supported.   

**For example:**    
* `Luck & (essentials | worldedit)` - matches any checks made against my user starting with "essentials" or "worldedit"
* `!Luck & !anticheat` - matches any checks not against my user and not starting with "anticheat"
* `anticheat & !anticheat.check` - matches any checks starting with "anticheat" but not starting with "anticheat.check"    
     
You get the idea. ;)

___
#### `/lp tree`  
**Permission**: luckperms.tree  
**Arguments**:  
* `[selection]` - the root of the tree (specify `.` to include all permissions)
* `[max level]` - how many sub branches should be returned (in other words, the width of the tree)
* `[player]` - the name of an online player to check against

Generates a tree view of permissions registered to the server. The tree is built using data exposed to the server by plugins, and expanded over time as plugins check for permissions.

All arguments are optional. The default selection is `.` (just a dot, which means all), and the default max level is `5`.

Selection allows you to only generate a part of the tree. For example, a selection of `luckperms.user` will only return the branch of the tree starting with "luckperms.user".

Max level allows you to define how many sub branches will be included. For example, if you set a max level of `2`, "luckperms.user" will be returned, but "luckperms.user.info" will not be shown.

___
#### `/lp search`  
**Permission**: luckperms.search  
**Arguments**:  
* `<permission>` - the permission to search for

Searches all users/groups for a specific permission, and returns a paginated list of all found entries. 

___
#### `/lp check`  
**Permission**: luckperms.check  
**Arguments**:  
* `<user>` - the user to check
* `<permission>` - the permission to check for

Performs a standard permission check on an online player, and returns the result. This check is equivalent to the checks performed by other plugins when checking for permissions.

___
#### `/lp networksync`  
**Permission**: luckperms.sync  
Refreshes all cached data with the storage provider, and then uses Redis (if configured) to "ping" all other connected servers and request that they sync too.

___
#### `/lp import`  
**Permission**: luckperms.import  
**Arguments**:  
* `<file>` - the file to import from

Imports data into LuckPerms from a file. The file must be a list of commands, starting with "/luckperms". This file can be generated using the export command. The file is expected to be in the root plugin directory.

___
#### `/lp export`  
**Permission**: luckperms.export  
**Arguments**:  
* `<file>` - the file to export to

Exports data from LuckPerms into a file. This file can either be used as a backup, or used to move data between LuckPerms installations. The file can be re-imported using the import command. The generated file will be in the root plugin directory.

___
#### `/lp reloadconfig`  
**Permission**: luckperms.reloadconfig  
Reloads some values from the configuration file. Not all entries are reloaded by this command, and some require a full server reboot to take effect. (storage settings, for example)

___
#### `/lp migration`  
**Permission**: luckperms.migration  
Lists commands availble to begin a migration process.

___
#### `/lp creategroup`  
**Permission**: luckperms.creategroup  
**Arguments**:  
* `<name>` - the name of the group

Creates a new group.

___
#### `/lp deletegroup`  
**Permission**: luckperms.deletegroup  
**Arguments**:  
* `<name>` - the name of the group

Permanently deletes a group.

___
#### `/lp listgroups`  
**Permission**: luckperms.listgroups  
Displays a list of all current groups.

___
#### `/lp createtrack`  
**Permission**: luckperms.createtrack  
**Arguments**:  
* `<name>` - the name of the track

Creates a new track.

___
#### `/lp deletetrack`  
**Permission**: luckperms.deletetrack  
**Arguments**:  
* `<name>` - the name of the track

Permanently deletes a track.

___
#### `/lp listtracks`  
**Permission**: luckperms.listtracks  
Displays a list of all current tracks.

___

### User   (/lp user \<user\> ...)
___
#### `/lp user <user> info`  
**Permission**: luckperms.user.info  
Displays information about a user, including their username, primary group, parents, and current contexts.

___
#### `/lp user <user> switchprimarygroup`  
**Permission**: luckperms.user.switchprimarygroup  
**Arguments**:  
* `<group>` - the group to switch to

This command allows you to change a user's primary group. If they are not already a member of the specified group, they will be added to it. This should not be used as a replacement to the "parent set" command. Their existing primary group will not be removed as a parent. (a user can have multiple parent groups)

___
#### `/lp user <user> promote`  
**Permission**: luckperms.user.promote  
**Arguments**:  
* `<track>` - the track to promote along
* `[server]` - the server to promote in
* `[world]` - the world to promote in

This command will promote a user along a track. Firstly, the command will check to see if the user is on the track specified in the given server/world. If the user is not on the track, or on the track in more than one place, the command will fail. If not, the user will be promoted up the track, and will be removed from the existing group. If the track action affects their primary group, that will be updated too.

___
#### `/lp user <user> demote`  
**Permission**: luckperms.user.demote  
**Arguments**:  
* `<track>` - the track to demote along
* `[server]` - the server to demote in
* `[world]` - the world to demote in

This command will demote a user along a track. Firstly, the command will check to see if the user is on the track specified in the given server/world. If the user is not on the track, or on the track in more than one place, the command will fail. If not, the user will be demoted down the track, and will be removed from the existing group. If the track action affects their primary group, that will be updated too.

___
#### `/lp user <user> showtracks`  
**Permission**: luckperms.user.showtracks  
Displays a list of all of the tracks a user is currently on.

___
#### `/lp user <user> clear`  
**Permission**: luckperms.user.clear  
**Arguments**:  
* `[server]` - the server to filter by
* `[world]` - the world to filter by

Clears the user's permissions, parent groups and meta.

___

### Group   (/lp group \<group\> ...)
___
#### `/lp group <group> info`  
**Permission**: luckperms.group.info  
Displays information about a group.

___
#### `/lp group <group> setweight`  
**Permission**: luckperms.group.setweight  
**Arguments**:  
* `<weight>` - the weight to set

Sets the groups weight value, which determines the order in which groups will be considered when accumulating a users permissions. Higher value = higher weight.

___
#### `/lp group <group> showtracks`  
**Permission**: luckperms.group.showtracks  
Displays a list of all of the tracks a group is currently on.

___
#### `/lp group <group> clear`  
**Permission**: luckperms.group.clear  
**Arguments**:  
* `[server]` - the server to filter by
* `[world]` - the world to filter by

Clears the group's permissions, parent groups and meta.

___
#### `/lp group <group> rename`  
**Permission**: luckperms.group.rename  
**Arguments**:  
* `<new name>` - the new name for the group

Changes a group's name. Note that any members of this group will not know about the change, and will still point to the old group name. If you wish to update this, please see the bulk edit commands.

___
#### `/lp group <group> clone`  
**Permission**: luckperms.group.clone  
**Arguments**:  
* `<new name>` - the name of the clone

Makes an exact copy of the group under a different name.

___

### Permission   (/lp user \<user\> permission ... | /lp group \<group\> permission ...)
___
#### `/lp user/group <user|group> permission info`  
**Permission**: luckperms.user.permission.info or luckperms.group.permission.info  
Displays a list of the permission nodes a user/group has.

___
#### `/lp user/group <user|group> permission set`  
**Permission**: luckperms.user.permission.set or luckperms.group.permission.set  
**Arguments**:  
* `<node>` - the permission node to set
* `<true|false>` - the value to set the permission to
* `[server]` - the server to set the permission on (specify "global" for all servers)
* `[world]` - the world to set the permission on

Sets a permission for a user/group. Giving a value of "false" will negate the permission.

___
#### `/lp user/group <user|group> permission unset`  
**Permission**: luckperms.user.permission.unset or luckperms.group.permission.unset  
**Arguments**:  
* `<node>` - the permission node to unset
* `[server]` - the server to unset the permission on (specify "global" for all servers)
* `[world]` - the world to unset the permission on

Unsets a permission for a user/group.

___
#### `/lp user/group <user|group> permission settemp`  
**Permission**: luckperms.user.permission.settemp or luckperms.group.permission.settemp  
**Arguments**:  
* `<node>` - the permission node to set
* `<true|false>` - the value to set the permission to
* `<duration>` - the duration until the permission will expire
* `[server]` - the server to set the permission on (specify "global" for all servers)
* `[world]` - the world to set the permission on

Sets a permission temporarily for a user/group. Giving a value of "false" will negate the permission. Duration should either be a time period, or a unix timestamp when the permission will expire. e.g. "3d13h45m" will set the permission to expire in 3 days, 13 hours and 45 minutes time. "1482694200" will set the permission to expire at 7:30PM on 25th December 2016.

___
#### `/lp user/group <user|group> permission unsettemp`  
**Permission**: luckperms.user.permission.unsettemp or luckperms.group.permission.unsettemp  
**Arguments**:  
* `<node>` - the permission node to unset
* `[server]` - the server to unset the permission on (specify "global" for all servers)
* `[world]` - the world to unset the permission on

Unsets a temproary permission for a user/group.

___
#### `/lp user/group <user|group> permission check`  
**Permission**: luckperms.user.permission.check or luckperms.group.permission.check  
**Arguments**:  
* `<node>` - the permission node to check for
* `[server]` - the server to check for the permission on (specify "global" for all servers)
* `[world]` - the world to check for the permission on

Checks to see if a user/group has a certain permission.

___
#### `/lp user/group <user|group> permission checkinherits`  
**Permission**: luckperms.user.permission.checkinherits or luckperms.group.permission.checkinherits  
**Arguments**:  
* `<node>` - the permission node to check for
* `[server]` - the server to check for the permission on (specify "global" for all servers)
* `[world]` - the world to check for the permission on

Checks to see if a user/group inherits a certain permission, and if so, where from.

___

### Parent   (/lp user \<user\> parent ... | /lp group \<group\> parent ...)
___
#### `/lp user/group <user|group> parent info`  
**Permission**: luckperms.user.parent.info or luckperms.group.parent.info  
Displays a list of a user/group's parent groups. (groups they inherit from)

___
#### `/lp user/group <user|group> parent set`  
**Permission**: luckperms.user.parent.set or luckperms.group.parent.set  
**Arguments**:  
* `<group>` - the group to set
* `[server]` - the server to set the group on (specify "global" for all servers)
* `[world]` - the world to set the group on

Sets a user/group's parent. Unlike the "parent add" command, this command will clear all existing groups set at the given context. The add command will simply "add" the group to the existing ones a user/group has. If the command is executed with no server or world arguments, this command will also update a user's primary group.

___
#### `/lp user/group <user|group> parent add`  
**Permission**: luckperms.user.parent.add or luckperms.group.parent.add  
**Arguments**:  
* `<group>` - the group to add
* `[server]` - the server to add the group on (specify "global" for all servers)
* `[world]` - the world to add the group on

Adds a parent to a user/group. Unlike the "parent set" command, this command will just accumulate the given parent with the ones the user/group already has. No existing parents will be removed from the user, and a user's primary group will be unaffected.

___
#### `/lp user/group <user|group> parent remove`  
**Permission**: luckperms.user.parent.remove or luckperms.group.parent.remove  
**Arguments**:  
* `<group>` - the group to remove
* `[server]` - the server to add remove group on (specify "global" for all servers)
* `[world]` - the world to add remove group on

Removes a parent from the user/group.

___
#### `/lp user/group <user|group> parent addtemp`  
**Permission**: luckperms.user.parent.addtemp or luckperms.group.parent.addtemp  
**Arguments**:  
* `<group>` - the group to add
* `<duration>` - the duration until the group will expire
* `[server]` - the server to add the group on (specify "global" for all servers)
* `[world]` - the world to add the group on

Adds a parent to a user/group temporarily. Duration should either be a time period, or a unix timestamp when the permission will expire. e.g. "3d13h45m" will set the permission to expire in 3 days, 13 hours and 45 minutes time. "1482694200" will set the permission to expire at 7:30PM on 25th December 2016.

___
#### `/lp user/group <user|group> parent removetemp`  
**Permission**: luckperms.user.parent.removetemp or luckperms.group.parent.removetemp  
**Arguments**:  
* `<group>` - the group to remove
* `[server]` - the server to add remove group on (specify "global" for all servers)
* `[world]` - the world to add remove group on

Removes a tempoary parent from the user/group.

___

### Meta   (/lp user \<user\> meta ... | /lp group \<group\> meta ...)
___
#### `/lp user/group <user|group> meta info`  
**Permission**: luckperms.user.meta.info or luckperms.group.meta.info  
Displays a list of a user/group's inherited meta (options), prefixes and suffixes.

___
#### `/lp user/group <user|group> meta set`  
**Permission**: luckperms.user.meta.set or luckperms.group.meta.set  
**Arguments**:  
* `<key>` - the key to set
* `<value>` - the value to set the key to
* `[server]` - the server to set the meta on (specify "global" for all servers)
* `[world]` - the world to set the meta on

Sets a meta key value pair for a user/group. These values can be read and modified by other plugins using Vault or the Sponge Permissions API. However, most users will never need to use them.

___
#### `/lp user/group <user|group> meta unset`  
**Permission**: luckperms.user.meta.unset or luckperms.group.meta.unset  
**Arguments**:  
* `<key>` - the key to unset
* `[server]` - the server to unset the meta on (specify "global" for all servers)
* `[world]` - the world to unset the meta on

Unsets a meta key value pair for a user/group.

___
#### `/lp user/group <user|group> meta settemp`  
**Permission**: luckperms.user.meta.settemp or luckperms.group.meta.settemp  
**Arguments**:  
* `<key>` - the key to set
* `<value>` - the value to set the key to
* `<duration>` - the duration until the meta will expire
* `[server]` - the server to set the meta on (specify "global" for all servers)
* `[world]` - the world to set the meta on

Sets a temporary meta key value pair for a user/group. Duration should either be a time period, or a unix timestamp when the permission will expire. e.g. "3d13h45m" will set the permission to expire in 3 days, 13 hours and 45 minutes time. "1482694200" will set the permission to expire at 7:30PM on 25th December 2016.

___
#### `/lp user/group <user|group> meta unsettemp`  
**Permission**: luckperms.user.meta.unsettemp or luckperms.group.meta.unsettemp  
**Arguments**:  
* `<key>` - the key to unset
* `[server]` - the server to unset the meta on (specify "global" for all servers)
* `[world]` - the world to unset the meta on

Unsets a temporary meta key value pair for a user/group.

___
#### `/lp user/group <user|group> meta addprefix`  
**Permission**: luckperms.user.meta.addprefix or luckperms.group.meta.addprefix  
**Arguments**:  
* `<priority>` - the priority to add the prefix at
* `<prefix>` - the actual prefix string
* `[server]` - the server to add the prefix on (specify "global" for all servers)
* `[world]` - the world to add the prefix on

Adds a prefix to a user/group. You can wrap the prefix in " " quotes to escape spaces. 

___
#### `/lp user/group <user|group> meta addsuffix`  
**Permission**: luckperms.user.meta.addsuffix or luckperms.group.meta.addsuffix  
**Arguments**:  
* `<priority>` - the priority to add the suffix at
* `<suffix>` - the actual suffix string
* `[server]` - the server to add the suffix on (specify "global" for all servers)
* `[world]` - the world to add the suffix on

Adds a suffix to a user/group. You can wrap the suffix in " " quotes to escape spaces. 

___
#### `/lp user/group <user|group> meta removeprefix`  
**Permission**: luckperms.user.meta.removeprefix or luckperms.group.meta.removeprefix  
**Arguments**:  
* `<priority>` - the priority to remove the prefix at
* `[prefix]` - the actual prefix string
* `[server]` - the server to remove the prefix on (specify "global" for all servers)
* `[world]` - the world to remove the prefix on

Removes a prefix from a user/group. You can wrap the prefix in " " quotes to escape spaces.

___
#### `/lp user/group <user|group> meta removesuffix`  
**Permission**: luckperms.user.meta.removesuffix or luckperms.group.meta.removesuffix  
**Arguments**:  
* `<priority>` - the priority to remove the suffix at
* `[suffix]` - the actual suffix string
* `[server]` - the server to remove the suffix on (specify "global" for all servers)
* `[world]` - the world to remove the suffix on

Removes a suffix from a user/group. You can wrap the suffix in " " quotes to escape spaces.

___
#### `/lp user/group <user|group> meta addtempprefix`  
**Permission**: luckperms.user.meta.addtempprefix or luckperms.group.meta.addtempprefix  
**Arguments**:  
* `<priority>` - the priority to add the prefix at
* `<prefix>` - the actual prefix string
* `<duration>` - the duration until the prefix will expire
* `[server]` - the server to add the prefix on (specify "global" for all servers)
* `[world]` - the world to add the prefix on

Adds a prefix to a user/group temporarily. You can wrap the prefix in " " quotes to escape spaces. Duration should either be a time period, or a unix timestamp when the permission will expire. e.g. "3d13h45m" will set the permission to expire in 3 days, 13 hours and 45 minutes time. "1482694200" will set the permission to expire at 7:30PM on 25th December 2016.

___
#### `/lp user/group <user|group> meta addtempsuffix`  
**Permission**: luckperms.user.meta.addtempsuffix or luckperms.group.meta.addtempsuffix  
**Arguments**:  
* `<priority>` - the priority to add the suffix at
* `<suffix>` - the actual suffix string
* `<duration>` - the duration until the suffix will expire
* `[server]` - the server to add the suffix on (specify "global" for all servers)
* `[world]` - the world to add the suffix on

Adds a suffix to a user/group temporarily. You can wrap the suffix in " " quotes to escape spaces. Duration should either be a time period, or a unix timestamp when the permission will expire. e.g. "3d13h45m" will set the permission to expire in 3 days, 13 hours and 45 minutes time. "1482694200" will set the permission to expire at 7:30PM on 25th December 2016.

___
#### `/lp user/group <user|group> meta removetempprefix`  
**Permission**: luckperms.user.meta.removetempprefix or luckperms.group.meta.removetempprefix  
**Arguments**:  
* `<priority>` - the priority to remove the prefix at
* `[prefix]` - the actual prefix string
* `[server]` - the server to remove the prefix on (specify "global" for all servers)
* `[world]` - the world to remove the prefix on

Removes a tempoary prefix from a user/group. You can wrap the prefix in " " quotes to escape spaces.

___
#### `/lp user/group <user|group> meta removetempsuffix`  
**Permission**: luckperms.user.meta.removetempsuffix or luckperms.group.meta.removetempsuffix  
**Arguments**:  
* `<priority>` - the priority to remove the suffix at
* `[suffix]` - the actual suffix string
* `[server]` - the server to remove the suffix on (specify "global" for all servers)
* `[world]` - the world to remove the suffix on

Removes a temporary suffix from a user/group. You can wrap the suffix in " " quotes to escape spaces.

___
#### `/lp user/group <user|group> meta clear`  
**Permission**: luckperms.user.meta.clear or luckperms.group.meta.clear  
**Arguments**:  
* `[server]` - the server to filter by
* `[world]` - the world to filter by

Removes all meta/prefixes/suffixes.

___

### Track   (/lp track \<track\> ...)
___
#### `/lp track <track> info`  
**Permission**: luckperms.track.info  
Displays the groups in the track.

___
#### `/lp track <track> append`  
**Permission**: luckperms.track.info  
**Arguments**:  
* `<group>` - the group to add

Adds a group onto the end of the track.

___
#### `/lp track <track> insert`  
**Permission**: luckperms.track.insert  
**Arguments**:  
* `<group>` - the group to insert
* `<position>` - the position to insert the group at

Inserts a group into a specific position within this track. A position of 1 would place it at the start of the track.

___
#### `/lp track <track> remove`  
**Permission**: luckperms.track.remove  
**Arguments**:  
* `<group>` - the group to remove

Removes a group from the track.

___
#### `/lp track <track> clear`  
**Permission**: luckperms.track.clear  
Removes all groups from the track.

___
#### `/lp track <track> rename`  
**Permission**: luckperms.track.rename  
**Arguments**:  
* `<new name>` - the new name for the track

Changes a track's name.

___
#### `/lp track <track> clone`  
**Permission**: luckperms.track.clone  
**Arguments**:  
* `<new name>` - the name of the clone

Makes an exact copy of the track under a different name.

___

### Log   (/lp log ...)
___
#### `/lp log recent`  
**Permission**: luckperms.log.recent  
**Arguments**:  
* `[user]` - the name/uuid of the user to filter by
* `[page]` - the page number to view

Shows a list of recent actions.

___
#### `/lp log search`  
**Permission**: luckperms.log.search  
**Arguments**:  
* `<query>` - the query to search for
* `[page]` - the page number to view

Searches for log entries matching the given query.

___
#### `/lp log notify`  
**Permission**: luckperms.log.notify  
**Arguments**:  
* `[on|off]` - whether to enable or disable

Toggles log notifications for the sender executing the command.

___
#### `/lp log export`  
**Permission**: luckperms.log.export  
**Arguments**:  
* `<file>` - the file to export to

Exports the log to a list of commands, recognisable by the "/lp import" command. This feature should rarely be used, and use of "/lp export" is reccomended instead.

___
#### `/lp log userhistory`  
**Permission**: luckperms.log.userhistory  
**Arguments**:  
* `<user>` - the user to search for
* `[page]` - the page number to view

Searches for log entries acting upon the given user.

___
#### `/lp log grouphistory`  
**Permission**: luckperms.log.grouphistory  
**Arguments**:  
* `<group>` - the group to search for
* `[page]` - the page number to view

Searches for log entries acting upon the given group.

___
#### `/lp log trackhistory`  
**Permission**: luckperms.log.trackhistory  
**Arguments**:  
* `<track>` - the track to search for
* `[page]` - the page number to view

Searches for log entries acting upon the given track.

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
*  luckperms.verbose
*  luckperms.search
*  luckperms.check
*  luckperms.import
*  luckperms.export
*  luckperms.reloadconfig
*  luckperms.migration
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
*  luckperms.user.permission.check
*  luckperms.user.permission.checkinherits
*  luckperms.user.parent.info
*  luckperms.user.parent.set
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
*  luckperms.user.switchprimarygroup
*  luckperms.user.showtracks
*  luckperms.user.promote
*  luckperms.user.demote
*  luckperms.user.bulkchange
*  luckperms.user.clear

### Group
*  luckperms.group.info
*  luckperms.group.permission.info
*  luckperms.group.permission.set
*  luckperms.group.permission.unset
*  luckperms.group.permission.settemp
*  luckperms.group.permission.unsettemp
*  luckperms.group.permission.check
*  luckperms.group.permission.checkinherits
*  luckperms.group.parent.info
*  luckperms.group.parent.set
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
