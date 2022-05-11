LuckPerms has a few placeholders available for use in supported plugins.

### PlaceholderAPI
To use the LuckPerms placeholders in plugins which support [PlaceholderAPI](https://www.spigotmc.org/resources/placeholderapi.6245/), you need to install the LuckPerms expansion.

To install the latest version of the expansion automagically from clip's ecloud system, simply run `/papi ecloud download LuckPerms` followed by `/papi reload`.

To manually install the latest version of the expansion, you need to:

* Download `Expansion-LuckPerms.jar` from [here](https://ci.lucko.me/job/LuckPermsPlaceholders/)
* Place it in `/plugins/PlaceholderAPI/expansions/`.

### MVdWPlaceholderAPI
To use the LuckPerms placeholders in plugins which support [MVdWPlaceholderAPI](https://www.spigotmc.org/resources/mvdwplaceholderapi.11182/), you need to install the LuckPerms placeholder hook plugin.

* Download `LuckPermsMVdWHook.jar` from [here](https://ci.lucko.me/job/LuckPermsPlaceholders/)
* Place it in your `/plugins/` folder.

### Fabric PlaceholderAPI
To use the Fabric LuckPerms placeholders in mods which support [Fabric PlaceholderAPI](https://placeholders.pb4.eu/), you need to install the LuckPerms placeholder hook mod. The placeholder format is slightly different and documented in their docs [here](https://placeholders.pb4.eu/user/mod-placeholders/#luckperms).

* Download `LuckPerms-Fabric-PlaceholderAPI-Hook.jar` from [here](https://ci.lucko.me/job/LuckPermsPlaceholders/)
* Place it in your `/mods/` folder.



## Placeholders

For placeholders with an **argument**, the argument must be included at the end of the placeholder separated by an underscore (`_`).

For example, the `%luckperms_meta%` placeholder requires a `<meta key>` argument. Assuming the meta key is e.g. *home*, the full placeholder would be `%luckperms_meta_home%`.

| Placeholder                                     | Argument                     | Description                                                  |
| ----------------------------------------------- | ---------------------------- | ------------------------------------------------------------ |
| `%luckperms_prefix%`                            |                              | Returns the player's prefix                                  |
| `%luckperms_suffix%`                            |                              | Returns the players suffix                                   |
| `%luckperms_meta%`                              | `<meta key>`                 | Returns a single value for the given meta key                |
| `%luckperms_meta_all%`                          | `<meta key>`                 | Returns all assigned values for the given meta key           |
| `%luckperms_prefix_element%`                    | `<element>`                  | Returns a prefix element using the given "meta stack" element definition. See [Prefix Stacking](Prefix-&-Suffix-Stacking) |
| `%luckperms_suffix_element%`                    | `<element>`                  | Returns a suffix element using the given "meta stack" element definition. See [Prefix Stacking](Prefix-&-Suffix-Stacking) |
| `%luckperms_context%`                           | `[context key]` (*optional*) | Returns all of the players current contexts. If a key is given as an argument, then only the values corresponding to the given key are returned. |
| `%luckperms_groups%`                            |                              | Returns a list of the groups directly inherited by the player. |
| `%luckperms_inherited_groups%`                  |                              | Returns a list of all of the groups inherited (directly or indirectly) by the player. |
| `%luckperms_primary_group_name%`                |                              | Returns the name of the player's primary group.              |
| `%luckperms_has_permission%`                    | `<permission>`               | Returns if the player directly has the exact given permission (not the same as a permission check!) |
| `%luckperms_inherits_permission%`               | `<permission>`               | Returns if the player inherits the exact given permission (not the same as a permission check!) |
| `%luckperms_check_permission%`                  | `<permission>`               | Returns the result of a permission check for the given permission on the player. |
| `%luckperms_in_group%`                          | `<group>`                    | Returns if the player is directly a member of the given group. |
| `%luckperms_inherits_group%`                    | `<group>`                    | Returns if the player is a direct or indirect member of the given group. |
| `%luckperms_on_track%`                          | `<track>`                    | Returns if the player's "primary group" is on this track. (*deprecated - avoid relying on primary groups, use the placeholder below instead!*) |
| `%luckperms_has_groups_on_track%`               | `<track>`                    | Returns if any of the groups the player is directly a member of is on the given track. |
| `%luckperms_highest_group_by_weight%`           |                              | Returns the name of the players highest weighted group, *not including* groups they indirectly inherit from others. |
| `%luckperms_lowest_group_by_weight%`            |                              | Returns the name of the players lowest weighted group, *not including* groups they indirectly inherit from others. |
| `%luckperms_highest_inherited_group_by_weight%` |                              | Returns the name of the players highest weighted group, *including* groups they indirectly inherit from others. |
| `%luckperms_lowest_inherited_group_by_weight%`  |                              | Returns the name of the players lowest weighted group, *including* groups they indirectly inherit from others. |
| `%luckperms_current_group_on_track%`            | `<track>`                    | If the player is currently on the given track, returns the name of the group. |
| `%luckperms_next_group_on_track%`               | `<track>`                    | If the player is currently on the given track, returns the name of the next group (the one they would be promoted to next). |
| `%luckperms_previous_group_on_track%`           | `<track>`                    | If the player is currently on the given track, returns the name of the previous group (the one they would be demoted to next). |
| `%luckperms_first_group_on_tracks%`             | `<tracks>`                   | Given a comma separated list of track names, finds the first group inherited by the player on any of the given tracks. |
| `%luckperms_last_group_on_tracks%`              | `<tracks>`                   | Given a comma separated list of track names, finds the last group inherited by the player on any of the given tracks. |
| `%luckperms_expiry_time%`                       | `<permission>`               | Gets the duration remaining on a temporary permission assigned directly to the player. |
| `%luckperms_inherited_expiry_time%`             | `<permission>`               | Gets the duration remaining on a temporary permission assigned directly to or inherited by the player. |
| `%luckperms_group_expiry_time%`                 | `<group name>`               | Gets the duration remaining on a temporary group membership assigned directly to the player. |
| `%luckperms_inherited_group_expiry_time%`       | `<group name>`               | Gets the duration remaining on a temporary group membership assigned directly to or inherited by the player. |

