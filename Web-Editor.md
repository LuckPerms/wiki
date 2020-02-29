LuckPerms features a web editor, which allows you to make changes to permissions data using a friendly interface in your web browser. It is safe, secure and easy to use. You don't need to host the page yourself - and it works for all storage types!

If you'd like more information about the technical details, see the project's [readme page](https://github.com/lucko/LuckPermsWeb/blob/master/editor/README.md).

___

### Getting started

Editor sessions are first created by executing a command on the server.


| Scope                            | Command                    |
|----------------------------------|----------------------------|
| **All groups and online users:** | `/lp editor`               |
| **All groups:**                  | `/lp editor groups`        |
| **All online users:**            | `/lp editor users`         |
| **For a specific group:**        | `/lp group <group> editor` |
| **For a specific user:**         | `/lp user <user> editor`   |

> Remember to use `/lpb` instead of `/lp` if you want to target your command to the BungeeCord version of LP and `/lpv` for Velocity.

Once the command has been executed, the server will begin creating a new session. It should only take a second or so (depending on your connection speed).

Once the session is ready, you will be sent a link.

![](https://i.imgur.com/9mJQnmBl.png)

To proceed, click on the URL, then press "Yes".

![](https://i.imgur.com/bSkrjWHl.png)

Your default web browser should then open the new editor session you've created.

___

### Using the editor

Once you've created and opened the session, you can use the interface to make changes to the user/group's data.

#### Adding a permission

To add a permission, type the node you'd like to add into the "Add Permission" input box and press enter. You can repeat this for all permissions that you want to add with the same values.  
When typing will the editor show a list of permissions matching your input. You can select one through the arrow keys or with your cursor and select it by pressing enter or clicking on it.

After you've set the permission(s), go to the "+" button and press it.

![](https://thumbs.gfycat.com/ChubbyWarmAmmonite-size_restricted.gif)

#### Editing existing data

To edit any value in the table, just click it.

![](https://thumbs.gfycat.com/MiniatureIdleAxolotl-size_restricted.gif)

#### Adding Context

To add context to a permission, either click the "Add Contexts" button before adding a permission, or click the area right under the "Contexts" column to edit the context of a permission.  
Use "world" or "server" as keys to set per-world and per-server permissions respectively. Note that a permission can only have one world and one server context at a time. You have to set the same permission again with the other context to make it apply on multiple worlds/servers.

![](https://thumbs.gfycat.com/SkeletalHarmoniousFattaileddunnart-size_restricted.gif)

#### Sorting the data

To change the sorting settings, click on the column heading you'd like to sort by.

![](https://thumbs.gfycat.com/MistySpectacularLamprey-size_restricted.gif)

___

### Saving your changes

Once you've finished making changes to the data, you need to save your changes back to the server.

Click on the "Save" button. The editor will generate a command which you need to execute in-game or in the console for your changes to apply. Simply clicking on the command will copy it to your clipboard.

When you run the command, a summary of the changes will be shown.

![](https://i.imgur.com/4SGTBbMl.png)
