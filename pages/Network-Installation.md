LuckPerms was written from the start with networks of servers in mind. When correctly setup and configured, permissions data will sync between servers and propagate instantly around your network.

When installing LuckPerms across a network, the regular [installation steps](Installation) and [requirements](Installation#requirements) still apply.

However, there is one additional requirement.

**All instances of LuckPerms must be connected to the same storage system.** This means you are limited to using `MySQL`, `MariaDB`, `PostgreSQL` or `MongoDB`. LuckPerms must be connected to the same SQL / MongoDB server, and access the same database or collection.
___

## Pre setup
Before you get started, there are a number of things you need to check. These aren't just here for the sake of it - these steps are important. Do not skip them!

LuckPerms supports networks using either `BungeeCord`, `Velocity` or `LilyPad`.

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

In the `config/sponge/global.conf` file on each of your backend Sponge servers, you need to set
```hocon
sponge {
    bungeecord {
        ip-forwarding=true
    }
}
```

After changing these settings, you need to fully restart the Spigot/Sponge servers and BungeeCord proxy.

You should also take steps to ensure that your network is correctly firewalled, to ensure malicious users cannot spoof connections to your backend servers. A guide on how to do this is provided [here](https://www.spigotmc.org/wiki/firewall-guide/) by SpigotMC.

### LilyPad
If you're using LilyPad: as per the [LilyPad setup guide](http://www.lilypadmc.org/threads/connecting-your-bukkit-servers.13/), you should ensure that the `LilyPad-Connect` plugin is installed and correctly configured on your backend server.

___

## Installing LuckPerms across your network
Installing LP on a network is fairly easy, however, there are a number of configuration options which need to be changed as you setup each instance.

The more general [Installation](Installation) guide provides details about how to install LuckPerms on a single server instance. This should be followed for each server in your network. (in most cases it's as simple as adding the plugin jar to the plugins/mods folder)

Once LuckPerms has been installed, you need to stop the server, open the main configuration file, and pay particular attention to the following options:

#### [`server`](Configuration#server)

If you want to set permissions or assign group inheritances on a per server basis within your setup, you'll need to change the value of `server` in your configuration file. (this is conveniently located right at the top of the file! 😄)

This value is used to define a "server" context for all players when they're connected to the instance.

More information about defining server and world specific permissions can be found [here](Advanced-Setup) and [here](Context).

#### [`storage-method`](Configuration#storage-method)

As mentioned at the top of this page, if you want data to sync between instances, then all of your LuckPerms instances need to connect to the same database. 

This means that `storage-method` should be set to 'mysql', 'mariadb', 'postgresql' or 'mongodb'. Remember to fill out your database connection info when you change these options!

#### [`messaging-service`](Configuration#messaging-service)

The "Messaging Service" is a feature within LuckPerms which allows servers to notify other servers within the network whenever changes are made. It also allows log entries to be dispatched across the network.

* If you're running multiple servers which are not connected to one proxy running LuckPerms, but use the same database set this option to `sql`.
* If you're running a small network with one BungeeCord/Velocity proxy running LuckPerms, then you should set this option to `pluginmsg`.
* If you're running a LilyPad network, set this to `lilypad`.
* If you're running a network with more than one BungeeCord/Velocity proxy, then it is advisable to install a Redis server (if you're running a network with more than one proxy, I'll assume you already know how to do this!), and set this option to `redis`. Remember to fill out your Redis credentials after changing this option!

___

## The BungeeCord/Velocity version of LuckPerms
A common misconception with the proxy version is that it's a replacement for installing LuckPerms on your backend Spigot/Sponge servers. This is untrue.

When LuckPerms is installed on a proxy, it does two things:

* It handles permissions checks made by **plugins on the proxy**. It does *not* intercept or handle permission checks made by plugins on the backend server.
* It forwards update notifications and log messages around the network when `messaging-service` is set to 'pluginmsg'.

This means that if you want LuckPerms to respond to permission checks on your backend Spigot or Sponge server, you need to install it there too, even if you have it on your proxy.
