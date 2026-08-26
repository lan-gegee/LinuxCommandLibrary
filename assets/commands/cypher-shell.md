# TAGLINE

Neo4j Cypher 查询语言 Shell

# TLDR

**使用默认设置连接 Neo4j**

```cypher-shell```

**使用凭据连接**

```cypher-shell -u [username] -p [password]```

**连接到指定地址**

```cypher-shell -a [neo4j://localhost:7687]```

**执行一条查询**并退出

```cypher-shell "MATCH (n) RETURN count(n)"```

**从文件执行查询**

```cypher-shell -f [queries.cypher]```

**连接到指定的数据库**

```cypher-shell -d [neo4j]```

**以纯文本格式输出**

```cypher-shell --format plain "MATCH (n) RETURN n LIMIT 5"```

# SYNOPSIS

**cypher-shell** [_options_] [_query_]

# PARAMETERS

**-a** _ADDRESS_, **--address** _ADDRESS_, **--uri** _ADDRESS_
> 连接地址（默认：neo4j://localhost:7687）。

**-u** _USER_, **--username** _USER_
> Neo4j 用户名。

**-p** _PASSWORD_, **--password** _PASSWORD_
> Neo4j 密码。

**-d** _DATABASE_, **--database** _DATABASE_
> 要连接的数据库。

**-f** _FILE_, **--file** _FILE_
> 从文件执行 Cypher 查询。

**--format** _FORMAT_
> 输出格式：auto、verbose、plain（默认：auto）。

**--encryption** _MODE_
> 加密模式：true、false、default。

**-P** _PARAM_, **--param** _PARAM_
> 定义会话参数（可重复使用）。

**--non-interactive**
> 强制使用非交互式（批处理）模式。

**--fail-fast**
> 处理文件时遇到第一个错误即退出。

**--fail-at-end**
> 处理完文件后报告所有错误。

**--change-password**
> 更改用户密码后退出。

**-v**, **--version**
> 显示版本信息。

**--help**
> 显示帮助信息。

# DESCRIPTION

**cypher-shell** 是针对 Neo4j 图数据库执行 Cypher 查询的命令行界面。Cypher 是 Neo4j 的声明式查询语言，用于创建、读取、更新和删除图数据。

在交互模式下，它提供用于探索图数据的 REPL 环境，支持命令历史和基本编辑功能。非交互模式则执行查询并返回结果，适用于脚本和自动化场景。

该 Shell 支持事务管理，可以将多条语句原子性地执行。它能以多种格式输出结果，既适合人工阅读，也便于机器解析。

# CAVEATS

通过命令行传递的密码可能会在进程列表中可见。较大的结果集可能占用大量内存。某些 Cypher 特性需要特定版本的 Neo4j。加密连接需要正确的证书配置。

# HISTORY

cypher-shell 由 Neo4j 作为其数据库工具的一部分推出。它取代了旧的 neo4j-shell，为现代 Neo4j 特性以及 **2016 年**随 **Neo4j 3.0** 引入的 Bolt 协议提供了更好的支持。

# INSTALL

```apk: sudo apk add cypher-shell```

```brew: brew install cypher-shell```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[neo4j](/man/neo4j)(1), [neo4j-admin](/man/neo4j-admin)(1)
