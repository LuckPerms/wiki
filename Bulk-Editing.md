LuckPerms provides some commands to help perform bulk permission modifications with ease. These commands should be used with care, as they can easily corrupt your setup if used in the wrong way. Having said that, most mistakes should be recoverable.  Also be aware that when performing changes to lots of users, there is a potential for a lot of load on your storage, as well as potentially high memory usage on your server.

## /perms group/user \<?\> bulkchange \<server|world\> \<from\> \<to\>
This command allows you to bulk change the context of a user/group's permissions. Context is the specific servers or worlds that a permission node applies in.

Instead of (badly) explaining how the system works, I have provided some examples below, so you can (hopefully!) teach yourself, and build the commands yourself. 😄

Just note that this command **will** modify group nodes, except if the group is a user's primary group.

#### Example 1
```
essentials.fly (server="factions")
essentials.ban (server="factions")
essentials.gamemode (server="creative")
essentials.msg
```
`/perms group/user <?> bulkchange server factions kitpvp`
```
essentials.fly (server="kitpvp")
essentials.ban (server="kitpvp")
essentials.gamemode (server="creative")
essentials.msg
```

#### Example 2
```
essentials.fly (server="factions") (world="world_nether")
essentials.ban (server="factions") (world="world_nether")
essentials.gamemode (server="creative") (world="world_nether")
essentials.msg
```
`/perms group/user <?> bulkchange world world_nether null`
```
essentials.fly (server="factions")
essentials.ban (server="factions")
essentials.gamemode (server="creative")
essentials.msg
```

#### Example 3
```
essentials.fly
essentials.ban
essentials.gamemode
essentials.msg
```
`/perms group/user <?> bulkchange server global creative`

`/perms group/user <?> bulkchange world null some_world`
```
essentials.fly (server="creative") (world="some_world")
essentials.ban (server="creative") (world="some_world")
essentials.gamemode (server="creative") (world="some_world")
essentials.msg (server="creative") (world="some_world")
```

## /perms usersbulkedit group \<group|null\> \<server|world\> \<from\> \<to\>
This command allows you to bulk change the context of all user's group memberships. Context is the specific servers or worlds that a permission node applies in.

The syntax is very similar to the above command.

I appreciate the example is a little lengthy, however it should show you pretty clearly how the commands work.

Like before, "null" = nothing, "global" = all servers, and "null" = all worlds.

This command will not modify a user's primary group.

#### Example 1
```
Luck is a member of "admin" (server="factions")
Luck is a member of "mod" (server="kitpvp")
Notch is a member of "owner"
Herobrine is a member of "owner" (server="creative") (world="world_the_end")
Cr33perM4n is a member of "donator" (server="kitpvp")
```
`/perms usersbulkedit group null world null world_nether`
```
Luck is a member of "admin" (server="factions") (world="world_nether")
Luck is a member of "mod" (server="kitpvp") (world="world_nether")
Notch is a member of "owner" (world="world_nether")
Herobrine is a member of "owner" (server="creative") (world="world_the_end")
Cr33perM4n is a member of "donator" (server="kitpvp") (world="world_nether")
```
`/perms usersbulkedit group null world null null`
```
Luck is a member of "admin" (server="factions")
Luck is a member of "mod" (server="kitpvp")
Notch is a member of "owner"
Herobrine is a member of "owner" (server="creative")
Cr33perM4n is a member of "donator" (server="kitpvp")
```
`/perms usersbulkedit group owner server null kitpvp`
```
Luck is a member of "admin" (server="factions")
Luck is a member of "mod" (server="kitpvp")
Notch is a member of "owner" (server="kitpvp")
Herobrine is a member of "owner" (server="creative")
Cr33perM4n is a member of "donator" (server="kitpvp")
```
`/perms usersbulkedit group null server kitpvp factions`
```
Luck is a member of "admin" (server="factions")
Luck is a member of "mod" (server="factions")
Notch is a member of "owner" (server="factions")
Herobrine is a member of "owner" (server="creative")
Cr33perM4n is a member of "donator" (server="factions")
```
`/perms usersbulkedit group null server factions null`
```
Luck is a member of "admin"
Luck is a member of "mod"
Notch is a member of "owner"
Herobrine is a member of "owner" (server="creative")
Cr33perM4n is a member of "donator"
```

#### Example 2
```
Luck is a member of "admin" (server="creative")
Notch is a member of "admin" (server="creative")
Herobrine is a member of "admin" (server="creative")
Cr33perM4n is a member of "donator" (server="creative")
```
`/perms usersbulkedit group admin server creative test`
```
Luck is a member of "admin" (server="test")
Notch is a member of "admin" (server="test")
Herobrine is a member of "admin" (server="test")
Cr33perM4n is a member of "donator" (server="creative")
```

## /perms usersbulkedit permission \<node|null\> \<server|world\> \<from\> \<to\>
Works in exactly the same way as the command above, except this modifies a user's permissions, not their group memberships.