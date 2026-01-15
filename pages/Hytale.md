
There is an **early beta / experiemental** version of **LuckPerms for [Hytale](https://hytale.com/)** available to [download from CurseForge](https://www.curseforge.com/hytale/mods/luckperms). This is the same LuckPerms you know and (maybe/hopefully) love from Minecraft, ported across and integrated with Hytale! 🎉

At time of writing, it is still very early days and a lot of things are unknown and uncertain. Hytale has quite a lot of modding capability, but there is a limited amount of official documentation and guidance.

LuckPerms for Hytale is built on top of the same common codebase as the other LuckPerms plugin/mods, but its integration with the server is not as stable. **You have been warned! There will be bugs! 🐞**

## FAQs

### Built-in permission system

When LuckPerms is installed, the built-in Hytale permission system is largely replaced. This is subject to change, but it's the approach we've gone with for now.

This means:

* The built-in `/op` command will not work. It should tell you if you try to use it! Use LuckPerms to configure permissions instead.
* The built-in `/perm` command will not work. You must use the LuckPerms `/lp` commands to configure permissions.

LuckPerms attempts to maintain compatibility with other mods checking permissions via `CommandSender#hasPermission` or `PermissionsModule#hasPermission`, but the other methods in `PermissionsModule` probably will not work as you expect (for now...).

### Finding permissions / troubleshooting 

If you don't know the permissions associated with a given command or feature, use the LuckPerms verbose feature! See the [Verbose](Verbose) wiki page for details.


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

This functionality is only intended for simple chat formatting needs. For more advanced chat formatting, we recommend using a dedicated chat plugin that integrates with LuckPerms.

The message format string supports the following placeholders:

* `<prefix>` is the players prefix meta value
* `{username>` is the players username
* `<suffix>` is the players suffix meta value
* `<message>` is the actual chat message sent by the player

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

### Known caveats/issues

Known caveats/issues are listed on the [Hytale pull request in the LuckPerms GitHub repo](https://github.com/LuckPerms/LuckPerms/pull/4213). If you're having issues or notice something missing, please check there to see if it's already known about and being worked on. :)

### Other

Please come and chat with us in [Discord](https://discord.gg/luckperms) for help. There is a dedicated channel for Hytale questions.