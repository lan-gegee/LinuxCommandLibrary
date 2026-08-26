# TAGLINE

从 mongodump 的输出恢复 MongoDB 数据

# TLDR

**从转储目录恢复**

```mongorestore [dump/]```

**恢复特定数据库**

```mongorestore --db=[database] [dump/database/]```

**恢复到远程主机**

```mongorestore --host=[hostname] --port=[27017] [dump/]```

**先删除再恢复**

```mongorestore --drop [dump/]```

**从归档文件恢复**

```mongorestore --archive=[backup.archive]```

# SYNOPSIS

**mongorestore** [_options_] [_directory_]

# PARAMETERS

**--db** _name_
> 目标数据库名称。

**--collection** _name_
> 目标集合。

**--drop**
> 恢复前删除集合。

**--host** _host_
> MongoDB 主机。

**--archive** _file_
> 从归档文件恢复。

**--gzip**
> 解压 gzip 压缩的输入。

# DESCRIPTION

**mongorestore** 从 mongodump 的输出恢复 MongoDB 数据。它是 MongoDB Database Tools 的一部分，可将 BSON 文件还原到 MongoDB 集合中，支持完整恢复和选择性恢复。

# INSTALL

```apk: sudo apk add mongodb-tools```

```nix: nix profile install nixpkgs#mongodb-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mongodump](/man/mongodump)(1), [mongoexport](/man/mongoexport)(1)
