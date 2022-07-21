Command usage is printed to the console/chat whenever invalid arguments are provided. **Simply typing /lp** will list all commands a user has permission to use.

If the only thing returned when you type a command is the plugin version, you do not have permission to use any of the commands. You need to use the server console to [give yourself access to LuckPerms commands first](Usage#granting-full-access-to-modify-permissions).

### Aliases
A list of aliases for each platform are listed below. Each command works in exactly the same manner, so you can use whichever you prefer.

| Bukkit / Sponge / Fabric / Forge / Nukkit   | BungeeCord         | Velocity             |
| ----------------------------------- | ------------------ | -------------------- |
| `/lp`                               | `/lpb`             | `/lpv`               |
| `/luckperms`                        | `/luckpermsbungee` | `/luckpermsvelocity` |
| `/permissions` (*deprecated*)       |                    |                      |
| `/perms` (*deprecated*)             |                    |                      |
| `/perm` (*deprecated*)              |                    |                      |

**`Important:`** The command aliases are different on BungeeCord and Velocity. This is so you can choose where the command is executed. If the aliases were the same, you would never be able to control LuckPerms on a backend server as the command would always be handled by the proxy!

If you are using Bukkit/Spigot, by default, all users with OP have access to LuckPerms commands. You can change this in the config.

# Overview
#### Arguments Key:
* `<required>` - you *must* specify this argument when running the command
* `[optional]` - you do not need to specify this argument. a default will be used if not given.

If you want to include spaces in arguments, you must escape the argument with quotes. `"  "`

The alias used below (`/lp`) can be exchanged for any of the ones listed in the aliases section above.

### General commands
General commands used to operate LuckPerms functions.

*  [/lp](General-Commands#lp)
*  [/lp `sync`](General-Commands#lp-sync)
*  [/lp `info`](General-Commands#lp-info)
*  [/lp `editor`](General-Commands#lp-editor-type)
*  [/lp `verbose` \<on | record | off | upload\> [filter]](General-Commands#lp-verbose-onrecordoffupload-filter)
*  [/lp `tree` [scope] [player]](General-Commands#lp-tree-scope-player)
*  [/lp `search` [comparison] \<permission\>](General-Commands#lp-search-comparison-permission)
*  [/lp `networksync`](General-Commands#lp-networksync)
*  [/lp `import` \<file | code --upload\> [--replace]](General-Commands#lp-import-filecode---upload---replace)
*  [/lp `export` \<file\> [--upload]](General-Commands#lp-export-file--upload)
*  [/lp `reloadconfig`](General-Commands#lp-reloadconfig)
*  [/lp `bulkupdate`](General-Commands#lp-bulkupdate-data-type-action-action-field-action-value-constraints)
*  [/lp `translations`](General-Commands#lp-translations)
*  [/lp `creategroup` \<group\> [weight] [displayname]](General-Commands#lp-creategroup-name-weight-displayname)
*  [/lp `deletegroup` \<group\>](General-Commands#lp-deletegroup-name)
*  [/lp `listgroups`](General-Commands#lp-listgroups)
*  [/lp `createtrack` \<track\>](General-Commands#lp-createtrack-name)
*  [/lp `deletetrack` \<track\>](General-Commands#lp-deletetrack-name)
*  [/lp `listtracks`](General-Commands#lp-listtracks)

### User commands
Commands used to view or modify a specific user.

Formed of `/lp user <user> ...` - where `<user>` is the username or uuid of the user being queried / modified.
*  [/lp user \<user\> `info`](User-Commands#lp-user-user-info)
*  [/lp user \<user\> `permission`](Permission-Commands)
*  [/lp user \<user\> `parent`](Parent-Commands)
*  [/lp user \<user\> `meta`](Meta-Commands)
*  [/lp user \<user\> `editor`](User-Commands#lp-user-user-editor)
*  [/lp user \<user\> `promote` \<track\> [context...]](User-Commands#lp-user-user-promote-track-context)
*  [/lp user \<user\> `demote` \<track\> [context...]](User-Commands#lp-user-user-demote-track-context)
*  [/lp user \<user\> `showtracks`](User-Commands#lp-user-user-showtracks)
*  [/lp user \<user\> `clear` [context...]](User-Commands#lp-user-user-clear-context)
*  [/lp user \<user\> `clone` \<user\>](User-Commands#lp-user-user-clone-user)

### Group commands
Commands used to view or modify a specific group.

Formed of `/lp group <group> ...` - where `<group>` is the name of the group being queried / modified.
*  [/lp group \<group\> `info`](Group-Commands#lp-group-group-info)
*  [/lp group \<group\> `permission`](Permission-Commands)
*  [/lp group \<group\> `parent`](Parent-Commands)
*  [/lp group \<group\> `meta`](Meta-Commands)
*  [/lp group \<group\> `editor`](Group-Commands#lp-group-group-editor)
*  [/lp group \<group\> `listmembers` [page]](Group-Commands#lp-group-group-listmembers-page)
*  [/lp group \<group\> `setweight` \<weight\>](Group-Commands#lp-group-group-setweight-weight)
*  [/lp group \<group\> `setdisplayname` \<name\>](Group-Commands#lp-group-group-setdisplayname-name)
*  [/lp group \<group\> `showtracks`](Group-Commands#lp-group-group-showtracks)
*  [/lp group \<group\> `clear` [context...]](Group-Commands#lp-group-group-clear-context)
*  [/lp group \<group\> `rename` \<new name\>](Group-Commands#lp-group-group-rename-new-name)
*  [/lp group \<group\> `clone` \<name of clone\>](Group-Commands#lp-group-group-clone-new-name)

### Permission commands
Commands used to view or modify the permissions data of a specific user or group.

Formed of either `/lp user <user> permission ...` or `/lp group <group> permission ...`
*  [`info`](Permission-Commands#lp-usergroup-usergroup-permission-info)
*  [`set` \<node\> \<true/false\> [context...]](Permission-Commands#lp-usergroup-usergroup-permission-set-node-truefalse-context)
*  [`unset` \<node\> [context...]](Permission-Commands#lp-usergroup-usergroup-permission-unset-node-context)
*  [`settemp` \<node\> \<true/false\> \<duration\> [temporary modifier] [context...]](Permission-Commands#lp-usergroup-usergroup-permission-settemp-node-truefalse-duration-temporary-modifier-context)
*  [`unsettemp` \<node\> [duration] [context...]](Permission-Commands#lp-usergroup-usergroup-permission-unsettemp-node-duration-context)
*  [`check` \<node\>](Permission-Commands#lp-usergroup-usergroup-permission-check-node)
*  [`clear` [context...]](Permission-Commands#lp-usergroup-usergroup-permission-clear-context)

### Parent commands
Commands used to view or modify the inheritance properties (parents) of a specific user or group.

Formed of either `/lp user <user> parent ...` or `/lp group <group> parent ...`
*  [`info`](Parent-Commands#lp-usergroup-usergroup-parent-info)
*  [`set` \<group\> [context...]](Parent-Commands#lp-usergroup-usergroup-parent-set-group-context)
*  [`add` \<group\> [context...]](Parent-Commands#lp-usergroup-usergroup-parent-add-group-context)
*  [`remove` \<group\> [context...]](Parent-Commands#lp-usergroup-usergroup-parent-remove-group-context)
*  [`settrack` \<track\> \<group\> [context...]](Parent-Commands#lp-usergroup-usergroup-parent-settrack-track-group-context)
*  [`addtemp` \<group\> \<duration\> [temporary modifier] [context...]](Parent-Commands#lp-usergroup-usergroup-parent-addtemp-group-duration-temporary-modifier-context)
*  [`removetemp` \<group\> [duration] [context...]](Parent-Commands#lp-usergroup-usergroup-parent-removetemp-group-duration-context)
*  [`clear` [context...]](Parent-Commands#lp-usergroup-usergroup-parent-clear-context)
*  [`cleartrack` \<track\> [context...]](Parent-Commands#lp-usergroup-usergroup-parent-cleartrack-track-context)
*  [`switchprimarygroup` \<group\>](Parent-Commands#lp-user-user-parent-switchprimarygroup-group)

### Meta commands
Commands used to view or modify the metadata of a specific user or group.

Formed of either `/lp user <user> meta ...` or `/lp group <group> meta ...`
*  [`info`](Meta-Commands#lp-usergroup-usergroup-meta-info)
*  [`set` \<key\> \<value\> [context...]](Meta-Commands#lp-usergroup-usergroup-meta-set-key-value-context)
*  [`unset` \<key\> [context...]](Meta-Commands#lp-usergroup-usergroup-meta-unset-key-value-context)
*  [`settemp` \<key\> \<value\> \<duration\> [temporary modifier] [context...]](Meta-Commands#lp-usergroup-usergroup-meta-settemp-key-value-duration-temporary-modifier-context)
*  [`unsettemp` \<key\> [context...]](Meta-Commands#lp-usergroup-usergroup-meta-unsettemp-key-context)
*  [`addprefix` \<priority\> \<prefix\> [context...]](Meta-Commands#lp-usergroup-usergroup-meta-addprefix-priority-prefix-context)
*  [`addsuffix` \<priority\> \<suffix\> [context...]](Meta-Commands#lp-usergroup-usergroup-meta-addsuffix-priority-suffix-context)
*  [`setprefix` [priority] \<prefix\> [context...]](Meta-Commands#lp-usergroup-usergroup-meta-setprefix-priority-prefix-context)
*  [`setsuffix` [priority] \<suffix\> [context...]](Meta-Commands#lp-usergroup-usergroup-meta-setsuffix-priority-suffix-context)
*  [`removeprefix` \<priority\> [prefix] [context...]](Meta-Commands#lp-usergroup-usergroup-meta-removeprefix-priority-prefix-context)
*  [`removesuffix` \<priority\> [suffix] [context...]](Meta-Commands#lp-usergroup-usergroup-meta-removesuffix-priority-suffix-context)
*  [`addtempprefix` \<priority\> \<prefix\> \<duration\> [temporary modifier] [context...]](Meta-Commands#lp-usergroup-usergroup-meta-addtempprefix-priority-prefix-duration-temporary-modifier-context)
*  [`addtempsuffix` \<priority\> \<suffix\> \<duration\> [temporary modifier] [context...]](Meta-Commands#lp-usergroup-usergroup-meta-addtempsuffix-priority-suffix-duration-temporary-modifier-context)
*  [`settempprefix` [priority] \<prefix\> \<duration\> [temporary modifier] [context...]](Meta-Commands#lp-usergroup-usergroup-meta-settempprefix-priority-prefix-duration-temporary-modifier-context)
*  [`settempsuffix` [priority] \<suffix\> \<duration\> [temporary modifier] [context...]](Meta-Commands#lp-usergroup-usergroup-meta-settempsuffix-priority-suffix-duration-temporary-modifier-context)
*  [`removetempprefix` \<priority\> [prefix] [context...]](Meta-Commands#lp-usergroup-usergroup-meta-removetempprefix-priority-prefix-context)
*  [`removetempsuffix` \<priority\> [suffix] [context...]](Meta-Commands#lp-usergroup-usergroup-meta-removetempsuffix-priority-suffix-context)
*  [`clear` [context...]](Meta-Commands#lp-usergroup-usergroup-meta-clear-context)

### Track commands
Commands used to view or modify a specific track.

Formed of `/lp track <track> ...` - where `<track>` is the name of the track being queried / modified.
*  [/lp track \<track\> `info`](Track-Commands#lp-track-track-info)
*  [/lp track \<track\> `editor`](Track-Commands#lp-track-track-editor)
*  [/lp track \<track\> `append` \<group\>](Track-Commands#lp-track-track-append-group)
*  [/lp track \<track\> `insert` \<group\> \<position\>](Track-Commands#lp-track-track-insert-group-position)
*  [/lp track \<track\> `remove` \<group\>](Track-Commands#lp-track-track-remove-group)
*  [/lp track \<track\> `clear`](Track-Commands#lp-track-track-clear)
*  [/lp track \<track\> `rename` \<new name\>](Track-Commands#lp-track-track-rename-new-name)
*  [/lp track \<track\> `clone` \<name of clone\>](Track-Commands#lp-track-track-clone-new-name)

### Log commands
Commands used to view the action log.
*  [/lp log `recent` [user] [page]](Log-Commands#lp-log-recent-user-page)
*  [/lp log `search` \<query\> [page]](Log-Commands#lp-log-search-query-page)
*  [/lp log `notify` [on|off]](Log-Commands#lp-log-notify-onoff)
*  [/lp log `userhistory` \<user\> [page]](Log-Commands#lp-log-userhistory-user-page)
*  [/lp log `grouphistory` \<group\> [page]](Log-Commands#lp-log-grouphistory-group-page)
*  [/lp log `trackhistory` \<track\> [page]](Log-Commands#lp-log-trackhistory-track-page)
