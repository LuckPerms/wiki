Even been in a situation where you need to find a permission for a certain command or feature, but can't find any documentation for it?

Maybe the documentation is outdated, or just doesn't contain the right info. Perhaps you want to debug an issue with players not having the right permissions, or are just interested in what plugins are checking for.

The verbose system solves all!

## How to use it
The command usage is as follows:

### `/lp verbose <on|record|off|paste> [filter]`
The first argument enables/disables the system, and the second sets up the filter.

| Option   | Description |
|----------|-------------|
| `on`     | Enables the system, and will send you an alert in chat when the filter is matched. |
| `record` | Same as "on", however you will not be notified via chat. |
| `off`    | Just disables the system, and clears any matches from memory. |
| `paste`  | Same as "off", but will also upload the first 500 results to GitHub, and provide you with a link. |

#### Filters
The filter is an expression used to match permission entries, and ignore entries you don't need. It could just be a player name, or much more advanced.

A filter string will match the start of the permission being checked, or the users full name. You can also use `&` (and) and `|` (or) symbols, and `!` to negate a match. Parenthesis `(  )` are also supported.

##### Some examples
* `Luck & (essentials | worldedit)` - Matches any checks made against "Luck" that start with "essentials" or "worldedit"
* `Luck & !anticheat` - Matches any checks made against "Luck" that do not start with "anticheat"
* `anticheat & !anticheat.check` - Matches checks on all users starting with "anticheat" but not starting with "anticheat.check"

## Example
I ran `/lp verbose record Luck & minecraft`, which enabled the system, and made it match any checks against "Luck" that start with "minecraft".

I then ran the `/help` command (to generate some permission checks), followed by `/lp verbose paste`.

The plugin then uploaded the results, and returned this link. [`https://git.io/vDUba`](https://git.io/vDUba)

If you take a look at the link, you'll see the results of the check. 😄 

Under metadata, you can see some data about the check. You'll notice that `Count: **58** / 72`. This means that during the checking period, 72 permissions were checked, and 58 matched the filter. The results of each of those checks are shown below.







