This is a sub-page of the main **Command Usage** page. [Click here to go back.](https://github.com/lucko/LuckPerms/wiki/Command-Usage)

Key things to remember from the main page:

* You use `/lpb` instead of `/lp` when running the plugin on BungeeCord
* You use `/lpv` instead of `/lp` when running the plugin on Velocity
* Required arguments are marked with angle brackets - e.g. `<required>`
* Optional arguments are marked with square brackets - e.g. `[optional]`
* If you want to include spaces in arguments, you must escape the argument with quotes - e.g. `"  "`

___

### Index
*  [`info`](#lp-usergroup-usergroup-permission-info)
*  [`set` \<node\> \<true/false\> [context...]](#lp-usergroup-usergroup-permission-set)
*  [`unset` \<node\> [context...]](#lp-usergroup-usergroup-permission-unset)
*  [`settemp` \<node\> \<true/false\> \<duration\> [temporary modifier] [context...]](#lp-usergroup-usergroup-permission-settemp)
*  [`unsettemp` \<node\> [context...]](#lp-usergroup-usergroup-permission-unsettemp)
*  [`check` \<node\> [context...]](#lp-usergroup-usergroup-permission-check)
*  [`checkinherits` \<node\> [context...]](#lp-usergroup-usergroup-permission-checkinherits)
*  [`clear` [context...]](#lp-usergroup-usergroup-permission-clear)

___
#### `/lp user/group <user|group> permission info`  
**Permission**: luckperms.user.permission.info or luckperms.group.permission.info  
Displays a list of the permission nodes a user/group has.

___
#### `/lp user/group <user|group> permission set <node> [true|false] [context...]`  
**Permission**: luckperms.user.permission.set or luckperms.group.permission.set  
**Arguments**:  
* `<node>` - the permission node to set
* `[true|false]` - the value to set the permission to (defaults to `true`)
* `[context...]` - the [contexts](https://github.com/lucko/LuckPerms/wiki/Context) to set the permission in

Sets (or gives) a permission for a user/group with "true", granting the permission. Providing a value of "false" will negate the permission. Not adding any context will set the permission in context "global".

___
#### `/lp user/group <user|group> permission unset <node> [context...]`  
**Permission**: luckperms.user.permission.unset or luckperms.group.permission.unset  
**Arguments**:  
* `<node>` - the permission node to unset
* `[context...]` - the [contexts](https://github.com/lucko/LuckPerms/wiki/Context) to unset the permission in

Unsets (or removes) a permission for a user/group.

___
#### `/lp user/group <user|group> permission settemp <node> <true|false> <duration> [temporary modifier] [context...]`  
**Permission**: luckperms.user.permission.settemp or luckperms.group.permission.settemp  
**Arguments**:  
* `<node>` - the permission node to set
* `<true|false>` - the value to set the permission to
* `<duration>` - the duration until the permission will expire
* `[temporary modifier]` - how the temporary permission should be applied
* `[context...]` - the [contexts](https://github.com/lucko/LuckPerms/wiki/Context) to set the permission in

Sets a permission temporarily for a user/group. Providing a value of "false" will negate the permission. Duration should either be a time period, or a unix timestamp when the permission will expire. e.g. "1mo3d13h45m" will set the permission to expire in 1 month, 3 days, 13 hours and 45 minutes time, while "1482694200" will set the permission to expire at 7:30PM on 25th December 2016.

The "temporary modifier" argument allows you to specify how the permission should be accumulated. You can pick between 3 different options.

| Modifier key | Description                                                               |
|--------------|---------------------------------------------------------------------------|
| `accumulate` | the duration of any existing nodes will just be added to the new duration |
| `replace`    | the longest duration will be kept, any others nodes will be forgotten     |
| `deny`       | the command will just fail if you try to add a duplicate temporary node   |

___
#### `/lp user/group <user|group> permission unsettemp <node> [context...]`  
**Permission**: luckperms.user.permission.unsettemp or luckperms.group.permission.unsettemp  
**Arguments**:  
* `<node>` - the permission node to unset
* `[context...]` - the [contexts](https://github.com/lucko/LuckPerms/wiki/Context) to unset the permission in

Unsets a temporary permission for a user/group.

___
#### `/lp user/group <user|group> permission check <node> [context...]`  
**Permission**: luckperms.user.permission.check or luckperms.group.permission.check  
**Arguments**:  
* `<node>` - the permission node to check for
* `[context...]` - the [contexts](https://github.com/lucko/LuckPerms/wiki/Context) to check for the permission in

Checks to see if a user/group has a certain permission.

___
#### `/lp user/group <user|group> permission checkinherits <node> [context...]`  
**Permission**: luckperms.user.permission.checkinherits or luckperms.group.permission.checkinherits  
**Arguments**:  
* `<node>` - the permission node to check for
* `[context...]` - the [contexts](https://github.com/lucko/LuckPerms/wiki/Context) to check for the permission in

Checks to see if a user/group inherits a certain permission, and if so, where from.

___
#### `/lp user/group <user|group> permission clear [context...]`  
**Permission**: luckperms.user.permission.clear or luckperms.group.permission.clear  
**Arguments**:  
* `[context...]` - the [contexts](https://github.com/lucko/LuckPerms/wiki/Context) to filter by

Removes all permissions from the user or group.

___
