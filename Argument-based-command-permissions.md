When enabled, LuckPerms will run extra permission checks when a player tries to modify or view permission data.

These permissions allow for finer control over what changes a player is able to make, including preventing them from granting specific groups, or making changes in certain contexts.

The extra checks can be broken down into 3 sections.

## Checks when a player modifies/views themselves or other users

### Modify self

When a player tries to use a command to modify themselves, LuckPerms will first check for `[base command permission].modify.self`. If this returns true, the action is will be allowed. If it returns false, the action will not be allowed.

If the player does not have a value set for the check (in other words, it's undefined), LuckPerms will then check for `luckperms.modify.user.self` to obtain a result. If neither checks return true, the action is not allowed.

#### Example
For example, if I run `/lp user Luck clear`, LuckPerms will check for the following permissions in this order.

* `luckperms.user.clear`
* `luckperms.user.clear.modify.self` (if this check returns true, the next permission will not be checked)
* `luckperms.modify.user.self`

If any of the checks return false, the action will not be allowed.

### Modify another player

When a player tries to use a command to modify another user, LuckPerms will first check for `[base command permission].modify.others`. If this returns true, the action is will be allowed. If it returns false, the action will not be allowed.

If the player does not have a value set for the check (in other words, it's undefined), LuckPerms will then check for `luckperms.modify.user.others` to obtain a result. If neither checks return true, the action is not allowed.

#### Example
For example, if I run `/lp user Notch clear`, LuckPerms will check for the following permissions in this order.

* `luckperms.user.clear`
* `luckperms.user.clear.modify.others` (if this check returns true/false, the next permission will not be checked)
* `luckperms.modify.user.others`

If any of the checks return false, the action will not be allowed.

### View self

When a player tries to use a command to view data about themselves, LuckPerms will first check for `[base command permission].view.self`. If this returns true, the action is will be allowed. If it returns false, the action will not be allowed.

If the player does not have a value set for the check (in other words, it's undefined), LuckPerms will then check for `luckperms.view.user.self` to obtain a result. If neither checks return true, the action is not allowed.

#### Example
For example, if I run `/lp user Luck permission info`, LuckPerms will check for the following permissions in this order.

* `luckperms.user.permission.info`
* `luckperms.user.permission.info.view.self` (if this check returns true/false, the next permission will not be checked)
* `luckperms.view.user.self`

If any of the checks return false, the action will not be allowed.

### View another player

When a player tries to use a command to view data about another user, LuckPerms will first check for `[base command permission].view.others`. If this returns true, the action is will be allowed. If it returns false, the action will not be allowed.

If the player does not have a value set for the check (in other words, it's undefined), LuckPerms will then check for `luckperms.view.user.others` to obtain a result. If neither checks return true, the action is not allowed.

#### Example
For example, if I run `/lp user Notch permission info`, LuckPerms will check for the following permissions in this order.

* `luckperms.user.permission.info`
* `luckperms.user.permission.info.view.others` (if this check returns true/false, the next permission will not be checked)
* `luckperms.view.user.others`

If any of the checks return false, the action will not be allowed.

## Checks when a player modifies/views a group

### Modify a group

When a player tries to use a command to modify a group, LuckPerms will first check for `[base command permission].modify.[group name]`. If this returns true, the action is will be allowed. If it returns false, the action will not be allowed.

If the player does not have a value set for the check (in other words, it's undefined), LuckPerms will then check for `luckperms.modify.group.[group name]` to obtain a result. If neither checks return true, the action is not allowed.

#### Example
For example, if I run `/lp group admin clear`, LuckPerms will check for the following permissions in this order.

* `luckperms.group.clear`
* `luckperms.group.clear.modify.admin` (if this check returns true/false, the next permission will not be checked)
* `luckperms.modify.group.admin`

If any of the checks return false, the action will not be allowed.

### View a group

When a player tries to use a command to view data about a group, LuckPerms will first check for `[base command permission].view.[group name]`. If this returns true, the action is will be allowed. If it returns false, the action will not be allowed.

If the player does not have a value set for the check (in other words, it's undefined), LuckPerms will then check for `luckperms.view.group.[group name]` to obtain a result. If neither checks return true, the action is not allowed.

#### Example
For example, if I run `/lp group admin permission info`, LuckPerms will check for the following permissions in this order.

* `luckperms.group.permission.info`
* `luckperms.group.permission.info.view.admin` (if this check returns true/false, the next permission will not be checked)
* `luckperms.view.group.admin`

If any of the checks return false, the action will not be allowed.

## Checks when a player makes changes in a specific context

## Checks when a player makes changes with a set of specific arguments