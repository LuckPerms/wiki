LuckPerms provides a command to help perform bulk permission modifications with ease. This command should be used with care, as it can easily corrupt or break your setup if used in the wrong way.

It may be wise to take a backup of your permission data before using the command, either by making a copy of your database / files, or by using the export command.

The commands design is basically stripped back SQL syntax. This means the data passed into the command can be converted directly to an SQL query, or used to modify data in YAML or JSON storage files. Those who have experience with SQL may find it easier to write queries directly into their database server instead of using this command.

These commands are **only available from the console**. This is because they have the potential to cause a great deal of damage to your servers data. You are asked to type a confirmation code before the action is processed, in order to prevent users from "sudoing" the console and gaining access to these commands.

The command usage is as follows...

## `/lp bulkupdate <data type> <action> [action field] [action value] [constraint...]`

A bit daunting at first, I know. To break it down...

| Argument | Description |
|----------|-------------|
| `data type` | the type of data being changed. (can be "all", "users" or "groups") |
| `action` | the action to perform on the data. (can be "update" or "delete") |
| `action field` | the field to act upon. only required for update actions. (can be "permission", "server" or "world") |
| `action value` | the value to replace with. only required for update actions |
| `constraint` | the constraints required for the update |

The `data type` is the simple bit. It simply tells LuckPerms what data should be affected by the update. Either just users, just groups, or users and groups.

The `action` is what will be done to the data. It can either be "update" or "delete". Delete simply means that any records which match the constraints will be deleted. Update will replace any values that match with another value.

The `action field` and `action value` arguments are optional because they only apply to the "update" action. The field is what will be updated, and the value is the replacement value for the field.

The `constraints` argument relates to the limitations of the update. Only the permissions (or entries) which match the constraints will be affected.

### Constraints
Constraints are split into 3 parts. The `field`, the `comparison` and the `value`.

The available `fields` are `permission`, `server` and `world`. Permission is just the permission node being stored in the file (remember that everything, even group memberships and prefixes are stored as permissions "under the hood"). The server and world fields relate to the server/world where the permission will apply. They are set to "global" if the permission doesn't have a value for either of them.

The `value` part of the constraint is just the expected value of the field, with respect to the comparison being used.

There are 4 different comparisons available.

| Comparison Symbol | Comparison Name | Description |
|-------------------|-----------------|-------------|
| `==`              | Equal to        | If the two values are the same. (ignores case) |
| `!=`              | Not equal to    | If the two values are not the same. (ignores case) |
| `~~`              | Similar to      | If the two values are "similar". Uses SQL's `LIKE` syntax. |
| `!~`              | Not similar to  | If the two values are not "similar". Uses SQL's `LIKE` syntax. |

More information about the syntax used by "similar" can be found [here](https://www.w3schools.com/sql/sql_like.asp) and [here](https://www.tutorialspoint.com/sql/sql-like-clause.htm).

The basic idea is that:
* `%` - The percent sign represents zero, one, or multiple characters
* `_` - The underscore represents a single character

##### Some examples
* `server ~~ hub_` will match server values "hub1", "hub2", "hub3" etc
* `permission !~ group.%` will match any permission which isn't a group
* `world == nether` will match world values exactly equal to "nether"

When constraints are defined in commands, the entire constraint must be wrapped with `" "` quotes.

If you are wanting to remove a specific context from a permission or group that has been assigned with a specific world or server context, you can simply just set the world and/or context to `global` which will essentially remove the context making that permission and/or group global again. 

### Command Examples
#### `/lp bulkupdate all update permission group.mod "permission == group.moderator"`
Will update all entries, and replace any occurrence of the "group.moderator" permission with "group.mod". (effectively renaming the group)

#### `/lp bulkupdate users delete "server ~~ hub%" "world == nether"`
Will delete any permission assigned to a user where the server starts with "hub" and the world is equal to "nether".

#### `/lp bulkupdate all delete "permission == essentials.fly"`
Will delete any permission entry where the permission is equal to "essentials.fly"

#### `/lp bulkupdate all delete "permission == group.vip"`
Will delete all memberships of the VIP group.

#### `/lp bulkupdate all update server global "server == factions"`
Will change any server entries from "factions" to "global"

#### `/lp bulkupdate all update permission essentials.ban "permission == essentials.mute" "server == survival"`
Will change any permission entries for "essentials.mute" to "essentials.ban" set on the "survival" server

#### `/lp bulkupdate all update server global "permission == group.mod" "server == survival"`
Will change all memberships of the MOD group to use the global context (Essentially removing the context)
