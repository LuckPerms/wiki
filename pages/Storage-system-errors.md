This page is an extension to the general [FAQ list](FAQ), with a focus on storage related issues and errors.

It includes a number of common errors & fixes for storage providers (mostly MySQL!).

___

Firstly, let's clarify how LuckPerms permission storage operates. We get a lot of (sometimes quite angry!) comments from people blaming us for things not working, when 95% of the time it's got nothing to do with LuckPerms. :cry:

In order to write permissions data to a storage backend, LuckPerms uses something called a "driver" to interact with the underlying storage system.

These drivers are made by 3rd parties. They are extensively tested, and produced (in most cases) by the organisation behind the database software.

Importantly:

* **If the error originates from the driver - it is *not* being caused by LuckPerms.**
* You *may* have experienced a bug in the driver itself, however this is unlikely
* The most likely cause is that something is setup or configured incorrectly.


Some common errors are listed below. If your issue isn't here, then feel free to open a bug report here on GitHub and we can point you in the right direction (or fix the issue if it turns out to be a LuckPerms bug!).

___

# Common errors

### LuckPerms cannot connect to my MySQL server

Errors such as:

> Caused by: java.util.concurrent.CompletionException: java.sql.SQLTransientConnectionException: luckperms - Connection is not available, request timed out after 5000ms.   
> ...   
> Caused by: java.sql.SQLTransientConnectionException: luckperms - Connection is not available, request timed out after 5000ms.


> luckperms - Failed to validate connection com.mysql.jdbc.JDBC4Connection@xxxxxxxxx (Communications link failure)   
> The last packet successfully received from the server was xxxxxxx milliseconds ago.  The last packet sent successfully to the server was xx milliseconds ago.)

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

___

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

___

### MySQL "No operations allowed after connection closed" error
If you get an error similar to:
> me.lucko.luckperms.lib.hikari.pool.PoolBase - luckperms-hikari - Failed to validate connection me.lucko.luckperms.lib.mysql.jdbc.JDBC4Connection@xxxxxxx (No operations allowed after connection closed.)

> me.lucko.luckperms.lib.hikari.pool.PoolBase - luckperms-hikari- Failed to validate connection me.lucko.luckperms.lib.mariadb.MariaDbConnection@xxxxxxx (xxx cannot be called on a closed connection)

... you need to modify the `maximum-lifetime` (LP config) and `wait_timeout` (MySQL config) settings.

Crucially, the `maximum-lifetime` value in the LP config must be **less than** the `wait_timeout` value in your MySQL config.

| `maximum-lifetime` |
|--------------------|
| Location: [LuckPerms config](https://github.com/LuckPerms/LuckPerms/blob/be92a6754404b387dead24ebc1dd3ca8af8e6456/bukkit/src/main/resources/config.yml#L125-L128) |
| Units: milliseconds |
| Default value: `1800000` (30 minutes) |


| `wait_timeout` |
|----------------|
| Location: [MySQL server config](https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_wait_timeout) |
| Units: seconds |
| Default value: `28800` (8 hours) |

It doesn't matter which value you change, so long as the `maximum-lifetime` is less than `wait_timeout`. Remember that the units of each value are different!

The default `maximum-lifetime` value of 30 minutes is fine for the **vast** majority of users. It only becomes a problem if you or your hosting provider have changed the wait timeout setting from the 8 hour default.

If your MySQL server is provided by a 3rd party, ask them what the value is set to.

___

### MySQL exceeded max connections

Errors similar to:

> Caused by: com.mysql.jdbc.exceptions.jdbc4.MySQLSyntaxErrorException: User 'xxxxxxxxx' has exceeded the 'max_user_connections' resource (current value: xxx)

Your MySQL user's max connections limit is being exceeded. By default, LuckPerms will use 10 connections per server. If you have lots of plugins connecting to the same MySQL server, you will need to increase this limit.

If you host your own MySQL server, there are some links below which explain how you can raise the limit.

* https://dev.mysql.com/doc/refman/5.5/en/too-many-connections.html
* https://www.electrictoolbox.com/update-max-connections-mysql/

If your MySQL server is provided by a hosting company, you need to ask them to raise the limit for you.

___

### MySQL Public Key Retrieval is not allowed

Errors similar to:

> Caused by: me.lucko.luckperms.lib.mysql.jdbc.exceptions.jdbc4.MySQLNonTransientConnectionException: Public Key Retrieval is not allowed

This is a MySQL error that is certainly possible to correct.

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
      allowPublicKeyRetrieval: true
```
and add last option, `allowPublicKeyRetrieval`, set to true.

___

### MySQL failed to set port

Errors similar to:

> Failed to set property port on target class me.lucko.luckperms.lib.mysql.jdbc.jdbc2.optional.MysqlDataSource
java.lang.NumberFormatException: For input string: xxxx

Your `address` setting in the LuckPerms configuration is unable to set the port, likely due to a mistyped or misformatted address and port. If the port is 3306, as it is by default, there is no need to set the port at all. The correct format for the `address` line is `"address:port"`.

___

### LuckPerms cannot connect to my Redis server
Check that the following is correct:

* You are using the correct address and port
* Your password is correct
* There are no firewall rules blocking the connection
* The Redis server is actually running
