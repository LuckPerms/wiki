In order to deliver its functionality, LuckPerms will under some circumstances make connections with and communicate with external services outside of the local server.

A number of 3rd party libraries are also used by the plugin.


## 3rd party software
LuckPerms utilises some software written by 3rd parties to provide it's functionality.   
Each respective software, along with its homepage, usage in LuckPerms, licence, and maintainer are documented below.

| Name & Link | Maintainer | Usage | License |
|-------------|------------|-------|---------|
| Google Guava <br> https://github.com/google/guava | Maintained by Google https://github.com/google | This is included in the jar file for *Bukkit-Legacy*, and provided by the Minecraft server on all other platforms. Provides a number of utilites used throughout the plugin | Apache License 2.0 https://github.com/google/guava/blob/master/COPYING |
| Google Gson <br> https://github.com/google/gson | Maintained by Google https://github.com/google | This is included in the jar file for *Bukkit-Legacy*, and provided by the Minecraft server on all other platforms. Used for reading/writing JSON data | Apache License 2.0 https://github.com/google/gson/blob/master/LICENSE |
| Caffeine cache <br> https://github.com/ben-manes/caffeine | Maintained by Ben Manes https://github.com/ben-manes | Downloaded at runtime. Caching utility | Apache License 2.0 https://github.com/ben-manes/caffeine/blob/master/LICENSE |
| text <br> https://github.com/KyoriPowered/text | Maintained by kashike/KyoriPowered https://github.com/KyoriPowered | Included in the plugin jar. Used for constructing text messages | MIT License https://github.com/KyoriPowered/text/blob/master/license.txt |
| Okio <br> https://github.com/square/okio | Maintained by square https://square.github.io/ | Downloaded at runtime. | Apache License 2.0 https://github.com/square/okio/blob/master/LICENSE.txt |
| OkHttp <br> https://square.github.io/okhttp/ | Maintained by square https://square.github.io/ | Downloaded at runtime. | Apache License 2.0 https://github.com/square/okhttp/blob/master/LICENSE.txt |
| ASM <br> http://asm.ow2.org/ | Maintained by OW2 https://www.ow2.org/ | Downloaded at runtime. Used to process downloaded dependencies | BSD 3-Clause License |
| jar-relocator <br> https://github.com/lucko/jar-relocator | Maintained by Luck (that's me!) https://github.com/lucko | Downloaded at runtime. Used to process downloaded dependencies | Apache License 2.0 https://github.com/lucko/jar-relocator/blob/master/LICENSE.txt |
| MariaDB Java Driver <br> https://github.com/MariaDB/mariadb-connector-j | Maintained by MariaDB https://mariadb.org/ | Downloaded at runtime if needed. Used to interact with the storage database | GNU Lesser General Public License v2.1 https://github.com/MariaDB/mariadb-connector-j/blob/master/LICENSE |
| MySQL Java Driver <br> https://dev.mysql.com/downloads/connector/j/ | Maintained by Oracle Corporation https://www.mysql.com/ | Downloaded at runtime if needed. Used to interact with the storage database | GNU General Public License v2.0 https://github.com/mysql/mysql-connector-j/blob/release/5.1/COPYING |
| PostgreSQL Java Driver <br> https://jdbc.postgresql.org/ | Maintained by PostgreSQL https://www.postgresql.org/ | Downloaded at runtime if needed. Used to interact with the storage database | BSD 2-clause License https://github.com/pgjdbc/pgjdbc/blob/master/LICENSE |
| H2 Database <br> http://www.h2database.com/ | Maintained by h2database https://github.com/h2database | Downloaded at runtime if needed. Used as a storage database | Mozilla Public License Version 2.0 or EPL 1.0 http://www.h2database.com/html/license.html |
| SQLite Database <br> https://github.com/xerial/sqlite-jdbc | Maintained by xerial https://github.com/xerial | Downloaded at runtime if needed. Used as a storage database | Apache License 2.0 https://github.com/xerial/sqlite-jdbc/blob/master/LICENSE |
| MongoDB Java Driver <br> https://mongodb.github.io/mongo-java-driver/ | Maintained by MongoDB https://www.mongodb.com/ | Downloaded at runtime if needed. Used to interact with the storage database | Apache License 2.0 https://github.com/mongodb/mongo-java-driver/blob/master/LICENSE.txt |
| HikariCP <br> https://github.com/brettwooldridge/HikariCP | Maintained by Brett Wooldridge https://github.com/brettwooldridge | Downloaded at runtime if needed. Used to manage connections with MySQL/MariaDB/PostgreSQL databases | Apache License 2.0 https://github.com/brettwooldridge/HikariCP/blob/dev/LICENSE |
| SLF4J <br> https://github.com/qos-ch/slf4j | Maintained by SLF4J https://www.slf4j.org/ | Downloaded at runtime if needed. Used by Hikari for logging. | MIT License https://github.com/qos-ch/slf4j/blob/master/LICENSE.txt |
| configurate <br> https://github.com/zml2008/configurate | Maintained by zml https://github.com/zml2008 | Downloaded at runtime if needed. Used to interact with flatfile storage types (yaml, json and hocon) | Apache License 2.0 https://github.com/zml2008/configurate/blob/master/LICENSE |
| Jedis <br> https://github.com/xetorthio/jedis | Maintained by Jonathan Leibiusky https://github.com/xetorthio | Downloaded at runtime if needed. Used to interact with the redis server | MIT License https://github.com/xetorthio/jedis/blob/master/LICENSE.txt |
| Apache Commons Pool <br> https://commons.apache.org/proper/commons-pool/ | Maintained by Apache https://www.apache.org/ | Downloaded at runtime if needed. Used by Jedis to pool Redis connections | Apache License 2.0 https://github.com/apache/commons-pool/blob/master/LICENSE.txt |


