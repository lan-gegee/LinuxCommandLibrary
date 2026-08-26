# TAGLINE

面向 Hadoop 的数据仓库系统

# TLDR

**启动 Hive shell**

```hive```

**执行查询**

```hive -e "SELECT * FROM [table]"```

**运行脚本文件**

```hive -f [script.hql]```

**设置配置**

```hive --hiveconf [key=value]```

**静默模式**

```hive -S -e "[query]"```

# SYNOPSIS

**hive** [_options_]

# PARAMETERS

**-e** _QUERY_
> 执行查询。

**-f** _FILE_
> 执行脚本文件。

**-S**, **--silent**
> 静默模式。

**--hiveconf** _KEY=VALUE_
> 设置配置。

**--database** _DB_
> 使用指定数据库。

**-i** _FILE_
> 初始化文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**Hive** 是面向 Hadoop 的数据仓库系统。它提供类 SQL 的查询语言（HiveQL），用于查询存储在 HDFS 中的大型数据集。

该工具将查询转换为 MapReduce、Tez 或 Spark 作业。它用于大数据平台上的数据分析和 ETL。

# CAVEATS

需要 Hadoop 集群。查询延迟高于 RDBMS。采用读时模式（schema on read）。

# HISTORY

Apache Hive 由 **Facebook** 开发，后贡献给 **Apache** 项目，用于基于 SQL 的大数据分析。

# INSTALL

```brew: brew install hive```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[beeline](/man/beeline)(1), [yarn](/man/yarn)(1), [impala](/man/impala)(1)
