This is a sub-page of the main **Command Usage** page. [Click here to go back.](Command-Usage)

Key things to remember from the main page:

* You use `/lpb` instead of `/lp` when running the plugin on BungeeCord
* You use `/lpv` instead of `/lp` when running the plugin on Velocity
* Required arguments are marked with angle brackets - e.g. `<required>`
* Optional arguments are marked with square brackets - e.g. `[optional]`
* If you want to include spaces in arguments, you must escape the argument with quotes - e.g. `"  "`

___

### Index
*  [/lp track \<track\> `info`](#lp-track-track-info)
*  [/lp track \<track\> `editor`](#lp-track-track-editor)
*  [/lp track \<track\> `append` \<group\>](#lp-track-track-append-group)
*  [/lp track \<track\> `insert` \<group\> \<position\>](#lp-track-track-insert-group-position)
*  [/lp track \<track\> `remove` \<group\>](#lp-track-track-remove-group)
*  [/lp track \<track\> `clear`](#lp-track-track-clear)
*  [/lp track \<track\> `rename` \<new name\>](#lp-track-track-rename-new-name)
*  [/lp track \<track\> `clone` \<name of clone\>](#lp-track-track-clone-new-name)

___
#### `/lp track <track> info`  
**Permission**: luckperms.track.info  
Displays the groups in the track.

___
#### `/lp track <track> editor`  

**Permission**: luckperms.track.editor  
Opens a web interface to edit permissions for the specified track. After changes are saved, a command will be given that you need to run for the changes to take effect.

___

#### `/lp track <track> append <group>`  

**Permission**: luckperms.track.append  
**Arguments**:  
* `<group>` - the group to add

Adds a group onto the end of the track.

___
#### `/lp track <track> insert <group> <position>`  
**Permission**: luckperms.track.insert  
**Arguments**:  
* `<group>` - the group to insert
* `<position>` - the position to insert the group at

Inserts a group into a specific position within this track. A position of 1 would place it at the start of the track.

___
#### `/lp track <track> remove <group>`  
**Permission**: luckperms.track.remove  
**Arguments**:  
* `<group>` - the group to remove

Removes a group from the track.

___
#### `/lp track <track> clear`  
**Permission**: luckperms.track.clear  
Removes all groups from the track.

___
#### `/lp track <track> rename <new name>`  
**Permission**: luckperms.track.rename  
**Arguments**:  
* `<new name>` - the new name for the track

Changes a track's name.

___
#### `/lp track <track> clone <new name>`  
**Permission**: luckperms.track.clone  
**Arguments**:  
* `<new name>` - the name of the clone

Makes an exact copy of the track under a different name.

___