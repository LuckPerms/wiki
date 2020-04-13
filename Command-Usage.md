Command usage is printed to the console/chat whenever invalid arguments are provided. **Simply typing /lp** will list all commands a user has permission to use.

If the only thing returned when you type a command is the plugin version, you do not have permission to use any of the commands. You need to use the server console to [give yourself access to LuckPerms commands first](https://github.com/lucko/LuckPerms/wiki/Usage#granting-full-access-to-modify-permissions).

### Aliases
A list of aliases for each platform are listed below. Each command works in exactly the same manner, so you can use whichever you prefer.

| Bukkit / Sponge / Nukkit  | BungeeCord       | Velocity           |
|---------------------------|------------------|--------------------|
| /luckperms                | /luckpermsbungee | /luckpermsvelocity |
| /perms                    | /bperms          | /vperms            |
| /permissions              | /bpermissions    | /vpermissions      |
| /perm                     | /bperm           | /vperm             |
| /lp                       | /lpb             | /lpv               |

**`Important:`** The command aliases are different on BungeeCord and Velocity. This is so you can choose where your command gets directed to. If commands were the same, you would never be able to control LuckPerms on a backend server.

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
*  [/lp `editor`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-editor-type)
*  [/lp `debug`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-debug)
*  [/lp `verbose` \<on | record | off | upload\> [filter]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-verbose-onrecordoffupload-filter)
*  [/lp `tree` [scope] [player]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-tree-scope-player)
*  [/lp `search` \<permission\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-search-permission)
*  [/lp `check` \<user\> \<permission\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-check-user-permission)
*  [/lp `networksync`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-networksync)
*  [/lp `import` \<file\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-import-file)
*  [/lp `export` \<file\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-export-file)
*  [/lp `reloadconfig`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-reloadconfig)
*  [/lp `bulkupdate`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-bulkupdate-data-type-action-action-field-action-value-constraints)
*  [/lp `migration`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-migration-plugin-name-options)
*  [/lp `creategroup` \<group\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-creategroup-name)
*  [/lp `deletegroup` \<group\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-deletegroup-name)
*  [/lp `listgroups`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-listgroups)
*  [/lp `createtrack` \<track\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-createtrack-name)
*  [/lp `deletetrack` \<track\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-deletetrack-name)
*  [/lp `listtracks`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-General#lp-listtracks)

### User commands
Commands used to view or modify a specific user.

Formed of `/lp user <user> ...` - where `<user>` is the username or uuid of the user being queried / modified.
*  [/lp user \<user\> `info`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-User#lp-user-user-info)
*  [/lp user \<user\> `permission`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Permission)
*  [/lp user \<user\> `parent`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Parent)
*  [/lp user \<user\> `meta`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta)
*  [/lp user \<user\> `editor`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-User#lp-user-user-editor)
*  [/lp user \<user\> `promote` \<track\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-User#lp-user-user-promote-track-context)
*  [/lp user \<user\> `demote` \<track\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-User#lp-user-user-demote-track-context)
*  [/lp user \<user\> `showtracks`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-User#lp-user-user-showtracks)
*  [/lp user \<user\> `clear` [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-User#lp-user-user-clear-context)
*  [/lp user \<user\> `clone` \<user\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-User#lp-user-user-clone-user)

### Group commands
Commands used to view or modify a specific group.

Formed of `/lp group <group> ...` - where `<group>` is the name of the group being queried / modified.
*  [/lp group \<group\> `info`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Group#lp-group-group-info)
*  [/lp group \<group\> `permission`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Permission)
*  [/lp group \<group\> `parent`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Parent)
*  [/lp group \<group\> `meta`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta)
*  [/lp group \<group\> `editor`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Group#lp-group-group-editor)
*  [/lp group \<group\> `listmembers` [page]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Group#lp-group-group-listmembers-page)
*  [/lp group \<group\> `setweight` \<weight\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Group#lp-group-group-setweight-weight)
*  [/lp group \<group\> `setdisplayname` \<name\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Group#lp-group-group-setdisplayname-name)
*  [/lp group \<group\> `showtracks`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Group#lp-group-group-showtracks)
*  [/lp group \<group\> `clear` [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Group#lp-group-group-clear-context)
*  [/lp group \<group\> `rename` \<new name\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Group#lp-group-group-rename-new-name)
*  [/lp group \<group\> `clone` \<name of clone\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Group#lp-group-group-clone-new-name)

### Permission commands
Commands used to view or modify the permissions data of a specific user or group.

Formed of either `/lp user <user> permission ...` or `/lp group <group> permission ...`
*  [`info`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Permission#lp-usergroup-usergroup-permission-info)
*  [`set` \<node\> \<true/false\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Permission#lp-usergroup-usergroup-permission-set-node-truefalse-context)
*  [`unset` \<node\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Permission#lp-usergroup-usergroup-permission-unset-node-context)
*  [`settemp` \<node\> \<true/false\> \<duration\> [temporary modifier] [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Permission#lp-usergroup-usergroup-permission-settemp-node-truefalse-duration-temporary-modifier-context)
*  [`unsettemp` \<node\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Permission#lp-usergroup-usergroup-permission-unsettemp-node-context)
*  [`check` \<node\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Permission#lp-usergroup-usergroup-permission-check-node-context)
*  [`checkinherits` \<node\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Permission#lp-usergroup-usergroup-permission-checkinherits-node-context)
*  [`clear` [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Permission#lp-usergroup-usergroup-permission-clear-context)

### Parent commands
Commands used to view or modify the inheritance properties (parents) of a specific user or group.

Formed of either `/lp user <user> parent ...` or `/lp group <group> parent ...`
*  [`info`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Parent#lp-usergroup-usergroup-parent-info)
*  [`set` \<group\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Parent#lp-usergroup-usergroup-parent-set-group-context)
*  [`add` \<group\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Parent#lp-usergroup-usergroup-parent-add-group-context)
*  [`remove` \<group\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Parent#lp-usergroup-usergroup-parent-remove-group-context)
*  [`settrack` \<track\> \<group\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Parent#lp-usergroup-usergroup-parent-settrack-track-group-context)
*  [`addtemp` \<group\> \<duration\> [temporary modifier] [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Parent#lp-usergroup-usergroup-parent-addtemp-group-duration-temporary-modifier-context)
*  [`removetemp` \<group\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Parent#lp-usergroup-usergroup-parent-removetemp-group-context)
*  [`clear` [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Parent#lp-usergroup-usergroup-parent-clear-context)
*  [`cleartrack` \<track\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Parent#lp-usergroup-usergroup-parent-cleartrack-track-context)
*  [`switchprimarygroup` \<group\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Parent#lp-user-user-parent-switchprimarygroup-group)

### Meta commands
Commands used to view or modify the metadata of a specific user or group.

Formed of either `/lp user <user> meta ...` or `/lp group <group> meta ...`
*  [`info`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta#lp-usergroup-usergroup-meta-info)
*  [`set` \<key\> \<value\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta#lp-usergroup-usergroup-meta-set-key-value-context)
*  [`unset` \<key\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta#lp-usergroup-usergroup-meta-unset-key-value-context)
*  [`settemp` \<key\> \<value\> \<duration\> [temporary modifier] [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta#lp-usergroup-usergroup-meta-settemp-key-value-duration-temporary-modifier-context)
*  [`unsettemp` \<key\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta#lp-usergroup-usergroup-meta-unsettemp-key-context)
*  [`addprefix` \<priority\> \<prefix\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta#lp-usergroup-usergroup-meta-addprefix-priority-prefix-context)
*  [`addsuffix` \<priority\> \<suffix\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta#lp-usergroup-usergroup-meta-addsuffix-priority-suffix-context)
*  [`setprefix` [priority] \<prefix\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta#lp-usergroup-usergroup-meta-setprefix-priority-prefix-context)
*  [`setsuffix` [priority] \<suffix\> [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta#lp-usergroup-usergroup-meta-setsuffix-priority-suffix-context)
*  [`removeprefix` \<priority\> [prefix] [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta#lp-usergroup-usergroup-meta-removeprefix-priority-prefix-context)
*  [`removesuffix` \<priority\> [suffix] [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta#lp-usergroup-usergroup-meta-removesuffix-priority-suffix-context)
*  [`addtempprefix` \<priority\> \<prefix\> \<duration\> [temporary modifier] [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta#lp-usergroup-usergroup-meta-addtempprefix-priority-prefix-duration-temporary-modifier-context)
*  [`addtempsuffix` \<priority\> \<suffix\> \<duration\> [temporary modifier] [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta#lp-usergroup-usergroup-meta-addtempsuffix-priority-suffix-duration-temporary-modifier-context)
*  [`settempprefix` [priority] \<prefix\> \<duration\> [temporary modifier] [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta#lp-usergroup-usergroup-meta-settempprefix-priority-prefix-duration-temporary-modifier-context)
*  [`settempsuffix` [priority] \<suffix\> \<duration\> [temporary modifier] [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta#lp-usergroup-usergroup-meta-settempsuffix-priority-suffix-duration-temporary-modifier-context)
*  [`removetempprefix` \<priority\> [prefix] [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta#lp-usergroup-usergroup-meta-removetempprefix-priority-prefix-context)
*  [`removetempsuffix` \<priority\> [suffix] [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta#lp-usergroup-usergroup-meta-removetempsuffix-priority-suffix-context)
*  [`clear` [context...]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Meta#lp-usergroup-usergroup-meta-clear-context)

### Track commands
Commands used to view or modify a specific track.

Formed of `/lp track <track> ...` - where `<track>` is the name of the track being queried / modified.
*  [/lp track \<track\> `info`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Track#lp-track-track-info)
*  [/lp track \<track\> `append` \<group\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Track#lp-track-track-append-group)
*  [/lp track \<track\> `insert` \<group\> \<position\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Track#lp-track-track-insert-group-position)
*  [/lp track \<track\> `remove` \<group\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Track#lp-track-track-remove-group)
*  [/lp track \<track\> `clear`](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Track#lp-track-track-clear)
*  [/lp track \<track\> `rename` \<new name\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Track#lp-track-track-rename-new-name)
*  [/lp track \<track\> `clone` \<name of clone\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Track#lp-track-track-clone-new-name)

### Log commands
Commands used to view the action log.
*  [/lp log `recent` [user] [page]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Log#lp-log-recent-user-page)
*  [/lp log `search` \<query\> [page]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Log#lp-log-search-query-page)
*  [/lp log `notify` [on|off]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Log#lp-log-notify-onoff)
*  [/lp log `export` \<file\>](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Log#lp-log-export-file)
*  [/lp log `userhistory` \<user\> [page]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Log#lp-log-userhistory-user-page)
*  [/lp log `grouphistory` \<group\> [page]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Log#lp-log-grouphistory-group-page)
*  [/lp log `trackhistory` \<track\> [page]](https://github.com/lucko/LuckPerms/wiki/Command-Usage:-Log#lp-log-trackhistory-track-page)
