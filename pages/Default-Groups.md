The way we handle defaults and default groups in LuckPerms is probably the most disliked feature in the whole plugin. Recently we've been adding some additional / alternative features to the plugin to allow a greater degree of control compared with what's seen in any of the other permission plugins out there, and hopefully making our approach people's favourite part of the plugin, not their least favourite.

# Where to start
So, here's our thinking.

Users on your server are likely to be split into two types. 

1. The standard player.
2. Players who have been added to a different group, or given their own special permissions.

You don't want to waste precious disk space storing data about Player Type #1. You only want to store data about your staff members, and people with special ranks. Regular "members" are just that, regular. There's no need to store any permissions data about them.

The next issue we face is how to decide if a user is "regular" or not. Imagine the following situation.

1. The default group is set to "default". When players join, they're given "default", and then get saved.
2. A little while down the line, you decide you want to change the default group to "member".
3. You then have all of your old players in the "default" group, and everyone else in "member". Not good.

Even if we don't save "regular" users, this issue can still happen.

1. The default group is set to "default".
2. You want to give "Notch" a special "essentials.fly" permission. Notch's permissions are saved, indicating he's a member of the "default" group, and has the special fly permission.
3. You then edit the default group. All of your "regular" members get the new default group, but Notch still has default!

For this reason, we made it so that the default group is **not** configurable. It makes things much easier for everyone, honestly! However, we understand this can sometimes be annoying to work with.

Here are your options.

### Keep using the default group, but change the "display name"
We strongly recommend for the reasons above that you keep using the default group.

Then, simply use `/lp group default setdisplayname <name>` to set a display name!


### Configure inheritance
This option would mean that all users are still in the "default" group. However, a parent group is configured for default, so it can inherit permissions from a group with a different name.

```
/lp creategroup member
/lp group default parent add member
```
