LuckPerms comes with a variety of Storage options to choose from.

The storage provider can be modified in the `config.yml` or `luckperms.conf` file.
```yaml
# +------------------------------------------------------------------------+ #
# |                               Storage                                  | #
# +------------------------------------------------------------------------+ #

# Which storage method the plugin should use.
# Currently supported: mysql, postgresql, sqlite, h2, json, yaml, mongodb
# Fill out connection info below if you're using MySQL, PostgreSQL or MongoDB
storage-method: h2
```

## H2 / SQLite
The default storage option is **H2**.   
Both are types of file based SQL databases. All data is stored within one file in the LuckPerms folder. The data cannot be easily edited with a text editor, unlike YAML or JSON. The plugin commands must be used to edit or view the data.

```yaml
storage-method: h2
storage-method: sqlite
```
