This is a sub-page of the main **Command Usage** page. [Click here to go back.](https://github.com/lucko/LuckPerms/wiki/Command-Usage)

Key things to remember from the main page:

* You use `/lpb` instead of `/lp` when running the plugin on BungeeCord
* You use `/lpv` instead of `/lp` when running the plugin on Velocity
* Required arguments are marked with angle brackets - e.g. `<required>`
* Optional arguments are marked with square brackets - e.g. `[optional]`
* If you want to include spaces in arguments, you must escape the argument with quotes - e.g. `"  "`

___

### Index
*  [/lp log `recent` [user] [page]](#lp-log-recent)
*  [/lp log `search` \<query\> [page]](#lp-log-search)
*  [/lp log `notify` [on|off]](#lp-log-notify)
*  [/lp log `export` \<file\>](#lp-log-export)
*  [/lp log `userhistory` \<user\> [page]](#lp-log-userhistory)
*  [/lp log `grouphistory` \<group\> [page]](#lp-log-grouphistory)
*  [/lp log `trackhistory` \<track\> [page]](#lp-log-trackhistory)

___
#### `/lp log recent [user] [page]`  
**Permission**: luckperms.log.recent  
**Arguments**:  
* `[user]` - the name/uuid of the user to filter by
* `[page]` - the page number to view

Shows a list of recent actions.

___
#### `/lp log search <query> [page]`  
**Permission**: luckperms.log.search  
**Arguments**:  
* `<query>` - the query to search for
* `[page]` - the page number to view

Searches for log entries matching the given query.

___
#### `/lp log notify [on|off]`  
**Permission**: luckperms.log.notify  
**Arguments**:  
* `[on|off]` - whether to enable or disable

Toggles log notifications for the sender executing the command.

___
#### `/lp log export <file>`  
**Permission**: luckperms.log.export  
**Arguments**:  
* `<file>` - the file to export to

Exports the log to a list of commands, recognisable by the "/lp import" command. This feature should rarely be used, and use of "/lp export" is recommended instead.

___
#### `/lp log userhistory <user> [page]`  
**Permission**: luckperms.log.userhistory  
**Arguments**:  
* `<user>` - the user to search for
* `[page]` - the page number to view

Searches for log entries acting upon the given user.

___
#### `/lp log grouphistory <group> [page]`  
**Permission**: luckperms.log.grouphistory  
**Arguments**:  
* `<group>` - the group to search for
* `[page]` - the page number to view

Searches for log entries acting upon the given group.

___
#### `/lp log trackhistory <track> [page]`  
**Permission**: luckperms.log.trackhistory  
**Arguments**:  
* `<track>` - the track to search for
* `[page]` - the page number to view

Searches for log entries acting upon the given track.

___