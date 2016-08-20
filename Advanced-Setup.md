## Intro
Whilst the basics of LuckPerms are fairly simple, you can leverage a number of features and internal rules to setup an advanced permission system.

## Permission Calculation
### Permissions are calculated based on a priority system as follows.

* **Non wildcard/regex permissions will be overridden by normal permissions**

Example: if a user has a true permission set for "luckperms.\*", and a false permission set for "luckperms.something", the non-wildcard permission will override the wildcard, and "luckperms.something" will be set to false, despite the wildcard.

* **More specific wildcards override less specific ones**

Example: if a user has "luckperms.\*" set to true, but "luckperms.user.\*" set to false, all of the user permissions will be set to false, despite the more generic wildcard for "luckperms.*".

* **Temporary permissions will override non-temporary permissions.**

Example: if a user has a false permission set for "test.node", and a temporary true permission set for "test.node", the temporary permission will override the permanent one, and the user will be granted the true node.

* **World specific permissions will override generic permissions.**

Example: if a user has a global "fly.use" permission, and then has a negated "fly.use" permission in the "world_nether" world, the world specific permission will override the globally defined one, and the user will be granted the negated node (provided they're in that world, of course.).

* **Server specific permissions will override generic/global permissions.**

Example: if a user has a global "fly.use" permission, and then has a negated "fly.use" permission on the "factions" server, the server specific permission will override the globally defined one, and the user will be granted the negated node (provided they're on that server).

* **Inherited permissions will be overridden by an objects own permissions.**

Example: A user is a member of the default group, which grants "some.thing.perm", but the users own permissions has "some.thing.perm" set to false. The inherited permission will be overridden by the users own permissions, and the user will be granted the negative node.

## Temporary Permissions
Temporary permissions are audited once every 3 seconds, to check if they have expired. This check happens regardless of the sync interval setting. This means that you can safely set temporary permissions to expire after a matter of seconds, and they will be removed on-time.

## Shorthand Permissions
LuckPerms has it's own system (although it's quite similar to PermissionsEx :P) that allows you to set permissions in a shorthand format.

Using the LuckPerms permission nodes as an example, say for instance, you wanted to let a user set and unset permissions for both groups and users.

Without shorthand, you would have to apply 4 nodes.
```
luckperms.user.setpermission
luckperms.user.unsetpermission
luckperms.group.setpermission
luckperms.group.unsetpermission
```
However, with shorthand, you can just apply the following node:

`luckperms.(user|group).(setpermission|unsetpermission)`

You use brackets to define part of a node as a shorthand group, and then use the vertical bar `|` to separate entries.

The shorthand system also works for server and world names.

There are some limitations, firstly, you cannot use shorthand in the first part of the node. (The "luckperms" part in the example above)

Additionally, you cannot combine shorthand and normal text in the same part of the node.
For example, `luckperms.(user|group).(set|unset)permission` would not work.

## Regex
LuckPerms has support for regex when defining permission nodes and server/world names.

Whenever regex is used, it MUST be prefixed with "R=", so LuckPerms knows to treat it as regex, and not as a normal string.

For example, if you wanted to give all members of the default group, the `essentials.fly` permission on all of your hub servers, where the hub server names are hub1, hub2, hub3, etc.
You would use the command `/perms group default set essentials.fly true R=hub\d+`.

You can also use regex in permission nodes.
Once again using LuckPerms permissions as an example, if you wanted a user to be able to create both groups and tracks, you would normally just add the two permission nodes. However with regex, you can just add one. `luckperms\.create.*` Remember to escape any characters, specifically dots, as the entire node will be parsed.
