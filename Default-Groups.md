The way I handle defaults and default groups in LuckPerms is probably the most disliked feature in the whole plugin. Recently I've been adding some additional / alternative features to the plugin to allow a greater degree of control compared with what's seen in any of the other permission plugins out there, and hopefully making my approach people's favourite part of the plugin, not their least favourite.

# Where to start
So, here's my thinking.

Users on your server are likely to be split into two types. 

1. The standard player.
2. Players who have been added to a different group, or given their own special permissions.

You don't want to waste precious disk space storing data about Player Type #1. You only want to store data about your staff members, and people with special ranks. Regular "members" are just that, regular. There's no need to store any data about them.

The next issue I face is how to decide if a user is "regular" or not. Imagine the following situation.

1. The default group is set to "default". When players join, they're given "default", and then get saved.
2. A little while down the line, you decide you want to change the default group to "member".
3. You then have all of your old players in the "default" group, and everyone else in "member". Not good.

Even if we don't save "regular" users, this issue can still happen.

1. The default group is set to "default".
2. You want to give "Notch" a special "essentials.fly" permission. Notch's permissions are saved, indicating he's a member of the "default" group, and has the special fly permission.
3. You then edit the default group. All of your "regular" members get the new default group, but Notch still has default!

For this reason, I made it so that the default group is **not** configurable. It makes things 10x easier for me. It means I can write efficient storage systems, with no chance of nasty race conditions occurring when a server admin decides to change the default group. However, I understand this is annoying for some people.

There's also issues with rankup plugins. If you want a "main" group, and then separate "level" ranks, you need to be able to grant more than one group by default. 

Here are your options.

## Keep using the default group, but just modify the "display name"
I strongly recommend for the reasons above that you keep using the default group.

Simply use `/lp group <group> setdisplayname <name>`


## Configure inheritance
This option would mean that all users are still in the "default" group. However, a parent group is configured for default, so it can inherit permissions from a group with a different name.

```
/luckperms creategroup member
/luckperms group default parents add member
```

## Configure default assignments
If you have more specific needs, then you can use this option. However, be aware that it will negate the storage space optimisations discussed in the first section of this page. All users will be explicitly saved, whether they are a "regular" user or not.

**Note:** This feature got removed in v5 of LuckPerms, if you still need it, see [this page](https://github.com/lucko/LuckPerms/wiki/Upgrading-from-v4-to-v5#other).

##### Note: see the "Default Assignments" section of the config for more detail on this.

The following rule will configure a different default group.
```yml
default-assignments:
  my-defaults-rule:
    if:
      has-true: <group.default>
    take:
      - group.default
    give:
      - group.member
    set-primary-group: member
```

Simply put, every time a user logs in, the plugin will check if they are a member of the "default" group. If they are, it will remove them from "default", add them to "member", and set their primary group to "member".

This system is very powerful, and allows you to configure defaults to your exact needs. Remember you _could_ add users to more than one "default" group. 😉 
