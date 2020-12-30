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

### extension-legacy-api
* [Source Code](https://github.com/LuckPerms/extension-legacy-api)
* [Download](https://ci.lucko.me/job/extension-legacy-api/)

An extension for LuckPerms v5, which implements the legacy v4 API.

This allows plugins coded against previous versions of LuckPerms to continue to operate with the newer versions.

This is not a long term solution, it exists merely to reduce some of the update burden on users. Developers are encouraged to update to the new v5 API as soon as possible.


**Event listening**

Only a limited number of events are able to be listened to.

Currently supported:

* `GroupCacheLoadEvent`
* `GroupDataRecalculateEvent`
* `NodeAddEvent`
* `NodeClearEvent`
* `NodeMutateEvent`
* `NodeRemoveEvent`
* `UserCacheLoadEvent`
* `UserDataRecalculateEvent`
* `UserDemoteEvent`
* `UserFirstLoginEvent`
* `UserLoadEvent`
* `UserPromoteEvent`
* `UserTrackEvent`

### extension-default-assignments
* [Source Code](https://github.com/LuckPerms/extension-default-assignments)
* [Download](https://ci.lucko.me/job/extension-default-assignments/)

An extension for LuckPerms v5, which implements the (now removed) default assignments functionality.

This allows users of the old system to update more seamlessly to the newer versions of the plugin.

This is not a long term solution, it exists merely to reduce some of the update burden on users. It is encouraged that users migrate away from this system.

To do so, consider exactly what purpose default assignments are having on your server, and try to find another approach to the problem. We're more than happy to help with ideas etc in the project Discord server.