# TAGLINE

SirixDB 双时态数据库的命令行客户端

# TLDR

创建 JSON 数据库和资源

```sirix-cli -l /tmp/mydb create json -r myresource -d '{"name": "Alice"}'```

查询资源

```sirix-cli -l /tmp/mydb query -r myresource```

运行 JSONiq 表达式（$$ 是文档根）

```sirix-cli -l /tmp/mydb query -r myresource '$$.name'```

更新并创建新版本

```sirix-cli -l /tmp/mydb update -r myresource '{"team": "engineering"}' -im as-first-child```

查询历史版本

```sirix-cli -l /tmp/mydb query -r myresource -rev 1```

显示资源的版本历史

```sirix-cli -l /tmp/mydb resource-history myresource```

# SYNOPSIS

**sirix-cli** **-l** _path_ _COMMAND_ [_ARGS_] [_OPTIONS_]

# PARAMETERS

**-l** _path_
> 本地数据库路径（目录）

**create** _type_ **-r** _resource_ **-d** _data_
> 创建一个数据库资源（例如 **json**），包含初始文档数据

**query** **-r** _resource_ [_expression_]
> 读取资源；可选的 JSONiq/XQuery 表达式；**-rev** 选择某个版本

**update** **-r** _resource_ _data_ **-im** _mode_
> 应用一次会产生新版本的更新

**resource-history** _resource_
> 列出资源的版本历史

# DESCRIPTION

**sirix-cli** 是 **SirixDB** 的全功能命令行界面。SirixDB 是一个可嵌入、只追加、双时态的数据库，通过结构共享将每次提交存储为空间高效的快照。与覆盖当前状态的工具不同，SirixDB 保留完整历史，因此打开任意过去版本的耗时与打开最新版本相同。

该 CLI 在本地数据库目录（**-l**）上操作：创建 JSON（或 XML）资源、运行 JSONiq/XQuery 查询、应用会产生新版本的更新以及查看历史。它与 **sirix-shell**（交互式查询 REPL）以及用于远程和智能体使用的 REST API / MCP 服务器互为补充。

# CAVEATS

SirixDB 需要较新的 Java 运行时（或 CLI 的 GraalVM 原生构建）。写入并发为每个资源一个写者；读取者具有快照隔离性。路径和存储布局由 SirixDB 在数据库目录下管理——数据库打开期间请勿手动编辑这些文件。

# HISTORY

**SirixDB** 是由 Johannes Lichtenberger 及贡献者维护的开源双时态存储系统；**sirix-cli** 是主仓库 **sirix** 中的 Kotlin CLI 模块。

# SEE ALSO

[sirix-shell](/man/sirix-shell)(1), [java](/man/java)(1), [jq](/man/jq)(1)

# RESOURCES

```[Source code](https://github.com/sirixdb/sirix)```

```[Homepage](https://sirix.io)```

```[Documentation](https://sirix.io/docs/)```

<!-- verified: 2026-07-16 -->
