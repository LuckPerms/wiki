### Summary
The tl;dr is...

* LuckPerms uses the servers internet connection to securely download required libraries when it first starts
* LuckPerms will send data to a remote server in order to provide certain functions - but never for metrics or monitoring purposes
* LuckPerms does not report to metrics or analytics services

The specific nature of these interactions and usages are documented below.

___

### Downloading libraries

LuckPerms makes use of a lot of libraries - all of which are listed [here](https://github.com/lucko/LuckPerms/wiki/Credits).

The plugin can be configured and used in a number of ways. For example, it supports a number of storage methods, each of which require their own set of drivers. Most plugins simply bundle (or "shade") these libraries into the plugin jar file - however, this is not practical for LuckPerms, as the high number of libraries would produce a huge final jar size. The solution is to download the *required* libraries at runtime, depending on the configuration being used.

##### The download process

* Downloads will only be attempted for libraries which are required
* Downloaded binaries are cached in the `/LuckPerms/lib/` folder after the initial download. If a library is already present here, a connection to the download server will not be attempted.
* The URL and version of libraries is hardcoded within the plugin - they will never automatically update.

All libraries are downloaded from https://repo1.maven.org/maven2/ - a public software repository commonly referred to as the "Central Repository" or "Maven Central".

This site is a trustworthy source - it is used by most Java developers and open source projects.

In the extreme event that the site is compromised, and as a precautionary measure, LuckPerms will perform additional verification during the download process to ensure that libraries are intact and as expected. 

##### The verification process

Each dependency that can be downloaded at runtime, along with it's version and location within Maven Central is defined in [this source code file](https://github.com/lucko/LuckPerms/blob/master/common/src/main/java/me/lucko/luckperms/common/dependencies/Dependency.java) in LuckPerms.

Each entry also includes a SHA-256 hash of the dependency file, at the time the release was first included within LuckPerms. This hash is used as a checksum for downloaded files.

When a dependency is downloaded from the repository, the same hashing process is performed on the downloaded data, and the hash of this is compared with the checksum of the dependency.

The integrity of the downloaded file can be assumed to be ok if the two hashes are equal. If the hashes are not equal, then one of twothings has most likely happened:

* Only a part of the file has been downloaded, something went wrong in the download process
* The dependency file has been tampered with in some way, and should not be trusted

In both cases, the downloaded binary data is discarded by LuckPerms, and the plugins startup is cancelled.

These checks are put in place to minimise the risk of malicious code from being executed should the download servers become compromised. It effectively eliminates the possibility of [arbitrary code execution](https://en.wikipedia.org/wiki/Arbitrary_code_execution) taking place, and makes the system just as secure as shading the dependencies directly into the jar.

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
