Primary groups are a fairly unimportant feature in LuckPerms.

The basic concept is this:
* Every user has a set of groups they are a member of, as well as a "primary" group.
* You can define groups to be active in specific servers or worlds
* A user must be a member of their primary group globally. (in all servers and worlds)
* A user must have a primary group.

## Why even bother with Primary groups?
It's a requirement of [Vault](https://dev.bukkit.org/bukkit-plugins/vault/). If you don't use Vault, then I wouldn't even worry about the concept of a "primary group".

## What if I want per-world or per-server primary groups?
As noted above, a user only has one primary group, and the user must have the primary group globally. (in all servers and worlds). However, if you don't want this behaviour, you can override it using some special permission nodes. This will change the output of Vault lookups.

```
/luckperms user Luck permission set vault.primarygroup.Owner true factions world_nether
```

Setting the above permission node would modify the output to "owner".

More options regarding the feature can be found in the LuckPerms config file:

```yml
# This block controls the Primary Group override feature
# See the wiki for more information.
vault-primary-groups-overrides:
  # If the feature is enabled
  enabled: false
  # If the check should query the user's inherited permissions.
  # (a value of false only checks the permissions they explicitly have)
  check-inherited-permissions: false
  # If LuckPerms should check if the group exists
  check-group-exists: true
  # If LuckPerms should check if the user is actually a member of the group
  check-user-member-of: true
```

## Can I use this feature to change the "display name" of a primary group?
Yes.

Make sure you set `check-inherited-permissions: true`, and then run, for example: `/luckperms group default permission set vault.primarygroup.Member true`


## Why does this system need to be so complicated?
I don't know really. I prefer to just give you lots of options, so you can configure the plugin to your liking. This is really all just a workaround to the poor design of Vault.