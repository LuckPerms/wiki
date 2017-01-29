## Intro
If you're running LuckPerms on multiple servers, you are likely to run into the issue at somepoint whereby you make a change on one server, but that change hasn't "propagated" to the other servers in your network yet.

This page documents ways to fix this problem.

Of course, none of this is necessary if you only have one server using LuckPerms, or if your servers do not share a common storage method. (connecting to the same database)

## Sync Interval
You can setup a sync interval, which will schedule a task that will repeatedly pull the latest changes from the storage.

The default value of this option is every **3 minutes**.

```yml
data:

  ...

  # Set to -1 to disable. If this is the only instance accessing the datastore, you can disable syncing.
  # e.g. if you're using sqlite or flatfile, this can be set to -1 to save resources.
  sync-minutes: 3
```

You can modify this value to your liking.

## /lp sync
The `/lp sync` command will force the plugin to run one of the update tasks described above. The latest version of data will be loaded from the database/files.

This command can also be useful when using file storage, and should be ran after you make any changes to the files.

## Messaging Services
Once setup, you can use the `/lp networksync` command to push changes to all other servers in the network.

#### Currently Supported
| Service | Description | 
|---------|-------------|
| Bungee | Uses the plugin messaging channels to push changes around your BungeeCord network. |
| Lilypad | Uses the LilyPad Connect Servers Pub Sub system to push changes around your LilyPad network. |
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

You need to setup a Redis server accessible to your server instance. The fill out the address and password options in the redis section.