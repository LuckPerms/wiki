Command usage is printed to the console/chat whenever invalid arguments are provided. **Simply typing /lp or /lpb** will list all commands a user has permission to use.

If the only thing returned when you type a command is the plugin version, you do not have permission to use any of the commands. You need to use the server console to [give yourself access to LuckPerms commands first](https://github.com/lucko/LuckPerms/wiki/Usage#granting-full-access-to-modify-permissions).

### Aliases
A list of aliases for each platform are listed below. Each command works in exactly the same manner, so you can use whichever you prefer.

| Bukkit / Sponge  | BungeeCord       |
|------------------|------------------|
| /luckperms       | /luckpermsbungee |
| /perms           | /bperms          |
| /permissions     | /bpermissions    |
| /perm            | /bperm           |
| /lp              | /lpb             |

**`Important:`** Commands are different on BungeeCord. This is so you can choose where your command gets directed to. If commands were the same, you would never be able to control LuckPerms on a backend server.

If you are using Bukkit/Spigot, by default, all users with OP have access to LuckPerms commands. You can change this in the config.

# Overview
#### Arguments Key:
* `<required>` - you *must* specify this argument when running the command
* `[optional]` - you do not need to specify this argument. a default will be used if not given.

If you want to include spaces in arguments, you must escape the argument with quotes. `"  "`

The alias used below (/lp) can be exchanged for any of the ones listed in the aliases section above.

### General
*  [/lp](#lp)
*  [/lp `sync`](#lp-sync)
*  [/lp `info`](#lp-info)
*  [/lp `verbose` \<on | record | off | paste\> [filter]](#lp-verbose)
*  [/lp `tree` [scope] [player]](#lp-tree)
*  [/lp `search` \<permission\>](#lp-search)
*  [/lp `check` \<user\> \<permission\>](#lp-check)
*  [/lp `networksync`](#lp-networksync)
*  [/lp `import` \<file\>](#lp-import)
*  [/lp `export` \<file\>](#lp-export)
*  [/lp `reloadconfig`](#lp-reloadconfig)
*  [/lp `bulkupdate`](#lp-bulkupdate)
*  [/lp `migration`](#lp-migration)
*  [/lp `creategroup` \<group\>](#lp-creategroup)
*  [/lp `deletegroup` \<group\>](#lp-deletegroup)
*  [/lp `listgroups`](#lp-listgroups)
*  [/lp `createtrack` \<track\>](#lp-createtrack)
*  [/lp `deletetrack` \<track\>](#lp-deletetrack)
*  [/lp `listtracks`](#lp-listtracks)

### User   (/lp user \<user\> ...)
*  [/lp user \<user\> `info`](#lp-user-user-info)
*  [/lp user \<user\> `permission`](#permission---lp-user-user-permission---lp-group-group-permission-)
*  [/lp user \<user\> `parent`](#parent---lp-user-user-parent---lp-group-group-parent-)
*  [/lp user \<user\> `meta`](#meta---lp-user-user-meta---lp-group-group-meta-)
*  [/lp user \<user\> `editor`](#lp-user-user-editor)
*  [/lp user \<user\> `promote` \<track\> [context...]](#lp-user-user-promote)
*  [/lp user \<user\> `demote` \<track\> [context...]](#lp-user-user-demote)
*  [/lp user \<user\> `showtracks`](#lp-user-user-showtracks)
*  [/lp user \<user\> `clear` [context...]](#lp-user-user-clear)

### Group   (/lp group \<group\> ...)
*  [/lp group \<group\> `info`](#lp-group-group-info)
*  [/lp group \<group\> `permission`](#permission---lp-user-user-permission---lp-group-group-permission-)
*  [/lp group \<group\> `parent`](#parent---lp-user-user-parent---lp-group-group-parent-)
*  [/lp group \<group\> `meta`](#meta---lp-user-user-meta---lp-group-group-meta-)
*  [/lp group \<group\> `editor`](#lp-group-group-editor)
*  [/lp group \<group\> `listmembers` [page]](#lp-group-group-listmembers)
*  [/lp group \<group\> `setweight` \<weight\>](#lp-group-group-setweight)
*  [/lp group \<group\> `showtracks`](#lp-group-group-showtracks)
*  [/lp group \<group\> `clear` [context...]](#lp-group-group-clear)
*  [/lp group \<group\> `rename` \<new name\>](#lp-group-group-rename)
*  [/lp group \<group\> `clone` \<name of clone\>](#lp-group-group-clone)

### Permission   (/lp user \<user\> permission ... | /lp group \<group\> permission ...)
*  [`info`](#lp-usergroup-usergroup-permission-info)
*  [`set` \<node\> \<true/false\> [context...]](#lp-usergroup-usergroup-permission-set)
*  [`unset` \<node\> [context...]](#lp-usergroup-usergroup-permission-unset)
*  [`settemp` \<node\> \<true/false\> \<duration\> [context...]](#lp-usergroup-usergroup-permission-settemp)
*  [`unsettemp` \<node\> [context...]](#lp-usergroup-usergroup-permission-unsettemp)
*  [`check` \<node\> [context...]](#lp-usergroup-usergroup-permission-check)
*  [`checkinherits` \<node\> [context...]](#lp-usergroup-usergroup-permission-checkinherits)

### Parent   (/lp user \<user\> parent ... | /lp group \<group\> parent ...)
*  [`info`](#lp-usergroup-usergroup-parent-info)
*  [`set` \<group\> [context...]](#lp-usergroup-usergroup-parent-set)
*  [`add` \<group\> [context...]](#lp-usergroup-usergroup-parent-add)
*  [`remove` \<group\> [context...]](#lp-usergroup-usergroup-parent-remove)
*  [`settrack` \<track\> \<group\> [context...]](#lp-usergroup-usergroup-parent-settrack)
*  [`addtemp` \<group\> \<duration\> [context...]](#lp-usergroup-usergroup-parent-addtemp)
*  [`removetemp` \<group\> [context...]](#lp-usergroup-usergroup-parent-removetemp)
*  [`clear` [context...]](#lp-usergroup-usergroup-parent-clear)
*  [`cleartrack` \<track\> [context...]](#lp-usergroup-usergroup-parent-cleartrack)
*  [`switchprimarygroup` \<group\>](#lp-user-user-parent-switchprimarygroup)

### Meta   (/lp user \<user\> meta ... | /lp group \<group\> meta ...)
*  [`info`](#lp-usergroup-usergroup-meta-info)
*  [`set` \<key\> \<value\> [context...]](#lp-usergroup-usergroup-meta-set)
*  [`unset` \<key\> [context...]](#lp-usergroup-usergroup-meta-unset)
*  [`settemp` \<key\> \<value\> \<duration\> [context...]](#lp-usergroup-usergroup-meta-settemp)
*  [`unsettemp` \<key\> [context...]](#lp-usergroup-usergroup-meta-unsettemp)
*  [`addprefix` \<priority\> \<prefix\> [context...]](#lp-usergroup-usergroup-meta-addprefix)
*  [`addsuffix` \<priority\> \<suffix\> [context...]](#lp-usergroup-usergroup-meta-addsuffix)
*  [`removeprefix` \<priority\> [prefix] [context...]](#lp-usergroup-usergroup-meta-removeprefix)
*  [`removesuffix` \<priority\> [suffix] [context...]](#lp-usergroup-usergroup-meta-removesuffix)
*  [`addtempprefix` \<priority\> \<prefix\> \<duration\> [context...]](#lp-usergroup-usergroup-meta-addtempprefix)
*  [`addtempsuffix` \<priority\> \<suffix\> \<duration\> [context...]](#lp-usergroup-usergroup-meta-addtempsuffix)
*  [`removetempprefix` \<priority\> [prefix] [context...]](#lp-usergroup-usergroup-meta-removetempprefix)
*  [`removetempsuffix` \<priority\> [suffix] [context...]](#lp-usergroup-usergroup-meta-removetempsuffix)
*  [`clear` [context...]](#lp-usergroup-usergroup-meta-clear)

### Track   (/lp track \<track\> ...)
*  [/lp track \<track\> `info`](#lp-track-track-info)
*  [/lp track \<track\> `append` \<group\>](#lp-track-track-append)
*  [/lp track \<track\> `insert` \<group\> \<position\>](#lp-track-track-insert)
*  [/lp track \<track\> `remove` \<group\>](#lp-track-track-remove)
*  [/lp track \<track\> `clear`](#lp-track-track-clear)
*  [/lp track \<track\> `rename` \<new name\>](#lp-track-track-rename)
*  [/lp track \<track\> `clone` \<name of clone\>](#lp-track-track-clone)

### Log   (/lp log ...)
*  [/lp log `recent` [user] [page]](#lp-log-recent)
*  [/lp log `search` \<query\> [page]](#lp-log-search)
*  [/lp log `notify` [on|off]](#lp-log-notify)
*  [/lp log `export` \<file\>](#lp-log-export)
*  [/lp log `userhistory` \<user\> [page]](#lp-log-userhistory)
*  [/lp log `grouphistory` \<group\> [page]](#lp-log-grouphistory)
*  [/lp log `trackhistory` \<track\> [page]](#lp-log-trackhistory)

# Command Detail

### General
___
#### `/lp`  
**Permission**: n/a  
Base LuckPerms command. Will print a list of the LuckPerms commands a user has permission to use, with brief information about what each command does, and what arguments it accepts.  

___
#### `/lp sync`  
**Permission**: luckperms.sync  
Performs a refresh of all currently loaded data. If any changes have been made to the data in the storage, this command will update the copy on the server to include those changes. 

___
#### `/lp info`  
**Permission**: luckperms.info  
Lists some information/data about LuckPerms, including debugging output, statistics, settings, and important values from the configuration. 

___
#### `/lp verbose`  
**Permission**: luckperms.verbose  
**Arguments**:  
* `<on|record|off|paste>` - whether to enable/disable logging, or to paste the logged output
* `[filter]` - the filter to sort the output

Controls the LuckPerms verbose logging system. This allows you to listen for all permission checks against players on the server. Whenever a permission is checked by a plugin, the check is passed onto the verbose handler.    

If your filters match the permission check, you will be notified.    

`on` will enable the system, and will send you an alert in chat when the filter is matched. `record` will do the same, however you will not be notified of checks in the chat. `off` will simply disable the checking, and `paste` will upload the first 3500 results to GitHub's pastebin, and provide you with a link.    

Filters match the start of permissions or the user being checked. You can use `&` (and) and `|` (or) symbols, and `!` to negate a match. Parenthesis `( )` are also supported.   

**For example:**    
* `Luck & (essentials | worldedit)` - matches any checks made against my user starting with "essentials" or "worldedit"
* `!Luck & !anticheat` - matches any checks not against my user and not starting with "anticheat"
* `anticheat & !anticheat.check` - matches any checks starting with "anticheat" but not starting with "anticheat.check"    
     
More information can be found [**here**](https://github.com/lucko/LuckPerms/wiki/Verbose)

___
#### `/lp tree`  
**Permission**: luckperms.tree  
**Arguments**:  
* `[scope]` - the root of the tree (specify `.` to include all permissions)
* `[player]` - the name of an online player to check against

Generates a tree view of permissions registered to the server. The tree is built using data exposed to the server by plugins, and expanded over time as plugins check for permissions.

All arguments are optional. The default selection is `.` (just a dot, which means all).

Scope allows you to only generate a part of the tree. For example, a scope of `luckperms.user` will only return the branch of the tree starting with "luckperms.user".

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
Refreshes all cached data with the storage provider, and then uses the plugins Messaging Service (if configured) to "ping" all other connected servers and request that they sync too.

___
#### `/lp import`  
**Permission**: luckperms.import  
**Arguments**:  
* `<file>` - the file to import from

Imports data into LuckPerms from a file. The file must be a list of commands, starting with "/luckperms". This file can be generated using the export command. The file is expected to be in the plugin directory.

___
#### `/lp export`  
**Permission**: luckperms.export  
**Arguments**:  
* `<file>` - the file to export to

Exports data from LuckPerms into a file. This file can either be used as a backup, or used to move data between LuckPerms installations. The file can be re-imported using the import command. The generated file will be in the plugin directory.

___
#### `/lp reloadconfig`  
**Permission**: luckperms.reloadconfig  
Reloads some values from the configuration file. Not all entries are reloaded by this command, and some require a full server reboot to take effect. (storage settings, for example)

___
#### `/lp bulkupdate`  
**Permission**: **Console Only**  
Allows you to perform a bulk modifiction to all permission data. A detailed guide on how to use this command can be found [here](https://github.com/lucko/LuckPerms/wiki/Bulk-Editing).

___
#### `/lp migration`  
**Permission**: luckperms.migration  
Main command used for the migration system. Allows you to import permissions data into LuckPerms from other permission plugins. More information about this feature can be found [here](https://github.com/lucko/LuckPerms/wiki/Migration).

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
#### `/lp user <user> editor`  
**Permission**: luckperms.user.editor  
Opens a web interface to edit permissions for the specified group. After changes are saved, a command will be given that you need to run for the changes to take effect.

___
#### `/lp user <user> promote`  
**Permission**: luckperms.user.promote  
**Arguments**:  
* `<track>` - the track to promote along
* `[context...]` - the contexts to promote in

This command will promote a user along a track. Firstly, the command will check to see if the user is on the track specified in the given contexts. If the user is not on the track, they will be added to the first group on the track. If they are on the track in more than one place, the command will fail. In all other cases, the user will be promoted up the track, and will be removed from the existing group. If the track action affects their primary group, that will be updated too.

___
#### `/lp user <user> demote`  
**Permission**: luckperms.user.demote  
**Arguments**:  
* `<track>` - the track to demote along
* `[context...]` - the contexts to demote in

This command will demote a user along a track. Firstly, the command will check to see if the user is on the track specified in the given contexts. If the user is not on the track, or on the track in more than one place, the command will fail. If not, the user will be demoted down the track, and will be removed from the existing group. If the track action affects their primary group, that will be updated too.

___
#### `/lp user <user> showtracks`  
**Permission**: luckperms.user.showtracks  
Displays a list of all of the tracks a user is currently on.

___
#### `/lp user <user> clear`  
**Permission**: luckperms.user.clear  
**Arguments**:  
* `[context...]` - the contexts to filter by

Clears the user's permissions, parent groups and meta.

___
### Group   (/lp group \<group\> ...)
___
#### `/lp group <group> info`  
**Permission**: luckperms.group.info  
Displays information about a group.

___
#### `/lp group <group> editor`  
**Permission**: luckperms.group.editor  
Opens a web interface to edit permissions for the specified group. After changes are saved, a command will be given that you need to run for the changes to take effect.

___
#### `/lp group <group> listmembers`  
**Permission**: luckperms.group.listmembers  
**Arguments**:  
* `[page]` - the page to view

Gets a list of the other users/groups which inherit directly from this group.

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
* `[context...]` - the contexts to filter by

Clears the group's permissions, parent groups and meta.

___
#### `/lp group <group> rename`  
**Permission**: luckperms.group.rename  
**Arguments**:  
* `<new name>` - the new name for the group

Changes a group's name. Note that any members of this group will not know about the change, and will still point to the old group name. If you wish to update this, you'll need to use the bulk change feature to update the existing entries.

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
* `[context...]` - the contexts to set the permission in

Sets (or gives) a permission for a user/group. Providing a value of "false" will negate the permission.

___
#### `/lp user/group <user|group> permission unset`  
**Permission**: luckperms.user.permission.unset or luckperms.group.permission.unset  
**Arguments**:  
* `<node>` - the permission node to unset
* `[context...]` - the contexts to unset the permission in

Unsets (or removes) a permission for a user/group.

___
#### `/lp user/group <user|group> permission settemp`  
**Permission**: luckperms.user.permission.settemp or luckperms.group.permission.settemp  
**Arguments**:  
* `<node>` - the permission node to set
* `<true|false>` - the value to set the permission to
* `<duration>` - the duration until the permission will expire
* `[context...]` - the contexts to set the permission in

Sets a permission temporarily for a user/group. Providing a value of "false" will negate the permission. Duration should either be a time period, or a unix timestamp when the permission will expire. e.g. "3d13h45m" will set the permission to expire in 3 days, 13 hours and 45 minutes time. "1482694200" will set the permission to expire at 7:30PM on 25th December 2016.

___
#### `/lp user/group <user|group> permission unsettemp`  
**Permission**: luckperms.user.permission.unsettemp or luckperms.group.permission.unsettemp  
**Arguments**:  
* `<node>` - the permission node to unset
* `[context...]` - the contexts to unset the permission in

Unsets a temporary permission for a user/group.

___
#### `/lp user/group <user|group> permission check`  
**Permission**: luckperms.user.permission.check or luckperms.group.permission.check  
**Arguments**:  
* `<node>` - the permission node to check for
* `[context...]` - the contexts to check for the permission in

Checks to see if a user/group has a certain permission.

___
#### `/lp user/group <user|group> permission checkinherits`  
**Permission**: luckperms.user.permission.checkinherits or luckperms.group.permission.checkinherits  
**Arguments**:  
* `<node>` - the permission node to check for
* `[context...]` - the contexts to check for the permission in

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
* `[context...]` - the contexts to set the group in

Sets a user/group's parent. Unlike the "parent add" command, this command will clear all existing groups set at the given context. The add command will simply "add" the group to the existing ones a user/group has. If the command is executed with no context arguments, this command will also update a user's primary group.

___
#### `/lp user/group <user|group> parent add`  
**Permission**: luckperms.user.parent.add or luckperms.group.parent.add  
**Arguments**:  
* `<group>` - the group to add
* `[context...]` - the contexts to add the group in

Adds a parent to a user/group. Unlike the "parent set" command, this command will just accumulate the given parent with the ones the user/group already has. No existing parents will be removed from the user, and a user's primary group will be unaffected.

___
#### `/lp user/group <user|group> parent remove`  
**Permission**: luckperms.user.parent.remove or luckperms.group.parent.remove  
**Arguments**:  
* `<group>` - the group to remove
* `[context...]` - the contexts to remove the group in

Removes a parent from the user/group.

___
#### `/lp user/group <user|group> parent settrack`  
**Permission**: luckperms.user.parent.settrack or luckperms.group.parent.settrack  
**Arguments**:  
* `<track>` - the track to set on
* `<group>` - the group to set to, or a number relating to the position of the group on the given track
* `[context...]` - the contexts to set the group in

Sets a users/groups position on a given track. This behaves in the same way as the set command, except it only clears existing groups which are on the specified track. Other parent groups are not affected.
___
#### `/lp user/group <user|group> parent addtemp`  
**Permission**: luckperms.user.parent.addtemp or luckperms.group.parent.addtemp  
**Arguments**:  
* `<group>` - the group to add
* `<duration>` - the duration until the group will expire
* `[context...]` - the contexts to add the group in

Adds a parent to a user/group temporarily. Duration should either be a time period, or a unix timestamp when the permission will expire. e.g. "3d13h45m" will set the permission to expire in 3 days, 13 hours and 45 minutes time. "1482694200" will set the permission to expire at 7:30PM on 25th December 2016.

___
#### `/lp user/group <user|group> parent removetemp`  
**Permission**: luckperms.user.parent.removetemp or luckperms.group.parent.removetemp  
**Arguments**:  
* `<group>` - the group to remove
* `[context...]` - the contexts to add remove group in

Removes a tempoary parent from the user/group.

___
#### `/lp user/group <user|group> parent clear`  
**Permission**: luckperms.user.parent.clear or luckperms.group.parent.clear  
**Arguments**:  
* `[context...]` - the contexts to filter by

Removes all parents.

___
#### `/lp user/group <user|group> parent cleartrack`  
**Permission**: luckperms.user.parent.cleartrack or luckperms.group.parent.cleartrack  
**Arguments**:  
* `<track>` - the track to remove on
* `[context...]` - the contexts to filter by

Removes all parents from the user/group on a given track.

___
#### `/lp user <user> parent switchprimarygroup`  
**Permission**: luckperms.user.parent.switchprimarygroup  
**Arguments**:  
* `<group>` - the group to switch to

This command is only available for users - as groups do not have "primary" groups.

This command allows you to change a user's primary group. If they are not already a member of the specified group, they will be added to it. This should not be used as a replacement to the "parent set" command. Their existing primary group will not be removed as a parent. (a user can have multiple parent groups)

If `primary-group-calculation` is set to something other than "stored" in the LuckPerms config, you should use the [`parent add`](#lp-usergroup-usergroup-parent-add) or [`parent set`](#lp-usergroup-usergroup-parent-set) commands instead of this.

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
* `[context...]` - the contexts to set the meta in

Sets a meta key value pair for a user/group. These values can be read and modified by other plugins using Vault or the Sponge Permissions API.

___
#### `/lp user/group <user|group> meta unset`  
**Permission**: luckperms.user.meta.unset or luckperms.group.meta.unset  
**Arguments**:  
* `<key>` - the key to unset
* `[context...]` - the contexts to unset the meta in

Unsets a meta key value pair for a user/group.

___
#### `/lp user/group <user|group> meta settemp`  
**Permission**: luckperms.user.meta.settemp or luckperms.group.meta.settemp  
**Arguments**:  
* `<key>` - the key to set
* `<value>` - the value to set the key to
* `<duration>` - the duration until the meta will expire
* `[context...]` - the contexts to set the meta in

Sets a temporary meta key value pair for a user/group. Duration should either be a time period, or a unix timestamp when the permission will expire. e.g. "3d13h45m" will set the permission to expire in 3 days, 13 hours and 45 minutes time. "1482694200" will set the permission to expire at 7:30PM on 25th December 2016.

___
#### `/lp user/group <user|group> meta unsettemp`  
**Permission**: luckperms.user.meta.unsettemp or luckperms.group.meta.unsettemp  
**Arguments**:  
* `<key>` - the key to unset
* `[context...]` - the contexts to unset the meta in

Unsets a temporary meta key value pair for a user/group.

___
#### `/lp user/group <user|group> meta addprefix`  
**Permission**: luckperms.user.meta.addprefix or luckperms.group.meta.addprefix  
**Arguments**:  
* `<priority>` - the priority to add the prefix at
* `<prefix>` - the actual prefix string
* `[context...]` - the contexts to add the prefix in

Adds a prefix to a user/group. You can wrap the prefix in " " quotes to escape spaces. 

___
#### `/lp user/group <user|group> meta addsuffix`  
**Permission**: luckperms.user.meta.addsuffix or luckperms.group.meta.addsuffix  
**Arguments**:  
* `<priority>` - the priority to add the suffix at
* `<suffix>` - the actual suffix string
* `[context...]` - the contexts to add the suffix in

Adds a suffix to a user/group. You can wrap the suffix in " " quotes to escape spaces. 

___
#### `/lp user/group <user|group> meta removeprefix`  
**Permission**: luckperms.user.meta.removeprefix or luckperms.group.meta.removeprefix  
**Arguments**:  
* `<priority>` - the priority to remove the prefix at
* `[prefix]` - the actual prefix string
* `[context...]` - the contexts to remove the prefix in

Removes a prefix from a user/group. You can wrap the prefix in " " quotes to escape spaces.

___
#### `/lp user/group <user|group> meta removesuffix`  
**Permission**: luckperms.user.meta.removesuffix or luckperms.group.meta.removesuffix  
**Arguments**:  
* `<priority>` - the priority to remove the suffix at
* `[suffix]` - the actual suffix string
* `[context...]` - the contexts to remove the suffix in

Removes a suffix from a user/group. You can wrap the suffix in " " quotes to escape spaces.

___
#### `/lp user/group <user|group> meta addtempprefix`  
**Permission**: luckperms.user.meta.addtempprefix or luckperms.group.meta.addtempprefix  
**Arguments**:  
* `<priority>` - the priority to add the prefix at
* `<prefix>` - the actual prefix string
* `<duration>` - the duration until the prefix will expire
* `[context...]` - the contexts to add the prefix in

Adds a prefix to a user/group temporarily. You can wrap the prefix in " " quotes to escape spaces. Duration should either be a time period, or a unix timestamp when the permission will expire. e.g. "3d13h45m" will set the permission to expire in 3 days, 13 hours and 45 minutes time. "1482694200" will set the permission to expire at 7:30PM on 25th December 2016.

___
#### `/lp user/group <user|group> meta addtempsuffix`  
**Permission**: luckperms.user.meta.addtempsuffix or luckperms.group.meta.addtempsuffix  
**Arguments**:  
* `<priority>` - the priority to add the suffix at
* `<suffix>` - the actual suffix string
* `<duration>` - the duration until the suffix will expire
* `[context...]` - the contexts to add the suffix in

Adds a suffix to a user/group temporarily. You can wrap the suffix in " " quotes to escape spaces. Duration should either be a time period, or a unix timestamp when the permission will expire. e.g. "3d13h45m" will set the permission to expire in 3 days, 13 hours and 45 minutes time. "1482694200" will set the permission to expire at 7:30PM on 25th December 2016.

___
#### `/lp user/group <user|group> meta removetempprefix`  
**Permission**: luckperms.user.meta.removetempprefix or luckperms.group.meta.removetempprefix  
**Arguments**:  
* `<priority>` - the priority to remove the prefix at
* `[prefix]` - the actual prefix string
* `[context...]` - the contexts to remove the prefix in

Removes a tempoary prefix from a user/group. You can wrap the prefix in " " quotes to escape spaces.

___
#### `/lp user/group <user|group> meta removetempsuffix`  
**Permission**: luckperms.user.meta.removetempsuffix or luckperms.group.meta.removetempsuffix  
**Arguments**:  
* `<priority>` - the priority to remove the suffix at
* `[suffix]` - the actual suffix string
* `[context...]` - the contexts to remove the suffix in

Removes a temporary suffix from a user/group. You can wrap the suffix in " " quotes to escape spaces.

___
#### `/lp user/group <user|group> meta clear`  
**Permission**: luckperms.user.meta.clear or luckperms.group.meta.clear  
**Arguments**:  
* `[context...]` - the contexts to filter by

Removes all meta/prefixes/suffixes.

___

### Track   (/lp track \<track\> ...)
___
#### `/lp track <track> info`  
**Permission**: luckperms.track.info  
Displays the groups in the track.

___
#### `/lp track <track> append`  
**Permission**: luckperms.track.append  
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
*  luckperms.tree
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
*  luckperms.user.parent.clear
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
*  luckperms.user.editor
*  luckperms.user.switchprimarygroup
*  luckperms.user.showtracks
*  luckperms.user.promote
*  luckperms.user.demote
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
*  luckperms.group.parent.clear
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
*  luckperms.group.editor
*  luckperms.group.listmembers
*  luckperms.group.showtracks
*  luckperms.group.setweight
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