## External Services
In order to deliver it's functionality, LuckPerms will under some circumstances make connections with and communicate with external services outside of the local server.

### `Downloading dependencies`
The dependencies outlined above where stated, are downloaded from the following
locations when LuckPerms first loads. The downloaded binaries are cached locally.

- https://repo1.maven.org/maven2/

On subsequent startups, if the cache files are intact, no communications are attempted.

When downloaded, the binaries are hashed and compared with expected checksums to validate the integrity of the file. This prevents malicious code from being executed in the event that the download servers become compromised.

### `Verbose / Tree pastebin functionality`
LuckPerms includes functionality which allows for data to be viewed inside of
GitHub's Gist pastebin service.

The uploaded data is posted "anonymously" and in "secret" mode. See here for more.
https://help.github.com/articles/about-gists/#secret-gists

When these features are used, LuckPerms will communicate and post data to the following endpoints.

- https://api.github.com/gists/ (used to create gists)
- https://git.io/ (used to shorten the gist's url)

### `Editor functionality`
LuckPerms includes functionality which allows for permission data to be viewed inside of
a web editor.

The uploaded data is posted "anonymously" and in "secret" mode. See here for more.
https://help.github.com/articles/about-gists/#secret-gists

When this functionality is used, LuckPerms will communicate and post data to the following endpoints.

- https://api.github.com/gists/ (used to create & read gists)
- https://gist.githubusercontent.com/ (used to read the content of a given gist)


The editor page itself at https://lpedit.lucko.me is hosted by GitHub pages, and proxied via CloudFlare. The server itself never attempts any communication with the site. Communication is performed using isloated data payloads hosted by GitHub Gist.

I (Luck) do not host, control or ever come into contact with any uploaded content.

### `Metrics and auto-updaters`

* LuckPerms **does not** and never will report back to analytics or monitoring services.
* LuckPerms **does not** and never will automatically check for (or automatically install 😠) updates. 