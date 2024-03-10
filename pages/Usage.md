This guide is intended for people who have never used a permissions plugin before. If you're familiar with the concept, and think you'll be able to understand things just from reading the command usages, we suggest you read the page on [Command Usage and Permissions](Command-Usage), as this gives a much more "straight to the point" description of how the plugin works.

If you're struggling to understand that, then this guide is a good place to start. :)


# Key Definitions
### Permission
On your server, there will be certain **features, commands, and functionality** which exist. Some of these features will be included with the server, and others are added with “plugins”. Most of these actions **have a permission associated with them**, so you can control which users have access to each feature or command.

A **permission is just a string** (a sequence of letters/digits), and is separated into parts using periods. For example, “minecraft.command.ban” is the permission for Minecraft's /ban command.

The string that represents a certain permission is also sometimes called a "permission node" or just "node" for short.

Permission nodes can have **three values**: `true`, `false`, and `undefined`.
- `true` means that the player *has that permission* and the condition(s) assigned to it will be given to the player.
- `false` means that the player *does not have that permission* and the condition(s) assigned to it will be *denied* to the player.
- `undefined` means that the permission is *not explicitly set* in LuckPerms. This **usually** means that it defaults to being the same as `false`. Very rarely, plugins can make `undefined` permissions default to `true`, in which case you need to **set them explicitly to `false`**. 

### Group
Instead of assigning permissions to every user individually, we have **groups of permissions**, which can then be **assigned to a user** as a whole.

For example, in my "admin" group, I might add permission to use the /ban and /unban commands, and then assign users to the admin group. This means that they will get all of the permissions from "admin", plus any they have themselves.

### Inheritance
Users and groups are able to **inherit permissions from each other**. For example, by default, all users inherit permissions from the "default" group. You can setup your own groups and inheritances for your server, and make your own unique system.

For example, I might have 3 groups, "default", "moderator" and "admin". I want moderator to inherit permissions from default, and admin to inherit permissions from moderator.

### Context
A term that you will encounter quite often with LuckPerms is "context".

**Context** in the most basic sense simply means the **circumstances where something will apply**.

Contexts are such a fundamental part of the plugin, they have their [very own wiki page](Context) dedicated to explaining their use.

# Getting Started
If you haven't got LuckPerms installed just yet, please refer to the [installation guide](Installation) first.

Then, please make sure you read the section about [choosing a Storage type](Storage-types) before proceeding. Whilst it is possible to change these options later, it's better to get them right the first time around.

## Granting full access to modify permissions
The first thing you'll want to do is give yourself full access to the plugin. When LuckPerms is first installed, nobody has access to any of the LP commands.

To do this, login to your server, and then open the server console.

Then, type `lp user <your username> permission set luckperms.* true`. (don't worry, the usage of this command will be explained later)

The result should look something like this:   
![](../img/usage-1.png)

Effectively, what this command does, is give your account the `luckperms.*` permission. (or sets it to true for the user) You'll notice there's a `*` character at the end of the permission string. This character is called a wildcard, and gives a user access to **all** permissions which start with "luckperms".

Now you've done this, you can either continue the setup process in-game, or keep typing commands into the console.

## Creating the first group
You can create a new group with the creategroup command. Let's create a new group called admin, and then give it a permission.

First, run `lp creategroup admin`. This will create a new empty group named "admin".

![](../img/usage-2.png)

Next, we want to add a permission to the admin group. The command to modify a group is `lp group <group>`. If you run the command, it will list each of the subcommands back to you.

![](../img/usage-3.png)

Since we want to add a permission, the subcommand we want is "permission". This allows you to modify the permissions held by the group. Again, running `lp group admin permission` will list the available sub-commands.

![](../img/usage-4.png)

Again, we see more commands we can use. The first is another "info" command. Since it's a sub command of "permission", this info command returns information about the permissions a group has. The next command however is the "set" command.

Remember, we used this earlier to give a user access to the "luckperms.*" permission. It works the same here.

Just running the command without any arguments will return information about how to use it. For example:    
![](../img/usage-5.png)

For example, I want to give my admin group access to "minecraft.command.ban". I can therefore just run `lp group admin permission set minecraft.command.ban true`.

![](../img/usage-6.png)

This command is giving `admin` access to the `minecraft.command.ban` permission. The true at the end is the value we're assigning the permission as. You can either set a permission to `true` or `false`. Setting a permission as true gives the user or group access to it, and setting it to false negates it. (specifically doesn't give them access)

If I decide later that I don't want admin to have this permission anymore, I can just use the unset command to remove it, with `lp group admin permission unset minecraft.command.ban`.

![](../img/usage-7.png)

## Adding a user to a group
Adding users to a group can be done with the "parent" command. (we just swap "permission" for "parent" in our command usage)

For example, to add myself to the admin group, I would run `lp user Luck parent add admin`.

![](../img/usage-8.png)

This command adds the user `Luck` to the `admin` group. This means that any permissions admin has, I also have through inheritance.

## Making a group inherit another group
As well as users, groups are also able to inherit other groups.

For example, suppose the following setup. (some of the permissions are just made up)

| Admin | Mod | Default |
|-------|-----|---------|
| minecraft.command.ban | minecraft.command.mute | minecraft.command.say |
| minecraft.command.pardon | minecraft.command.unmute | minecraft.command.me |
| some.cool.admin.perm | some.cool.mod.perm | |
| someplugin.vanish | chatcolor.bold | |

I want users in my admin group to also have access to mod and default permissions, and I want users in the mod group to have access to default's permissions.

To achieve this, I can setup the groups to inherit from each other.

The command `lp group admin parent add mod` will make admin inherit all of mods permissions. I can then do the same for mod, and run `lp group mod parent add default`.

![](../img/usage-9.png)

The inheritance is recursive, so since although admin how only inherits directly from mod, mod inherits from default. This means admin has access to both the permissions in mod **and** default.

A user in admin has access therefore to `minecraft.command.ban` and `minecraft.command.mute`, *and* `minecraft.command.say`.

## Removing parent groups
Removing parent groups is done with a spookily similar command.

To remove myself from admin, I'd just run `lp user Luck parent remove admin`.

![](../img/usage-10.png)
