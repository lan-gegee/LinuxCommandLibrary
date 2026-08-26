# TAGLINE

Apache Hive 的 JDBC 命令行客户端

# TLDR

**连接 HiveServer2**

```beeline -u jdbc:hive2://[localhost]:10000/[default]```

使用用户名和密码**连接**

```beeline -u jdbc:hive2://[localhost]:10000/[default] -n [username] -p [password]```

直接**执行查询**

```beeline -u jdbc:hive2://[localhost]:10000 -e "[SELECT * FROM table_name]"```

**从文件执行查询**

```beeline -u jdbc:hive2://[localhost]:10000 -f [path/to/script.sql]```

以 CSV 格式输出**连接**

```beeline -u jdbc:hive2://[localhost]:10000 --outputformat=csv2```

**重新连接**上次使用的 URL

```beeline -r```

# SYNOPSIS

**beeline** [_OPTIONS_] [_QUERY_]

# PARAMETERS

**-u** _URL_
> JDBC 连接 URL（例如 jdbc:hive2://localhost:10000/default）。

**-n** _USERNAME_
> 用于身份验证的用户名。

**-p** _PASSWORD_
> 用于身份验证的密码。

**-w** _FILE_
> 存放密码的文件路径。

**-d** _DRIVER_
> 要使用的 JDBC 驱动类。

**-e** _QUERY_
> 执行查询字符串。多条语句可用分号分隔。

**-f** _FILE_
> 从文件执行 SQL 脚本。

**-i**, **--init** _FILE_
> 在执行命令前先运行初始化文件。

**-r**
> 重新连接上次使用的 URL（Hive 2.1.0 起）。

**--outputformat** _FORMAT_
> 输出格式：table、vertical、csv、tsv、dsv、csv2、tsv2、json、jsonfile。

**--showHeader**
> 在输出中显示列名（默认：true）。

**--silent**
> 抑制信息性消息和查询日志。

**--verbose**
> 显示调试信息和错误详情。

**--hiveconf** _KEY_=_VALUE_
> 设置 Hive 配置属性。

**--hivevar** _KEY_=_VALUE_
> 定义 Hive 会话变量。

**--force**
> 出错时仍继续执行脚本。

**--incremental**
> 取到行后立即显示。

**--help**
> 显示用法信息。

# DESCRIPTION

**Beeline** 是 HiveServer2 的 JDBC 命令行客户端，基于 SQLLine CLI 构建。它提供了对 HiveServer2 实例执行 Hive 查询的接口，同时支持嵌入式模式（运行内嵌的 Hive）和远程模式（通过 Thrift 连接）。

生产环境推荐使用远程模式，因为它更安全，不需要直接访问 HDFS 或元存储。Beeline 连接的 HiveServer2 默认运行在 10000 端口。该客户端支持多种身份验证方式，包括 Kerberos、LDAP 和自定义认证。

连接 URL 中可以包含会话变量、Hive 配置参数和连接属性。Beeline 支持基于 ZooKeeper 的服务发现、SSL/TLS 连接以及便于穿越防火墙部署的 HTTP 传输模式。

# CAVEATS

Beeline 已取代被废弃的 Hive CLI。一些旧的 CLI 专用命令行为可能有所不同。连接 URL 必须正确格式化并对特殊字符进行转义。使用 Kerberos 身份验证时，需要正确配置 keytab 和 principal。

# HISTORY

Beeline 作为推荐的 HiveServer2 客户端被引入，用以取代最初的 Hive CLI。它基于开源 JDBC 命令行工具 SQLLine。Hive CLI 之所以被废弃，是因为它要求直接访问 Hadoop 和 Hive 库；而 Beeline 提供通过 JDBC 连接的瘦客户端模型，提升了安全性和部署灵活性。

# SEE ALSO

[hive](/man/hive)(1)
