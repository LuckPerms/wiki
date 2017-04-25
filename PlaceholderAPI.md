LuckPerms has a few placeholders available in extended_clip's [PlaceholderAPI](https://www.spigotmc.org/resources/placeholderapi.6245/).

The LuckPerms identifier is just **"luckperms"**.

## Usage

To use the placeholders, you need to run the commands below. These will install the LuckPerms placeholder expansion so you can use all the placeholders listed below.
##### `/papi ecloud download LuckPerms`
##### `/papi reload`
Keep in mind you will need to be opped in order to run these commands (* will not work).

Also note that if you only want to retrieve prefix/suffix data, you can use the Vault placeholders if you have Vault installed on your server, and the Vault expansion installed.

## Placeholders
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
### `%luckperms_check_permission_<permission>%`
**Description:** Checks to see if the player has a given permission. This is done in the same way a plugin would check for a permission    
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