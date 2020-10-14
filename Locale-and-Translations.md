### Overview

All in-game messages in LuckPerms can be customised and translated using the translation system.

The base translation file for *English* can be found here: [`luckperms_en.properties`](https://github.com/lucko/LuckPerms/blob/master/common/src/main/resources/luckperms_en.properties)

## Contributing

Translation into other languages is organised on our [Crowdin project](https://crowdin.com/project/luckperms).

We greatly appreciate any help! :heart:

## Using the translated messages

Translations can be loaded into the plugin as follows:

* Create the folder `/plugins/LuckPerms/translations/`
* Export the modified `.properties` file, and rename it to `<locale id>.properties`.
  * A list of the supported locale ids can be found [here](https://www.localeplanet.com/java/)
  * For example, to load translations for *Spanish* use `es.properties`, or for *Portuguese (Brazil)* use `pt_BR.properties`
* Restart the server

Players will be sent messages translated to the language selected in their Minecraft client settings, if possible. If no such translation exists, the built-in English messages are used.
