## Initial Setup

1. Download the `LuckPerms-???-x.x.x.jar` file that corresponds to your platform. You can find the latest versions [here](https://ci.lucko.me/job/LuckPerms/).
2. Navigate to your mods/plugins directory. This is usually either `/server/plugins/` or `/server/mods/`. Then place the LuckPerms jar in this directory.
3. Fully stop & start your server, and allow the default configuration to be generated.
4. Fully stop your server, and open the config file. It will be located at `/plugins/LuckPerms/config.yml` or `/config/luckperms/luckperms.conf`.
5. Read through the config file, and change the options to suit your server, especially taking note of the **Storage** settings.
6. Start your server again.

You can change a number of settings in the config file. The file has detailed annotations that should make it clear what each option does.

### Requirements
#### Java 8
The only requirement is that you must be using **Java 8**.

Most hosts have updated by now, but if your provider still doesn't run Java 8, ask them nicely to update.

If you control your own server, shame on you for not updating yet! The process is simple, there's tons of guides online if you're struggling to do it. It's not good to be running outdated software. :wink:

#### Older Bukkit versions
If you are getting errors related to "NoSuchMethod" or "ClassNotFound", the likelihood is you're using an older Bukkit version. Before reporting it as an issue to me, please first try using the "Bukkit-Legacy" version found on the "Development Builds" download page.