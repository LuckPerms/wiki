LuckPerms has a number of online editors / viewers built into the plugin. These do not require self hosting, and public versions everyone can use are deployed in the following locations:

* https://luckperms.net/editor/
* https://luckperms.net/verbose/
* https://luckperms.net/treeview/
* https://bytebin.lucko.me/

However, we appreciate there is some interest in self hosting these sites, to allow for customisation or implementing custom behaviour. It's not really something we recommend doing (there's not much to gain from it) - but alas, here are the details.

This guide assumes the user has some previous technical knowledge of setting up (web) applications on Linux server machines.

___

### Step 1: Installing bytebin

The first thing you'll need to do is install and configure a copy of bytebin. This is the system that allows for data to be transferred between the LuckPerms plugin and your web browser (when using the sites).

If you only want to customise the interfaces, you can skip this step, but if you want to totally self-host the whole system, this is necessary.

The source code for bytebin is at https://github.com/lucko/bytebin - you can compile it using [Maven](https://maven.apache.org/) with `mvn clean package` - the jar will be in `/target/`.

Alternatively, you can download a pre-compiled binary here: https://ci.lucko.me/job/bytebin/

```bash
mkdir bytebin
cd bytebin
curl -O https://ci.lucko.me/job/bytebin/lastSuccessfulBuild/artifact/target/bytebin.jar
touch config.json
```

Then open the newly created `config.json` file with your favourite text editor, and add the following entries.

```json
{
  "host": "127.0.0.1",
  "port": 8080,
  "keyLength": 10,
  "lifetimeMinutes": 10080,
  "maxContentLengthMb": 10
}
```

`host` and `port` are what the instance will listen on. `keyLength` is how long the generated data tokens will be. `lifetimeMinutes` is how long content should persist for before being deleted. `maxContentLengthMb` is how large uploaded files are allowed to be.

There are additional configuration variables which define rate limiting for read/write ops, but configuring these is beyond the scope of this guide. The respective variables are accessed [here](https://github.com/lucko/bytebin/blob/bf7b4dc2f8cdfd912b8acd71f0a347da3c481838/src/main/java/me/lucko/bytebin/Bytebin.java#L192-L200).

You'll then most likely want to setup the bytebin instance behind a reverse proxy. Below is an example for [nginx](https://www.nginx.com/).

```nginx
server {
    listen 80;
    listen 443;

    server_name bytebin.example.com;

    client_max_body_size 30M;
    client_body_timeout 60s;

    location / {
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_redirect http:// https://;

        proxy_pass http://127.0.0.1:8080;
    }
}
```

Now, you can run bytebin with `java -jar bytebin.jar` - and the service should be accessible at `https://bytebin.example.com/`.

### Step 2: Installing the site

The source for the web apps is available from GitHub: https://github.com/LuckPerms/LuckPermsWeb

You will need to build and host this site on your web server. You can either use the [automatic setup script](https://github.com/LuckPerms/web-installer#automatic-setup) or [install manually](https://github.com/LuckPerms/web-installer#manual-setup).

### Step 3: Configuring the plugin to use your custom bytebin / site

Add the following to the end of the LuckPerms `config.yml`.

```yml
web-editor-url: 'https://example.com/luckperms/editor/'
verbose-viewer-url: 'https://example.com/luckperms/verbose/'
tree-viewer-url: 'https://example.com/luckperms/treeview/'

# only required if you did Step 1
bytebin-url: 'https://bytebin.example.com/'
```
