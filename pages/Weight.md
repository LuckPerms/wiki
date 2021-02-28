# Weights
Weights are an integral part of the way LuckPerms operates, and are based on the premise of resolving conflict where it may appear.

There are two different, independent weights systems in LuckPerms, the first being [**group weight**](#group-weights) and the second being [**meta weight**](#meta-weights) (like prefixes and suffixes).

In all cases, **a higher weight number is a higher priority** 

* When setting up weights, it is recommended that large gaps be left between groups, like going up by 100 instead of 1. This is so that if you want to insert groups/prefixes/suffixes later, you do not have to redefine everything.
* Weights can be any number, even negative!


## Group Weights
Group weights determine, in cases where a user has more than one group, which group's nodes take precedence when the nodes conflict. This is best explained by an example:

* Suppose a player was in group default and in group "admin". There is one permission node in each group, and it is `essentials.fly`.
* In default group, `essentials.fly` is set to `false`. In "admin" group, `essentials.fly` is set to `true`. Without setting up weights, it is inconsistent and unclear which node the player will get - there is no way to know for sure whether they will be able to fly or not.
* This is where __weights__ come in. Setting default in this example to have a higher weight than "admin" will result in the player being **unable** to fly. Setting admin to have a higher weight than default will result in the player being **able** to fly.

Likewise, whenever a player has several groups, the permissions in the highest weighted group will override the permissions in any lower weighted ones that conflict. 

### Setting group weights
There are two ways to set weight for a group; using a [command](#Group-Commands#lp-group-group-setweight-weight), and using the [editor](#Web-Editor#luckperms-nodes).

* With commands, you run /`lp group <group> setweight <weight>`.
* In the editor, you add the node `weight.<weight>` to the group.


## Meta Weights

Meta weights are very similar to group weights, but for prefixes and suffixes. In the same way the group weights work, when a player inherits multiple prefixes or suffixes, the highest weighted one is the one that will display.

### Setting meta weights
There are two ways to set a weight for a prefix or suffix; using a [command](#Meta-Commands), and using the [editor](#Web-Editor#luckperms-nodes).

* With commands, you simply set the weight when you add or set a prefix or suffix to a group or player: `/lp user/group <user|group> meta setprefix/addprefix <weight> <prefix>`.
* In the editor, you simply add or modify the node `prefix.<weight>.<prefix>` to change the weight. The same principle applies to suffixes.
