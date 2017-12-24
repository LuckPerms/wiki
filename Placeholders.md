LuckPerms has a few placeholders available for use in supported plugins.

# Usage
## PlaceholderAPI
To use the LuckPerms placeholders in plugins which support clip's [PlaceholderAPI](https://www.spigotmc.org/resources/placeholderapi.6245/), you need to install the LuckPerms expansion.

### Automatic install
* To install the latest version of the expansion automagically from clip's ecloud system, simply run the following commands.
  * `/papi ecloud download LuckPerms`
  * `/papi reload`

* You will need to be opped in order to run these commands (or you can just run them from console).

### Manual install
* To manually install the latest version of the expansion, you need to...
* Download `Expansion-LuckPerms.jar` from [here](https://ci.lucko.me/job/LuckPermsPlaceholders/), and ...
* Place it in `/plugins/PlaceholderAPI/expansions/`.

## MVdWPlaceholderAPI
To use the LuckPerms placeholders in plugins which support Maximvdw's [MVdWPlaceholderAPI](https://www.spigotmc.org/resources/mvdwplaceholderapi.11182/), you need to install the LuckPerms placeholder hook plugin.

* Download `LuckPermsMVdWHook.jar` from [here](https://ci.lucko.me/job/LuckPermsPlaceholders/), and ...
* Place it in your `/plugins/` folder.

# Placeholders
### `%luckperms_group_name%`
**Description:** Returns the name of the players primary group    
**Example:** n/a

___
### `%luckperms_context_<context key>%`
**Description:** Returns the value of the given context, or empty if the context is not assigned.    
**Example:** %luckperms_context_server%

___
### `%luckperms_groups%`
**Description:** Returns a list of all groups on the server, separated by commas    
**Example:** n/a

___
### `%luckperms_has_permission_<permission>%`
**Description:** Checks if the player has the given permission set directly. Does not account for wildcards, or inherited permissions.    
**Example:** %luckperms_has_permission_essentials.ban%

___
### `%luckperms_inherits_permission_<permission>%`
**Description:** Checks if the player has or inherits the given permission. Does not account for wildcards, or inherited permissions. The `check_permission` placeholder is preferred over this placeholder.    
**Example:** %luckperms_inherits_permission_essentials.ban%

___
### `%luckperms_check_permission_<permission>%`
**Description:** Checks to see if the player has a given permission. This is done in the same way a plugin would check for a permission.    
**Example:** %luckperms_check_permission_some.cool.permission%

___
### `%luckperms_in_group_<group>%`
**Description:** Returns if the player is a member of a given group. Does not include inherited groups.    
**Example:** %luckperms_in_group_admin%

___
### `%luckperms_inherits_group_<group>%`
**Description:** Returns if the player is in or inherits a given group.    
**Example:** %luckperms_inherits_group_vip%

___
### `%luckperms_on_track_<track>%`
**Description:** Returns if the players primary group is on the given track.    
**Example:** %luckperms_on_track_staff%

___
### `%luckperms_has_groups_on_track_<track>%`
**Description:** Returns if the player inherits from any groups on the given track    
**Example:** %luckperms_on_track_donor%

___
### `%luckperms_highest_group_by_weight%`
**Description:** Returns the name of the players highest prioity group.    
**Example:** n/a

___
### `%luckperms_lowest_group_by_weight%`
**Description:** Returns the name of the players lowest priority group.    
**Example:** n/a

___
### `%luckperms_first_group_on_tracks_<tracks>%`
**Description:** Returns the name of the first group a player has on the given tracks. Tracks represents a comma separated list of tracks. Each group in the tracks is considered in order.    
**Example:** %luckperms_first_group_on_tracks_staff,donor%

___
### `%luckperms_last_group_on_tracks_<tracks>%`
**Description:** Returns the name of the last group a player has on the given tracks. Tracks represents a comma separated list of tracks. Each group in the tracks is considered in reverse order.    
**Example:** %luckperms_last_group_on_tracks_staff,donor%

___
### `%luckperms_expiry_time_<permission>%`
**Description:** Gets the time until the given permission will expire for the player. Returns empty if the player doesn't have the permission.    
**Example:** %luckperms_expiry_time_essentials.fly%

___
### `%luckperms_group_expiry_time_<group name>%`
**Description:** Gets the time until the given group membership will expire for the player. Returns empty if the player doesn't have the group.    
**Example:** %luckperms_group_expiry_time_vip%

___
### `%luckperms_prefix%`
**Description:** Returns the players prefix. Results may be more accurate using the Vault placeholders, as this lookup is not affected by the Vault configuration options.    
**Example:** n/a

___
### `%luckperms_suffix%`
**Description:** Returns the players suffix. Results may be more accurate using the Vault placeholders, as this lookup is not affected by the Vault configuration options.    
**Example:** n/a

___
### `%luckperms_meta_<meta key>%`
**Description:** Returns the value associated with the given meta key.    
**Example:** %luckperms_meta_some-key%

___
