The main configuration file for LuckPerms can be found at these locations.

| Platform      | Location                                                                                                                      |
|---------------|-------------------------------------------------------------------------------------------------------------------------------|
| Bukkit/Spigot | [`/plugins/LuckPerms/config.yml`](https://github.com/LuckPerms/LuckPerms/blob/master/bukkit/src/main/resources/config.yml)        |
| BungeeCord    | [`/plugins/LuckPerms/config.yml`](https://github.com/LuckPerms/LuckPerms/blob/master/bungee/src/main/resources/config.yml)        |
| Sponge        | [`/config/luckperms/luckperms.conf`](https://github.com/LuckPerms/LuckPerms/blob/master/sponge/src/main/resources/luckperms.conf) |
| Fabric        | [`/config/luckperms/luckperms.conf`](https://github.com/LuckPerms/LuckPerms/blob/master/fabric/src/main/resources/luckperms.conf) |
| Forge         | [`/config/luckperms/luckperms.conf`](https://github.com/LuckPerms/LuckPerms/blob/master/forge/src/main/resources/luckperms.conf)  |
| Nukkit        | [`/plugins/LuckPerms/config.yml`](https://github.com/LuckPerms/LuckPerms/blob/master/nukkit/src/main/resources/config.yml)        |
| Velocity      | [`/plugins/luckperms/config.yml`](https://github.com/LuckPerms/LuckPerms/blob/master/velocity/src/main/resources/config.yml)      |

Links to the default file for each platform are above. Please note that the configuration file does not automatically update when new options are added. The default options are used if nothing is found in the file.

# Index
### Essential Settings
* [`server`](#server)
* [`use-server-uuid-cache`](#use-server-uuid-cache)

### Storage Settings
* [`storage-method`](#storage-method)
* [`data`](#data)
* [`pool-settings`](#pool-settings)
* [`split-storage`](#split-storage)

### Update Propagation & Messaging Service
* [`sync-minutes`](#sync-minutes)
* [`watch-files`](#watch-files)
* [`messaging-service`](#messaging-service)
* [`auto-push-updates`](#auto-push-updates)
* [`push-log-entries`](#push-log-entries)
* [`broadcast-received-log-entries`](#broadcast-received-log-entries)
* [`redis`](#redis)
* [`rabbitmq`](#rabbitmq)

### Customization Settings
* [`temporary-add-behaviour`](#temporary-add-behaviour)
* [`primary-group-calculation`](#primary-group-calculation)
* [`argument-based-command-permissions`](#argument-based-command-permissions)
* [`log-notify`](#log-notify)
* [`meta-formatting`](#meta-formatting)

### Permission Calculation & Inheritance
* [`inheritance-traversal-algorithm`](#inheritance-traversal-algorithm)

##### Permission resolution settings
* [`include-global`](#include-global)
* [`include-global-world`](#include-global-world)
* [`apply-global-groups`](#apply-global-groups)
* [`apply-global-world-groups`](#apply-global-world-groups)

##### Meta lookup settings
* [`meta-value-selection-default`](#meta-value-selection-default)
* [`meta-value-selection`](#meta-value-selection)

##### Inheritance settings
* [`apply-wildcards`](#apply-wildcards)
* [`apply-regex`](#apply-regex)
* [`apply-shorthand`](#apply-shorthand)

###### Bukkit
* [`apply-bukkit-child-permissions`](#apply-bukkit-child-permissions)
* [`apply-bukkit-default-permissions`](#apply-bukkit-default-permissions)
* [`apply-bukkit-attachment-permissions`](#apply-bukkit-attachment-permissions)

###### Bungee
* [`apply-bungee-config-permissions`](#apply-bungee-config-permissions)

###### Sponge
* [`apply-sponge-implicit-wildcards`](#apply-sponge-implicit-wildcards)
* [`apply-sponge-default-subjects`](#apply-sponge-default-subjects)

##### Extra settings
* [`world-rewrite`](#world-rewrite)
* [`group-weight`](#group-weight)

### Fine Tuning Options
##### Server Operator / Vault (Bukkit version only)
* [`enable-ops`](#enable-ops)
* [`auto-op`](#auto-op)
* [`commands-allow-op`](#commands-allow-op)
* [`use-vault-server`](#use-vault-server)
* [`vault-server`](#vault-server)
* [`vault-include-global`](#vault-include-global)
* [`vault-ignore-world`](#vault-ignore-world)
* [`vault-debug`](#vault-debug)

### Miscellaneous Settings
* [`debug-logins`](#debug-logins)
* [`allow-invalid-usernames`](#allow-invalid-usernames)
* [`prevent-primary-group-removal`](#prevent-primary-group-removal)
* [`contexts.json`](#contextsjson)

# Config Sources

LuckPerms will attempt to resolve configuration settings from various sources (in the following order).

1. **System Properties**
2. **Environment Variables**
3. **Configuration File** (`config.yml` or `luckperms.conf`, depending on the platform)
4. Fallback to default values

### System Properties

[System properties](https://docs.oracle.com/javase/tutorial/essential/environment/sysprop.html) are a generic way to configure Java applications. They can either be set using a command line flag, or programmatically using the [`java.lang.System`](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/System.html) API.

e.g. To replicate the following YAML from a LuckPerms config.yml with system properties:

```yaml
server: example

storage-method: mysql
data:
  address: 192.168.0.100
```

... start your server with the following arguments:

```
java
  -Dluckperms.server=example
  -Dluckperms.storage-method=mysql
  -Dluckperms.data.address=192.168.0.100
  -jar server.jar
```

### Environment Variables

[Environment variables](https://en.wikipedia.org/wiki/Environment_variable) are a generic way to configure any application. The way they are defined depends on your setup. An example is given below for unix-like shells, but you can also [easily set them](https://docs.docker.com/engine/reference/commandline/run/#set-environment-variables--e---env---env-file) if you're running your server in a Docker container, for example.

e.g. To replicate the following YAML from a LuckPerms config.yml with environment variables:

```yaml
server: example

storage-method: mysql
data:
  address: 192.168.0.100
```

... start your server like so:

```bash
export LUCKPERMS_SERVER="example"
export LUCKPERMS_STORAGE_METHOD="mysql"
export LUCKPERMS_DATA_ADDRESS="192.168.0.100"

java -jar server.jar
```

# Descriptions

### `server`
The name of the server, used for server specific permissions.   

If set to "global" this setting is ignored. More details about how server specific permissions are groups work can be found [here](Advanced-Setup).

##### Example
```yaml
server: global
```

___
### `use-server-uuid-cache`

If the servers own UUID cache/lookup facility should be used when there is no record for a player in the LuckPerms cache.

When this setting is disabled, LP only uses its own cache. 

##### Example
```yaml
use-server-uuid-cache: false
```

___
### `storage-method`
Which storage method the plugin should use.

See [here](Storage-types) for a full list of supported types.

**Accepts:** `mysql`, `mariadb`, `postgresql`, `sqlite`, `h2`, `json`, `yaml`, `hocon`, `mongodb`

If your MySQL server supports it, the `mariadb` option is preferred over `mysql`. `h2` is also generally preferred over `sqlite`.

##### Example
```yaml
storage-method: h2
```

___
### `data`
This section is used for specifying credentials used for storage methods.

* **`address`** - the host to be used for the database. Uses the standard DB engine port by default. If you have a non-default port, specify it here using `host:port`.
* **`database`** - the database which should be used by LuckPerms
* **`username`** - the username to be used
* **`password`** - the password to be used. Leave empty to use no authentication.


##### Example
```yaml
data:
  address: localhost
  database: minecraft
  username: root
  password: ''
```

___
### `pool-settings`

These settings apply to the MySQL connection pool. The default values will be suitable for the majority of users. Do not change these settings unless you know what you're doing!

Sets the maximum size of the MySQL connection pool. Basically this value will determine the maximum number of actual
connections to the database backend. More information about determining the size of connection pools can be found here:

https://github.com/brettwooldridge/HikariCP/wiki/About-Pool-Sizing

##### Example
```yaml
data:
  pool-settings:
    maximum-pool-size: 10
```

___
### `split-storage`
The split storage section allows you to use multiple storage options for different types of data.

**The different types of data are:**

* **`user`** - data about users, including their permissions, parents and meta
* **`group`** - data about groups, including their permissions, parents and meta
* **`track`** - data about tracks (or so called "ladders")
* **`uuid`** - a cache of `uuid <-- --> username` used by LuckPerms when usernames are used in the `/lp user` command instead of uuids.
* **`log`** - the action log stored by LuckPerms

The allowed storage types are detailed above.

##### Example
```yaml
split-storage:
  enabled: true
  methods:
    user: mariadb
    group: yaml
    track: yaml
    uuid: mariadb
    log: mariadb
```

___
### `sync-minutes`
This option controls how frequently LuckPerms will perform a sync task.

A sync task will refresh all data from the storage, and ensure that the most up-to-date data is being used by the plugin.

This is disabled by default, as most users will not need it. However, if you're using a remote storage type without a messaging service setup, you may wish to set this value to something like 3.

Set to -1 to disable the task completely.

##### Example
```yaml
data:
  sync-minutes: 3
```

___
### `watch-files`
When using a file-based storage type, LuckPerms will monitor the data files for changes, and then schedule automatic updates when changes are detected.

If you don't want this to happen, set this option to false.

##### Example
```yaml
watch-files: true
```

___
### `messaging-service`
Settings for the messaging service.

If enabled and configured, LuckPerms will use the messaging system to inform other connected servers of changes. Use the command "/luckperms networksync" to push changes. Data is NOT stored using this service. It is only used as a messaging platform.

If you decide to enable this feature, you should set "sync-minutes" to -1, as there is no need for LuckPerms to poll the database for changes.

**Available options:**
* **`sql`** - uses the SQL database to form a queue system for communication. Will only work when `storage-method` is set to MySQL or MariaDB. This is chosen by default when the option is set to 'none' and SQL storage is in use. Set to `notsql` to disable this.
* **`pluginmsg`** - uses the plugin messaging channels to communicate. LuckPerms must be installed on your BungeeCord/Velocity proxy & all connected backend servers. This won't work if you have multiple proxies. The option needs to be set on all LP instances. Using `sql` is recommended over this option!
* **`lilypad`** - uses LilyPad's pub sub to push changes. You need to have the LilyPad-Connect plugin installed.
* **`redis`** - uses Redis pub sub to push changes.
* **`rabbitmq`** - uses RabbitMQ pub sub (AMQP) to push changes.
* **`none`** - nothing!

##### Example
```yaml
messaging-service: none
```

___
### `auto-push-updates`
If LuckPerms should automatically push updates after a change has been made with a command.

##### Example
```yaml
auto-push-updates: true
```

___
### `push-log-entries`
If LuckPerms should push logging entries to connected servers via the messaging service.

##### Example
```yaml
push-log-entries: true
```

___
### `broadcast-received-log-entries`
If LuckPerms should broadcast received logging entries to players on this platform.

If you have LuckPerms installed on your backend servers as well as a BungeeCord proxy, you should set this option to false on either your backends or your proxies, to avoid players being messaged twice about log entries.

##### Example
```yaml
broadcast-received-log-entries: true
```

___
### `redis`
Settings for Redis.

* **`address`** - the host to be used for redis (single node). Uses the standard port by default (6379). If you have a non-default port, specify it here using `host:port`.
* **`addresses`** - the hosts to be used for redis (cluster).
* **`password`** - the password to be used. Leave empty to use no authentication.

##### Example
For redis single node:
```yaml
redis:
  enabled: true
  address: localhost
  password: 'passw0rd'
```

For redis cluster:
```yaml
redis:
  enabled: true
  addresses:
    - redis-node1
    - redis-node2
  password: 'passw0rd'
```

---
### `rabbitmq`
Settings for RabbitMQ (AMQP).

* **`address`** - the host to be used for rabbitmq. Uses the standard AMQP port by default (5672). If you have a non-default port, specify it here using `host:port`.
* **`vhost`** - the virtual host to use for LuckPerms. In most cases, this can (and should) be left default. See [here](https://www.rabbitmq.com/vhosts.html) for more information on virtual hosts.
* **`username`** - the username to be used. Default is guest, which is a user that has all privileges on the / virtual host. See [here](https://www.rabbitmq.com/access-control.html) for more information on access control.
* **`password`** - the password to be used. Default is guest, which is the password for the guest user (see above)

##### Example
```yaml
rabbitmq:
  enabled: true
  address: localhost
  vhost: '/'
  username: 'guest'
  password: 'guest'
```

___
### `temporary-add-behaviour`

Controls how temporary permissions/parents/meta should be accumulated. The default behaviour is `deny`.

* **`accumulate`** - the duration of any existing nodes will just be added to the new duration
* **`replace`** - the longest duration will be kept, any others nodes will be forgotten
* **`deny`** - the command will just fail if you try to add a duplicate temporary node

##### Example
```yaml
temporary-add-behaviour: deny
```

___
### `primary-group-calculation`

How should LuckPerms determine a users "primary" group. The default is `parents-by-weight`.

* **`stored`** - use the value stored against the users record in the file/database
* **`parents-by-weight`** - use the users most highly weighted parent
* **`all-parents-by-weight`** - same as above, but calculates based upon all parents inherited from both directly and indirectly

##### Example
```yaml
primary-group-calculation: parents-by-weight
```

___
### `argument-based-command-permissions`

If LuckPerms should run extra permission checks when a player uses commands to modify permission data.

This system is documented in detail [here](Argument-based-command-permissions).

##### Example
```yaml
argument-based-command-permissions: true
```

___
### `log-notify`

If the plugin should send log notifications to users whenever permissions are modified. Notifications are only sent to those with the appropriate permission to receive the notification. 

Notifications can also be disabled temporarily in-game using `/lp log notify off`

##### Example
```yaml
log-notify: true
```

___
### `meta-formatting`

How LuckPerms should form prefixes and suffixes.

This system is documented in detail [here](Prefix-&-Suffix-Stacking).

___
### `inheritance-traversal-algorithm`

The algorithm LuckPerms should use when traversing the "inheritance tree".

* **`breadth-first`** - See: https://en.wikipedia.org/wiki/Breadth-first_search
* **`depth-first-pre-order`** - See: https://en.wikipedia.org/wiki/Depth-first_search
* **`depth-first-post-order`** - See: https://en.wikipedia.org/wiki/Depth-first_search

##### Example
```yaml
inheritance-traversal-algorithm: depth-first-pre-order
```

___
### `include-global`
If players on this server should have their global permissions applied. (permissions that were not set with a specific server).

If this option is set to false, only permissions that were specifically set to apply on this server will apply. Do not set to false if the "server" option above is set to global. More details about how server specific permissions are groups work can be found [here](Advanced-Setup).

##### Example
```yaml
include-global: true
```

___
### `include-global-world`

Similar to the option above, except this works with worlds. If set to false, only permissions that are set in specific worlds will be given to users. Any permissions set without a specific world context will not be applied.

##### Example
```yaml
include-global-world: true
```

___
### `apply-global-groups`
This option operates in the same manner as "include-global", except changes the setting for group inheritance.

When calculating a players permissions, the plugin will scale the inheritance tree, resolving group memberships recursively. If this setting is set to false, and as a result, a group is not "applied", then none of that groups parents will be considered, and the inheritance lookup will stop at that point.

This means that even if a player indirectly inherits a group on a specific server, the group will not be applied if it is inherited through a non-server specific group.

For example, with this setting false, and the following setup:

```
User "Luck" inherits from group "admin" globally, and admin inherits from "default" on a specific server.
```

Even though Luck inherits default on the specific server, it will not be applied, because the inheritance lookup stops at admin. The parent groups of admin are therefore never even considered.

##### Example
```yaml
apply-global-groups: true
```

___
### `apply-global-world-groups`

Similar to the option above, except this works with worlds. If set to false, only groups that are set in specific worlds will be assigned and resolved for users. Any groups set without a specific world context will not be applied.

##### Example
```yaml
apply-global-world-groups: true
```

___
### `meta-value-selection-default`

Defines how meta values should be selected. The default value is `inheritance`.

* **`inheritance`** - Selects the meta value that was inherited first
* **`highest-number`** - Selects the highest numerical meta value
* **`lowest-number`** - Selects the lowest numerical meta value

##### Example
```yaml
meta-value-selection-default: inheritance
```

___
### `meta-value-selection`

Defines how meta values should be selected per key.

See the option above for available settings.

##### Example
```yaml
meta-value-selection:
  max-homes: highest-number
```

___
### `apply-wildcards`
If the plugin should apply wildcard permissions.

If plugin authors do not provide their own wildcard permissions, then enabling this option will allow LuckPerms to parse them instead. Bukkit especially did not endorse this practice, however it has become common among server administrators. On Sponge, this setting control whether "node.part.\*" style wildcards will function.

##### Example
```yaml
apply-wildcards: true
```

___
### `apply-regex`
If the plugin should parse regex permissions.

If set to true, LuckPerms will detect any regex permissions, marked with "r=" at the start of the node, and return all requests matching the node. If you do not have any regex permissions setup, enabling this option will have no impact on performance. More info on this feature can be found [here](Advanced-Setup#regex).

##### Example
```yaml
apply-regex: true
```

___
### `apply-shorthand`
If the plugin should resolve and apply any shorthand (GLOB style) permissions.

More info on this feature can be found [here](Advanced-Setup#shorthand-permissions).

##### Example
```yaml
apply-shorthand: true
```

___
### `apply-bukkit-child-permissions`
If the plugin should apply Bukkit child permissions.

Plugin authors can define custom permissions structures for their plugin, which will be resolved and used by LuckPerms if this setting is enabled.

This is enabled by default, as it is a standard Bukkit feature, which most server admins expect to work. However, if you'd prefer not to use this system, it can be safely disabled.

##### Example
```yaml
apply-bukkit-child-permissions: true
```

___
### `apply-bukkit-default-permissions`
If the plugin should apply Bukkit default permissions.

Plugin authors can define permissions which should be given to all users by default, or setup permissions which should/shouldn't be given to opped players. If this option is set to false, LuckPerms will ignore these defaults.

This is enabled by default, as it is a standard Bukkit feature, which most server admins expect to work. However, if you'd prefer not to use this system, it can be safely disabled.

##### Example
```yaml
apply-bukkit-default-permissions: true
```

___
### `apply-bukkit-attachment-permissions`
If the plugin should apply Bukkit attachment permissions.

Other plugins on the server are able to add their own "permission attachments" to players. This allows them to grant players additional permissions which last until the end of the session, or until they're removed. If this option is set to false, LuckPerms will not include these attachment permissions when considering if a player should have access to a certain permission.

You may also see a slight performance improvement by enabling this feature. Combined with disabling the OP system, this system can be quite effective at disabling malicious attempts by plugins to grant arbitrary permissions to players.

This is enabled by default, as it is a standard Bukkit feature, which most server admins expect to work. However, if you'd prefer not to use this system, it can be safely disabled.

##### Example
```yaml
apply-bukkit-attachment-permissions: true
```

___
### `apply-bungee-config-permissions`
If the plugin should apply the permissions & groups defined in the BungeeCord config.yml

If set to false, LuckPerms will ignore these values.

This is disabled by default, as permissions should really be defined within LuckPerms, so they can be viewed and edited in-game alongside everything else.

##### Example
```yaml
apply-bungee-config-permissions: false
```

___
### `apply-sponge-implicit-wildcards`
If the plugin should resolve and apply permissions according to Sponge's implicit wildcard inheritance system.

That being: If a user has been granted `example`, then the player should have also be automatically granted `example.function`, `example.another`, `example.deeper.nesting`, and so on.

If this option is set to false, this system will not be applied.

This is enabled by default, as it is a standard Sponge feature, which most server admins / plugin authors expect to work. However, if you'd prefer not to use this system, it can be disabled.

##### Example
```hocon
apply-sponge-implicit-wildcards=true
```

___
### `apply-sponge-default-subjects`
If the plugin should apply Sponge default subject permissions.

Plugins can manipulate a set of default permissions granted to all users. If this option is set to false, the plugin will ignore this data when considering if a player has a permission.

This is enabled by default, as it is a standard Sponge feature, which most server admins / plugin authors expect to work. However, if you'd prefer not to use this system, it can be disabled.

##### Example
```hocon
apply-sponge-default-subjects=true
```

___
### `world-rewrite`

Allows you to set "aliases" for the worlds sent forward for context calculation. These aliases are provided in addition to the real world name. Applied recursively.

##### Example
```yaml
world-rewrite:
  world_nether: world
  world_the_end: world
```

___
### `enable-ops`
If the vanilla OP system should be used.

If set to false, all users will be de-opped, and the op/deop commands will be disabled.

##### Example
```yaml
enable-ops: true
```

___
### `auto-op`
If set to true, any user with the permission "luckperms.autoop" will automatically be granted server operator status.

This permission can be inherited, or set on specific servers/worlds, temporarily, etc. Additionally, setting this to true will force the "enable-ops" option above to false. All users will be de-opped unless they have the permission node, and the op/deop commands will be disabled.

It is important to note that this setting is only checked when a player first joins the server, and when they switch worlds. Therefore, simply removing this permission from a user will not automatically de-op them. A player may need to relog to have the change take effect.

It is recommended that you use this option instead of assigning a single '\*' permission.

##### Example
```yaml
auto-op: false
```

___
### `commands-allow-op`
If opped players should be allowed to use LuckPerms commands.

Set to false to only allow users who have the permissions access to the commands

##### Example
```yaml
commands-allow-op: true
```

___
### `use-vault-server`
If the `vault-server` option below should be used.

When this option is set to false, the server value defined above under "server" is used for Vault operations.

##### Example
```yaml
use-vault-server: false
```

___
### `vault-server`
The name of the server used within Vault operations.

If you don't want Vault operations to be server specific, set this to "global".

Will only take effect if `use-vault-server` is set to true above.

##### Example
```yaml
vault-server: global
```

___
### `vault-include-global`
If global permissions should be considered when retrieving meta or player groups.

##### Example
```yaml
vault-include-global: true
```

___
### `vault-ignore-world`
If Vault operations should ignore any world arguments if supplied.

By default, if a world argument is not supplied, permissions will be set on the players current world. (Vault design is just 10/10). Set this to true to change this behaviour.

##### Example
```yaml
vault-ignore-world: false
```

___
### `vault-debug`
If LuckPerms should print debugging info to console when a plugin uses a Vault function

##### Example
```yaml
vault-debug: false
```

___
### `debug-logins`

If LuckPerms should produce extra logging output when it handles logins.

Useful if you're having issues with UUID forwarding or data not being loaded.

The debug messages look like this:
```
[INFO]: [LP] Processing pre-login for c1d60c50-70b5-4722-8057-87767557e50d - Luck
[INFO]: UUID of player Luck is c1d60c50-70b5-4722-8057-87767557e50d
[INFO]: [LP] Processing login for c1d60c50-70b5-4722-8057-87767557e50d - Luck
[INFO]: Luck[/xxx:xxx] logged in with entity id xxx at ([xxx]x, x, x)
```

##### Example
```yaml
debug-logins: false
```

___
### `allow-invalid-usernames`

If set to true, LuckPerms will allow usernames with non alphanumeric characters.

Note that due to the design of the storage implementation, usernames must still be 16 characters or less.

##### Example
```yaml
allow-invalid-usernames: false
```

___
### `prevent-primary-group-removal`

If set to false, the plugin will allow a user's primary group to be removed with the `parent remove` command, and will set their primary group back to default.

##### Example
```yaml
prevent-primary-group-removal: false
```

___




## contexts.json
The `contexts.json` file is found alongside the main LuckPerms configuration file, and allows you to set two things.

### Static Contexts
Static contexts are [contexts](Command-Usage#what-is-context) which never change, and are granted to all players on the server by default.

LuckPerms provides one static context by default, called "server". This value is set using the `server` option in the main configuration file.

For example, if in my network, I have 3 factions servers, each with distinct names. The in LP config of each server, I have the server names set to `factions1`, `factions2` and `factions3`. However, I want to grant a permission on all of the servers.

To achieve this, on all of the factions servers, I can add a static context called `servertype` and set it to `factions`.
```json
{
  "static-contexts": {
  	"servertype": "factions"
  },
}
```

Then, I can use `/lp group default permission set some.permission true servertype=factions` to set a permission on all of the factions servers.


### Default Contexts
Default contexts are [contexts](Command-Usage#what-is-context) which are used by default in all commands executed on the server, if nothing is specifically specified.

```json
{
  "default-contexts": {
  	"server": "survival"
  },
}
```

With the above set, running `/lp user Luck permission set some.permission true` would set `some.permission` to true for me in the `server=survival` context.
