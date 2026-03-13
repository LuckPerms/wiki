LuckPerms has a number of online editors / viewers built into the plugin. The interfaces have been designed such that individual users/servers do not need to host their own instances, and public versions everyone can use are deployed in the following locations:

* https://luckperms.net/editor/
* https://luckperms.net/verbose/
* https://luckperms.net/treeview/

There is occasionally some interest in self-hosting. In general, **we do not recommend doing this**, but since the code is open-source, suitably experienced admins are welcome to have a go. The following notes serve as a starting point.

You will also need to sort out:

* a Linux server for hosting
* a domain
* setting up DNS records
* TLS certificates

etc. and all of the fun things that go along with the above, like: patching, maintenance, security.

___

### Deploy LuckPermsWeb stack on a server

On a server:

```bash
git clone git@github.com:LuckPerms/LuckPermsWeb.git
cd LuckPermsWeb
docker compose up -d
```

will expose the interface on port `8080`.

At this point, you should be able to access the UI at `http://<your server ip>:8080/` - but this isn't very secure, so the next step is probably to put this app behind a reverse proxy (e.g. NGINX), then configure a domain + DNS, then TLS certificates. All of this is beyond the scope of this guide.


### Configuring the plugin to use your custom stack

Assuming, for example, your stack is hosted and available at `https://luckperms.yourdomain.com/`:

Add the following to the end of the LuckPerms `config.yml`.


```yml
bytebin-url: https://luckperms.yourdomain.com/data/
bytesocks-url: https://luckperms.yourdomain.com/ws/

web-editor-url: https://luckperms.yourdomain.com/editor/
verbose-viewer-url: https://luckperms.yourdomain.com/verbose/
tree-viewer-url: https://luckperms.yourdomain.com/treeview/
```
