# Frequently Asked Questions
These are some of the questions I get asked quite frequently. I'd appreciate it if you check to see if your question has already been answered here before asking me directly. 😄 

### I'm using EssentialsChat and it's not working
Please make sure you are using the latest version of [EssentialsX](https://ci.drtshock.net/job/essentialsx/) and you have [Vault](https://dev.bukkit.org/bukkit-plugins/vault/) installed on your server. The "**X**" part of Essentials**X** is important - the older versions of Essentials do not work.

### Where do I install LuckPerms?
If you run a network of servers, you should install LuckPerms into the plugin folder of every server you want to use LuckPerms on.

If you also want to use LuckPerms to apply permissions on your BungeeCord proxy, you should place LuckPermsBungee.jar into your BungeeCord plugins folder.

If you choose to only install LuckPerms on your BungeeCord proxy, it will have no impact on any permission checks performed by plugins on any backend Spigot/Sponge servers. If you want that functionality, you need to install LuckPerms on those servers too.

### Can I just install LuckPerms on BungeeCord?
The permissions system used on BungeeCord is completely separate from the systems used on the backend Spigot/Sponge server.

If you want the permission checks performed by Spigot/Sponge plugins to be handled by LuckPerms, install LuckPerms on your Spigot/Sponge server.

If you want the permission checks performed by BungeeCord plugins to be handled by LuckPerms, install LuckPerms on your proxy.

You **can** just install it on the proxy, but any checks which are performed by Spigot/Sponge plugins will not be handled by LuckPerms.

### How do I get permissions to sync across multiple servers
Connect each LuckPerms installation to the same MySQL/MongoDB server. You can use `/luckperms sync` to pull the latest changes from the database. You can also [setup a Messaging Service](https://github.com/lucko/LuckPerms/wiki/Instant-Update-Propagation#messaging-services) to have your changes sync instantly between servers.

### LuckPerms cannot connect to my Redis server
Check that the following is correct:

* You are using the correct address and port
* Your password is correct
* There are no firewall rules blocking the connection
* The Redis server is actually running

### LuckPerms cannot connect to my MySQL server
Check that the following is correct:

* You are using the correct address and port
* You are using the correct username / password
* That the database exists and is accessible by the user
* That the server is online & accepting connections
* There are no firewall rules blocking the connection
* MySQL is bound to the correct port, and is accessible from the server where LuckPerms is installed
* Check that your MySQL max connections limit is not being exceeded. By default, LuckPerms will use 10 connections per server. If you have lots of plugins connecting to the same server, you will need to increase this limit.

If you are getting `Communications link failure` errors, or errors relating to a timeout, then something from the list above is incorrect.

To give the user access to the LuckPerms tables, execute:
```sql
GRANT ALL PRIVILEGES ON [databasename].* TO '[username]'@'[ipaddress]';
```
obviously replacing the parts in [ ].

For example:
```sql
GRANT ALL PRIVILEGES ON luckperms.* TO 'luck'@'%';
```

Then, when you have finished your changes, run:
```sql
FLUSH PRIVILEGES;
```

### MySQL SSL errors
If you get an error similar to:
> Establishing SSL connection without server's identity verification is not recommended. According to MySQL requirements SSL connection must be established by default if explicit option isn't set. For compliance with existing applications not using SSL the verifyServerCertificate property is set to 'false'. You need either to explicitly disable SSL by setting useSSL=false, or set useSSL=true and provide truststore for server certificate verification.

... you need to disable SSL for MySQL connections.

You can do this by editing the connection properties in the LuckPerms config file. Under the "Storage" section, locate:
```yaml
data:
  pool-settings:
    # This setting allows you to define extra properties for connections.
    properties:
      useUnicode: true
      characterEncoding: utf8
      useSSL: false
      verifyServerCertificate: false
```

and add the last two options.

### MySQL "No operations allowed after connection closed" error
If you get an error similar to:
> com.zaxxer.hikari.pool.PoolBase - luckperms - Failed to validate connection com.mysql.jdbc.JDBC4Connection@xxxxxxx (No operations allowed after connection closed.)

... you need to modify the `maximum-lifetime` setting in the 'pool-settings' section, within "Storage", in the LuckPerms config file.

This setting (defaults to 30 minutes and measured in milliseconds) must be **less** than the `wait_timeout` value set on your MySQL server.

https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_wait_timeout

The default value of 30 minutes is fine for the **vast** majority of users. It only becomes a problem if you or your hosting provider has changed the wait timeout setting.

If your MySQL server is provided by a 3rd party, ask them what the value is set to.
