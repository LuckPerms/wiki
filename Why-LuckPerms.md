**Hi there!** 👋

This page attempts to answer a number of questions/reactions people tend to have when they first discover the project, and address why you should use LuckPerms. It's awesome, I promise!

So firstly, some FAQs.

___

#### Yet another permissions plugin?
Yep. I thought there was room for improvement among the plugins already out there. LuckPerms aims to be fast, reliable and flexible. The project's main goals centre around high performance and a wide feature set. It has an extensive developer API and supports a variety of data storage options.

#### I've been using [x] plugin for years and it works great! Why should I bother switching?
Most of the other available permission plugins date back a number of years, and were created in the early Bukkit era. Whilst this may mean they're stable, it also means they're often abandoned by the original authors, and receive no updates, support or bug fixes. LuckPerms is still a growing and active resource, and I endeavour to reply to all bug reports, issues and feature requests in a timely manner.

#### LuckPerms seems like a pretty big resource, and I just want something simple and lightweight.
Although the plugin has a pretty huge set of customisation options, the default values are fine for most users. The LuckPerms in-game and online interfaces are very straight forward to use, and there is a extensive set of wiki pages and setup guides you can read here on GitHub. 🎉

#### I run a big network and performance is important. How does LuckPerms perform?
The plugin has been written and improved over time with large servers in mind. It has proven itself to be reliable and efficient and currently runs on a number of popular networks in the community.

LuckPerms has been designed to make use of multithreading for almost all of its operations - something which previously hadn't been attempted in many permissions plugins. Lookups for permission checks and meta data are cached, and the internal data structures are designed in order to make queries as fast and efficient as possible.

___

For the rest of this article, I'll focus on some of the new features LuckPerms has, which you are unlikely to find in other plugins.

### Web editor
As well as the command interface, you can also use the web editor to make changes to your permission data. Anyone can use the editor, no matter which storage type you're using.

The interface is split into multiple tabs. You can add/remove entries, as well as change attributes on existing entries.

![](https://imgur.com/a/YAStkW4)

It's super easy to use.

The Web editor is such a powerful tool that it has its own [wiki page](Web-Editor).

___

### Verbose
LuckPerms has a [verbose](Verbose) system, which allows you to monitor permission checks made by other plugins, occurring in real time.

![](https://imgur.com/a/12ThFUN)

You can trace exactly where permission checks originate from - right down to the line of code which caused the check!

![](https://i.imgur.com/ut3S9Ps.png)

You can also upload recordings to the web, for easier analysis and reading.

![](https://i.imgur.com/tRRosMp.png)

___

### Permission Trees
LuckPerms allows you [build "permission trees"](General-Commands#lp-tree-scope-player) of all permissions known to the server. The data is populated using permissions registered to the server by plugins.

As the server runs for longer periods, the tree also grows, as permissions checked for by plugins on the server are added.

An example tree:

![](https://imgur.com/a/316vPEY)


You can also color the trees, depending on whether a certain player has a permission. This allows you to easily visualise which permissions a player has access to.

___

### Command interface & tab completion
The command system is super easy to use and understand. As well as the [documentation available here on the wiki](Command-Usage), command usage and listings can also be viewed in-game.

![](http://i.imgur.com/XIVPP6P.png)

All LuckPerms commands are fully tab completable, meaning you have to do less typing to get stuff done!

[![](https://zippy.gfycat.com/AnnualYoungKoi.gif)](https://gfycat.com/AnnualYoungKoi)

___

### Action logging
LuckPerms makes a detailed log of all changes made to permissions. If you have a rogue staff member try to give themselves permissions, instead of trawling through the servers log file, you can simply search for any actions executed by them!

![](http://i.imgur.com/Jfu8XCI.png)

You can also view the history of certain users, groups, or tracks, or look at the actions executed by a user.

___

### Supports multiple versions and platforms
LuckPerms was build to support as many server versions and types as possible.  
The latest version of LuckPerms is compatible with Spigot and any fork of it and supports versions from 1.8.8 up to the latest one.

For older versions or different platforms (BungeeCord, Velocity, Sponge, NukkitX, etc.) does LuckPerms have alternative downloads available on its [website](https://luckperms.net).
