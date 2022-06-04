This is a sub-page of the main **Command Usage** page. [Click here to go back.](Command-Usage)

Key things to remember from the main page:

* You use `/lpb` instead of `/lp` when running the plugin on BungeeCord
* You use `/lpv` instead of `/lp` when running the plugin on Velocity
* Required arguments are marked with angle brackets - e.g. `<required>`
* Optional arguments are marked with square brackets - e.g. `[optional]`
* If you want to include spaces in arguments, you must escape the argument with quotes - e.g. `"  "`

___

### Index
*  [`info`](#lp-usergroup-usergroup-parent-info-page-sorting-mode)
*  [`set` \<group\> [context...]](#lp-usergroup-usergroup-parent-set-group-context)
*  [`add` \<group\> [context...]](#lp-usergroup-usergroup-parent-add-group-context)
*  [`remove` \<group\> [context...]](#lp-usergroup-usergroup-parent-remove-group-context)
*  [`settrack` \<track\> \<index | group\> [context...]](#lp-usergroup-usergroup-parent-settrack-track-indexgroup-context)
*  [`addtemp` \<group\> \<duration\> [temporary modifier] [context...]](#lp-usergroup-usergroup-parent-addtemp-group-duration-temporary-modifier-context)
*  [`removetemp` \<group\> [duration] [context...]](#lp-usergroup-usergroup-parent-removetemp-group-duration-context)
*  [`clear` [context...]](#lp-usergroup-usergroup-parent-clear-context)
*  [`cleartrack` \<track\> [context...]](#lp-usergroup-usergroup-parent-cleartrack-track-context)
*  [`switchprimarygroup` \<group\>](#lp-user-user-parent-switchprimarygroup-group)

___
#### `/lp user/group <user|group> parent info [page] [sorting mode]`  
**Permission**: luckperms.user.parent.info or luckperms.group.parent.info  
**Arguments**:  
* `[page]` - the page number to view
* `[sorting mode]` - how the results will be sorted
  

Displays a list of a user/group's parent groups. (groups they inherit from)

The "sorting mode" argument allows you to specify how the list will be sorted. You can pick between 4 different options.

| Sorting mode             | Description                                                              |
|--------------------------|--------------------------------------------------------------------------|
| `priority`               | The list will be sorted according to the platform's inheritance rules    |
| `!priority`/`reverse`    | The list will be sorted by priority and then reversed                    |
| `abc`/`alphabetically`   | The list will be sorted alphabetically (A - Z)                           |
| `!abc`/`!alphabetically` | The list will be sorted alphabetically and then reversed (Z - A)         |

___
#### `/lp user/group <user|group> parent set <group> [context...]`  
**Permission**: luckperms.user.parent.set or luckperms.group.parent.set  
**Arguments**:  
* `<group>` - the group to set
* `[context...]` - the [contexts](Context) to set the group in

Sets a user/group's parent. Unlike the "parent add" command, this command will clear all existing groups set at the given context. The add command will simply "add" the group to the existing ones a user/group has. If the command is executed with no context arguments, this command will also update a user's primary group.

___
#### `/lp user/group <user|group> parent add <group> [context...]`  
**Permission**: luckperms.user.parent.add or luckperms.group.parent.add  
**Arguments**:  
* `<group>` - the group to add
* `[context...]` - the [contexts](Context) to add the group in

Adds a parent to a user/group. Unlike the "parent set" command, this command will just accumulate the given parent with the ones the user/group already has. No existing parents will be removed from the user, and a user's primary group will be unaffected.

___
#### `/lp user/group <user|group> parent remove <group> [context...]`  
**Permission**: luckperms.user.parent.remove or luckperms.group.parent.remove  
**Arguments**:  
* `<group>` - the group to remove
* `[context...]` - the [contexts](Context) to remove the group in

Removes a parent from the user/group.  
If the removed group was the users primary group, will they be set back to default as primary.

___
#### `/lp user/group <user|group> parent settrack <track> <index|group> [context...]`  
**Permission**: luckperms.user.parent.settrack or luckperms.group.parent.settrack  
**Arguments**:  
* `<track>` - the track to set on
* `<index|group>` - the group to set to, or an index number relating to the position of the group on the given track
* `[context...]` - the [contexts](Context) to set the group in

Sets a users/groups position on a given track. This behaves in the same way as the set command, except it only clears existing groups which are on the specified track. Other parent groups are not affected.
___
#### `/lp user/group <user|group> parent addtemp <group> <duration> [temporary modifier] [context...]`  
**Permission**: luckperms.user.parent.addtemp or luckperms.group.parent.addtemp  
**Arguments**:  
* `<group>` - the group to add
* `<duration>` - the duration until the group will expire
* `[temporary modifier]` - how the temporary permission should be applied
* `[context...]` - the [contexts](Context) to add the group in

Adds a parent to a user/group temporarily. Duration should either be a time period, or a unix timestamp when the permission will expire. e.g. "1mo3d13h45m" will set the permission to expire in 1 month, 3 days, 13 hours and 45 minutes time, while "1482694200" will set the permission to expire at 7:30PM on 25th December 2016.  

The "temporary modifier" argument allows you to specify how the permission should be accumulated. You can pick between 3 different options.

| Modifier key | Description                                                               |
|--------------|---------------------------------------------------------------------------|
| `accumulate` | the duration of any existing nodes will just be added to the new duration |
| `replace`    | the longest duration will be kept, any others nodes will be forgotten     |
| `deny`       | the command will just fail if you try to add a duplicate temporary node   |

___
#### `/lp user/group <user|group> parent removetemp <group> [duration] [context...]`  
**Permission**: luckperms.user.parent.removetemp or luckperms.group.parent.removetemp  
**Arguments**:  
* `<group>` - the group to remove
* `[duration]` - the duration to subtract from the temporary group membership, can be omitted to remove entirely
* `[context...]` - the [contexts](Context) to remove the group in

Removes a temporary parent from the user/group.

___
#### `/lp user/group <user|group> parent clear [context...]`  
**Permission**: luckperms.user.parent.clear or luckperms.group.parent.clear  
**Arguments**:  
* `[context...]` - the [contexts](Context) to filter by

Removes all parents the user or group has.  
This will add them back to the `default` group.

___
#### `/lp user/group <user|group> parent cleartrack <track> [context...]`  
**Permission**: luckperms.user.parent.cleartrack or luckperms.group.parent.cleartrack  
**Arguments**:  
* `<track>` - the track to remove on
* `[context...]` - the [contexts](Context) to filter by

Removes all parents from the user/group on a given track.

___
#### `/lp user <user> parent switchprimarygroup <group>`  
**Permission**: luckperms.user.parent.switchprimarygroup  
**Arguments**:  
* `<group>` - the group to switch to

This command is only available for users - as groups do not have "primary" groups.

This command allows you to change a user's primary group. If they are not already a member of the specified group, they will be added to it. This should not be used as a replacement to the "parent set" command. Their existing primary group will not be removed as a parent. (a user can have multiple parent groups)

If `primary-group-calculation` is set to something other than "stored" in the LuckPerms config, you should use the [`parent add`](#lp-usergroup-usergroup-parent-add-group-context) or [`parent set`](#lp-usergroup-usergroup-parent-set-group-context) commands instead of this.

___

