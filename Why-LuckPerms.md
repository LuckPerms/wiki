**Hi there!** 👋 

This page attempts to answer a number of questions/reactions people tend to have when they first discover the plugin. 

(it also serves as a great way for me to explain all the great things the project can do. It's awesome, I promise!)

___

### Yet another permissions plugin?
Yep. I thought there was room for improvement among the plugins already out there. 😄 

LuckPerms is an advanced permissions plugin, aiming to be a **fast**, **reliable** and **flexible** alternative to existing permission plugins. The project's main goals are centered around **high performance** and a wide feature set, filling the gaps of functionality and building upon existing features found in other plugins. LuckPerms also includes an extensive API for developers, and support for a variety of Minecraft server software & data storage options.

___

### I've been using [x] plugin for years and it works great for me! Why should I bother switching?
Most of the other available permission plugins date back a number of years, and were created in the early Bukkit era. Whilst this may mean they're stable, it also means they're often abandoned by the original authors, and receive no updates, support or bug fixes. LuckPerms is still a growing and active resource, and I endeavour to reply to all bug reports, issues and feature requests in a timely manner.

In addition, LuckPerms offers a number of innovative and original features, which you simply will not find elsewhere. (more on these features later!)

___

### LuckPerms seems like a pretty big resource, and I just want something simple and lightweight.
Although the plugin has a pretty huge set of configuration options, the default values are fine for most people. Hooray! 🎉

You shouldn't even need to touch the configuration file if you just want to setup something basic for your server. The LuckPerms in-game and online interfaces are very straight forward to use, and there is a massive set of wiki pages and setup guides you can read here on GitHub.

___

### I run a big network and performance is important. How does LuckPerms perform?
The plugin has been written and improved over time with large servers in mind. It has proven itself to be reliable and efficient and currently runs on a number of popular networks in the community.

From the very start, LuckPerms has been written to make use of multithreading for almost all of it's operations - something which previously hadn't been attempted in many permissions plugins. This design has proven to be highly effective, and is the reason why LuckPerms scales so well.

___

### Come on then, tell me, why should I use LuckPerms?
LuckPerms is capable of a lot, and at least on a technical level, outperforms the majority of other plugins. I don't accredit this to my own ability to create good plugins, but rather to timing.

I started working on the plugin in early 2016. I could model LuckPerms around what existing permissions plugins had done well, and avoid mistakes and flaws which I saw in existing options. 

With that in mind, if you're interested in what LuckPerms can do "technically", a good place to start is the [Command Usage](https://github.com/lucko/LuckPerms/wiki/Command-Usage) page, or take a look at some of the pages listed under **Features** in the wiki contents.

For the rest of this article, I'll focus on some of the new features LuckPerms has, which you are unlikely to find in other plugins.

### Verbose
LuckPerms has a [verbose](https://github.com/lucko/LuckPerms/wiki/Verbose) system, which allows you to monitor permission checks made by other plugins, occurring in real time.

[![](https://giant.gfycat.com/ArtisticPleasantAlbacoretuna.gif)](https://gfycat.com/ArtisticPleasantAlbacoretuna)

You can trace exactly where permission checks originate from - right down to the line of code which caused the check!

[![](https://i.imgur.com/Ta7gtd9.png)](https://i.imgur.com/Ta7gtd9.png)

You can also upload recordings to the web, for easier analysis and reading.
[https://git.io/vQitM](https://git.io/vQitM)

### Permission Trees
LuckPerms allows you [build "permission trees"](https://github.com/lucko/LuckPerms/wiki/Command-Usage#lp-tree) of all permissions known to the server. The data is populated using permissions registered to the server by plugins.

As the server runs for longer periods, the tree also grows, as permissions checked for by plugins on the server are added.

An example tree:

[![](https://i.imgur.com/68fLMaQ.png)](https://git.io/vbhyZ)


You can also color the trees, depending on whether a certain player has a permission. This allows you to easily visualise which permissions a player has access to.

For example:

[![](https://i.imgur.com/OR5GNcP.png)](https://git.io/vbhyV)

### Command interface & tab completion
The command system for LP is designed to be as easy to use as possible. As well as the [extensive documentation here on the wiki](https://github.com/lucko/LuckPerms/wiki/Command-Usage), command usage and listings can also be viewed in-game.

![](http://i.imgur.com/XIVPP6P.png)

All LuckPerms commands are fully tab completable, meaning you have to do less typing to get stuff done!

[![](https://zippy.gfycat.com/AnnualYoungKoi.gif)](https://gfycat.com/AnnualYoungKoi)

### Web editor
As well as the command interface, you can also use the web editor to make changes to your permission data. Anyone can use the editor, no matter which storage type you're using.

It's super easy to use.

[![](https://giant.gfycat.com/ShorttermPowerfulGoldeneye.gif)](https://gfycat.com/ShorttermPowerfulGoldeneye)

### Action logging
LuckPerms also makes a detailed log of all changes made to permissions. If you have a rogue staff member try to give themselves permissions, instead of trawling through the servers log file, you can simply search for any actions executed by them!

![](http://i.imgur.com/Jfu8XCI.png)

You can also view the history of certain users, groups, or tracks, or look at the actions executed by a user.