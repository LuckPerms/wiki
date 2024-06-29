LuckPerms can store its data in a number of ways. These options can be changed in the "Storage Settings" section of the config file.

### Possible options

* **Remote databases** - require connection to a storage server hosted separately
  * MySQL
  * MariaDB (preferred over MySQL)
  * PostgreSQL
  * MongoDB
* **Flatfile/local databases** - don't require any extra setup, they "just work". This format is not easily editable.
  * H2 (preferred over SQLite)
  * SQLite
* **Readable & editable text files**
  * YAML (.yml files)
  * JSON (.json files)
  * HOCON (.conf files)
  * TOML (.toml files)

The default option is `H2`.

#### Remote databases
| Benefits | Drawbacks |
|----------------------------------------------------------------------|-----------------------------------------------|
| Allows data to be shared between multiple servers.                   | Complicated to setup??                        |
| Generally more reliable                                              | Requires extra resources to host the database |
| Can generally handle more data, and supports concurrent reads/writes |                                               |
| Indexed, more efficient when performing bulk queries and updates     |                                               |

#### Flatfile databases
| Benefits                                                         | Drawbacks                                       |
|------------------------------------------------------------------|-------------------------------------------------|
| Generally more reliable and more efficient than editable files   | Not (easily) possible to edit the data directly |
| Indexed, more efficient when performing bulk queries and updates | Sometimes prone to data corruption issues       |
|                                                                  | Data cannot be shared between servers           |

#### Text (config) files
| Benefits | Drawbacks |
|----------|-----------|
| Human readable!                                  | Less efficient use of disk space compared to a flatfile database                     |
| It's possible to edit/inspect the files directly | Difficult to perform bulk queries and updates                                        |
|                                                  | Data cannot be shared between servers                                                |
|                                                  | More prone to corruption due to human error (mistakes when editing the data by hand) |

___

### More details

#### Flatfile/local databases (H2 & SQLite)
* All data is stored within one file in the LuckPerms folder.
* The data cannot be easily edited with a text editor, unlike YAML or JSON.
* The plugin commands must be used to edit or view the data.

With `H2`, all data is stored in the `luckperms-h2.mv.db` file.   
With `SQLite`, all data is stored in the `luckperms-sqlite.db` file.

To use either of these options, set:
```yaml
storage-method: h2
storage-method: sqlite
```

#### Readable & editable text files (YAML / JSON / HOCON / TOML)
* Data is stored in multiple files within the LuckPerms folder.
* The files can be read/edited when the server is running, and changes will be automatically applied.

With `YAML`, data is stored with a `.yml` extension in the `yaml-storage` directory.   
With `JSON`, data is stored with a `.json` extension in the `json-storage` directory.   
With `HOCON`, data is stored with a `.conf` extension in the `hocon-storage` directory.  
With `TOML`, data is stored with a `.toml` extension in the `toml-storage` directory.
   
The layouts inside of these types are very similar, and only differ in syntax.

Some example files are shown at [end of this page](#example-files).

To use either of these options, set:
```yaml
storage-method: yaml
storage-method: json
storage-method: hocon
storage-method: toml
```

#### Remote databases (MySQL / MariaDB / PostgreSQL / MongoDB)
You will need to input the address, port, database, username and password values for your database server into the configuration file.   
   
This option is recommended for users expecting to store a lot of data, or thinking about expanding into a network of servers. If you are already running multiple servers and want to sync data between them, then you need to use a remote database type.   
   
The schema layouts can be found [here](https://github.com/LuckPerms/LuckPerms/tree/master/common/src/main/resources/me/lucko/luckperms/schema).

To use either of these options, set:
```yaml
storage-method: mysql
storage-method: mariadb
storage-method: postgresql
storage-method: mongodb
```

___

### Example files
##### Example YAML file
```yml
uuid: c1d60c50-70b5-4722-8057-87767557e50d
name: Luck
primary-group: default
permissions:
- test.permission:
    value: true
    context:
      server: factions
- negated.permission.example:
    value: false
- special.test.perm
- special.test.permission
parents:
- default
prefixes:
- '&c[Admin] ':
    priority: 10
meta:
- homes:
    value: '10'
```

##### Example JSON file
```json
{
  "uuid": "c1d60c50-70b5-4722-8057-87767557e50d",
  "name": "Luck",
  "primaryGroup": "default",
  "permissions": [
    {
      "permission": "test.permission",
      "value": true,
      "context": {
        "server": "factions"
      }
    },
    {
      "permission": "negated.permission.example",
      "value": false
    },
    {
      "permission": "special.test.perm",
      "value": true
    },
    {
      "permission": "special.test.permission",
      "value": true
    }
  ],
  "parents": [
    {
      "group": "default"
    }
  ],
  "prefixes": [
    {
      "prefix": "&c[Admin] ",
      "priority": 10
    }
  ],
  "meta": [
    {
      "key": "homes",
      "value": "10"
    }
  ]
}
```

##### Example HOCON file
```conf
uuid=c1d60c50-70b5-4722-8057-87767557e50d
name=Luck
primary-group=default
permissions=[
    {
        permission="test.permission"
        value=true
        context {
            server=factions
        }
    },
    {
        permission="negated.permission.example"
        value=false
    },
    {
        permission="special.test.perm"
        value=true
    },
    {
        permission="special.test.permission"
        value=true
    }
]
parents=[
    {
        group=default
    }
]
prefixes=[
    {
        prefix="&c[Admin] "
        priority=10
    }
]
meta=[
    {
        key=homes
        value="10"
    }
]
```

##### Example TOML file
```toml
uuid = "c1d60c50-70b5-4722-8057-87767557e50d"
name = "Luck"
primary-group = "default"

[[permissions]]
  permission = "test.permission"
  value = true

  [permissions.context]
    server = "factions"

[[permissions]]
  permission = "negated.permission.example"
  value = false

[[permissions]]
  permission = "special.test.perm"
  value = true

[[permissions]]
  permission = "special.test.permission"
  value = true

[[parents]]
  group = "default"

[[prefixes]]
  prefix = "&c[Admin] "
  priority = 10

[[meta]]
  key = "homes"
  value = "10"
```
