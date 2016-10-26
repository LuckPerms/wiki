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
/luckperms user Luck permission set vault.primarygroup.owner factions world_nether
```

Setting the above permission node would modify the output to "owner". It will obviously behave in the same way as any other permission node, and is therefore inherited.

I make no check that the user is actually in the "owner" group before providing this output to Vault. A user can have the "vault.primarygroup.owner" permission, and not even be a member of the owner group. Care must be taken when using this method.

(This is really just a workaround to the poor design of Vault.)