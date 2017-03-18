LuckPerms comes with a variety of Storage options to choose from.

The storage option can be modified in the `config.yml` or `luckperms.conf` file.
```yaml
# +------------------------------------------------------------------------+ #
# |                               Storage                                  | #
# +------------------------------------------------------------------------+ #

# Which storage method the plugin should use.
# Currently supported: mysql, postgresql, sqlite, h2, json, yaml, mongodb
# Fill out connection info below if you're using MySQL, PostgreSQL or MongoDB
storage-method: h2
```

Remember that if you switch storage type, your data will not be automatically transferred. To manually move data between storage providers, please see [here](https://github.com/lucko/LuckPerms/wiki/Switching-storage-types) for more information.   
   
The available options are outlined below.   
   
## H2 / SQLite
The default storage option is **H2**.   
   
Both are types of file based SQL databases. All data is stored within one file in the LuckPerms folder. The data cannot be easily edited with a text editor, unlike YAML or JSON. The plugin commands must be used to edit or view the data.

If you opt for H2 (the default), all data is stored in the `luckperms-h2.mv.db` file. The file for SQLite is `luckperms-sqlite.db`.

To use either of these options, set:
```yaml
storage-method: h2
# or
storage-method: sqlite
```

## JSON / YAML
JSON and YAML options store data in readable and editable text files. YAML is stored with the `.yml` extension, whereas JSON is stored with `.json`.   
   
The layouts inside of these types are very similar, and only differ in syntax.

##### Example YAML file
```yml
uuid: c1d60c50-70b5-4722-8057-87767557e50d
name: Luck
primary-group: default
perms:
  group.default: true
  test.permission: true
  other.test.permission: false
  special.permission: true
```

##### Example JSON file
```json
{
  "uuid": "c1d60c50-70b5-4722-8057-87767557e50d",
  "name": "Luck",
  "primaryGroup": "default",
  "perms": {
    "group.default": true,
    "test.permission": true,
    "other.test.permission": false,
    "special.permission": true
  }
}
```

To use either of these options, set:
```yaml
storage-method: yaml
# or
storage-method: json
```

## MySQL / PostgreSQL
Data stored in MySQL or PostgreSQL is in the same format as H2/SQLite above, however the data is instead stored on a remote server. This means that the same set of data can be shared by multiple servers.   
   
You will need to input the address, port, database, username and password values for your database server into the configuration file.   
   
This option is recommended for users expecting to store a lot of data, or thinking about expanding into a network of servers. If you are already running multiple servers and want to sync data between them, then this option is a must.   
   
The schema layouts can be found [here](https://github.com/lucko/LuckPerms/tree/master/common/src/main/resources).

To use either of these options, set:
```yaml
storage-method: mysql
# or
storage-method: postgresql
```

## MongoDB
LuckPerms also supports MongoDB, which is a remote database, somewhat similar to MySQL. This option is only likely to be used by a small proportion of users.

To use this option, set:
```yaml
storage-method: mongodb
```