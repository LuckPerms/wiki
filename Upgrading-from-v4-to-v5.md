The upgrade from LuckPerms v4 to LuckPerms v5 is fairly significant - most notably:

* A new developer API has been implemented.
* A brand new version of the web editor has been introduced.
* A number of features have been rewritten internally to be easier to understand and maintain going forward.

There's still much more to come with this update - but in order to allow users to start making the most of all of the shiny new features, we've decided to release it now.

___

### Before updating...
**Please please please make backups of your data.**

It should be fairly stable, but this release (at the moment) has received significantly less testing than previous releases.

### API compatibility

If you have any plugins which use the native LuckPerms API, these plugins will likely stop working after the update.

You have two options for fixing this:

1. Ask the author of the plugin to update to support the new API version. (preferred)
2. Install the `extension-legacy-api` extension. More details available [here](https://github.com/lucko/LuckPerms/wiki/Extensions).

### Other

If you previously made use of "default assignments" (last section in the config file), you'll need to [install the `extension-default-assignments` extension](https://github.com/lucko/LuckPerms/wiki/Extensions), and consider migrating away from the feature.
