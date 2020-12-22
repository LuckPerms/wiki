## How to
Switching datastores is easy.

1. Firstly, run `/luckperms export <file>`
2. Then, stop your server completely.
3. Edit your config file and change the storage type.
4. Now, start your server again. Let the new datastore initialise.
5. Then, run `/luckperms import <file>`
6. All of your data should have been moved to the new datastore.

\<file\> is the name of the file that you want to save to/load from. The file will/must be located in the LuckPerms data folder. You can call it whatever you like in the export command (e.g. `data`) - but you obviously need to use the same name when you re-import it.

## Web Exporting

1. Run `/luckperms export --upload`
2. Take the 10 digit code that it gives you and save it somewhere.
3. Completely stop the server
4. Edit your config file and change the storage type.
5. Run `/luckperms import <10 digit code> --upload`
6. All of your data should be moved to the new datastore

## Backups
You can also use this feature to backup all of your LuckPerms data. Just run the export command, and save the file output in a safe place. Note that the `--upload` variant of the webexport command will expire and as such is likely not the ideal method for backup storage.

