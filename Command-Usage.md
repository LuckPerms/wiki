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

### General
*  [/lp](Command-Usage:-General#lp)
*  [/lp `sync`](#lp-sync)
*  [/lp `info`](#lp-info)
*  [/lp `editor`](#lp-editor)
*  [/lp `debug`](#lp-debug)
*  [/lp `verbose` \<on | record | off | paste\> [filter]](#lp-verbose)
*  [/lp `tree` [scope] [player]](#lp-tree)
*  [/lp `search` \<permission\>](#lp-search)
*  [/lp `check` \<user\> \<permission\>](#lp-check)
*  [/lp `networksync`](#lp-networksync)
*  [/lp `import` \<file\>](#lp-import)
*  [/lp `export` \<file\>](#lp-export)
*  [/lp `reloadconfig`](#lp-reloadconfig)
*  [/lp `bulkupdate`](#lp-bulkupdate)
*  [/lp `migration`](#lp-migration)
*  [/lp `creategroup` \<group\>](#lp-creategroup)
*  [/lp `deletegroup` \<group\>](#lp-deletegroup)
*  [/lp `listgroups`](#lp-listgroups)
*  [/lp `createtrack` \<track\>](#lp-createtrack)
*  [/lp `deletetrack` \<track\>](#lp-deletetrack)
*  [/lp `listtracks`](#lp-listtracks)

### User   (/lp user \<user\> ...)
*  [/lp user \<user\> `info`](#lp-user-user-info)
*  [/lp user \<user\> `permission`](#permission---lp-user-user-permission---lp-group-group-permission-)
*  [/lp user \<user\> `parent`](#parent---lp-user-user-parent---lp-group-group-parent-)
*  [/lp user \<user\> `meta`](#meta---lp-user-user-meta---lp-group-group-meta-)
*  [/lp user \<user\> `editor`](#lp-user-user-editor)
*  [/lp user \<user\> `promote` \<track\> [context...]](#lp-user-user-promote)
*  [/lp user \<user\> `demote` \<track\> [context...]](#lp-user-user-demote)
*  [/lp user \<user\> `showtracks`](#lp-user-user-showtracks)
*  [/lp user \<user\> `clear` [context...]](#lp-user-user-clear)

### Group   (/lp group \<group\> ...)
*  [/lp group \<group\> `info`](#lp-group-group-info)
*  [/lp group \<group\> `permission`](#permission---lp-user-user-permission---lp-group-group-permission-)
*  [/lp group \<group\> `parent`](#parent---lp-user-user-parent---lp-group-group-parent-)
*  [/lp group \<group\> `meta`](#meta---lp-user-user-meta---lp-group-group-meta-)
*  [/lp group \<group\> `editor`](#lp-group-group-editor)
*  [/lp group \<group\> `listmembers` [page]](#lp-group-group-listmembers)
*  [/lp group \<group\> `setweight` \<weight\>](#lp-group-group-setweight)
*  [/lp group \<group\> `setdisplayname` \<name\>](#lp-group-group-setdisplayname)
*  [/lp group \<group\> `showtracks`](#lp-group-group-showtracks)
*  [/lp group \<group\> `clear` [context...]](#lp-group-group-clear)
*  [/lp group \<group\> `rename` \<new name\>](#lp-group-group-rename)
*  [/lp group \<group\> `clone` \<name of clone\>](#lp-group-group-clone)

### Permission   (/lp user \<user\> permission ... | /lp group \<group\> permission ...)
*  [`info`](#lp-usergroup-usergroup-permission-info)
*  [`set` \<node\> \<true/false\> [context...]](#lp-usergroup-usergroup-permission-set)
*  [`unset` \<node\> [context...]](#lp-usergroup-usergroup-permission-unset)
*  [`settemp` \<node\> \<true/false\> \<duration\> [temporary modifier] [context...]](#lp-usergroup-usergroup-permission-settemp)
*  [`unsettemp` \<node\> [context...]](#lp-usergroup-usergroup-permission-unsettemp)
*  [`check` \<node\> [context...]](#lp-usergroup-usergroup-permission-check)
*  [`checkinherits` \<node\> [context...]](#lp-usergroup-usergroup-permission-checkinherits)

### Parent   (/lp user \<user\> parent ... | /lp group \<group\> parent ...)
*  [`info`](#lp-usergroup-usergroup-parent-info)
*  [`set` \<group\> [context...]](#lp-usergroup-usergroup-parent-set)
*  [`add` \<group\> [context...]](#lp-usergroup-usergroup-parent-add)
*  [`remove` \<group\> [context...]](#lp-usergroup-usergroup-parent-remove)
*  [`settrack` \<track\> \<group\> [context...]](#lp-usergroup-usergroup-parent-settrack)
*  [`addtemp` \<group\> \<duration\> [temporary modifier] [context...]](#lp-usergroup-usergroup-parent-addtemp)
*  [`removetemp` \<group\> [context...]](#lp-usergroup-usergroup-parent-removetemp)
*  [`clear` [context...]](#lp-usergroup-usergroup-parent-clear)
*  [`cleartrack` \<track\> [context...]](#lp-usergroup-usergroup-parent-cleartrack)
*  [`switchprimarygroup` \<group\>](#lp-user-user-parent-switchprimarygroup)

### Meta   (/lp user \<user\> meta ... | /lp group \<group\> meta ...)
*  [`info`](#lp-usergroup-usergroup-meta-info)
*  [`set` \<key\> \<value\> [context...]](#lp-usergroup-usergroup-meta-set)
*  [`unset` \<key\> [context...]](#lp-usergroup-usergroup-meta-unset)
*  [`settemp` \<key\> \<value\> \<duration\> [temporary modifier] [context...]](#lp-usergroup-usergroup-meta-settemp)
*  [`unsettemp` \<key\> [context...]](#lp-usergroup-usergroup-meta-unsettemp)
*  [`addprefix` \<priority\> \<prefix\> [context...]](#lp-usergroup-usergroup-meta-addprefix)
*  [`addsuffix` \<priority\> \<suffix\> [context...]](#lp-usergroup-usergroup-meta-addsuffix)
*  [`removeprefix` \<priority\> [prefix] [context...]](#lp-usergroup-usergroup-meta-removeprefix)
*  [`removesuffix` \<priority\> [suffix] [context...]](#lp-usergroup-usergroup-meta-removesuffix)
*  [`addtempprefix` \<priority\> \<prefix\> \<duration\> [temporary modifier] [context...]](#lp-usergroup-usergroup-meta-addtempprefix)
*  [`addtempsuffix` \<priority\> \<suffix\> \<duration\> [temporary modifier] [context...]](#lp-usergroup-usergroup-meta-addtempsuffix)
*  [`removetempprefix` \<priority\> [prefix] [context...]](#lp-usergroup-usergroup-meta-removetempprefix)
*  [`removetempsuffix` \<priority\> [suffix] [context...]](#lp-usergroup-usergroup-meta-removetempsuffix)
*  [`clear` [context...]](#lp-usergroup-usergroup-meta-clear)

### Track   (/lp track \<track\> ...)
*  [/lp track \<track\> `info`](#lp-track-track-info)
*  [/lp track \<track\> `append` \<group\>](#lp-track-track-append)
*  [/lp track \<track\> `insert` \<group\> \<position\>](#lp-track-track-insert)
*  [/lp track \<track\> `remove` \<group\>](#lp-track-track-remove)
*  [/lp track \<track\> `clear`](#lp-track-track-clear)
*  [/lp track \<track\> `rename` \<new name\>](#lp-track-track-rename)
*  [/lp track \<track\> `clone` \<name of clone\>](#lp-track-track-clone)

### Log   (/lp log ...)
*  [/lp log `recent` [user] [page]](#lp-log-recent)
*  [/lp log `search` \<query\> [page]](#lp-log-search)
*  [/lp log `notify` [on|off]](#lp-log-notify)
*  [/lp log `export` \<file\>](#lp-log-export)
*  [/lp log `userhistory` \<user\> [page]](#lp-log-userhistory)
*  [/lp log `grouphistory` \<group\> [page]](#lp-log-grouphistory)
*  [/lp log `trackhistory` \<track\> [page]](#lp-log-trackhistory)