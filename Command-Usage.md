Command usage is printed to the console/chat whenever invalid arguments are provided. **Simply typing /lp or /lpb** will list all commands a user has permission to use.

If the only thing returned when you type a command is the plugin version, you do not have permission to use any of the commands. You need to use the server console to [give yourself access to LuckPerms commands first](https://github.com/lucko/LuckPerms/wiki/Usage#granting-full-access-to-modify-permissions).

### Aliases
A list of aliases for each platform are listed below. Each command works in exactly the same manner, so you can use whichever you prefer.

| Bukkit / Sponge  | BungeeCord       |
|------------------|------------------|
| /luckperms       | /luckpermsbungee |
| /perms           | /bperms          |
| /permissions     | /bpermissions    |
| /perm            | /bperm           |
| /lp              | /lpb             |

**`Important:`** Commands are different on BungeeCord. This is so you can choose where your command gets directed to. If commands were the same, you would never be able to control LuckPerms on a backend server.

If you are using Bukkit/Spigot, by default, all users with OP have access to LuckPerms commands. You can change this in the config.

# Overview
#### Arguments Key:
* `<required>` - you *must* specify this argument when running the command
* `[optional]` - you do not need to specify this argument. a default will be used if not given.

If you want to include spaces in arguments, you must escape the argument with quotes. `"  "`

The alias used below (/lp) can be exchanged for any of the ones listed in the aliases section above.

### General commands
General commands used to operate LuckPerms functions.

*  [/lp](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp)
*  [/lp `sync`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-sync)
*  [/lp `info`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-info)
*  [/lp `editor`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-editor)
*  [/lp `debug`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-debug)
*  [/lp `verbose` \<on | record | off | paste\> [filter]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-verbose)
*  [/lp `tree` [scope] [player]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-tree)
*  [/lp `search` \<permission\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-search)
*  [/lp `check` \<user\> \<permission\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-check)
*  [/lp `networksync`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-networksync)
*  [/lp `import` \<file\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-import)
*  [/lp `export` \<file\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-export)
*  [/lp `reloadconfig`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-reloadconfig)
*  [/lp `bulkupdate`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-bulkupdate)
*  [/lp `migration`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-migration)
*  [/lp `creategroup` \<group\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-creategroup)
*  [/lp `deletegroup` \<group\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-deletegroup)
*  [/lp `listgroups`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-listgroups)
*  [/lp `createtrack` \<track\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-createtrack)
*  [/lp `deletetrack` \<track\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-deletetrack)
*  [/lp `listtracks`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-listtracks)

### User commands
Commands used to view or modify a specific user.

Formed of `/lp user <user> ...` - where `<user>` is the username of uuid of the user being queried / modified.
*  [/lp user \<user\> `info`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-User#lp-user-user-info)
*  [/lp user \<user\> `permission`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Permission)
*  [/lp user \<user\> `parent`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Parent)
*  [/lp user \<user\> `meta`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta)
*  [/lp user \<user\> `editor`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-User#lp-user-user-editor)
*  [/lp user \<user\> `promote` \<track\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-User#lp-user-user-promote)
*  [/lp user \<user\> `demote` \<track\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-User#lp-user-user-demote)
*  [/lp user \<user\> `showtracks`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-User#lp-user-user-showtracks)
*  [/lp user \<user\> `clear` [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-User#lp-user-user-clear)

### Group commands
Commands used to view or modify a specific group.

Formed of `/lp group <group> ...` - where `<group>` is the name of the group being queried / modified.
*  [/lp group \<group\> `info`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Group#lp-group-group-info)
*  [/lp group \<group\> `permission`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Permission)
*  [/lp group \<group\> `parent`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Parent)
*  [/lp group \<group\> `meta`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta)
*  [/lp group \<group\> `editor`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Group#lp-group-group-editor)
*  [/lp group \<group\> `listmembers` [page]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Group#lp-group-group-listmembers)
*  [/lp group \<group\> `setweight` \<weight\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Group#lp-group-group-setweight)
*  [/lp group \<group\> `setdisplayname` \<name\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Group#lp-group-group-setdisplayname)
*  [/lp group \<group\> `showtracks`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Group#lp-group-group-showtracks)
*  [/lp group \<group\> `clear` [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Group#lp-group-group-clear)
*  [/lp group \<group\> `rename` \<new name\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Group#lp-group-group-rename)
*  [/lp group \<group\> `clone` \<name of clone\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Group#lp-group-group-clone)

### Permission commands
Commands used to view or modify the permissions data of a specific user or group.

Formed of either `/lp user <user> permission ...` or `/lp group <group> permission ...`
*  [`info`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Permission#lp-usergroup-usergroup-permission-info)
*  [`set` \<node\> \<true/false\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Permission#lp-usergroup-usergroup-permission-set)
*  [`unset` \<node\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Permission#lp-usergroup-usergroup-permission-unset)
*  [`settemp` \<node\> \<true/false\> \<duration\> [temporary modifier] [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Permission#lp-usergroup-usergroup-permission-settemp)
*  [`unsettemp` \<node\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Permission#lp-usergroup-usergroup-permission-unsettemp)
*  [`check` \<node\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Permission#lp-usergroup-usergroup-permission-check)
*  [`checkinherits` \<node\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Permission#lp-usergroup-usergroup-permission-checkinherits)

### Parent commands
Commands used to view or modify the inheritance properties (parents) of a specific user or group.

Formed of either `/lp user <user> parent ...` or `/lp group <group> parent ...`
*  [`info`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Parent#lp-usergroup-usergroup-parent-info)
*  [`set` \<group\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Parent#lp-usergroup-usergroup-parent-set)
*  [`add` \<group\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Parent#lp-usergroup-usergroup-parent-add)
*  [`remove` \<group\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Parent#lp-usergroup-usergroup-parent-remove)
*  [`settrack` \<track\> \<group\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Parent#lp-usergroup-usergroup-parent-settrack)
*  [`addtemp` \<group\> \<duration\> [temporary modifier] [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Parent#lp-usergroup-usergroup-parent-addtemp)
*  [`removetemp` \<group\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Parent#lp-usergroup-usergroup-parent-removetemp)
*  [`clear` [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Parent#lp-usergroup-usergroup-parent-clear)
*  [`cleartrack` \<track\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Parent#lp-usergroup-usergroup-parent-cleartrack)
*  [`switchprimarygroup` \<group\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Parent#lp-user-user-parent-switchprimarygroup)

### Meta commands
Commands used to view or modify the metadata of a specific user or group.

Formed of either `/lp user <user> meta ...` or `/lp group <group> meta ...`
*  [`info`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta#lp-usergroup-usergroup-meta-info)
*  [`set` \<key\> \<value\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta#lp-usergroup-usergroup-meta-set)
*  [`unset` \<key\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta#lp-usergroup-usergroup-meta-unset)
*  [`settemp` \<key\> \<value\> \<duration\> [temporary modifier] [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta#lp-usergroup-usergroup-meta-settemp)
*  [`unsettemp` \<key\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta#lp-usergroup-usergroup-meta-unsettemp)
*  [`addprefix` \<priority\> \<prefix\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta#lp-usergroup-usergroup-meta-addprefix)
*  [`addsuffix` \<priority\> \<suffix\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta#lp-usergroup-usergroup-meta-addsuffix)
*  [`removeprefix` \<priority\> [prefix] [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta#lp-usergroup-usergroup-meta-removeprefix)
*  [`removesuffix` \<priority\> [suffix] [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta#lp-usergroup-usergroup-meta-removesuffix)
*  [`addtempprefix` \<priority\> \<prefix\> \<duration\> [temporary modifier] [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta#lp-usergroup-usergroup-meta-addtempprefix)
*  [`addtempsuffix` \<priority\> \<suffix\> \<duration\> [temporary modifier] [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta#lp-usergroup-usergroup-meta-addtempsuffix)
*  [`removetempprefix` \<priority\> [prefix] [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta#lp-usergroup-usergroup-meta-removetempprefix)
*  [`removetempsuffix` \<priority\> [suffix] [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta#lp-usergroup-usergroup-meta-removetempsuffix)
*  [`clear` [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta#lp-usergroup-usergroup-meta-clear)

### Track commands
Commands used to view or modify a specific track.

Formed of `/lp track <track> ...` - where `<track>` is the name of the track being queried / modified.
*  [/lp track \<track\> `info`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Track#lp-track-track-info)
*  [/lp track \<track\> `append` \<group\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Track#lp-track-track-append)
*  [/lp track \<track\> `insert` \<group\> \<position\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Track#lp-track-track-insert)
*  [/lp track \<track\> `remove` \<group\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Track#lp-track-track-remove)
*  [/lp track \<track\> `clear`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Track#lp-track-track-clear)
*  [/lp track \<track\> `rename` \<new name\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Track#lp-track-track-rename)
*  [/lp track \<track\> `clone` \<name of clone\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Track#lp-track-track-clone)

### Log commands
Commands used to view the action log.
*  [/lp log `recent` [user] [page]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Log#lp-log-recent)
*  [/lp log `search` \<query\> [page]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Log#lp-log-search)
*  [/lp log `notify` [on|off]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Log#lp-log-notify)
*  [/lp log `export` \<file\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Log#lp-log-export)
*  [/lp log `userhistory` \<user\> [page]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Log#lp-log-userhistory)
*  [/lp log `grouphistory` \<group\> [page]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Log#lp-log-grouphistory)
*  [/lp log `trackhistory` \<track\> [page]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Log#lp-log-trackhistory)