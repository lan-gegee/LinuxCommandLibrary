# TAGLINE

将 MongoDB 集合中的数据导出为 JSON 或 CSV 文件

# TLDR

**将集合导出为 JSON**

```mongoexport --db=[database] --collection=[collection] --out=[output.json]```

**导出为 CSV**

```mongoexport --db=[database] --collection=[collection] --type=csv --fields=[field1,field2] --out=[output.csv]```

**带查询条件导出**

```mongoexport --db=[database] --collection=[collection] --query='{"field":"value"}'```

**从远程主机导出**

```mongoexport --host=[hostname] --port=[27017] --db=[database] --collection=[collection]```

# SYNOPSIS

**mongoexport** [_options_]

# PARAMETERS

**--db** _name_
> 数据库名称。

**--collection** _name_
> 要导出的集合。

**--out** _file_
> 输出文件路径。

**--type** _type_
> 输出类型（json、csv）。

**--fields** _fields_
> CSV 导出的字段。

**--query** _json_
> 过滤查询。

**--host** _host_
> MongoDB 主机。

# DESCRIPTION

**mongoexport** 将 MongoDB 集合中的数据导出为 JSON 或 CSV 文件。它是 MongoDB Database Tools 的一部分，可用于备份、数据迁移和报表。

# INSTALL

```apk: sudo apk add mongodb-tools```

```nix: nix profile install nixpkgs#mongodb-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mongoimport](/man/mongoimport)(1), [mongodump](/man/mongodump)(1)
