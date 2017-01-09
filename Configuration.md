The configuration files are heavily annotated with descriptions of exactly what each option does, however, this page goes into more detail on each section.

## Index
* General

## General
#### `server`
**Default**: global   
The name of this server instance. Used for per-server permissions. More info on this can be found [here](https://github.com/lucko/LuckPerms/wiki/Advanced-Setup).
____

#### `include-global`
**Default**: true (false on BungeeCord)   
If players on this server should have their global permissions applied. (permissions that were not set with a specific server). If this option is set to false, only permissions that were specifically set to apply on this server will apply. Do not set to false if the "server" option above is set to global.
____

#### `include-global-world`
**Default**: true   
Similar to the option above, except this works with worlds. If set to false, only permissions that are set in specific worlds will be given to users.
____

#### `apply-global-groups`
**Default**: true   
This option operates in the same manner as "include-global", except changes the setting for group inheritance.
____

#### `apply-global-world-groups`
**Default**: true   
Same as above, except changes the behaviour for worlds.
____

#### `online-mode`
**Default**: true   
If this server is in offline or online mode. This setting allows a player to have the same UUID across a network of offline mode/mixed servers.   

You should generally reflect the setting in server.properties here. Except when...

1. You have Spigot servers connected to a BungeeCord proxy, with online-mode set to false, but 'bungeecord' set to true in the spigot.yml AND 'ip-forward' set to true in the BungeeCord config.yml. In this case, set online-mode in LuckPerms to true, despite the server being in offline mode.
2. You are only running one server instance using LuckPerms, (not a network) In this case, set online-mode to true no matter what is set in server.properties. (we can just fallback to the servers uuid cache)
3. If your proxy is running in offline mode, and you are using PaperSpigot (https://ci.destroystokyo.com/job/PaperSpigot/), you should set "bungee-online-mode" to false in the paper.yml, and set "online-mode" to true in all LuckPerms configs. This approach is thoroughly recommended for offline mode networks.
____

#### `log-notify`
**Default**: true   
If the plugin should send log notifications to users whenever permissions are modified. Notifications are only sent to those with permission to view them, and this command acts as a global toggle for /lp log notify \<on|off\>
____


## Permission Calculation
#### `apply-wildcards`
**Default**: true   
If the plugin should apply wildcard permissions. If plugin authors do not provide their own wildcard permissions, then enabling this option will allow LuckPerms to parse them instead. Bukkit especially did not endorse this practice, however it has become common among server administrators. On Sponge, this setting control whether "node.part.*" style wildcards will function.
____

#### `apply-regex`
**Default**: true   
If the plugin should parse regex permissions. If set to true, LuckPerms will detect any regex permissions, marked with "r=" at the start of the node, and return all requests matching the node. If you do not have any regex permissions setup, enabling this option will have no impact on performance. More info on this feature can be found [here](https://github.com/lucko/LuckPerms/wiki/Advanced-Setup#regex).
____

#### `apply-shorthand`
**Default**: true   
If the plugin should resolve and apply any shorthand (GLOB style) permissions. More info on this feature can be found [here](https://github.com/lucko/LuckPerms/wiki/Advanced-Setup#shorthand-permissions).
____

#### `group-weight`
**Default**: empty   
This section allows you to define a list of group weights, as opposed to setting them with the [set weight command](https://github.com/lucko/LuckPerms/wiki/Command-Usage#perms-group-group-setweight). Higher weight = higher priority. The default weight is 0.   
   
**Example**:   
```yml
group-weight:
  admin: 10
  mod: 5
  default: 1
```








