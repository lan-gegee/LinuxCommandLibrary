# TAGLINE

向 MongoDB 导入数据

# TLDR

**导入 JSON 文件**

```mongoimport --db [dbname] --collection [coll] --file [data.json]```

**导入 CSV 文件**

```mongoimport --db [dbname] --collection [coll] --type csv --headerline --file [data.csv]```

**带认证导入**

```mongoimport -u [user] -p [pass] --db [dbname] --collection [coll] --file [data.json]```

**从 URI 导入**

```mongoimport --uri "[mongodb://host/db]" --collection [coll] --file [data.json]```

**先删除再导入**

```mongoimport --db [dbname] --collection [coll] --drop --file [data.json]```

**导入 JSON 数组**

```mongoimport --db [dbname] --collection [coll] --jsonArray --file [array.json]```

# SYNOPSIS

**mongoimport** [_options_] [_file_]

# PARAMETERS

**--db** _NAME_
> 数据库名称。

**--collection** _NAME_
> 集合名称。

**--file** _FILE_
> 输入文件路径。

**--type** _TYPE_
> 文件类型（json、csv、tsv）。

**--headerline**
> 将首行用作字段名。

**--drop**
> 导入前删除集合。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mongoimport** 向 MongoDB 导入数据。它支持 JSON、CSV 和 TSV 格式。

该工具批量加载文档，适用于数据迁移和数据库初始化填充。

# CAVEATS

不适合大数据集。BSON 请使用 mongorestore。大导入可能较慢。

# HISTORY

mongoimport 是 **MongoDB Database Tools** 的一部分，自 MongoDB 早期版本起就提供数据导入能力。

# INSTALL

```apk: sudo apk add mongodb-tools```

```nix: nix profile install nixpkgs#mongodb-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mongoexport](/man/mongoexport)(1), [mongorestore](/man/mongorestore)(1), [mongosh](/man/mongosh)(1)
