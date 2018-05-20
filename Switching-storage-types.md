## How to
Switching datastores is easy.

1. Firstly, run `/luckperms export <file>`
2. Then, stop your server completely.
3. Edit your config file and change the storage type.
4. Now, start your server again. Let the new datastore initialise.
5. Then, run `/luckperms import <file>`
6. All of your data should have been moved to the new datastore.

\<file\> is the name of the file that you want to save to/load from. The file will/must be located in the LuckPerms data folder. You can call it whatever you like in the export command (e.g. `data.txt`) - but you obviously need to use the same name when you re-import it.

## Backups
You can also use this feature to backup all of your LuckPerms data. Just run the export command, and save the file output in a safe place.

## How does it work?
The export command converts all of your data into a list of commands, than when executed, will recreate your existing setup. The import command just runs each command sequentially. This means that you can export/import small parts of your data, by deleting the parts you don't need.

