# TAGLINE

对存储在 Amazon S3 中的数据运行 SQL 查询

# TLDR

**启动查询执行**

```aws athena start-query-execution --query-string "[SELECT * FROM table LIMIT 10]" --work-group [primary]```

带输出位置**启动查询**

```aws athena start-query-execution --query-string "[SELECT * FROM logs]" --result-configuration OutputLocation=s3://[bucket/results/]```

**获取查询执行状态**

```aws athena get-query-execution --query-execution-id [query-id]```

**获取查询结果**

```aws athena get-query-results --query-execution-id [query-id]```

**列出查询执行记录**

```aws athena list-query-executions --work-group [primary]```

**创建数据库**

```aws athena start-query-execution --query-string "CREATE DATABASE [mydb]" --work-group [primary]```

**列出**数据目录中的数据库

```aws athena list-databases --catalog-name AwsDataCatalog```

# SYNOPSIS

**aws athena** _command_ [_options_]

# PARAMETERS

**start-query-execution**
> 异步执行 SQL 查询

**get-query-execution**
> 获取查询执行的信息

**get-query-results**
> 检索已完成查询的结果

**stop-query-execution**
> 取消正在运行的查询

**list-query-executions**
> 列出查询执行 ID

**list-databases**
> 列出数据目录中的数据库

**list-table-metadata**
> 列出数据库中的表

**create-work-group**
> 创建用于查询的工作组

**get-work-group**
> 获取工作组配置

**--query-string** _sql_
> 要执行的 SQL 语句

**--query-execution-id** _id_
> 查询执行的标识符

**--work-group** _name_
> 运行查询所用的工作组

**--query-execution-context** _context_
> 数据库和数据目录上下文（Database=db,Catalog=catalog）

**--result-configuration** _config_
> 输出位置和加密设置（OutputLocation=s3://path/）

**--max-results** _n_
> 返回结果的最大数量

**--next-token** _token_
> 上一次响应返回的分页令牌

**--catalog-name** _name_
> 要查询的数据目录（如 AwsDataCatalog）

# DESCRIPTION

**aws athena** 管理 Amazon Athena——一项使用标准 SQL 分析 Amazon S3 中数据的交互式查询服务。Athena 无服务器化运行，无需搭建任何基础设施。

查询通过 **start-query-execution** 异步执行，它会返回一个查询执行 ID。使用 **get-query-execution** 检查状态，完成后使用 **get-query-results** 检索结果。结果同时也会存储在指定的 S3 输出位置中。

工作组用于组织查询，并控制结果位置、加密和查询限制等设置。**--query-execution-context** 参数指定要查询哪个数据库和数据目录。

Athena 使用 AWS Glue Data Catalog 存储表元数据，也可以使用外部的 Hive metastore。表通过 CREATE EXTERNAL TABLE 等 DDL 语句建立在 S3 数据之上。

# CAVEATS

查询按扫描的数据量计费；请使用分区和列式格式（Parquet、ORC）来降低成本。查询结果会在配置的保留期后过期。长时间运行的查询可能超时。访问 S3 数据和 Glue 目录需要相应的 IAM 权限。

# HISTORY

**Amazon Athena** 于 **2016 年 11 月**推出，是基于 Presto 的无服务器查询服务。它让用户无需配置基础设施即可对 S3 数据执行 SQL 查询。Athena 与 AWS Glue 集成以实现 schema 发现，支持 ANSI SQL 并针对分析工作负载常见的嵌套数据类型做了扩展。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-s3](/man/aws-s3)(1), [aws-glue](/man/aws-glue)(1)
