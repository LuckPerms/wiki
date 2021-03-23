This page is a continuation of the main [Migration guide](Migration). 

Once you've followed the instructions to move your data from GroupManager or PermissionsEx to LuckPerms, the resources on this page will hopefully help you to quickly get up to speed!

Firstly, there are some tables below which compare the commands in GroupManager and PermissionsEx with their **equivalents** in LuckPerms. If you knew how to do something in GM or PEX, hopefully these tables will help you to quickly find how to do it in LuckPerms.

Of course, there is also the [full command documentation for LuckPerms](Command-Usage), which is probably better to get used to!

Secondly, there is an additional resource that you can install to your server that will allow you to keep using *some* PermissionsEx and GroupManager commands, and have them automatically routed to LuckPerms. You can find more information about that [here](https://github.com/LuckPerms/LuckPermsCompat). However, generally, we encourage that you "rip off the bandaid" so to speak and get used to the *proper* LuckPerms commands right away - with a little time they will become 2nd nature just like GM or PEX commands once did!

Good luck, and we hope you enjoy using LuckPerms!

#### GroupManager command equivalents
| GroupManager                               | LuckPerms                                                |
| ------------------------------------------ | -------------------------------------------------------- |
| manuadd \<player\> \<group\>               | lp user \<player\> parent set \<group\>                  |
| manudel \<player\>                         | lp user \<player\> clear                                 |
| manuaddsub \<player\> \<group\>            | lp user \<player\> parent add \<group\>                  |
| manudelsub \<player\> \<group\>            | lp user \<player\> parent remove \<group\>               |
| manpromote \<player\> \<group\>            | lp user \<player\> promote \<track\>                     |
| mandemote \<player\> \<group\>             | lp user \<player\> demote \<track\>                      |
| manwhois \<player\>                        | lp user \<player\> info                                  |
| manuaddp \<player\> \<permission\>         | lp user \<player\> permission set \<permission\> true    |
| manudelp \<player\> \<permission\>         | lp user \<player\> permission unset \<permission\>       |
| manulistp \<player\>                       | lp user \<player\> permission info                       |
| manucheckp \<player\> \<permission\>       | lp user \<player\> haspermission \<permission\>          |
| manuaddv \<player\> prefix \<value\>       | lp user \<player\> meta addprefix \<priority\> \<value\> |
| manuaddv \<player\> suffix \<value\>       | lp user \<player\> meta addsuffix \<priority\> \<value\> |
| manuaddv \<player\> \<variable\> \<value\> | lp user \<player\> meta set \<variable\> \<value\>       |
| manudelv \<player\> \<variable\>           | lp user \<player\> meta unset \<variable\>               |
| manulistv \<player\>                       | lp user \<player\> meta info                             |
|                                            |                                                          |
| mangadd \<group\>                          | lp creategroup \<group\>                                 |
| mangdel \<group\>                          | lp deletegroup \<group\>                                 |
| mangaddi \<group1\> \<group2\>             | lp group \<group1\> parent add \<group2\>                |
| mangdeli \<group1\> \<group2\>             | lp group \<group1\> parent remove \<group2\>             |
| listgroups                                 | lp listgroups                                            |
| mangaddp \<group\> \<permission\>          | lp group \<group\> permission set \<permission\> true    |
| mangdelp \<group\> \<permission\>          | lp group \<group\> permission unset \<permission\>       |
| manglistp \<group\>                        | lp group \<group\> permission info                       |
| mangcheckp \<group\> \<permission\>        | lp group \<group\> haspermission \<permission\>          |
| mangaddv \<player\> prefix \<value\>       | lp group \<group\> meta addprefix \<priority\> \<value\> |
| mangaddv \<player\> suffix \<value\>       | lp group \<group\> meta addsuffix \<priority\> \<value\> |
| mangaddv \<player\> \<variable\> \<value\> | lp group \<group\> meta set \<variable\> \<value\>       |
| mangdelv \<player\> \<variable\>           | lp group \<group\> meta unset \<variable\>               |
| manglistv \<player\>                       | lp group \<group\> meta info                             |
|                                            |                                                          |
| mansave                                    | lp sync                                                  |
| manload                                    | lp sync                                                  |


#### PermissionsEx command equivalents
| PermissionsEx                                                | LuckPerms                                                    |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| pex                                                          | lp                                                           |
| pex reload                                                   | lp sync                                                      |
| pex toggle debug                                             | [lp verbose \<option>](Verbose)                              |
| pex user \<user\> check \<permission\>                       | lp user \<user\> haspermission \<permission\>                |
| pex backend                                                  | lp info                                                      |
| pex import \<backend\>                                       | lp export \<file\> / lp import \<file\>                      |
|                                                              |                                                              |
| pex user \<user\> list                                       | lp user \<user\> permission info                             |
| pex user \<user\> prefix                                     | lp user \<user\> meta info                                   |
| pex user \<user\> prefix \<prefix\>                          | lp user \<user\> meta addprefix \<priority\> \<prefix\>      |
| pex user \<user\> suffix                                     | lp user \<user\> meta info                                   |
| pex user \<user\> suffix \<suffix\>                          | lp user \<user\> meta addsuffix \<priority\> \<suffix\>      |
| pex user \<user\> delete                                     | lp user \<user\> clear                                       |
| pex user \<user\> add \<permission\> \<world\>               | lp user \<user\> permission set \<permission\> \<true/false\> world=\<world\> |
| pex user \<user\> remove \<permission\> \<world\>            | lp user \<user\> permission unset \<permission\> world=\<world\> |
| pex user \<user\> timed add \<permission\> \<time\> \<world\> | lp user \<user\> permission settemp \<permission\> \<true/false\> \<time\> world=\<world\> |
| pex user \<user\> timed remove \<permission\> \<time\> \<world\> | lp user \<user\> permission unsettemp \<permission\> world=\<world\> |
| pex user \<user\> set \<option\> \<value\> \<world\>         | lp user \<user\> meta set \<option\> \<value\> world=\<world\> |
|                                                              |                                                              |
| pex user \<user\> group list                                 | lp user \<user\> parent info                                 |
| pex user \<user\> group add \<group\> \<world\>              | lp user \<user\> parent add \<group\> world=\<world\>        |
| pex user \<user\> group add \<group\> \<world\> \<time\>     | lp user \<user\> parent addtemp \<group\> \<time\> world=\<world\> |
| pex user \<user\> group set \<group\>                        | lp user \<user\> parent set \<group\>                        |
| pex user \<user\> group remove \<group\> \<world\>           | lp user \<user\> parent remove \<group\> world=\<world\>     |
| pex groups list                                              | lp listgroups                                                |
| pex group \<group\> list                                     | lp group \<group\> permission info                           |
| pex group \<group\> prefix                                   | lp group \<group\> meta info                                 |
| pex group \<group\> prefix \<prefix\>                        | lp group \<group\> meta addprefix \<priority\> \<prefix\>    |
| pex group \<group\> suffix                                   | lp group \<group\> meta info                                 |
| pex group \<group\> suffix \<suffix\>                        | lp group \<group\> meta addsuffix \<priority\> \<suffix\>    |
| pex group \<group\> create                                   | lp creategroup \<group\>                                     |
| pex group \<group\> delete                                   | lp deletegroup \<group\>                                     |
| pex group \<group\> parents list                             | lp group \<group\> parent info                               |
| pex group \<group\> users                                    | lp group \<group\> listmembers                               |
| pex group \<group\> parents set \<parents\>                  | lp group \<group\> parent add \<parent\>                     |
| pex group \<group\> add \<permission\> \<world\>             | lp group \<group\> permission set \<permission\> \<true/false\> world=\<world\> |
| pex group \<group\> remove \<permission\> \<world\>          | lp group \<group\> permission unset \<permission\> world=\<world\> |
| pex group \<group\> timed add \<permission\> \<time\> \<world\> | lp group \<group\> permission settemp \<permission\> \<true/false\> \<time\> world=\<world\> |
| pex group \<group\> timed remove \<permission\> \<time\> \<world\> | lp group \<group\> permission unsettemp \<permission\> world=\<world\> |
| pex group \<group\> set \<option\> \<value\> \<world\>       | lp group \<group\> meta set \<option\> \<value\> world=\<world\> |
|                                                              |                                                              |
| pex group \<group\> user add \<user\>                        | lp user \<user\> parent add \<group\>                        |
| pex group \<group\> user remove \<user\>                     | lp user \<user\> parent remove \<group\>                     |
| pex promote \<user\> \<ladder\>                              | lp user \<user\> promote \<ladder\>                          |
| pex demote \<user\> \<ladder\>                               | lp user \<user\> demote \<ladder\>                           |



