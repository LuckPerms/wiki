LuckPerms is able to automatically import permissions data from other plugins - we call this system "migration".

### Intro
It should be noted that these scripts are not perfect. They will do a pretty decent job at converting all of your existing data, and work perfectly in *most cases*. However, not all data is the same, and there are sometimes things I haven't accounted for.

LuckPerms has some similarities with other permission plugins, however, some parts are fundamentally different, and therefore sometimes automatic migration is tricky.

Additionally, letting the plugin migrate all of your data for you means you will not have a chance to learn any of the LuckPerms commands. This may become an issue later on. 😉 If you're migrating from PermissionsEx or GroupManager, you might [find this page useful](Migrating-from-GroupManager-or-PermissionsEx).

If you have an old permissions setup, or a setup you're not completely happy with, now might be a great time to have a restructure and cleanup, and a chance to learn LuckPerms commands in the process!


#### Supported plugins
Migration is supported for:

* GroupManager
* PermissionsEx (Bukkit/Spigot only)
* zPermissions
* bPermissions
* PermissionsBukkit
* PowerRanks
* UltraPermissions
* BungeePerms (migration can only be performed on the proxy)

## The process
The migration process is fairly simple, however it varies slightly for each platform.

#### Step 1: Install LuckPerms

Firstly, you need to [install LuckPerms](Installation). Don't remove your old permissions plugin yet.

Ensure that your old permissions plugin is still enabling properly. The migration process won't work if your old setup is broken.

If you intend to change your data [storage type](Storage-types), for instance, to mysql, it is easiest to do this now. If you decide to change storage types after the migration, follow the instructions in [Switching Storage Types](Switching-storage-types).

#### Step 2: Install the correct migration plugin

Download the jar that corresponds to your existing permission plugin from the table below. Add it to your plugins folder too.

| Plugin            | Migration Jar                                                | Migration Command            |
| ----------------- | ------------------------------------------------------------ | ---------------------------- |
| GroupManager      | [luckperms-migration-groupmanager.jar](https://ci.lucko.me/job/luckperms-migration/lastSuccessfulBuild/artifact/groupmanager/build/libs/luckperms-migration-groupmanager.jar) | `/migrate-groupmanager`      |
| PermissionsEx     | [luckperms-migration-permissionsex.jar](https://ci.lucko.me/job/luckperms-migration/lastSuccessfulBuild/artifact/permissionsex/build/libs/luckperms-migration-permissionsex.jar) | `/migrate-permissionsex`     |
| zPermissions      | [luckperms-migration-zpermissions.jar](https://ci.lucko.me/job/luckperms-migration/lastSuccessfulBuild/artifact/zpermissions/build/libs/luckperms-migration-zpermissions.jar) | `/migrate-zpermissions`      |
| bPermissions      | [luckperms-migration-bpermissions.jar](https://ci.lucko.me/job/luckperms-migration/lastSuccessfulBuild/artifact/bpermissions/build/libs/luckperms-migration-bpermissions.jar) | `/migrate-bpermissions`      |
| PermissionsBukkit | [luckperms-migration-permissionsbukkit.jar](https://ci.lucko.me/job/luckperms-migration/lastSuccessfulBuild/artifact/permissionsbukkit/build/libs/luckperms-migration-permissionsbukkit.jar) | `/migrate-permissionsbukkit` |
| PowerRanks        | [luckperms-migration-powerranks.jar](https://ci.lucko.me/job/luckperms-migration/lastSuccessfulBuild/artifact/powerranks/build/libs/luckperms-migration-powerranks.jar) | `/migrate-powerranks`        |
| UltraPermissions  | [luckperms-migration-ultrapermissions.jar](https://ci.lucko.me/job/luckperms-migration/lastSuccessfulBuild/artifact/ultrapermissions/build/libs/luckperms-migration-ultrapermissions.jar) | `/migrate-ultrapermissions` |
| BungeePerms       | [luckperms-migration-bungeeperms.jar](https://ci.lucko.me/job/luckperms-migration/lastSuccessfulBuild/artifact/bungeeperms/build/libs/luckperms-migration-bungeeperms.jar) | `/migrate-bungeeperms`       |

#### Step 3: Restart your server, then run the migration command.

Restart the server to allow your existing plugin, LuckPerms, and the migration plugin to load correctly.

Then, go to your server console and run the migration command listed in the table above.

Sit back, relax, and let LuckPerms handle the rest! You will be notified of the migration progress, and then notified again once it has finished.

When the process has finished, stop the server, remove the your old permissions plugin and the migration jar, then start your server again.

If you're migrating from GroupManager or PermissionsEx, there are some additional resources [here](Migrating-from-GroupManager-or-PermissionsEx) which may be useful!