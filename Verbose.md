Even been in a situation where you need to find a permission for a certain command or feature, but can't find any documentation for it?

Maybe the documentation is outdated, or just doesn't contain the right info. Perhaps you want to debug an issue with players not having the right permissions, or are just interested in what plugins are checking for.

The verbose system allows you to monitor permission checks occurring in real time! 😄 

## How to use it
The command usage is as follows:

### `/lp verbose <on|record|off|upload> [filter]`
The first argument enables/disables the system, and the second sets up the filter.

| Option   | Description |
|----------|-------------|
| `on`     | Enables the system, and will send you an alert in chat when the filter is matched. |
| `record` | Same as "on", however you will not be notified via chat. |
| `off`    | Just disables the system, and clears any matches from memory. |
| `upload  | Same as "off", but will upload the results to the web viewer for easier analysis, and provide you with a link. |

#### Filters
The filter is an expression used to match permission entries, and ignore entries you don't need. It could just be a player name, or much more advanced.

A filter string will match the start of the permission being checked, or the users full name. You can use `&` (and), `|` (or), and `!` (not / negate) to setup expressions. Parenthesis `(  )` are also supported.

##### Some examples
* `Luck & (essentials | worldedit)` - Matches any checks made against "Luck" that start with "essentials" or "worldedit"
* `Luck & !anticheat` - Matches any checks made against "Luck" that do not start with "anticheat"
* `anticheat & !anticheat.check` - Matches checks on all users starting with "anticheat" but not starting with "anticheat.check"

## Web viewer
The web viewer exposes the same information available in-game, but is easier to analyse when there are lots of checks being processed.

You can simply click on an entry to see more information about the nature of the check.

![](https://i.imgur.com/lhL6uaO.png)






