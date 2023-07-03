## Intro
Whilst the basics of LuckPerms are fairly simple, you can leverage a number of features and internal rules to setup an advanced permission system.

## Server and World specific permissions
LuckPerms is designed for multi-server networks. You can define permissions that only apply on certain servers and in certain worlds.

#### Some important config options:
```yml
# The name of the server, used for server specific permissions. Set to 'global' to disable.
server: global
```
This is the name of the server. If you want to set server specific permissions, you need to name your server by changing this option. Servers in your network can share the same name if you like.

```yml
# If users on this server should have their global permissions/groups applied.
include-global: true
```
The include global option is also important.

Permissions in LuckPerms are either server specific (they only apply on certain servers) or global (they apply on all servers). 

By setting the above option to **false**, only permissions that are explicitly set on that server will be applied. Global (or non-server-specific) permissions will not apply.

By changing these two options, you can setup super flexible & powerful per-server permissions and groups.

### Examples
#### Example 1
```yml
server: global
include-global: true
```
* /luckperms user Luck set minecraft.command.gamemode true **WILL APPLY**
* /luckperms user Luck set minecraft.command.gamemode true factions **WILL NOT APPLY** while not on the server "factions"

#### Example 2
```yml
server: lobby
include-global: true
```
* /luckperms user Luck set minecraft.command.gamemode true **WILL APPLY**
* /luckperms user Luck set minecraft.command.gamemode true lobby **WILL APPLY**

#### Example 3
```yml
server: bungeecord
include-global: false
```
* /luckperms user Luck set minecraft.command.gamemode true **WILL NOT APPLY**
* /luckperms user Luck set bungeecord.command.alert true bungeecord **WILL APPLY**

#### Example 4
```yml
server: global
include-global: false
```
**NO PERMISSIONS WILL APPLY**

If no server is defined, and global permissions are not being included, then nothing will be applying.

## Permission Calculation
### Permissions are calculated based on a priority system as follows.

* **Server specific permissions will override generic/global permissions.**

Example: if a user has a global "fly.use" permission, and then has a negated "fly.use" permission on the "factions" server, the server specific permission will override the globally defined one, and the user will be granted the negated node (provided they're on that server).

* **World specific permissions will override generic permissions.**

Example: if a user has a global "fly.use" permission, and then has a negated "fly.use" permission in the "world_nether" world, the world specific permission will override the globally defined one, and the user will be granted the negated node (provided they're in that world, of course.).

* **Temporary permissions will override non-temporary permissions.**

Example: if a user has a false permission set for "test.node", and a temporary true permission set for "test.node", the temporary permission will override the permanent one, and the user will be granted the true node for the duration defined for that temporary permission.

* **Wildcard/regex permissions will be overridden by normal permissions**

Example: if a user has a true permission set for "luckperms.\*", and a false permission set for "luckperms.something", the non-wildcard permission will override the wildcard, and "luckperms.something" will be set to false, despite the wildcard.

* **Temporary permissions will override other temporary permissions with a longer expiry time**

Example: if a user has a temporary true permission set for "fly.use" that expires in 1 day, and a temporary false permission set for "fly.use" that expires in 1 hour, the temporary permission expiring in 1 hour will override the one expiring in 1 day, and the negative node will take precedence for the duration of 1 hour.

* **More specific wildcards override less specific ones**

Example: if a user has "luckperms.\*" set to true, but "luckperms.user.\*" set to false, all of the user permissions will be set to false, despite the more generic wildcard for "luckperms.*".

* **Inherited permissions will be overridden by an objects own permissions.**

Example: A user is a member of the default group, which grants "some.thing.perm", but the users own permissions has "some.thing.perm" set to false. The inherited permission will be overridden by the users own permissions, and the user will be granted the negative node.

## Temporary Permissions
Temporary permissions are audited once every 3 seconds, to check if they have expired. This check happens regardless of the sync interval setting. This means that you can safely set temporary permissions to expire after a matter of seconds, and they will be removed on-time.

## Shorthand Permissions
LuckPerms has it's own system (although it's quite similar to PermissionsEx :P) that allows you to set permissions in a shorthand format.

### Examples
#### Example 1
Using the LuckPerms permission nodes as an example, say for instance, you wanted to let a user set and unset permissions for both groups and users.

Without shorthand, you would have to apply 4 nodes.
```
luckperms.user.setpermission
luckperms.user.unsetpermission
luckperms.group.setpermission
luckperms.group.unsetpermission
```
However, with shorthand, you can just apply the following node:

`luckperms.{user,group}.{setpermission,unsetpermission}`

You use curly brackets to define part of a node as a shorthand group, and then use the comma character `,` to separate entries.

#### Example 2
You can use the `-` character to create character ranges.
Without shorthand, you would have to apply 4 nodes.
```
coolkits.kit.a
coolkits.kit.b
coolkits.kit.c
coolkits.kit.d
```
However, with shorthand, you can just apply the following node:

`coolkits.kit.{a-d}`

#### Example 3
You can use the `-` character to create number ranges.
Without shorthand, you would have to apply 4 nodes.
```
prisonmines.teleport.1
prisonmines.teleport.2
prisonmines.teleport.3
prisonmines.teleport.4
```
However, with shorthand, you can just apply the following node:

`prisonmines.teleport.{1-4}`

## Regex
LuckPerms has support for regex when defining permission nodes.

Whenever regex is used, it MUST be prefixed with "R=", so LuckPerms knows to treat it as regex, and not as a normal string.

For example, if you wanted a user to be able to create both groups and tracks, you would normally just add the two permission nodes. However with regex, you can just add one. `luckperms\.create.*` Remember to escape any characters (including dots) as the entire node will be parsed.
