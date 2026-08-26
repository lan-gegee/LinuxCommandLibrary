# TAGLINE

管理 MySQL 的 SQL 模式设置

# TLDR

**获取数据库集群当前的 SQL 模式**

```doctl databases sql-mode get [cluster_id]```

**为数据库集群设置 SQL 模式**

```doctl databases sql-mode set [cluster_id] [ANSI_QUOTES] [STRICT_TRANS_TABLES]```

**获取 SQL 模式并指定输出格式**

```doctl databases sql-mode get [cluster_id] --format [SQLMode]```

# SYNOPSIS

**doctl** **databases** **sql-mode** _command_ [_options_]

# SUBCOMMANDS

**get**
> 获取 MySQL 数据库集群当前的 SQL 模式。

**set**
> 为 MySQL 数据库集群设置 SQL 模式。以空格分隔的参数提供一个或多个模式。

# PARAMETERS

**--format** _columns_
> 以逗号分隔的输出列列表。

**--no-header**
> 返回不带表头的原始数据。

# DESCRIPTION

**doctl databases sql-mode** 管理 DigitalOcean 托管 MySQL 数据库集群的 SQL 模式设置。SQL 模式控制 MySQL 如何处理查询语法验证、数据类型转换和错误情况。

常见的 SQL 模式包括 STRICT_TRANS_TABLES（拒绝无效数据）、ANSI_QUOTES（将双引号视为标识符引号）、NO_ZERO_DATE（不允许 '0000-00-00' 日期）以及 ONLY_FULL_GROUP_BY（要求 GROUP BY 包含所有非聚合列）。

设置 SQL 模式会完全替换现有配置，而不是在其基础上追加。要添加一个模式，应先用 **get** 获取当前的模式，然后在 **set** 命令中把它们全部列出。

# SEE ALSO

[doctl-databases](/man/doctl-databases)(1), [doctl](/man/doctl)(1), [mysql](/man/mysql)(1)
