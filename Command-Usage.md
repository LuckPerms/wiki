Command usage is printed to the console/chat whenever invalid arguments are provided. Simply typing /perms will list all commands a user has permission to use.

### Aliases
| Bukkit / Sponge  | Bungee           |
|------------------|------------------|
| /luckperms       | /luckpermsbungee |
| /perms           | /bperms          |
| /permissions     | /bpermissions    |
| /lp              | /lpb             |
| /perm            | /bperm           |

Arguments: \<required\> [optional]

Users with OP have access to all commands.

Additionally, you can use wildcards to grant users access to a selection of commands.
* **All commands** - luckperms.*
* **All user commands** - luckperms.user.*
* **All group commands** - luckperms.group.*
* **All track commands** - luckperms.track.*
* **All log commands** - luckperms.log.*

### General
*  /perms
*  /perms `sync`
*  /perms `info`
*  /perms `debug`
*  /perms `import` \<file\>
*  /perms `creategroup` \<group\>
*  /perms `deletegroup` \<group\>
*  /perms `listgroups`
*  /perms `createtrack` \<track\>
*  /perms `deletetrack` \<track\>
*  /perms `listtracks`

### Super Secret Console Commands
*  /perms `export` \<file\> - exports all data to a file
*  /perms `migration` - lists the platforms availble for migration
*  /perms `queuecommand` \<command args...\> - queues a command for execution. Should be used if you use LuckPerms commands in scripts.

### User   (/lp user \<user\> ...)
*  /perms user \<user\> `info`
*  **/perms user \<user\> `permission`** (see the "permission" section below.)
*  **/perms user \<user\> `parent`** (see the "parent" section below)
*  **/perms user \<user\> `meta`** (see the "meta" section below)
*  /perms user \<user\> `getuuid`
*  /perms user \<user\> `haspermission` \<node\> [server] [world]
*  /perms user \<user\> `inheritspermission` \<node\> [server] [world]
*  /perms user \<user\> `setprimarygroup` \<group\>
*  /perms user \<user\> `showtracks`
*  /perms user \<user\> `promote` \<track\>
*  /perms user \<user\> `demote` \<track\>
*  /perms user \<user\> `showpos` \<track\>
*  /perms user \<user\> `bulkchange` \<server|world\> \<from\> \<to\> (see the wiki page for details)
*  /perms user \<user\> `clear`

### Group   (/lp group \<group\> ...)
*  /perms group \<group\> `info`
*  **/perms group \<group\> `permission`** (see the "permission" section below.)
*  **/perms group \<group\> `parent`** (see the "parent" section below)
*  **/perms group \<group\> `meta`** (see the "meta" section below)
*  /perms group \<group\> `haspermission` \<node\> [server] [world]
*  /perms group \<group\> `inheritspermission` \<node\> [server] [world]
*  /perms group \<group\> `showtracks`
*  /perms group \<group\> `bulkchange` \<server|world\> \<from\> \<to\> (see the wiki page for details)
*  /perms group \<group\> `clear`
*  /perms group \<group\> `rename` \<new name\>
*  /perms group \<group\> `clone` \<name of clone\>

### Permission   (/lp user \<user\> permission ... | /lp group \<group\> permission ...)
*  `info`
*  `set` \<node\> \<true/false\> [server] [world]
*  `unset` \<node\> [server] [world]
*  `settemp` \<node\> \<true/false\> \<duration\> [server] [world]
*  `unsettemp` \<node\> [server] [world]

### Parent   (/lp user \<user\> parent ... | /lp group \<group\> parent ...)
*  `info`
*  `add` \<group\> [server] [world]
*  `remove` \<group\> [server] [world]
*  `addtemp` \<group\> \<duration\> [server] [world]
*  `removetemp` \<group\> [server] [world]

### Meta   (/lp user \<user\> meta ... | /lp group \<group\> meta ...)
*  `info`
*  `set` \<key\> \<value\> [server] [world]
*  `unset` \<key\> [server] [world]
*  `settemp` \<key\> \<value\> \<duration\> [server] [world]
*  `unsettemp` \<key\> [server] [world]
*  `addprefix` \<priority\> \<prefix\> [server] [world]
*  `addsuffix` \<priority\> \<suffix\> [server] [world]
*  `removeprefix` \<priority\> \<prefix\> [server] [world]
*  `removesuffix` \<priority\> \<suffix\> [server] [world]
*  `addtempprefix` \<priority\> \<prefix\> \<duration\> [server] [world]
*  `addtempsuffix` \<priority\> \<suffix\> \<duration\> [server] [world]
*  `removetempprefix` \<priority\> \<prefix\> [server] [world]
*  `removetempsuffix` \<priority\> \<suffix\> [server] [world]
*  `clear` [server] [world]

### Track
*  /perms track \<track\> `info`
*  /perms track \<track\> `append` \<group\>
*  /perms track \<track\> `insert` \<group\> \<position\>
*  /perms track \<track\> `remove` \<group\>
*  /perms track \<track\> `clear`
*  /perms track \<track\> `rename` \<new name\>
*  /perms track \<track\> `clone` \<name of clone\>

### Log
*  /perms log `recent` [user] [page]
*  /perms log `search` \<query\> [page]
*  /perms log `notify` [on|off]
*  /perms log `export` \<file\>
*  /perms log `userhistory` \<user\> [page]
*  /perms log `grouphistory` \<group\> [page]
*  /perms log `trackhistory` \<track\> [page]

### User Bulk Edit
(see the wiki page for details)
*  /perms usersbulkedit `group` \<group|null\> \<server|world\> \<from\> \<to\>
*  /perms usersbulkedit `permission` \<node|null\> \<server|world\> \<from\> \<to\>

## Command Permissions
### General
*  luckperms.sync
*  luckperms.info
*  luckperms.debug
*  luckperms.import
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
*  luckperms.user.parent.info
*  luckperms.user.parent.add
*  luckperms.user.parent.remove
*  luckperms.user.parent.addtemp
*  luckperms.user.parent.removetemp
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
*  luckperms.user.getuuid
*  luckperms.user.haspermission
*  luckperms.user.inheritspermission
*  luckperms.user.setprimarygroup
*  luckperms.user.showtracks
*  luckperms.user.promote
*  luckperms.user.demote
*  luckperms.user.showpos
*  luckperms.user.bulkchange
*  luckperms.user.clear

### Group
*  luckperms.group.info
*  luckperms.group.permission.info
*  luckperms.group.permission.set
*  luckperms.group.permission.unset
*  luckperms.group.permission.settemp
*  luckperms.group.permission.unsettemp
*  luckperms.group.parent.info
*  luckperms.group.parent.add
*  luckperms.group.parent.remove
*  luckperms.group.parent.addtemp
*  luckperms.group.parent.removetemp
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
*  luckperms.group.haspermission
*  luckperms.group.inheritspermission
*  luckperms.group.showtracks
*  luckperms.group.bulkchange
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
