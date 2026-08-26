# TAGLINE

创建 MongoDB 数据库的二进制导出

# TLDR

**转储整个数据库**

```mongodump --db [database]```

**转储指定集合**

```mongodump --db [database] --collection [collection]```

**带认证转储**

```mongodump --uri "mongodb://[user]:[pass]@[host]/[db]"```

**转储到指定目录**

```mongodump --out [/path/to/backup]```

**转储为归档文件**

```mongodump --archive=[backup.archive]```

**压缩转储**

```mongodump --gzip --out [backup/]```

**带查询条件转储**

```mongodump --db [db] --collection [coll] --query '{"status": "active"}'```

**从远程主机转储**

```mongodump --host [hostname] --port [27017]```

# SYNOPSIS

**mongodump** [_--uri uri_] [_--db database_] [_--collection coll_] [_--out dir_] [_--archive file_] [_options_]

# PARAMETERS

**--uri** _URI_
> MongoDB 连接 URI。

**--host** _HOST_
> 服务器主机名。

**--port** _PORT_
> 服务器端口。

**--db**, **-d** _DATABASE_
> 要转储的数据库。

**--collection**, **-c** _COLL_
> 要转储的集合。

**--out**, **-o** _DIR_
> 输出目录。

**--archive**[=_FILE_]
> 输出为归档文件。

**--gzip**
> 压缩输出。

**--query**, **-q** _JSON_
> 过滤文档。

**--queryFile** _FILE_
> 从文件读取查询条件。

**--username**, **-u** _USER_
> 认证用户名。

**--password**, **-p** _PASS_
> 认证密码。

**--authenticationDatabase** _DB_
> 认证数据库。

**--oplog**
> 包含 oplog 以支持时间点恢复。

**--dumpDbUsersAndRoles**
> 包含用户和角色。

**--numParallelCollections** _N_
> 并行转储的集合数。

**-j** _N_
> 并行转储的文档数。

# DESCRIPTION

**mongodump** 创建 MongoDB 数据库的二进制导出。它直接从 MongoDB 读取数据并写入 BSON 文件，保留文档结构和类型。

输出格式是一个目录结构：每个数据库一个文件夹，其中包含每个集合的 BSON 文件和元数据 JSON 文件。归档格式则把所有内容合并为单个文件。

--oplog 选项会捕获转储期间发生的操作，从而支持时间点恢复。这对活跃数据库的一致性备份至关重要。

查询过滤只导出匹配的文档，可用于部分备份、测试数据提取或归档特定记录。

压缩（--gzip）可显著减小备份体积。与归档格式结合使用时，会生成适合存储或传输的单个压缩文件。

并行选项可以加速大规模备份。多个集合可以同时转储，集合内的文档也可以并行处理。

# CAVEATS

不建议用于大型生产数据库——请改用文件系统快照。没有 --oplog 时备份不是原子的。索引作为元数据保存，在恢复时重建。需要对被转储的所有数据库拥有读权限。

# HISTORY

**mongodump** 从早期版本起就是 **MongoDB** 的一部分，由 MongoDB, Inc.（前身为 10gen）开发。它提供导出 MongoDB 数据的标准方法，配合 mongorestore 完成导入。它是 MongoDB Database Tools 软件包的一部分。

# INSTALL

```apk: sudo apk add mongodb-tools```

```nix: nix profile install nixpkgs#mongodb-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mongorestore](/man/mongorestore)(1), [mongoexport](/man/mongoexport)(1), [mongoimport](/man/mongoimport)(1), [mongo](/man/mongo)(1)
