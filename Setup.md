Setup is a fairly simple process.

1. Grab the LuckPerms jar that corresponds to your platform.
2. Place the plugin jar in your plugins/mods folder.
3. Start the server once, and let it generate the config file.
4. Stop the server, and fill out the configuration options.

You can change a number of settings in the config file. The file has detailed annotations that should make it clear what each option does.

### Requirements
#### Java 8
The only requirement is that you must be using **Java 8**.

Most hosts have updated by now, but if your provider still doesn't run Java 8, ask them nicely to update.

If you control your own server, shame on you for not updating yet! The process is simple, there's tons of guides online if you're struggling to do it. It's not good to be running outdated software. :wink:

#### Older Bukkit versions
If you are getting errors related to "NoSuchMethod" or "ClassNotFound", the likelihood is you're using an older Bukkit version. Before reporting it as an issue to me, please first try using the "bukkit-legacy" version found on the "Development Builds" download page.