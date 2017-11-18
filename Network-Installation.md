LuckPerms was written from the start with networks of servers in mind. When correctly setup and configured, permissions data will sync between servers and propagate instantly around your network.

When installing LuckPerms across a network, the regular [installation steps](https://github.com/lucko/LuckPerms/wiki/Setup) and [requirements](https://github.com/lucko/LuckPerms/wiki/Setup#requirements) still apply.

However, there is one additional requirement.

**All instances of LuckPerms must be connected to the same storage system.** This means you are limited to using `MySQL`, `MariaDB`, `PostgreSQL` or `MongoDB`. LuckPerms must be connected to the same SQL / MongoDB server, and access the same database or collection.
___

## Pre setup
Before you get started, there are a number of things you need to check. These aren't just here for the sake of it - these steps are important. Do not skip them!

LuckPerms supports networks using either `BungeeCord` or `LilyPad`.

### BungeeCord
LuckPerms uses a player's unique ids (UUID) as an index when saving data. A players uuid is provided by the server implementation, however, this value can depend on the state of the `online-mode` setting.

When using BungeeCord, it is **absolutely crucial** that BungeeCord's IP forwarding system is setup and configured correctly.

In `config.yml` file for your BungeeCord proxy(ies), you need to set
```yml
ip_forward: true
```

In the `spigot.yml` file on each of your backend Spigot servers, you need to set
```yml
# This option is found under "settings"
bungeecord: true
```

After changing these settings, you need to fully restart the Spigot servers and BungeeCord proxy.

You should also take steps to ensure that your network is correctly firewalled, to ensure malicious users cannot spoof connections to your backend servers. A guide on how to do this is provided [here](https://www.spigotmc.org/wiki/firewall-guide/) by SpigotMC.

### LilyPad
As per the [LilyPad setup guide](http://www.lilypadmc.org/threads/connecting-your-bukkit-servers.13/), you should ensure that the `LilyPad-Connect` plugin is installed and correctly configured on your backend server.
