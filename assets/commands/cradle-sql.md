# TAGLINE

通过 Cradle 框架执行 SQL 查询

# TLDR

**执行 SQL 查询**

```cradle sql "[SELECT * FROM users]"```

**从 SQL 文件运行查询**

```cradle sql --file [queries.sql]```

**在指定数据库连接上执行**

```cradle sql --connection [mysql] "[query]"```

**将表导出为 SQL 文件**

```cradle sql --export [table_name] > [backup.sql]```

**将 SQL 文件导入**数据库

```cradle sql --import [backup.sql]```

**显示所有表**

```cradle sql "SHOW TABLES"```

# SYNOPSIS

**cradle sql** [_options_] [_query_]

# PARAMETERS

_QUERY_
> 要执行的 SQL 查询。需用引号包裹。

**--file** _FILE_
> 从文件执行 SQL 命令。

**--connection** _NAME_
> 使用指定的数据库连接。

**--export** _TABLE_
> 将表数据导出为 SQL 语句。

**--import** _FILE_
> 将 SQL 文件导入数据库。

**--database** _NAME_
> 覆盖默认数据库。

**--format** _FORMAT_
> 输出格式：table、json、csv。

**--help**
> 显示帮助信息。

# DESCRIPTION

**cradle sql** 提供对 Cradle 框架中已配置数据库的直接 SQL 访问。它允许执行查询、导入/导出数据以及进行各类数据库操作，而无需单独的客户端。

该命令使用框架的数据库配置，支持应用设置中定义的多个连接。查询结果可以多种格式输出，适合直接显示或交给其他工具处理。

该工具适用于开发过程中的调试、数据检查和快速的数据库操作。它与 Cradle 应用的其余部分保持一致的身份验证与连接处理方式。

# CAVEATS

直接 SQL 访问会绕过应用层的校验。破坏性查询（DROP、DELETE、TRUNCATE）会直接执行而不经确认，除非框架本身加入了防护措施。在运行可能造成破坏的操作之前，务必备份数据。

# HISTORY

cradle sql 是作为 Cradle PHP 框架 CLI 工具的一部分开发的，目的是提供便捷的数据库访问途径。它沿用了其他 PHP 框架（如 Laravel 的 Artisan）中框架集成式数据库命令的模式。

# SEE ALSO

[cradle](/man/cradle)(1), [mysql](/man/mysql)(1), [psql](/man/psql)(1), [sqlite3](/man/sqlite3)(1)

# RESOURCES

```[Source code](https://github.com/CradlePHP/cradle)```

```[Homepage](https://cradlephp.github.io/)```

<!-- verified: 2026-06-23 -->
