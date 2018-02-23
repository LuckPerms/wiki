LuckPerms features a web editor, which allows you to make changes to permissions data using a friendly interface in your web browser. It is safe, secure and easy to use. You don't need to host the page yourself - and it works for all storage types!

If you'd like more information about the technical details, see the project's [readme page](https://github.com/lucko/LuckPermsWeb/blob/master/editor/README.md).

___

### Getting started

Editor sessions are first created by executing a command on the server.

##### To create an editor session for all groups and any online users, run
`/lp editor`

##### To create an editor session for all groups, run
`/lp editor users`

##### To create an editor session for all users, run
`/lp editor groups`

##### To create an editor session for a group, run
`/lp group <group> editor`

##### To create an editor session for a user, run
`/lp user <user> editor`

> Remember to use `/lpb` instead of `/lp` if you want to target your command to the BungeeCord version of LP.

Once the command has been executed, the server will begin creating a new session. It should only take a second or so (depending on your connection speed).

Once the session is ready, you will be sent a link.

![](https://i.imgur.com/iqxlldA.png)

To proceed, click on the URL, then press "Yes".

![](https://i.imgur.com/yFNXCEp.png)

Your default web browser should then open the new editor session you've created.

___

### Using the editor

Once you've created and opened the session, you can use the interface to make changes to the user/group's data.

#### Adding a permission

To add a permission, type the node you'd like to add into the "Permission" input box, then press the enter key, or click the "add" button.

![](https://giant.gfycat.com/TerrificAccomplishedIndusriverdolphin.gif)

#### Editing existing data

To edit any value in the table, just click it.

![](https://giant.gfycat.com/FirmLightheartedAddax.gif)

#### Sorting the data

To change the sorting settings, click on the column heading you'd like to sort by.

![](https://giant.gfycat.com/PastFinishedCougar.gif)

___

### Saving your changes

Once you've finished making changes to the data, you need to save your changes back to the server.

Click on the "Save" button, or use the `CTRL + S` keyboard shortcut to save.

![](https://giant.gfycat.com/NegativeIncompleteCougar.gif)

The editor will generate a command which you need to execute in-game or in the console for your changes to apply. Simply clicking on the command will copy it to your clipboard.

When you run the command, a summary of the changes will be shown.

![](https://i.imgur.com/dXbpjQ9.png)