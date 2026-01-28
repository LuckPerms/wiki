
There is an **early beta** version of **LuckPerms for [Hytale](https://hytale.com/)** available from our [downloads page](https://luckperms.net/download). This is the same LuckPerms you know and (maybe/hopefully) love from Minecraft, ported across and integrated with Hytale! 🎉

At time of writing, it is still very early days and a lot of things are unknown and uncertain. Hytale has quite a lot of modding capability, but there is a limited amount of official documentation and guidance.

LuckPerms for Hytale is built on top of the same common codebase as the other LuckPerms plugin/mods, but its integration with the server is not as stable. **You have been warned! There will be bugs! 🐞** However, we believe that basing the Hytale version of LuckPerms on top of the same core code as the well-proven Minecraft versions should enable us to make things very stable, quite quickly!

## FAQs

* [I've never used LuckPerms before! How do I get started?](#ive-never-used-luckperms-before-how-do-i-get-started)
* [OP doesn't work anymore!](#op-doesnt-work-anymore)
* [Compatibility with other mods/plugins](#compatibility-with-other-modsplugins)
* [Finding permissions and troubleshooting](#finding-permissions-and-troubleshooting)
* [Chat formatting](#chat-formatting)
* [Integrating with the LuckPerms API](#integrating-with-the-luckperms-api)
* [Known caveats/issues](#known-caveatsissues)

### I've never used LuckPerms before! How do I get started?

Hello and welcome!

There is lots of useful information here on the wiki. Thankfully, the Hytale edition of LuckPerms behaves mostly the same as the Minecraft editions, so everything that has been written before is still relevant. Yay!

If you've never used a permissions plugin before, we suggest you just start at the top and work your way down!

* The basics of permissions are covered in detail in the [Getting Started](Usage) page.
* A more to the point command reference can be found in the [Command Usage](Command-Usage) subpages.

### OP doesn't work anymore!

When LuckPerms is installed, the built-in Hytale permission system is largely replaced. This is so LuckPerms can intercept and handle permissions checks for players.

This means that:

* The built-in `/op` command will not work as expected. Use LuckPerms to configure permissions instead.

* The built-in `/perm` command will not work as expected. You must use the LuckPerms `/lp` commands to configure permissions for players.

If you want to replicate OP-like functionality (full access to **all** commands, features, etc), you can use the following LuckPerms commands:

* `/lp user <user> permission set *` - give `<user>` all permissions
* `/lp group <group> permission set *` - give any user in `<group>` all permissions (e.g. you may want to do this for your "admin" or "owner" group)

### Compatibility with other mods/plugins

LuckPerms attempts to maintain compatibility with other mods checking permissions via `CommandSender#hasPermission` or `PermissionsModule#hasPermission`, but the other methods in `PermissionsModule` probably will not work as you expect.

By default, LuckPerms will delegate permission checks for non-Player entities to the built-in Hytale permissions system. This means that you *can* use the built-in `/perm` commands to configure permissions for **non-Player** NPCs, "service accounts", or the Nitrado "anonymous" user. Player permissions **must** be configured through LuckPerms.

LuckPerms has a built-in chat formatter that is enabled by default (see below for more info). If you want to use LuckPerms prefixes or suffixes in chat messages, we recommend that you leave it enabled and disable chat formatting functionality in any other mods you may have installed. :)

### Finding permissions / troubleshooting

If you don't know the permissions associated with a given command or feature, use the LuckPerms verbose feature! See the [Verbose](Verbose) wiki page for details.

You can also use the built-in `/help` command, which will bring up a UI listing available commands and their corresponding permissions.


### Chat formatting

Unlike LuckPerms on other platforms, LuckPerms for Hytale includes a basic, built-in, chat formatter. It is enabled by default.

It can be configured with the following settings in the LuckPerms `config.yml` file:

```yml
# Configuration for the built-in LuckPerms chat formatter.
chat-formatter:

  # If LuckPerms should handle chat formatting.
  enabled: true

  # The format to use.
  message-format: "<prefix><username><suffix>: <message>"
```

The message format string supports the following placeholders:

* `<prefix>` is the player's **prefix** meta value
* `<username>` is the player's **username**
* `<suffix>` is the player's **suffix** meta value
* `<message>` is the **chat message** sent by the player

The format string, as well as the prefix and suffix values support formatting using [MiniMessage](https://docs.papermc.io/adventure/minimessage/format/). (Yes, this is a Minecraft format, but it's good and it was easier to reuse it!)

Formatting from the prefix and suffix will intentionally "*spill over*" into subsequent parts of the format.

Some examples:

| Command                                                                                           | Result                        |
|---------------------------------------------------------------------------------------------------|-------------------------------|
| `/lp user lucko meta setprefix 10 "<red>[ADMIN] "`                                                | ![](../img/hytale-chat-1.png) |
| `/lp user lucko meta setprefix 10 "<red>[ADMIN]</red> "`<br>(note the close `</red>` tag).        | ![](../img/hytale-chat-2.png) |
| `/lp user lucko meta setprefix 10 "<red>[ADMIN] "`<br>`/lp user lucko meta setsuffix 10 "<gray>"` | ![](../img/hytale-chat-3.png) |


Hopefully you get the idea. For more information:

* [Prefixes, Suffixes & Meta](Prefixes,-Suffixes-&-Meta) (LP wiki)
* [MiniMessage format](https://docs.papermc.io/adventure/minimessage/format/) (PaperMC docs)

The built-in functionality is only intended for simple chat formatting and likely will not be enhanced further. For more advanced chat formatting, we recommend using a dedicated chat plugin that integrates with LuckPerms (although we aren't aware of any that exist, yet!).

### Integrating with the LuckPerms API

We have created a basic example plugin which demonstrates how to access the LuckPerms API from a Hytale plugin.

[https://github.com/LuckPerms/api-cookbook-hytale](https://github.com/LuckPerms/api-cookbook-hytale)

The key things are:

#### 1) Declare LuckPerms as a dependency or optional dependency

In your plugin `manifest.json`, you must include either:

```json
{
  "Dependencies": {
    "LuckPerms:LuckPerms": "*"
  }
}
```

or

```json
{
  "OptionalDependencies": {
    "LuckPerms:LuckPerms": "*"
  }
}
```

This is because Hytale's plugin manager isolates classloaders between plugins, except if a dependency is declared.

#### 2) Obtain the API instance from JavaPlugin.start() or later

LuckPerms performs it's final initialisation during the "start" phase, it is **not** ready during the "setup" phase.

```java
  @Override
  protected void setup() {
    // doesn't work! ❌
    LuckPerms luckPerms = LuckPermsProvider.get();
  }

  @Override
  protected void start() {
    // works! ✅
    LuckPerms luckPerms = LuckPermsProvider.get();
  }
```

#### 3) PlayerAdapter and ContextManager expect `PlayerRef`

Methods in the LuckPerms API that expect a "player" object need to be passed a `PlayerRef`, **not** a `Player`.

For example:

```java
// PlayerAdapter is a convenience class for converting
// between Hytale's PlayerRef and LuckPerms' User objects
PlayerAdapter<PlayerRef> playerAdapter = LuckPermsProvider.get().getPlayerAdapter(PlayerRef.class);

User user = playerAdapter.getUser(playerRef);
CachedPermissionData permissionData = playerAdapter.getPermissionData(playerRef);
CachedMetaData metaData = playerAdapter.getMetaData(playerRef);

// Get the players prefix, for example :)
String prefix = metaData.getPrefix();
```


### Known caveats/issues

Known caveats/issues are listed on the [Hytale pull request in the LuckPerms GitHub repo](https://github.com/LuckPerms/LuckPerms/pull/4213). If you're having issues or notice something missing, please check there to see if it's already known about and being worked on. :)

### Other

Please come and chat with us in [Discord](https://discord.gg/luckperms) for help. There is a dedicated channel for Hytale questions.