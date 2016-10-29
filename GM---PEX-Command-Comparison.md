## Group Manager
| Group Manager Commands                  | LuckPerms Commands                                        |
|-----------------------------------------|-----------------------------------------------------------|
| manuadd <player> <group>                | lp user <player> parent add <group>                       |
| manudel <player>                        | lp user <player> parent clear                             |
| manuaddsub <player> <group>             | lp user <player> parent add <group>                       |
| manudelsub <player> <group>             | lp user <player> parent remove <group>                    |
| manpromote <player> <group>             | lp user <player> promote <track>                          |
| mandemote <player> <group>              | lp user <player> demote <track>                           |
| manwhois <player>                       | lp user <player> info                                     |
| manuaddp <player> <permission>          | lp user <player> permission set <permission> true         |
| manudelp <player> <permission>          | lp user <player> permission unset <permission>            |
| manulistp <player>                      | lp user <player> permission info                          |
| manucheckp <player> <permission>        | lp user <player> haspermission <permission>               |
| manuaddv <player> prefix <value>        | lp user <player> meta addprefix <priority> <value>        |
| manuaddv <player> suffix <value>        | lp user <player> meta addsuffix <priority> <value>        |
| manuaddv <player> <variable> <value>    | lp user <player> meta set <variable> <value>              |
| manudelv <player> <variable>            | lp user <player> meta unset <variable>                    |
| manulistv <player>                      | lp user <player> meta info                                |
|-----------------------------------------|-----------------------------------------------------------|
| mangadd <group>                         | lp creategroup <group>                                    |
| mangdel <group>                         | lp deletegroup <group>                                    |
| mangaddi <group1> <group2>              | lp group <group1> parent add <group2>                     |
| mangdeli <group1> <group2>              | lp group <group1> parent remove <group2>                  |
| listgroups                              | lp listgroups                                             |
| mangaddp <group> <permission>           | lp group <group> permission set <permission> true         |
| mangdelp <group> <permission>           | lp group <group> permission unset <permission>            |
| manglistp <group>                       | lp group <group> permission info                          |
| mangcheckp <group> <permission>         | lp group <group> haspermission <permission>               |
| mangaddv <player> prefix <value>        | lp group <group> meta addprefix <priority> <value>        |
| mangaddv <player> suffix <value>        | lp group <group> meta addsuffix <priority> <value>        |
| mangaddv <player> <variable> <value>    | lp group <group> meta set <variable> <value>              |
| mangdelv <player> <variable>            | lp group <group> meta unset <variable>                    |
| manglistv <player>                      | lp group <group> meta info                                |
|-----------------------------------------|-----------------------------------------------------------|
| mansave                                 | lp sync                                                   |
| manload                                 | lp sync                                                   |