Command usage is printed to the console/chat whenever invalid arguments are provided. Simply typing /perms will list all commands a user has permission to use.

### Aliases
| Bukkit           | Bungee           |
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
*  /perms - n/a
*  /perms `sync` - luckperms.sync
*  /perms `info` - luckperms.info
*  /perms `debug` - luckperms.debug
*  /perms `import` \<file\> - luckperms.import
*  /perms `creategroup` \<group\> - luckperms.creategroup
*  /perms `deletegroup` \<group\> - luckperms.deletegroup
*  /perms `listgroups` - luckperms.listgroups
*  /perms `createtrack` \<track\> - luckperms.createtrack
*  /perms `deletetrack` \<track\> - luckperms.deletetrack
*  /perms `listtracks` - luckperms.listtracks

### User
*  /perms user \<user\> `info` - luckperms.user.info
*  /perms user \<user\> `getuuid` - luckperms.user.getuuid
*  /perms user \<user\> `listnodes` - luckperms.user.listnodes
*  /perms user \<user\> `haspermission` \<node\> [server] [world] - luckperms.user.haspermission
*  /perms user \<user\> `inheritspermission` \<node\> [server] [world] - luckperms.user.inheritspermission
*  /perms user \<user\> `set` \<node\> \<true/false\> [server] [world] - luckperms.user.setpermission
*  /perms user \<user\> `unset` \<node\> [server] [world] -  luckperms.user.unsetpermission
*  /perms user \<user\> `addgroup` \<group\> [server] [world] - luckperms.user.addgroup
*  /perms user \<user\> `removegroup` \<group\> [server] [world] - luckperms.user.removegroup
*  /perms user \<user\> `settemp` \<node\> \<true/false\> \<duration\> [server] [world] - luckperms.user.settemppermission
*  /perms user \<user\> `unsettemp` \<node\> [server] [world] - luckperms.user.unsettemppermission
*  /perms user \<user\> `addtempgroup` \<group\> \<duration\> [server] [world] - luckperms.user.addtempgroup
*  /perms user \<user\> `removetempgroup` \<group\> [server] [world] - luckperms.user.removetempgroup
*  /perms user \<user\> `setprimarygroup` \<group\> - luckperms.user.setprimarygroup
*  /perms user \<user\> `showtracks` - luckperms.user.showtracks
*  /perms user \<user\> `promote` \<track\> - luckperms.user.promote
*  /perms user \<user\> `demote` \<track\> - luckperms.user.demote
*  /perms user \<user\> `showpos` \<track\> - luckperms.user.showpos
*  /perms user \<user\> `clear` - luckperms.user.clear

### Group
*  /perms group \<group\> `info` - 	luckperms.group.info
*  /perms group \<group\> `listnodes` - luckperms.group.listnodes
*  /perms group \<group\> `haspermission` \<node\> [server] [world] - luckperms.group.haspermission
*  /perms group \<group\> `inheritspermission` \<node\> [server] [world] - luckperms.group.inheritspermission
*  /perms group \<group\> `set` \<node\> \<true/false\> [server] [world] - luckperms.group.setpermission
*  /perms group \<group\> `unset` \<node\> [server] [world] - luckperms.group.unsetpermission
*  /perms group \<group\> `setinherit` \<group\> [server] [world] - luckperms.group.setinherit
*  /perms group \<group\> `unsetinherit` \<group\> [server] [world] - luckperms.group.unsetinherit
*  /perms group \<group\> `settemp` \<node\> \<true/false\> \<duration\> [server] [world] - settemppermission
*  /perms group \<group\> `unsettemp` \<node\> [server] [world] - luckperms.group.unsettemppermission
*  /perms group \<group\> `settempinherit` \<group\> \<duration\> [server] [world] - luckperms.group.settempinherit
*  /perms group \<group\> `unsettempinherit` \<group\> [server] [world] - luckperms.group.unsettempinherit
*  /perms group \<group\> `showtracks` - luckperms.group.showtracks
*  /perms group \<group\> `clear` - luckperms.group.clear

### Track
*  /perms track \<track\> `info` - luckperms.track.info
*  /perms track \<track\> `append` \<group\> - luckperms.track.append
*  /perms track \<track\> `insert` \<group\> \<position\> - luckperms.track.insert
*  /perms track \<track\> `remove` \<group\> - luckperms.track.remove
*  /perms track \<track\> `clear` - luckperms.track.clear

### Log
*  /perms log `recent` [user] [page] - luckperms.log.recent
*  /perms log `search` \<query\> [page] - luckperms.log.search
*  /perms log `notify` [on|off] - luckperms.log.notify
*  /perms log `export` \<file\> - luckperms.log.export
*  /perms log `userhistory` \<user\> [page] - luckperms.log.userhistory
*  /perms log `grouphistory` \<group\> [page] - luckperms.log.grouphistory
*  /perms log `trackhistory` \<track\> [page] - luckperms.log.trackhistory