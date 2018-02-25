### Summary
The tl;dr is...

* LuckPerms uses the servers internet connection to securely download required libraries when it first starts
* LuckPerms will send data to a remote server in order to provide certain functions - but never for metrics or monitoring purposes
* LuckPerms uses a number of libraries written by 3rd parties - reinventing the wheel is (usually? sometimes??) bad

For clarity, the nature of these interactions and usages are documented below. 

> Understandably, some server admins are particularly careful about the plugins they install on their server.   
> For example, "using the internet to download and execute binaries" may scream of [arbitrary code execution](https://en.wikipedia.org/wiki/Arbitrary_code_execution) when read by some people. I want to emphasize that I hear your cries - and have tried to implement these features securely and responsibly.

___

### Downloading libraries

LuckPerms makes use of a lot of libraries - all of which are listed at the end of this page.

The plugin can be configured and used in a number of ways. For example, it supports a number of storage methods, each of which require their own set of drivers. Most plugins simply bundle (or "shade") these libraries into the plugin jar file - however, this is not practical for LuckPerms, as the high number of libraries would produce a huge final jar size. The solution is to download the *required* libraries at runtime, depending on the configuration being used.

##### The download process

* Downloads will only be attempted for libraries which are required
* Downloaded binaries are cached in the `/LuckPerms/lib/` folder after the initial download. If a library is already present here, a connection to the download server will not be attempted.
* The URL and version of libraries is hardcoded within the plugin - they will never automatically update.

All libraries are downloaded from https://repo1.maven.org/maven2/ - a public software repository commonly referred to as the "Central Repository" or "Maven Central".

This site is a trustworthy source - it is used by most Java developers and open source projects.

In the extreme event that the site is compromised, and as a precautionary measure, LuckPerms will perform additional verification during the download process to ensure that libraries are intact and as expected. 

Before being saved to disk, the binary data is hashed and compared against expected checksums to validate the integrity of the file. This prevents malicious code from being executed in the event that the download servers become compromised.

___

### Web editor / Verbose viewer / Tree viewer functionality

* **Web Editor** - A web based permissions editor for data stored in the plugin.
* **Verbose Viewer** - A web based viewer for verbose recording logs.
* **Tree Viewer** - A web based viewer to visualise tree permission structures.

The clients for each of these applications can be found at

* https://luckperms.github.io/editor/
* https://luckperms.github.io/verbose/
* https://luckperms.github.io/treeview/

respectively. 

These sites are hosted and published using [GitHub Pages](https://pages.github.com/). They are not backed by a special web server. All dynamic functionality is provided using client-side JavaScript.

The source code for these sites is freely available here: https://github.com/lucko/LuckPermsWeb

Communication between the editors/viewers and the plugin (which runs on your MC server) is performed using isolated data payloads.

There is never any direct communication between the editors/viewers and the server. You can freely share the links to editor sessions - changes must be applied by running a command on the MC server.

Data is posted to & read from https://bytebin.lucko.me/ - effectively a very simple pastebin API.   
This is (currently) hosted by me (Luck) using DigitalOcean & CloudFlare.

Again, the source is freely available here: https://github.com/lucko/bytebin

Posted data is retained for 24 hours and then deleted.

___

### Metrics and auto-updaters

* LuckPerms **does not** and never will report back to analytics or monitoring services.
* LuckPerms **does not** and never will automatically check for (or automatically install 😠) updates. 

___

### 3rd party software
LuckPerms utilises some software written by 3rd parties to provide it's functionality.   
Each respective software, along with its homepage, maintainer, usage in LuckPerms, and licence is documented below.

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
