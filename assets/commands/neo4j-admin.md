# TAGLINE

管理 Neo4j 数据库

# TLDR

将数据库**转储到文件**（数据库必须已停止）

```neo4j-admin database dump --to-path=[/backups] [neo4j]```

从转储文件**加载数据库**

```neo4j-admin database load --from-path=[/backups] [neo4j]```

**设置初始管理员密码**

```neo4j-admin dbms set-initial-password [password]```

**检查数据库一致性**

```neo4j-admin database check [neo4j]```

向新数据库**批量导入 CSV 数据**

```neo4j-admin database import full --nodes=[nodes.csv] --relationships=[rels.csv] [neo4j]```

**显示堆内存和页缓存的内存建议**

```neo4j-admin server memory-recommendation```

# SYNOPSIS

**neo4j-admin** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 管理命令类别：database、dbms 或 server。

**database dump**
> 将数据库转储为单文件归档，用于离线备份。

**database load**
> 从转储文件加载数据库。

**database import full**
> 将 CSV 文件中的数据批量导入新数据库。

**database check**
> 检查数据库的一致性和完整性。

**dbms set-initial-password**
> 在首次启动前设置初始管理员密码。

**server memory-recommendation**
> 打印针对堆内存和页缓存的启发式内存建议。

**--additional-config** _file_
> 从文件提供额外配置。

**--expand-commands**
> 允许在配置值中进行命令展开。

**--verbose**
> 启用详细输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**neo4j-admin** 是 Neo4j 图数据库的管理工具。它负责备份与恢复（dump/load）、数据库一致性检查、批量数据导入、内存配置建议以及初始设置任务。

在 Neo4j 5 及以上版本中，命令按类别组织：**database**（单数据库操作，如 dump、load、import、check）、**dbms**（系统级操作，如设置初始密码）和 **server**（服务器配置，如内存建议）。某些操作要求先停止数据库。

# CAVEATS

部分操作（dump、load、import）需要先停止数据库。通常需要管理员权限。命令语法在 Neo4j 4.x 和 5.x 之间变化很大；此处示例使用的是 Neo4j 5+ 的语法。

# HISTORY

neo4j-admin 自早期版本起就是 Neo4j 发行版的一部分。命令结构在 **Neo4j 5**（2022 年）中经历了大幅重组，由扁平命令（如 `dump`、`memrec`）改为分类子命令（如 `database dump`、`server memory-recommendation`）。

# INSTALL

```apk: sudo apk add neo4j```

```brew: brew install neo4j```

```nix: nix profile install nixpkgs#neo4j```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[neo4j](/man/neo4j)(1), [cypher-shell](/man/cypher-shell)(1)
