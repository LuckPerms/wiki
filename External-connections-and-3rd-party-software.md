In order to deliver it's functionality, LuckPerms will under some circumstances make connections with and communicate with external services outside of the local server.

A number of 3rd party libraries are also used by the plugin.


## 3rd party software
LuckPerms utilises some software written by 3rd parties to provide it's functionality.   
Each respective software, along with it's homepage, usage in LuckPerms, licence, and maintainer are documented below.

### `Google Guava`
- https://github.com/google/guava
- This is included in the jar file for *Bukkit-Legacy*, and provided by the Minecraft server on all other platforms.
- Provides a number of utilites used throughout the plugin
- Apache License 2.0 https://github.com/google/guava/blob/master/COPYING
- Maintained by Google https://github.com/google

### `Google Gson`
- https://github.com/google/gson
- This is included in the jar file for *Bukkit-Legacy*, and provided by the Minecraft server on all other platforms.
- Used for reading/writing JSON data
- Apache License 2.0 https://github.com/google/gson/blob/master/LICENSE
- Maintained by Google https://github.com/google

### `Caffeine cache`
- https://github.com/ben-manes/caffeine
- Downloaded at runtime
- Caching utility
- Apache License 2.0 https://github.com/ben-manes/caffeine/blob/master/LICENSE
- Maintained by Ben Manes https://github.com/ben-manes

### `MariaDB Java Driver`
- https://github.com/MariaDB/mariadb-connector-j
- Downloaded at runtime if needed
- Used to interact with the storage database
- GNU Lesser General Public License v2.1 https://github.com/MariaDB/mariadb-connector-j/blob/master/LICENSE
- Maintained by MariaDB https://mariadb.org/

### `MySQL Java Driver`
- https://dev.mysql.com/downloads/connector/j/
- Downloaded at runtime if needed
- Used to interact with the storage database
- GNU General Public License v2.0 https://github.com/mysql/mysql-connector-j/blob/release/5.1/COPYING
- Maintained by Oracle Corporation https://www.mysql.com/

### `PostgreSQL Java Driver`
- https://jdbc.postgresql.org/
- Downloaded at runtime if needed
- Used to interact with the storage database
- BSD 2-clause "Simplified" License https://github.com/pgjdbc/pgjdbc/blob/master/LICENSE
- Maintained by PostgreSQL https://www.postgresql.org/

### `H2 Database`
- http://www.h2database.com/
- Downloaded at runtime if needed
- Used as a storage database
- Mozilla Public License Version 2.0 or EPL 1.0 http://www.h2database.com/html/license.html
- Maintained by h2database https://github.com/h2database

### `SQLite Database`
- https://github.com/xerial/sqlite-jdbc
- Downloaded at runtime if needed
- Used as a storage database
- Apache License 2.0 https://github.com/xerial/sqlite-jdbc/blob/master/LICENSE
- Maintained by xerial https://github.com/xerial

### `MongoDB Java Driver`
- https://mongodb.github.io/mongo-java-driver/
- Downloaded at runtime if needed
- Used to interact with the storage database
- Apache License 2.0 https://github.com/mongodb/mongo-java-driver/blob/master/LICENSE.txt
- Maintained by MongoDB https://www.mongodb.com/

### `HikariCP`
- https://github.com/brettwooldridge/HikariCP
- Downloaded at runtime if needed
- Used to manage connections with MySQL/MariaDB/PostgreSQL databases
- Apache License 2.0 https://github.com/brettwooldridge/HikariCP/blob/dev/LICENSE
- Maintained by Brett Wooldridge https://github.com/brettwooldridge

### `SLF4J`
- https://github.com/qos-ch/slf4j
- Downloaded at runtime if needed
- Used by Hikari for logging.
- MIT License https://github.com/qos-ch/slf4j/blob/master/LICENSE.txt
- Maintained by SLF4J https://www.slf4j.org/

### `Jedis`
- https://github.com/xetorthio/jedis
- Downloaded at runtime if needed
- Used to interact with the redis server
- MIT License https://github.com/xetorthio/jedis/blob/master/LICENSE.txt
- Maintained by Jonathan Leibiusky https://github.com/xetorthio


## External Services
In order to deliver it's functionality, LuckPerms will under some circumstances make connections with and communicate with external services outside of the local server.

### `Downloading dependencies`
The dependencies outlined above where stated, are downloaded from the following
locations when LuckPerms first loads. The downloaded binaries are cached locally.

On subsequent startups, if the cache files are intact, no communications are attempted.

- https://repo1.maven.org/maven2/
- https://github.com/lucko/jedis/releases/

### `Verbose / Tree pastebin functionality`
LuckPerms includes functionality which allows for data to be viewed inside of
GitHub's Gist pastebin service.

The uploaded data is posted "anonymously" and in "secret" mode. See here for more.
https://help.github.com/articles/about-gists/#secret-gists

When these features are used, LuckPerms will communicate and post data to the following endpoints.

- https://api.github.com/gists/
- https://git.io/

### `Editor functionality`
LuckPerms includes functionality which allows for permission data to be viewed inside of
a web editor.

The uploaded data is posted "anonymously" and in "secret" mode. See here for more.
https://help.github.com/articles/about-gists/#secret-gists

When this functionality is used, LuckPerms will communicate and post data to the following endpoints.

- https://api.github.com/gists/
- https://gist.githubusercontent.com/


The editor page itself at https://lpedit.lucko.me is hosted by GitHub pages, and proxied via CloudFlare.

I (Luck) do not host, control or ever come into contact with any content.

### `Metrics`
LuckPerms **does not** and never will report back to analytics services.