This is a sub-page of the main **Command Usage** page. [Click here to go back.](Command-Usage)

Key things to remember from the main page:

* You use `/lpb` instead of `/lp` when running the plugin on BungeeCord
* You use `/lpv` instead of `/lp` when running the plugin on Velocity
* Required arguments are marked with angle brackets - e.g. `<required>`
* Optional arguments are marked with square brackets - e.g. `[optional]`
* If you want to include spaces in arguments, you must escape the argument with quotes - e.g. `"  "`

___

### Index
*  [`info`](#lp-usergroup-usergroup-permission-info-page-sorting-mode)
*  [`set` \<node\> \<true/false\> [context...]](#lp-usergroup-usergroup-permission-set-node-truefalse-context)
*  [`unset` \<node\> [context...]](#lp-usergroup-usergroup-permission-unset-node-context)
*  [`settemp` \<node\> \<true/false\> \<duration\> [temporary modifier] [context...]](#lp-usergroup-usergroup-permission-settemp-node-truefalse-duration-temporary-modifier-context)
*  [`unsettemp` \<node\> [duration] [context...]](#lp-usergroup-usergroup-permission-unsettemp-node-duration-context)
*  [`check` \<node\>](#lp-usergroup-usergroup-permission-check-node)
*  [`clear` [context...]](#lp-usergroup-usergroup-permission-clear-context)

___
#### `/lp user/group <user|group> permission info [page] [sorting mode]`  
**Permission**: luckperms.user.permission.info or luckperms.group.permission.info  
**Arguments**:  
* `[page]` - the page number to view
* `[sorting mode]` - how the results will be sorted

Displays a list of the permission nodes a user/group has.

The "sorting mode" argument allows you to specify how the list will be sorted. You can pick between 4 different options.

| Sorting mode             | Description                                                              |
|--------------------------|--------------------------------------------------------------------------|
| `priority`               | the results will be sorted according to the platform's inheritance rules |
| `!priority`/`reverse`    | it will sort it by priority and then reverse the list                    |
| `abc`/`alphabetically`   | the list will be sorted alphabetically (A - Z)                           |
| `!abc`/`!alphabetically` | will sort the list alphabetically and then reverse it (Z - A)            |

___
#### `/lp user/group <user|group> permission set <node> [true|false] [context...]`  
**Permission**: luckperms.user.permission.set or luckperms.group.permission.set  
**Arguments**:  
* `<node>` - the permission node to set
* `[true|false]` - the value to set the permission to (defaults to `true`)
* `[context...]` - the [contexts](Context) to set the permission in

Sets (or gives) a permission for a user/group with "true", granting the permission. Providing a value of "false" will negate the permission. Not adding any context will set the permission in context "global".

___
#### `/lp user/group <user|group> permission unset <node> [context...]`  
**Permission**: luckperms.user.permission.unset or luckperms.group.permission.unset  
**Arguments**:  
* `<node>` - the permission node to unset
* `[context...]` - the [contexts](Context) to unset the permission in

Unsets (or removes) a permission for a user/group.

___
#### `/lp user/group <user|group> permission settemp <node> <true|false> <duration> [temporary modifier] [context...]`  
**Permission**: luckperms.user.permission.settemp or luckperms.group.permission.settemp  
**Arguments**:  
* `<node>` - the permission node to set
* `<true|false>` - the value to set the permission to
* `<duration>` - the duration until the permission will expire
* `[temporary modifier]` - how the temporary permission should be applied
* `[context...]` - the [contexts](Context) to set the permission in

Sets a permission temporarily for a user/group. Providing a value of "false" will negate the permission. Duration should either be a time period, or a unix timestamp when the permission will expire. e.g. "1mo3d13h45m" will set the permission to expire in 1 month, 3 days, 13 hours and 45 minutes time, while "1482694200" will set the permission to expire at 7:30PM on 25th December 2016.

The "temporary modifier" argument allows you to specify how the permission should be accumulated. You can pick between 3 different options.

| Modifier key | Description                                                               |
|--------------|---------------------------------------------------------------------------|
| `accumulate` | the duration of any existing nodes will just be added to the new duration |
| `replace`    | the longest duration will be kept, any others nodes will be forgotten     |
| `deny`       | the command will just fail if you try to add a duplicate temporary node   |

___
#### `/lp user/group <user|group> permission unsettemp <node> [duration] [context...]`  
**Permission**: luckperms.user.permission.unsettemp or luckperms.group.permission.unsettemp  
**Arguments**:  
* `<node>` - the permission node to unset
* `[duration]` - the duration to subtract from the temporary permission, can be omitted to remove entirely
* `[context...]` - the [contexts](Context) to unset the permission in

Unsets a temporary permission for a user/group.

___
#### `/lp user/group <user|group> permission check <node>`  
**Permission**: luckperms.user.permission.check or luckperms.group.permission.check  
**Arguments**:  

* `<node>` - the permission node to check

Checks to see if a user/group has a certain permission, providing useful information about the factors that influenced the result of the check.

___
#### `/lp user/group <user|group> permission clear [context...]`  
**Permission**: luckperms.user.permission.clear or luckperms.group.permission.clear  
**Arguments**:  
* `[context...]` - the [contexts](Context) to filter by

Removes all permissions from the user or group.

___
