Contexts are a fundamental part of the way LuckPerms works. They are probably the most important concept in the whole plugin, and are incredibly powerful when used correctly.

___

**Context** in the most basic sense simply means the **circumstances where something will apply**.

A single "context" consists of a `key` and a `value`, and are represented in the form `key=value`. This will (hopefully) begin to make more sense when coupled with an example.

### Example
As we said previously, contexts are the circumstances where something will apply. As an example, let's suppose I wanted to set a permission, but **I only want the permission to apply in the "world_nether" world**. To achieve this, I'd supply a context when setting the permission to specify where the permission should apply.

In this case, the context **key** is `"world"`, and the **value** is `"world_nether"`. This would be represented in LuckPerms as `world=world_nether`.

In order to achieve this behaviour, I'd use something like: `/lp user Luck permission set test.permission world=world_nether` - specifying the context at the end of the command.

___

Contexts can be combined with each other to form so called "context sets" - simply a collection of context pairs.

Context sets exist in two places:

* LuckPerms internally will calculate what it deems to be a **players** "current context set" - in other words, the contexts which the player currently satisfies. If the player is in the `world_nether` world, then their current context set will contain the `world=world_nether` context.  
It's important to point out that players that are currently offline won't have any context set. You can see this by using the `/lp user <user> info` command and check the "Has contextual data" option on the bottom of the output.

* **Each permission, parent/group, prefix/suffix/meta setting** also has it's own context set - indicating the contexts a player must have for the respective permission/parent/meta value to apply.

Crucially, for a permission/parent/meta value to apply, the player must satisfy **all** of the contexts required by the value. (when I say satisfy, I mean their current context set must contain all of the contexts required by the value - or mathematically, the players context set must be a subset of the value's context set)

___

### Contexts provided by LuckPerms
The context system is designed to be extensible - the system should not (and is not!) confined to only a few types of contexts.

With that said, LuckPerms provides by default, two contexts of it's own. Other plugins are also able to provide their own contexts by registering a `ContextCalculator` in the API.

| Context Key | Description | Example |
|-------------|-------------|---------|
| `server`    | The player's current server. This value is determined by the **server** setting at the very top of the LuckPerms config file. | `server=survival` |
| `world`    | The player's current world - this value is just retrieved from the server. When LuckPerms runs on a BungeeCord/Velocity proxy, the world context value refers to the subserver the player is currently connected to. | `world=world_nether` |
| `proxy`    | This context is only applied when LuckPerms is running on a BungeeCord proxy with RedisBungee installed. It refers to the proxy the player is currently connected to. | `proxy=redisbungee1` |

___

### Defining your own contexts
In addition to the contexts provided by LuckPerms, it is also possible to add extra contexts of your own.

Contexts can either be provided **statically** or **dynamically**.

* **Static contexts** are contexts which are given equally to all players - all players satisfy the context with the same value. (for example, the "server" context - all players get the same key & value) Static contexts can either be defined in a special config file or via the API.
* **Dynamic contexts** are given depending on a certain factor, and have to be registered by a plugin using the API.

#### Defining static contexts
Static contexts can be defined in the `contexts.json` file within the `/LuckPerms/` plugin directory. (in the same folder as the main config)

The file contains two properties, but we're only interested in the one called `static-contexts`.

For example, if we wanted to add our own context called `"server-type"`, to indicate the server type in addition to the server name (which would've already been provided by LuckPerms), simply add:

```json
{
  "static-contexts": {
    "server-type": "skyblock"
  },
}
```

Once added, we can use the `server-type` context when defining permissions/parents/meta to limit those values to specific server types. e.g. `/lp user Luck parent add donor server-type=skyblock`.

You can add as many contexts as you like to this file.

### Default Contexts
Default contexts allow you to specify contexts that are applied to commands if you don't add contexts to the end of the command - for example `/lp user Luck permission set example.permission`. You can define them in the `contexts.yml` file, in the same folder as the main config.

For example, to add a default context to the file, simply add, below the static-contexts section:

```json
{
 "default-contexts": {
    "world": "world_nether",
    "server": "survival"
  }
}
```

This would mean that, for `/lp` commands on the server which you've added the default context, any commands that can be performed with a context will use `world=world_nether,server=survival` unless you specify otherwise.
