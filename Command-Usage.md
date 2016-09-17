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
*  /perms - n/a
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

### User
*  /perms user \<user\> `info`
*  /perms user \<user\> `getuuid`
*  /perms user \<user\> `listnodes`
*  /perms user \<user\> `haspermission` \<node\> [server] [world]
*  /perms user \<user\> `inheritspermission` \<node\> [server] [world]
*  /perms user \<user\> `set` \<node\> \<true/false\> [server] [world]
*  /perms user \<user\> `unset` \<node\> [server] [world]
*  /perms user \<user\> `addgroup` \<group\> [server] [world]
*  /perms user \<user\> `removegroup` \<group\> [server] [world]
*  /perms user \<user\> `settemp` \<node\> \<true/false\> \<duration\> [server] [world]
*  /perms user \<user\> `unsettemp` \<node\> [server] [world]
*  /perms user \<user\> `addtempgroup` \<group\> \<duration\> [server] [world]
*  /perms user \<user\> `removetempgroup` \<group\> [server] [world]
*  /perms user \<user\> `setprimarygroup` \<group\>
*  /perms user \<user\> `showtracks`
*  /perms user \<user\> `promote` \<track\>
*  /perms user \<user\> `demote` \<track\>
*  /perms user \<user\> `showpos` \<track\>
*  /perms user \<user\> `chatmeta`
*  /perms user \<user\> `addprefix` \<priority\> \<prefix\> [server] [world]
*  /perms user \<user\> `addsuffix` \<priority\> \<suffix\> [server] [world]
*  /perms user \<user\> `removeprefix` \<priority\> \<prefix\> [server] [world]
*  /perms user \<user\> `removesuffix` \<priority\> \<suffix\> [server] [world]
*  /perms user \<user\> `addtempprefix` \<priority\> \<prefix\> \<duration\> [server] [world]
*  /perms user \<user\> `addtempsuffix` \<priority\> \<suffix\> \<duration\> [server] [world]
*  /perms user \<user\> `removetempprefix` \<priority\> \<prefix\> [server] [world]
*  /perms user \<user\> `removetempsuffix` \<priority\> \<suffix\> [server] [world]
*  /perms user \<user\> `clear`

### Group
*  /perms group \<group\> `info`
*  /perms group \<group\> `listnodes`
*  /perms group \<group\> `haspermission` \<node\> [server] [world]
*  /perms group \<group\> `inheritspermission` \<node\> [server] [world]
*  /perms group \<group\> `set` \<node\> \<true/false\> [server] [world]
*  /perms group \<group\> `unset` \<node\> [server] [world]
*  /perms group \<group\> `setinherit` \<group\> [server] [world]
*  /perms group \<group\> `unsetinherit` \<group\> [server] [world]
*  /perms group \<group\> `settemp` \<node\> \<true/false\> \<duration\> [server] [world]
*  /perms group \<group\> `unsettemp` \<node\> [server] [world]
*  /perms group \<group\> `settempinherit` \<group\> \<duration\> [server] [world]
*  /perms group \<group\> `unsettempinherit` \<group\> [server] [world]
*  /perms group \<group\> `showtracks`
*  /perms group \<group\> `chatmeta`
*  /perms group \<group\> `addprefix` \<priority\> \<prefix\> [server] [world]
*  /perms group \<group\> `addsuffix` \<priority\> \<suffix\> [server] [world]
*  /perms group \<group\> `removeprefix` \<priority\> \<prefix\> [server] [world]
*  /perms group \<group\> `removesuffix` \<priority\> \<suffix\> [server] [world]
*  /perms group \<group\> `addtempprefix` \<priority\> \<prefix\> \<duration\> [server] [world]
*  /perms group \<group\> `addtempsuffix` \<priority\> \<suffix\> \<duration\> [server] [world]
*  /perms group \<group\> `removetempprefix` \<priority\> \<prefix\> [server] [world]
*  /perms group \<group\> `removetempsuffix` \<priority\> \<suffix\> [server] [world]
*  /perms group \<group\> `clear`
*  /perms group \<group\> `rename` \<new name\>

### Track
*  /perms track \<track\> `info`
*  /perms track \<track\> `append` \<group\>
*  /perms track \<track\> `insert` \<group\> \<position\>
*  /perms track \<track\> `remove` \<group\>
*  /perms track \<track\> `clear`
*  /perms track \<track\> `rename` \<new name\>

### Log
*  /perms log `recent` [user] [page]
*  /perms log `search` \<query\> [page]
*  /perms log `notify` [on|off]
*  /perms log `export` \<file\>
*  /perms log `userhistory` \<user\> [page]
*  /perms log `grouphistory` \<group\> [page]
*  /perms log `trackhistory` \<track\> [page]


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
*  luckperms.user.getuuid
*  luckperms.user.listnodes
*  luckperms.user.haspermission
*  luckperms.user.inheritspermission
*  luckperms.user.setpermission
*  luckperms.user.unsetpermission
*  luckperms.user.addgroup
*  luckperms.user.removegroup
*  luckperms.user.settemppermission
*  luckperms.user.unsettemppermission
*  luckperms.user.addtempgroup
*  luckperms.user.removetempgroup
*  luckperms.user.setprimarygroup
*  luckperms.user.showtracks
*  luckperms.user.promote
*  luckperms.user.demote
*  luckperms.user.showpos
*  luckperms.user.chatmeta
*  luckperms.user.addprefix
*  luckperms.user.addsuffix
*  luckperms.user.removeprefix
*  luckperms.user.removesuffix
*  luckperms.user.addtempprefix
*  luckperms.user.addtempsuffix
*  luckperms.user.removetempprefix
*  luckperms.user.removetempsuffix
*  luckperms.user.clear

### Group
*  luckperms.group.info
*  luckperms.group.listnodes
*  luckperms.group.haspermission
*  luckperms.group.inheritspermission
*  luckperms.group.setpermission
*  luckperms.group.unsetpermission
*  luckperms.group.setinherit
*  luckperms.group.unsetinherit
*  luckperms.group.settemppermission
*  luckperms.group.unsettemppermission
*  luckperms.group.settempinherit
*  luckperms.group.unsettempinherit
*  luckperms.group.showtracks
*  luckperms.group.chatmeta
*  luckperms.group.addprefix
*  luckperms.group.addsuffix
*  luckperms.group.removeprefix
*  luckperms.group.removesuffix
*  luckperms.group.addtempprefix
*  luckperms.group.addtempsuffix
*  luckperms.group.removetempprefix
*  luckperms.group.removetempsuffix
*  luckperms.group.clear
*  luckperms.group.rename

### Track
*  luckperms.track.info
*  luckperms.track.append
*  luckperms.track.insert
*  luckperms.track.remove
*  luckperms.track.clear
*  luckperms.track.rename

### Log
*  luckperms.log.recent
*  luckperms.log.search
*  luckperms.log.notify
*  luckperms.log.export
*  luckperms.log.userhistory
*  luckperms.log.grouphistory
*  luckperms.log.trackhistory
