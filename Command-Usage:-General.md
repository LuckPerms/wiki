This is a sub-page of the main **Command Usage** page. [Click here to go back.](https://github.com/lucko/LuckPerms/wiki/Command-Usage)

Key things to remember from the main page:

* You use `/lpb` instead of `/lp` when running the plugin on BungeeCord
* You use `/lpv` instead of `/lp` when running the plugin on Velocity
* Required arguments are marked with angle brackets - e.g. `<required>`
* Optional arguments are marked with square brackets - e.g. `[optional]`
* If you want to include spaces in arguments, you must escape the argument with quotes - e.g. `"  "`

___

### Index
*  [/lp](#lp)
*  [/lp `sync`](#lp-sync)
*  [/lp `info`](#lp-info)
*  [/lp `editor`](#lp-editor-type)
*  [/lp `debug`](#lp-debug)
*  [/lp `verbose` \<on | record | off | upload\> [filter]](#lp-verbose-onrecordoffupload-filter)
*  [/lp `tree` [scope] [player]](#lp-tree-scope-player)
*  [/lp `search` \<permission\>](#lp-search-permission)
*  [/lp `check` \<user\> \<permission\>](#lp-check-user-permission)
*  [/lp `networksync`](#lp-networksync)
*  [/lp `import` \<file\>](#lp-import-file)
*  [/lp `export` \<file\>](#lp-export-file)
*  [/lp `reloadconfig`](#lp-reloadconfig)
*  [/lp `bulkupdate`](#lp-bulkupdate-data-type-action-action-field-action-value-constraints)
*  [/lp `migration`](#lp-migration-plugin-name-options)
*  [/lp `creategroup` \<group\>](#lp-creategroup-name)
*  [/lp `deletegroup` \<group\>](#lp-deletegroup-name)
*  [/lp `listgroups`](#lp-listgroups)
*  [/lp `createtrack` \<track\>](#lp-createtrack-name)
*  [/lp `deletetrack` \<track\>](#lp-deletetrack-name)
*  [/lp `listtracks`](#lp-listtracks)

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
#### `/lp editor [type]`  
**Permission**: luckperms.editor  
**Arguments**:  
* `[type]` - the types to include in the editor session. can be "all", "users" or "groups"

Opens a web interface to edit permissions data. After changes are saved, a command will be given that you need to run for the changes to take effect.

___
#### `/lp debug`  
**Permission**: luckperms.debug  
Records debugging output and provides you with a link.

___
#### `/lp verbose <on|record|off|upload> [filter]`  
**Permission**: luckperms.verbose  
**Arguments**:  
* `<on|record|off|upload>` - whether to enable/disable logging, or to upload the logged output
* `[filter]` - the filter to sort the output

Controls the LuckPerms verbose logging system. This allows you to listen for all permission checks against players on the server. Whenever a permission is checked by a plugin, the check is passed onto the verbose handler.    

If your filters match the permission check, you will be notified.    

`on` will enable the system, and will send you an alert in chat when the filter is matched. `record` will do the same, however you will not be notified of checks in the chat. `off` will simply disable the checking, and `upload` will upload the first results to the web viewer, and provide you with a link.    

Filters match the start of permissions or the user being checked. You can use `&` (and) and `|` (or) symbols, and `!` to negate a match. Parenthesis `( )` are also supported.   

**For example:**    
* `Luck & (essentials | worldedit)` - matches any checks made against my user starting with "essentials" or "worldedit"
* `!Luck & !anticheat` - matches any checks not against my user and not starting with "anticheat"
* `anticheat & !anticheat.check` - matches any checks starting with "anticheat" but not starting with "anticheat.check"    
     
More information can be found [**here**](https://github.com/lucko/LuckPerms/wiki/Verbose)

___
#### `/lp tree [scope] [player]`  
**Permission**: luckperms.tree  
**Arguments**:  
* `[scope]` - the root of the tree (specify `.` to include all permissions)
* `[player]` - the name of an online player to check against

Generates a tree view of permissions registered to the server. The tree is built using data exposed to the server by plugins, and expanded over time as plugins check for permissions.

All arguments are optional. The default selection is `.` (just a dot, which means all).

Scope allows you to only generate a part of the tree. For example, a scope of `luckperms.user` will only return the branch of the tree starting with "luckperms.user".

___
#### `/lp search <permission>`  
**Permission**: luckperms.search  
**Arguments**:  
* `<permission>` - the permission to search for

Searches all users/groups for a specific permission, and returns a paginated list of all found entries. 

___
#### `/lp check <user> <permission>`  
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
#### `/lp import <file>`  
**Permission**: luckperms.import  
**Arguments**:  
* `<file>` - the file to import from

Imports data into LuckPerms from a file. The file must be a list of commands, starting with "/luckperms". This file can be generated using the export command. The file is expected to be in the plugin directory.

___
#### `/lp export <file>`  
**Permission**: luckperms.export  
**Arguments**:  
* `<file>` - the file to export to

Exports data from LuckPerms into a file. This file can either be used as a backup, or used to move data between LuckPerms installations. The file can be re-imported using the import command. The generated file will be in the plugin directory.

___
#### `/lp reloadconfig`  
**Permission**: luckperms.reloadconfig  
Reloads some values from the configuration file. Not all entries are reloaded by this command, and some require a full server reboot to take effect. (storage settings, for example)

___
#### `/lp bulkupdate <data type> <action> [action field] [action value] [constraints...]`  
**Permission**: **Console Only**  
**Arguments**:  
* `<data type>` - the type of data being changed. (can be `all`, `users` or `groups`)
* `<action>` - the action to perform on the data. (can be `update` or `delete`)
* `[action field]` - the field to act upon. only required for update actions. (can be `permission`, `server` or `world`)
* `[action value]` - the value to replace with. only required for update actions
* `[constraints]` - the constraints required for the update

Allows you to perform a bulk modification to all permission data. A detailed guide on how to use this command can be found [here](https://github.com/lucko/LuckPerms/wiki/Bulk-Editing).

___
#### `/lp migration <plugin name> [options]`  
**Permission**: luckperms.migration  
**Arguments**:  
* `<plugin name>` - the plugin to migrate data from
* `[options]` - the options required for certain plugin migrations

Main command used for the migration system. Allows you to import permissions data into LuckPerms from other permission plugins. More information about this feature can be found [here](https://github.com/lucko/LuckPerms/wiki/Migration).

___
#### `/lp creategroup <name>`  
**Permission**: luckperms.creategroup  
**Arguments**:  
* `<name>` - the name of the group

Creates a new group.

___
#### `/lp deletegroup <name>`  
**Permission**: luckperms.deletegroup  
**Arguments**:  
* `<name>` - the name of the group

Permanently deletes a group.

___
#### `/lp listgroups`  
**Permission**: luckperms.listgroups  
Displays a list of all current groups.

___
#### `/lp createtrack <name>`  
**Permission**: luckperms.createtrack  
**Arguments**:  
* `<name>` - the name of the track

Creates a new track.

___
#### `/lp deletetrack <name>`  
**Permission**: luckperms.deletetrack  
**Arguments**:  
* `<name>` - the name of the track

Permanently deletes a track.

___
#### `/lp listtracks`  
**Permission**: luckperms.listtracks  
Displays a list of all current tracks.

___