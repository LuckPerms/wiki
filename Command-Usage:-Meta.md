This is a sub-page of the main **Command Usage** page. [Click here to go back.](https://github.com/lucko/LuckPerms/wiki/Command-Usage)

Key things to remember from the main page:

* You use `/lpb` instead of `/lp` when running the plugin on BungeeCord
* You use `/lpv` instead of `/lp` when running the plugin on Velocity
* Required arguments are marked with angle brackets - e.g. `<required>`
* Optional arguments are marked with square brackets - e.g. `[optional]`
* If you want to include spaces in arguments, you must escape the argument with quotes - e.g. `"  "`

___

### Index
*  [`info`](#lp-usergroup-usergroup-meta-info)
*  [`set` \<key\> \<value\> [context...]](#lp-usergroup-usergroup-meta-set)
*  [`unset` \<key\> [context...]](#lp-usergroup-usergroup-meta-unset)
*  [`settemp` \<key\> \<value\> \<duration\> [temporary modifier] [context...]](#lp-usergroup-usergroup-meta-settemp)
*  [`unsettemp` \<key\> [context...]](#lp-usergroup-usergroup-meta-unsettemp)
*  [`addprefix` \<priority\> \<prefix\> [context...]](#lp-usergroup-usergroup-meta-addprefix)
*  [`addsuffix` \<priority\> \<suffix\> [context...]](#lp-usergroup-usergroup-meta-addsuffix)
*  [`setprefix` [priority] \<prefix\> [context...]](#lp-usergroup-usergroup-meta-setprefix)
*  [`setsuffix` [priority] \<suffix\> [context...]](#lp-usergroup-usergroup-meta-setsuffix)
*  [`removeprefix` \<priority\> [prefix] [context...]](#lp-usergroup-usergroup-meta-removeprefix)
*  [`removesuffix` \<priority\> [suffix] [context...]](#lp-usergroup-usergroup-meta-removesuffix)
*  [`addtempprefix` \<priority\> \<prefix\> \<duration\> [temporary modifier] [context...]](#lp-usergroup-usergroup-meta-addtempprefix)
*  [`addtempsuffix` \<priority\> \<suffix\> \<duration\> [temporary modifier] [context...]](#lp-usergroup-usergroup-meta-addtempsuffix)
*  [`settempprefix` [priority] \<prefix\> \<duration\> [temporary modifier] [context...]](#lp-usergroup-usergroup-meta-settempprefix)
*  [`settempsuffix` [priority] \<suffix\> \<duration\> [temporary modifier] [context...]](#lp-usergroup-usergroup-meta-settempsuffix)
*  [`removetempprefix` \<priority\> [prefix] [context...]](#lp-usergroup-usergroup-meta-removetempprefix)
*  [`removetempsuffix` \<priority\> [suffix] [context...]](#lp-usergroup-usergroup-meta-removetempsuffix)
*  [`clear` [context...]](#lp-usergroup-usergroup-meta-clear)

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
* `[temporary modifier]` - how the temporary permission should be applied
* `[context...]` - the contexts to set the meta in

Sets a temporary meta key value pair for a user/group. Duration should either be a time period, or a unix timestamp when the permission will expire. e.g. "3d13h45m" will set the permission to expire in 3 days, 13 hours and 45 minutes time. "1482694200" will set the permission to expire at 7:30PM on 25th December 2016.  
LuckPerms uses a format for the relative time similar to the [SimpleDateFormat](https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html) used in java. I.e. `1M` would be one month while `1m` would be one minute.

The "temporary modifier" argument allows you to specify how the permission should be accumulated. You can pick between 3 different options.

| Modifier key | Description                                                               |
|--------------|---------------------------------------------------------------------------|
| `accumulate` | the duration of any existing nodes will just be added to the new duration |
| `replace`    | the longest duration will be kept, any others nodes will be forgotten     |
| `deny`       | the command will just fail if you try to add a duplicate temporary node   |

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
#### `/lp user/group <user|group> meta setprefix`  
**Permission**: luckperms.user.meta.setprefix or luckperms.group.meta.setprefix  
**Arguments**:  
* `[priority]` - the priority to set the prefix at
* `<prefix>` - the actual prefix string
* `[context...]` - the contexts to set the prefix in

Sets a prefix for a user/group. You can wrap the prefix in " " quotes to escape spaces. This is different from the `addprefix` command in that existing prefixes set in the same context are removed when the new prefix is added. Another difference is that the priority argument is optional in the setprefix command - LuckPerms will dertermine an appropriate value for the priority when the command is ran.

___
#### `/lp user/group <user|group> meta setsuffix`  
**Permission**: luckperms.user.meta.setsuffix or luckperms.group.meta.setsuffix  
**Arguments**:  
* `[priority]` - the priority to set the suffix at
* `<suffix>` - the actual suffix string
* `[context...]` - the contexts to set the suffix in

Sets a suffix for a user/group. You can wrap the suffix in " " quotes to escape spaces. This is different from the `addsuffix` command in that existing suffixes set in the same context are removed when the new suffix is added. Another difference is that the priority argument is optional in the setsuffix command - LuckPerms will dertermine an appropriate value for the priority when the command is ran.

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
* `[temporary modifier]` - how the temporary permission should be applied
* `[context...]` - the contexts to add the prefix in

Adds a prefix to a user/group temporarily. You can wrap the prefix in " " quotes to escape spaces. Duration should either be a time period, or a unix timestamp when the permission will expire. e.g. "3d13h45m" will set the permission to expire in 3 days, 13 hours and 45 minutes time. "1482694200" will set the permission to expire at 7:30PM on 25th December 2016.  
LuckPerms uses a format for the relative time similar to the [SimpleDateFormat](https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html) used in java. I.e. `1M` would be one month while `1m` would be one minute.

The "temporary modifier" argument allows you to specify how the permission should be accumulated. You can pick between 3 different options.

| Modifier key | Description                                                               |
|--------------|---------------------------------------------------------------------------|
| `accumulate` | the duration of any existing nodes will just be added to the new duration |
| `replace`    | the longest duration will be kept, any others nodes will be forgotten     |
| `deny`       | the command will just fail if you try to add a duplicate temporary node   |

___
#### `/lp user/group <user|group> meta addtempsuffix`  
**Permission**: luckperms.user.meta.addtempsuffix or luckperms.group.meta.addtempsuffix  
**Arguments**:  
* `<priority>` - the priority to add the suffix at
* `<suffix>` - the actual suffix string
* `<duration>` - the duration until the suffix will expire
* `[temporary modifier]` - how the temporary permission should be applied
* `[context...]` - the contexts to add the suffix in

Adds a suffix to a user/group temporarily. You can wrap the suffix in " " quotes to escape spaces. Duration should either be a time period, or a unix timestamp when the permission will expire. e.g. "3d13h45m" will set the permission to expire in 3 days, 13 hours and 45 minutes time. "1482694200" will set the permission to expire at 7:30PM on 25th December 2016.  
LuckPerms uses a format for the relative time similar to the [SimpleDateFormat](https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html) used in java. I.e. `1M` would be one month while `1m` would be one minute.

The "temporary modifier" argument allows you to specify how the permission should be accumulated. You can pick between 3 different options.

| Modifier key | Description                                                               |
|--------------|---------------------------------------------------------------------------|
| `accumulate` | the duration of any existing nodes will just be added to the new duration |
| `replace`    | the longest duration will be kept, any others nodes will be forgotten     |
| `deny`       | the command will just fail if you try to add a duplicate temporary node   |

___
#### `/lp user/group <user|group> meta settempprefix`  
**Permission**: luckperms.user.meta.settempprefix or luckperms.group.meta.settempprefix  
**Arguments**:  
* `[priority]` - the priority to set the prefix at
* `<prefix>` - the actual prefix string
* `<duration>` - the duration until the prefix will expire
* `[temporary modifier]` - how the temporary permission should be applied
* `[context...]` - the contexts to set the prefix in

Sets a prefix to a user/group temporarily. You can wrap the prefix in " " quotes to escape spaces. This is different from the `addtempprefix` command in that existing prefixes set in the same context are removed when the new prefix is added. Another difference is that the priority argument is optional in the settempprefix command - LuckPerms will dertermine an appropriate value for the priority when the command is ran.

Duration should either be a time period, or a unix timestamp when the permission will expire. e.g. "3d13h45m" will set the permission to expire in 3 days, 13 hours and 45 minutes time. "1482694200" will set the permission to expire at 7:30PM on 25th December 2016.  
LuckPerms uses a format for the relative time similar to the [SimpleDateFormat](https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html) used in java. I.e. `1M` would be one month while `1m` would be one minute.

The "temporary modifier" argument allows you to specify how the permission should be accumulated. You can pick between 3 different options.

| Modifier key | Description                                                               |
|--------------|---------------------------------------------------------------------------|
| `accumulate` | the duration of any existing nodes will just be added to the new duration |
| `replace`    | the longest duration will be kept, any others nodes will be forgotten     |
| `deny`       | the command will just fail if you try to add a duplicate temporary node   |

___
#### `/lp user/group <user|group> meta settempsuffix`  
**Permission**: luckperms.user.meta.settempsuffix or luckperms.group.meta.settempsuffix  
**Arguments**:  
* `[priority]` - the priority to set the suffix at
* `<suffix>` - the actual suffix string
* `<duration>` - the duration until the suffix will expire
* `[temporary modifier]` - how the temporary permission should be applied
* `[context...]` - the contexts to set the suffix in

Sets a suffix to a user/group temporarily. You can wrap the suffix in " " quotes to escape spaces. This is different from the `addtempsuffix` command in that existing suffixes set in the same context are removed when the new suffix is added. Another difference is that the priority argument is optional in the settempsuffix command - LuckPerms will dertermine an appropriate value for the priority when the command is ran.

Duration should either be a time period, or a unix timestamp when the permission will expire. e.g. "3d13h45m" will set the permission to expire in 3 days, 13 hours and 45 minutes time. "1482694200" will set the permission to expire at 7:30PM on 25th December 2016.  
LuckPerms uses a format for the relative time similar to the [SimpleDateFormat](https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html) used in java. I.e. `1M` would be one month while `1m` would be one minute.

The "temporary modifier" argument allows you to specify how the permission should be accumulated. You can pick between 3 different options.

| Modifier key | Description                                                               |
|--------------|---------------------------------------------------------------------------|
| `accumulate` | the duration of any existing nodes will just be added to the new duration |
| `replace`    | the longest duration will be kept, any others nodes will be forgotten     |
| `deny`       | the command will just fail if you try to add a duplicate temporary node   |

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
