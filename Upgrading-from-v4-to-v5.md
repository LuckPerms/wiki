The upgrade from LuckPerms v4 to LuckPerms v5 is fairly significant - most notably:

* A new developer API has been implemented.
* A brand new version of the web editor has been introduced.
* A number of features have been rewritten internally to be easier to understand and maintain going forward.

There's still much more to come with this update - but in order to allow users to start making the most of all of the shiny new features, we've decided to release it now.

___

### Before updating...
**Please please please make backups of your data.**

### API compatibility

If you have any plugins which use the previous version of the LuckPerms API, these plugins will likely stop working after the update.

You have two options for fixing this:

1. Ask the author of the plugin to update to support the new API version. (preferred)
2. Install the `extension-legacy-api` extension.

#### Installing the extension
1. Go to your main `/LuckPerms/` folder. (this is probably at `/plugins/LuckPerms`)
2. Create a folder within this directory called `extensions`.
3. Download [`extension-legacy-api.jar`](https://ci.lucko.me/job/extension-legacy-api/lastSuccessfulBuild/artifact/build/libs/extension-legacy-api-1.0.0.jar) and put it in the extensions folder.
4. Restart your server.

### Other

If you previously made use of "default assignments" (last section in the config file), you'll need to [install the `extension-default-assignments` extension](Extensions), and consider migrating away from the feature.
