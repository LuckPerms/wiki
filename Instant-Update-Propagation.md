## Intro
If you're running LuckPerms on multiple servers, you are likely to run into the issue at somepoint whereby you make a change on one server, but that change hasn't "propagated" to the other servers in your network yet.

This page documents ways to fix this problem.

Of course, none of this is necessary if you only have one server using LuckPerms, or if your servers do not share a common storage method. (connecting to the same database)

## Sync Interval
You can setup a sync interval, which will schedule a task that will repeatedly pull the latest changes from the storage.

The default value of this option is **-1** (meaning is is disabled)

```yml
data:

  ...

  # This option controls how frequently LuckPerms will perform a sync task.
  # A sync task will refresh all data from the storage, and ensure that the most up-to-date data is being used by the plugin.
  #
  # This is disabled by default, as most users will not need it. However, if you're using a remote storage type
  # without a messaging service setup, you may wish to set this value to something like 3.
  #
  # Set to -1 to disable the task completely.
  sync-minutes: -1
```

You can modify this value to your liking.

## Watch files
If you're using a file based storage type (JSON or YAML), then LuckPerms can listen for changes made to those data files, and automatically update when it detects that a change has been made.

```yml
# When using a file-based storage type, LuckPerms can monitor the data files for changes, and then schedule automatic
# updates when changes are detected.
#
# If you don't want this to happen, set this option to false.
watch-files: true
```

This means that you can simply edit one of the data files, and press save, and your changes will be applied to the server.

## /lp sync
The `/lp sync` command will force the plugin to run one of the update tasks described above. The latest version of data will be loaded from the database/files.

This command can also be useful when using file storage, in order to request an update.

## Messaging Services
Once setup, you can use the `/lp networksync` command to push changes to all other servers in the network.

#### Currently Supported
| Service | Description | 
|---------|-------------|
| Bungee | Uses the plugin messaging channels to push changes around your BungeeCord network. |
| Lilypad | Uses the LilyPad Connect Server's Pub Sub system to push changes around your LilyPad network. |
| Redis | Uses Redis Pub Sub to push changes to all other connected servers. |

#### Bungee
```yml
messaging-service: bungee
```

You must have LuckPerms installed on your proxy server, and have the option above set in all configs. This option does not support multiple BungeeCord proxies, you should be using Redis in this case.

#### LilyPad
```yml
messaging-service: lilypad
```

You need to have the `LilyPad-Connect` plugin installed on your server.

#### Redis
```yml
messaging-service: redis

# Settings for Redis.
# Port 6379 is used by default; set address to "host:port" if differs
redis:
  enabled: true
  address: localhost
  password: ''
```

You need to setup a Redis server which is accessible to your server instance. Then fill out the address and password options in the redis section.

Please ensure that appropriate firewall rules are setup to prevent unauthorised access to your Redis server.