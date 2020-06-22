### What does it do?
The "meta stacking" feature allows you to display multiple prefixes or suffixes alongside a players username in chat.

You still need to have a chat formatting plugin installed. 

### How does it work?
When the chat formatting plugin requests a players prefix/suffix, instead of just returning the prefix with the highest weight, LuckPerms can apply a set of rules to combine a number of prefixes/suffixes together.

The default settings look like this:
```yml
meta-formatting:
  prefix:
    format:
      - "highest"
    duplicates: first-only
    start-spacer: ""
    middle-spacer: " "
    end-spacer: ""
  suffix:
    format:
      - "highest"
    duplicates: first-only
    start-spacer: ""
    middle-spacer: " "
    end-spacer: ""
```

All this means is that when a prefix  or suffix is requested, the one with the highest weight is returned.

### How do I add other elements?
The following elements are allowed.

| Element | Description |
|---------|-------------|
| `highest` | Selects the value with the highest weight, from all values held by or inherited by the player. |
| `lowest` | Same as above, except takes the one with the lowest weight. |
| `highest_own` | Selects the value with the highest weight, but will not accept any inherited values. |
| `lowest_own` | Same as above, except takes the value with the lowest weight. |
| `highest_inherited` | Selects the value with the highest weight, but will only accept inherited values. |
| `lowest_inherited` | Same as above, except takes the value with the lowest weight. |
| `highest_on_track_<track>` | Selects the value with the highest weight, but only if the value was inherited from a group on the given track. |
| `lowest_on_track_<track>` | Same as above, except takes the value with the lowest weight. |
| `highest_not_on_track_<track>` | Selects the value with the highest weight, but only if the value was inherited from a group not on the given track. |
| `lowest_not_on_track_<track>` | Same as above, except takes the value with the lowest weight. |
| `highest_from_group_<group>` | Selects the value with the highest weight, but only if the value was inherited from the given group. |
| `lowest_from_group_<group>` | Same as above, except takes the value with the lowest weight. |
| `highest_not_from_group_<group>` | Selects the value with the highest weight, but only if the value was not inherited from the given group. |
| `lowest_not_from_group_<group>` | Same as above, except takes the value with the lowest weight. |

### Duplicate Settings
| Element | Description |
|---------|-------------|
| `first-only` | Allows only the first duplicate |
| `last-only` | Allows only the last duplicate |
| `retain-all` | Allows all duplicates |
| `none` | Allows no duplicates |

### An example
For example, on a prison server, you might have 3 types of group. The "gameplay" rank, a user's donor group, and staff groups.

If a user is in all 3 groups, I want all three prefixes to display. e.g.   
`[Mine C] [Donor] [Admin] Luck: hi!`.

But if a user doesn't have a staff group, then I want to show   
`[Mine C] [Donor] Luck: hi`.

This is all possible with the stacking system. Each "element" in the stack has to be added to the format section.

```yml
prefix:
  format:
    - "highest_on_track_prison"
    - "highest_on_track_donor"
    - "highest_on_track_staff"
  duplicates: first-only
  start-spacer: ""
  middle-spacer: " "
  end-spacer: ""
```

If the player doesn't have any values that apply to the element, then it gets excluded from the stack.

The start, middle and end spacers allow you to control how each element is separated. For example:

  ```yml
  prefix:
    format:
      - "highest_on_track_prison"
      - "highest_on_track_donor"
      - "highest_on_track_staff"
    duplicates: first-only
    start-spacer: "★ "
    middle-spacer: " | "
    end-spacer: " "
  ```

... would result in:   
`★ [Mine C] | [Donor] | [Admin] Luck: hi`.

You can obviously change these values in accordance with your chat formatting plugin, which may provide similar options too.
