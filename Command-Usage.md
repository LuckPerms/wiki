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
*  /perms
*  /perms `sync`
*  /perms `networksync`
*  /perms `info`
*  /perms `verbose` \<true|false\> [filters...]
*  /perms `import` \<file\>
*  /perms `creategroup` \<group\>
*  /perms `deletegroup` \<group\>
*  /perms `listgroups`
*  /perms `createtrack` \<track\>
*  /perms `deletetrack` \<track\>
*  /perms `listtracks`

### Super Secret Console Commands
*  /perms `export` \<file\>
*  /perms `migration`
*  /perms `queuecommand` \<command args...\>

### User   (/lp user \<user\> ...)
*  /perms user \<user\> `info`
*  **/perms user \<user\> `permission`** (see the "permission" section below.)
*  **/perms user \<user\> `parent`** (see the "parent" section below)
*  **/perms user \<user\> `meta`** (see the "meta" section below)
*  /perms user \<user\> `getuuid`
*  /perms user \<user\> `switchprimarygroup` \<group\>
*  /perms user \<user\> `promote` \<track\>
*  /perms user \<user\> `demote` \<track\>
*  /perms user \<user\> `showtracks`
*  /perms user \<user\> `bulkchange` \<server|world\> \<from\> \<to\> (see the wiki page for details)
*  /perms user \<user\> `clear`

### Group   (/lp group \<group\> ...)
*  /perms group \<group\> `info`
*  **/perms group \<group\> `permission`** (see the "permission" section below.)
*  **/perms group \<group\> `parent`** (see the "parent" section below)
*  **/perms group \<group\> `meta`** (see the "meta" section below)
*  /perms group \<group\> `showtracks`
*  /perms group \<group\> `bulkchange` \<server|world\> \<from\> \<to\> (see the wiki page for details)
*  /perms group \<group\> `clear`
*  /perms group \<group\> `rename` \<new name\>
*  /perms group \<group\> `clone` \<name of clone\>

### Permission   (/lp user \<user\> permission ... | /lp group \<group\> permission ...)
*  `info`
*  `set` \<node\> \<true/false\> [server] [world]
*  `unset` \<node\> [server] [world]
*  `settemp` \<node\> \<true/false\> \<duration\> [server] [world]
*  `unsettemp` \<node\> [server] [world]

### Parent   (/lp user \<user\> parent ... | /lp group \<group\> parent ...)
*  `info`
*  `add` \<group\> [server] [world]
*  `remove` \<group\> [server] [world]
*  `addtemp` \<group\> \<duration\> [server] [world]
*  `removetemp` \<group\> [server] [world]

### Meta   (/lp user \<user\> meta ... | /lp group \<group\> meta ...)
*  `info`
*  `set` \<key\> \<value\> [server] [world]
*  `unset` \<key\> [server] [world]
*  `settemp` \<key\> \<value\> \<duration\> [server] [world]
*  `unsettemp` \<key\> [server] [world]
*  `addprefix` \<priority\> \<prefix\> [server] [world]
*  `addsuffix` \<priority\> \<suffix\> [server] [world]
*  `removeprefix` \<priority\> \<prefix\> [server] [world]
*  `removesuffix` \<priority\> \<suffix\> [server] [world]
*  `addtempprefix` \<priority\> \<prefix\> \<duration\> [server] [world]
*  `addtempsuffix` \<priority\> \<suffix\> \<duration\> [server] [world]
*  `removetempprefix` \<priority\> \<prefix\> [server] [world]
*  `removetempsuffix` \<priority\> \<suffix\> [server] [world]
*  `clear` [server] [world]

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
#### `/perms user <user> permission info` `/perms group <group> permission info`  
**Permission**: luckperms.user.permission.info or luckperms.group.permission.info  
Displays a list of the permission nodes a user/group has.

___
#### `/perms user <user> permission set` `/perms group <group> permission set`  
**Permission**: luckperms.user.permission.set or luckperms.group.permission.set  
**Arguments**:  
* `<node>` - the permission node to set
* `<true|false>` - the value to set the permission to
* `[server]` - the server to set the permission on (specify "global" for all servers)
* `[world]` - the world to set the permission on

Sets a permission for a user/group. Giving a value of "false" will negate the permission.

___
#### `/perms user <user> permission unset` `/perms group <group> permission unset`  
**Permission**: luckperms.user.permission.unset or luckperms.group.permission.unset  
**Arguments**:  
* `<node>` - the permission node to unset
* `[server]` - the server to unset the permission on (specify "global" for all servers)
* `[world]` - the world to unset the permission on

Unsets a permission for a user/group.

___
#### `/perms user <user> permission settemp` `/perms group <group> permission settemp`  
**Permission**: luckperms.user.permission.settemp or luckperms.group.permission.settemp  
**Arguments**:  
* `<node>` - the permission node to set
* `<true|false>` - the value to set the permission to
* `<duration>` - the duration until the permission will expire
* `[server]` - the server to set the permission on (specify "global" for all servers)
* `[world]` - the world to set the permission on

Sets a permission temporarily for a user/group. Giving a value of "false" will negate the permission. Duration should either be a time period, or a unix timestamp when the permission will expire. e.g. "3d13h45m" will set the permission to expire in 3 days, 13 hours and 45 minutes time. "1482694200" will set the permission to expire at 7:30PM on 25th December 2016.

___
#### `/perms user <user> permission unsettemp` `/perms group <group> permission unsettemp`  
**Permission**: luckperms.user.permission.unsettemp or luckperms.group.permission.unsettemp  
**Arguments**:  
* `<node>` - the permission node to unset
* `[server]` - the server to unset the permission on (specify "global" for all servers)
* `[world]` - the world to unset the permission on

Unsets a temproary permission for a user/group.

___
#### `/perms user <user> permission check` `/perms group <group> permission check`  
**Permission**: luckperms.user.permission.check or luckperms.group.permission.check  
**Arguments**:  
* `<node>` - the permission node to check for
* `[server]` - the server to check for the permission on (specify "global" for all servers)
* `[world]` - the world to check for the permission on

Checks to see if a user/group has a certain permission.

___
#### `/perms user <user> permission checkinherits` `/perms group <group> permission checkinherits`  
**Permission**: luckperms.user.permission.checkinherits or luckperms.group.permission.checkinherits  
**Arguments**:  
* `<node>` - the permission node to check for
* `[server]` - the server to check for the permission on (specify "global" for all servers)
* `[world]` - the world to check for the permission on

Checks to see if a user/group inherits a certain permission, and if so, where from.

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
