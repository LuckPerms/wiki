This is a sub-page of the main **Command Usage** page. [Click here to go back.](https://github.com/lucko/LuckPerms/wiki/Command-Usage)

Key things to remember from the main page:

* You use `/lpb` instead of `/lp` when running the plugin on BungeeCord
* You use `/lpv` instead of `/lp` when running the plugin on Velocity
* Required arguments are marked with angle brackets - e.g. `<required>`
* Optional arguments are marked with square brackets - e.g. `[optional]`
* If you want to include spaces in arguments, you must escape the argument with quotes - e.g. `"  "`

___

### Index
*  [/lp user \<user\> `info`](#lp-user-user-info)
*  [/lp user \<user\> `permission`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Permission)
*  [/lp user \<user\> `parent`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Parent)
*  [/lp user \<user\> `meta`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta)
*  [/lp user \<user\> `editor`](#lp-user-user-editor)
*  [/lp user \<user\> `promote` \<track\> [context...]](#lp-user-user-promote-track-context)
*  [/lp user \<user\> `demote` \<track\> [context...]](#lp-user-user-demote-track-context)
*  [/lp user \<user\> `showtracks`](#lp-user-user-showtracks)
*  [/lp user \<user\> `clear` [context...]](#lp-user-user-clear-context)
*  [/lp user \<user\> `clone` \<user\>](#lp-user-user-clone-user)

___
#### `/lp user <user> info`  
**Permission**: luckperms.user.info  
Displays information about a user, including their username, primary group, parents, and current contexts.

___
#### `/lp user <user> editor`  
**Permission**: luckperms.user.editor  
Opens a web interface to edit permissions for the specified group. After changes are saved, a command will be given that you need to run for the changes to take effect.

___
#### `/lp user <user> promote <track> [context...]`  
**Permission**: luckperms.user.promote  
**Arguments**:  
* `<track>` - the track to promote along
* `[context...]` - the [contexts](https://github.com/lucko/LuckPerms/wiki/Context) to promote in

This command will promote a user along a track. Firstly, the command will check to see if the user is on the track specified in the given contexts. If the user is not on the track, they will be added to the first group on the track. If they are on the track in more than one place, the command will fail. In all other cases, the user will be promoted up the track, and will be removed from the existing group. If the track action affects their primary group, that will be updated too.

___
#### `/lp user <user> demote <track> [context...]`  
**Permission**: luckperms.user.demote  
**Arguments**:  
* `<track>` - the track to demote along
* `[context...]` - the [contexts](https://github.com/lucko/LuckPerms/wiki/Context) to demote in

This command will demote a user along a track. Firstly, the command will check to see if the user is on the track specified in the given contexts. If the user is not on the track, or on the track in more than one place, the command will fail. If not, the user will be demoted down the track, and will be removed from the existing group. If the track action affects their primary group, that will be updated too.

___
#### `/lp user <user> showtracks`  
**Permission**: luckperms.user.showtracks  
Displays a list of all of the tracks a user is currently on.

___
#### `/lp user <user> clear [context...]`  
**Permission**: luckperms.user.clear  
**Arguments**:  
* `[context...]` - the [contexts](https://github.com/lucko/LuckPerms/wiki/Context) to filter by

Clears the user's permissions, parent groups and meta.

___
#### `/lp user <user> clone <user>`  
**Permission**: luckperms.user.clone  
**Arguments**:  
* `<user>` - the name of the other user

Clones the users data onto another user.

___