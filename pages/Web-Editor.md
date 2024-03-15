LuckPerms features a web editor, which allows you to make changes to permissions data using a friendly interface in your web browser. It is safe, secure and easy to use. You don't need to host the page yourself - and it works for all storage types!

If you'd like more information about the technical details, please see the [technical info page](Web-Editor-Technical-Details).

___

### Getting started

Editor sessions are first created by executing a command on the server.
You can run different commands to open sessions with different scopes:


| Scope                                          | Command                                             |
|------------------------------------------------|-----------------------------------------------------|
| **All groups and online/non-default users:**   | `/lp editor` or `lp editor all`                     |
| **All groups:**                                | `/lp editor groups`                                 |
| **All online and non-default users:**          | `/lp editor users`                                  |
| **All online users:**                          | `/lp editor online`                                 |
| **For a specific group:**                      | `/lp group <group> editor`                          |
| **For a specific user:**                       | `/lp user <user> editor`                            |
| **For users only with a specific permission:** | `/lp editor users <filter>` or `lp editor <filter>` |

> Remember to use `/lpb` or `/lpv` instead of `/lp` if you want to target your command to a BungeeCord/Velocity version of LP.

> The user permission filter command will load only users with a directly applied permission matching the filter to the editor.

Once the command has been executed, the server will begin creating a new session. It should only take a second or so (depending on your connection speed).

Once the session is ready, you will be sent a link.

![](../img/webeditor-1.png)

To proceed, click on the URL, then press "**Yes**".

![](../img/webeditor-2.png)

Your default web browser should then open the new editor session you've created.

___

### Using the editor

Once you've created and opened the session, you can use the interface to make changes to the user/group's data.

### Editor Context

You can add contexts in the editor in addition to in-game. To do so, either click the "Add Contexts" button before adding a permission or simply fill in the `key` and `value` fields after a permission with appropriate keys and values, such as `world` and `nether`, or `server` and `hub`.

Note that a permission can only have one world and one server context at a time. You have to set the same permission again with the other context to make it apply on multiple worlds/servers.

#### Adding a permission

To add a permission, type the node you'd like to add into the "Add Permission" input box and press enter. You can repeat this for all permissions that you want to add with the same properties.  
When typing the editor will show a list of suggestions matching your input so far. You can select one through the arrow keys or with your cursor and include it by pressing enter or clicking on it.
After you've entered the permission(s), click the "+" button to add.

You can add multiple permissions at once! Just type or copy/paste them into the box, and add them as usual.

![](../img/webeditor-3.gif)

#### Editing existing data

To edit any value in the table, just click it.

![](../img/webeditor-4.gif)

#### Sorting the data

To change the sorting settings, click on the column heading you'd like to sort by.

![](../img/webeditor-5.gif)

#### LuckPerms Nodes

The editor allows you to add or change aspects about groups and players such as weight and parents using nodes.

| Function                                | Node                         |
| --------------------------------------- | ---------------------------- |
| **To define a user or group's parent:** | `group.<parentgroup>`        |
| **To set a group's displayname:**       | `displayname.<name>`         |
| **To set a group's weight:**            | `weight.<weightnumber>`      |
| **To add a prefix:**                    | `prefix.<priority>.<prefix>` |
| **To add a suffix:**                    | `suffix.<priority>.<suffix>` |
| **To add meta:**                        | `meta.<key>.<value>`         |

___

### Saving your changes

Once you've finished making changes to the data, you need to save your changes back to the server.

Click on the "Save" button, or use the `CTRL + S` keyboard shortcut to save, and the editor will generate a command which you need to execute in-game or in the console for your changes to apply. Simply clicking on the command will copy it to your clipboard.

![](../img/webeditor-6.gif)

When you run the command, a summary of the changes will be shown.

![](../img/webeditor-7.png)
