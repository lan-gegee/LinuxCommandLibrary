# TAGLINE

通用数据库工具与 SQL 客户端

# TLDR

**启动 DBeaver** 图形界面

```dbeaver```

**打开指定的数据库**连接

```dbeaver -con "name=[connection_name]"```

**以内联参数连接**

```dbeaver -con "driver=postgresql|host=localhost|database=mydb"```

**打开 SQL 文件**并将其关联到数据源

```dbeaver -con "name=[connection]" -f [script.sql]```

**运行已保存的任务**（如数据导出任务）

```dbeaver -runTask "@[project]:[task]"```

**停止正在运行的 DBeaver** 实例

```dbeaver -stop```

# SYNOPSIS

**dbeaver** [_options_]

# PARAMETERS

**-con** _CONNECTION_
> 连接参数（名称、驱动、主机、数据库、用户等）。

**-f** _FILE_
> 在 DBeaver UI 中打开文件；配合 -con 时将其关联到数据源。

**-runTask** _@PROJECT:TASK_
> 执行已保存的任务；返回表示成功或失败的退出码。

**-var** _NAME=VALUE_
> 为 -runTask 设置变量（可重复使用）。

**-stop**
> 退出正在运行的 DBeaver 实例。

**-nosplash**
> 启动时不显示启动画面。

**-data** _DIR_
> 工作区目录位置。

**-nl** _LOCALE_
> 覆盖系统区域设置。

**-clean**
> 清除缓存数据后全新启动。

**--help**
> 显示帮助信息。

# DESCRIPTION

**DBeaver** 是一款面向开发者和数据库管理员的免费通用数据库工具与 SQL 客户端。它通过 JDBC 驱动支持众多数据库，包括 PostgreSQL、MySQL、MariaDB、SQLite、Oracle、SQL Server 等。

该应用提供图形化的数据库管理界面，包括带语法高亮和自动补全的 SQL 编辑器、可视化查询构建器、ER 图、数据导入导出以及模式比较。它还支持 MongoDB 和 Cassandra 等 NoSQL 数据库。

DBeaver 的命令行可以在 UI 中打开连接和文件，并通过 -runTask 执行已保存的任务（如数据导出或备份任务），这是官方支持的 DBeaver 自动化方式。

# CAVEATS

需要 Java 运行时环境。部分企业功能需要付费的企业版。大结果集可能占用大量内存。连接配置保存在工作区中，版本升级时可能需要迁移。

# HISTORY

DBeaver 由 **Serge Rider** 创建并于 **2010 年**首次发布。它最初只是一个简单的数据库查看器，后来演化为功能全面的数据库管理工具。该项目由 DBeaver Corp 维护，提供社区版和企业版。

# INSTALL

```pacman: sudo pacman -S dbeaver```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mysql](/man/mysql)(1), [psql](/man/psql)(1), [sqlite3](/man/sqlite3)(1)

# RESOURCES

```[Source code](https://github.com/dbeaver/dbeaver)```

```[Homepage](https://dbeaver.io)```

```[Documentation](https://dbeaver.com/docs/dbeaver/)```

<!-- verified: 2026-07-11 -->
