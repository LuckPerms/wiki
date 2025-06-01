Extensions are a way to "bolt on" additional functionality to the plugin. Extensions work independently of the platform LuckPerms is running on (i.e. Bukkit, Sponge, etc) and can therefore be installed in the same way on all platforms. They use the native API provided by the plugin.

They're essentially "plugins for a plugin" - a bit confusing, and maybe overkill - but it seems to be a good solution to me!

___

### Installing extensions

Extensions come in the form of `.jar` files. To install them:

1. Navigate to the main `/LuckPerms/` folder (the one where `config.yml` is.)
2. Create a sub-folder called `extensions`
3. Add the extension `.jar` file to the extensions folder.
4. Restart the server.

___

## Official extensions

### REST API

See [here](Standalone-and-REST-API) for info. :)

### Deprecated extensions

The extensions below were released approximately 6 years ago (as of June 2025) to help ease the upgrade burden from LuckPerms v4 to LuckPerms v5. We now consider that users have had long enough to update, and they are now deprecated and no longer supported.

* [extension-legacy-api](https://github.com/LuckPerms/extension-legacy-api)
* [extension-default-assignments](https://github.com/LuckPerms/extension-default-assignments)
