Data can be synchronised between different servers with ease.

## Requirements
For data to sync, you **must** be using a remote storage type. All of your servers need to be connected to the same database.

See the page for [Storage types](Storage-types) for more information. You need to use one of the "**remote databases**" listed on that page.

## Instantly propagating updates
Simply connecting the servers to the same database isn't enough for data to be synced instantly between them. LuckPerms needs to know that data has changed in order to update it.

This can be achieved in a number of ways.

All of these settings are located in the config under `Update propagation & messaging service`.

### Sync Interval
You can set a sync interval, which will make LuckPerms periodically pull the latest changes from the database.   
The setting is controlled in the config, and defaults to `-1` (meaning the task is disabled).

```yml
sync-minutes: -1
```

### Watch files
If you're using a file based storage type (YAML, JSON or HOCON), then LuckPerms can listen for changes made to those data files, and automatically update when it detects that a change has been made.

This means that you can simply edit one of the data files, and press save, and your changes will be applied to the server.   
The setting is controlled in the config, and is enabled by default.

```yml
watch-files: true
```

### /lp sync
The `/lp sync` command will make the plugin pull the latest changes from the database/files.

### Messaging Services
Once setup, other servers in the network will be "pinged" when a change is made, and will request the latest copy of data from the database.

Data is **not** stored using this service - it is only used as a messaging platform.

A messaging service can be configured in the config, under the `messaging-service` option.

#### Possible options
| Service | Description | 
|---------|-------------|
| sql | Uses the SQL database to form a queue system for communication. This is chosen by default if remote SQL storage is in use. |
| pluginmsg | Uses the plugin messaging channels to communicate with the proxy. LuckPerms must be installed on your proxy & all connected servers backend servers. Won't work if you have more than one proxy. |
| lilypad | Uses LilyPad Connect's PubSub system to communicate. |
| redis | Connects to a Redis instance and uses PubSub to communicate. |
| rabbitmq | Connects to a RabbitMQ instance and uses PubSub over AMQP to communicate. |
| nats | Connects to a Nats instance and uses PubSub to communicate. | 
| custom | Forces the messaging-service to use your own custom implementation that you provide through the LuckPerms API. |

It is also possible to provide your own implementation of this service via the LuckPerms API. Make sure you set the messaging-service option in the config to `custom` otherwise it will throw an error on startup.
