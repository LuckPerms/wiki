LuckPerms has a few placeholders available in extended_clip's [PlaceholderAPI](https://www.spigotmc.org/resources/placeholderapi.6245/).

The LuckPerms identifier is just **"luckperms"**.

| Placeholder | Description | Example |
|-------------|-------------|---------|
| `%luckperms_group_name%`                     | Returns the name of the players primary group | n/a |
| `%luckperms_context_<context key>%`          | Returns the value of the given context, or empty if the context is not assigned. | %luckperms_context_server% |
| `%luckperms_groups%`                         | Returns a list of all groups on the server, separated by commas | n/a |
| `%luckperms_has_permission_<permission>%`    | Checks if the player has the given permission set directly. Does not account for wildcards, or inherited permissions | %luckperms_has_permission_essentials.ban% |
| `%luckperms_check_permission_<permission>%`  | Checks to see if the player has a given permission. This is done in the same way a plugin would check for a permission | %luckperms_check_permission_some.cool.permission% |
| `%luckperms_in_group_<group>%`               | Returns if the player is a member of a given group. Does not include inherited groups. | %luckperms_in_group_admin% |
| `%luckperms_inherits_group_<group>%`         | Returns if the player is in or inherits a given group. | %luckperms_inherits_group_vip% |
| `%luckperms_on_track_<track>%`               | Returns if the players primary group is on the given track | %luckperms_on_track_staff% |
| `%luckperms_has_groups_on_track_<track>%`    | Returns if the player inherits from any groups on the given track | %luckperms_on_track_donor% |
| `%luckperms_highest_group_by_weight%`        | Returns the name of the players highest prioity group. | n/a |
| `%luckperms_lowest_group_by_weight%`         | Returns the name of the players lowest priority group | n/a |
| `%luckperms_first_group_on_tracks_<tracks>%` | Returns the name of the first group a player has on the given tracks. Tracks represents a comma separated list of tracks. Each group in the tracks is considered in order. | %luckperms_first_group_on_tracks_staff,donor% |
| `%luckperms_last_group_on_tracks_<tracks>%`  | Returns the name of the last group a player has on the given tracks. Tracks represents a comma separated list of tracks. Each group in the tracks is considered in reverse order. | %luckperms_last_group_on_tracks_staff,donor% |
| `%luckperms_expiry_time_<permission>%`       | Gets the time until the given permission will expire for the player. Returns empty if the player doesn't have the permission. | %luckperms_expiry_time_essentials.fly% |
| `%luckperms_group_expiry_time_<group name>%` | Gets the time until the given group membership will expire for the player. Returns empty if the player doesn't have the group. | %luckperms_group_expiry_time_vip% |
| `%luckperms_prefix%`                         | Returns the players prefix. Results may be more accurate using the Vault placeholders, as this lookup is not affected by the Vault configuration options. | n/a |
| `%luckperms_suffix%`                         | Returns the players suffix. Results may be more accurate using the Vault placeholders, as this lookup is not affected by the Vault configuration options. | n/a |
| `%luckperms_meta_<meta key>%`                | Returns the value associated with the given meta key. | %luckperms_meta_some-key% |

To use the placeholders, simply download a copy of `Expansion-LuckPerms.jar` from the CI server, and place it in the `/plugins/PlaceholderAPI/expansions/` folder.     
[**Click here to download the expansion**](https://ci.lucko.me/job/LuckPermsPlaceholders/)

You can then use the LuckPerms placeholders in the same way as any other PlaceholderAPI placeholders.


Also note that if you only want to retrieve prefix/suffix data, you can use the Vault placeholders if you have Vault installed on your server, and the Vault expansion installed.