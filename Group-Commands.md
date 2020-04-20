This is a sub-page of the main **Command Usage** page. [Click here to go back.](Command-Usage)

Key things to remember from the main page:

* You use `/lpb` instead of `/lp` when running the plugin on BungeeCord
* You use `/lpv` instead of `/lp` when running the plugin on Velocity
* Required arguments are marked with angle brackets - e.g. `<required>`
* Optional arguments are marked with square brackets - e.g. `[optional]`
* If you want to include spaces in arguments, you must escape the argument with quotes - e.g. `"  "`

___

### Index
*  [/lp group \<group\> `info`](#lp-group-group-info)
*  [/lp group \<group\> `permission`](Permission-Commands)
*  [/lp group \<group\> `parent`](Parent-Commands)
*  [/lp group \<group\> `meta`](Meta-Commands)
*  [/lp group \<group\> `editor`](#lp-group-group-editor)
*  [/lp group \<group\> `listmembers` [page]](#lp-group-group-listmembers-page)
*  [/lp group \<group\> `setweight` \<weight\>](#lp-group-group-setweight-weight)
*  [/lp group \<group\> `setdisplayname` \<name\> [context...]](#lp-group-group-setdisplayname-name)
*  [/lp group \<group\> `showtracks`](#lp-group-group-showtracks)
*  [/lp group \<group\> `clear` [context...]](#lp-group-group-clear-context)
*  [/lp group \<group\> `rename` \<new name\>](#lp-group-group-rename-new-name)
*  [/lp group \<group\> `clone` \<name of clone\>](#lp-group-group-clone-new-name)

___
#### `/lp group <group> info`  
**Permission**: luckperms.group.info  
Displays information about a group.

___
#### `/lp group <group> editor`  
**Permission**: luckperms.group.editor  
Opens a web interface to edit permissions for the specified group. After changes are saved, a command will be given that you need to run for the changes to take effect.

___
#### `/lp group <group> listmembers [page]`  
**Permission**: luckperms.group.listmembers  
**Arguments**:  
* `[page]` - the page to view

Gets a list of the other users/groups which inherit directly from this group.

___
#### `/lp group <group> setweight <weight>`  
**Permission**: luckperms.group.setweight  
**Arguments**:  
* `<weight>` - the weight to set

Sets the groups weight value, which determines the order in which groups will be considered when accumulating a users permissions. Higher value = higher weight.

___
#### `/lp group <group> setdisplayname <name>`  
**Permission**: luckperms.group.setdisplayname  
**Arguments**:  
* `<name>` - the name to set
* `[context...]` - the [contexts](Context) to set the display name in

Sets the groups display name. This can effectively be used as an "alias" for the group.

___
#### `/lp group <group> showtracks`  
**Permission**: luckperms.group.showtracks  
Displays a list of all of the tracks a group is currently on.

___
#### `/lp group <group> clear [context]`  
**Permission**: luckperms.group.clear  
**Arguments**:  
* `[context...]` - the [contexts](Context) to filter by

Clears the group's permissions, parent groups and meta.

___
#### `/lp group <group> rename <new name>`  
**Permission**: luckperms.group.rename  
**Arguments**:  
* `<new name>` - the new name for the group

Changes a group's name. Note that any members of this group will not know about the change, and will still point to the old group name. If you wish to update this, you'll need to use the bulk change feature to update the existing entries.

___
#### `/lp group <group> clone <new name>`  
**Permission**: luckperms.group.clone  
**Arguments**:  
* `<new name>` - the name of the clone

Makes an exact copy of the group under a different name.

___