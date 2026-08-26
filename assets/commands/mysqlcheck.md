# TAGLINE

检查、修复和优化 MySQL 表

# TLDR

**检查数据库中的所有表**

```mysqlcheck -u [user] -p [database]```

**检查所有数据库**

```mysqlcheck -u [user] -p --all-databases```

**修复表**

```mysqlcheck -u [user] -p --repair [database]```

**优化表**

```mysqlcheck -u [user] -p --optimize [database]```

**分析表**

```mysqlcheck -u [user] -p --analyze [database]```

**检查指定的表**

```mysqlcheck -u [user] -p [database] [table]```

**自动修复**

```mysqlcheck -u [user] -p --auto-repair [database]```

# SYNOPSIS

**mysqlcheck** [_options_] [_database_] [_tables_]

# PARAMETERS

_DATABASE_
> 数据库名。

_TABLES_
> 要检查的特定表。

**--all-databases**
> 检查所有数据库。

**--repair**
> 修复损坏的表。

**--optimize**
> 优化表。

**--analyze**
> 分析表。

**--auto-repair**
> 自动修复问题。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mysqlcheck** 用于检查、修复和优化 MySQL 表。它维护数据库的完整性。

该工具运行 CHECK、REPAIR、ANALYZE 和 OPTIMIZE。是数据库维护的必备工具。

# CAVEATS

可能锁定表。修复前请先备份。某些存储引擎不支持所有操作。

# HISTORY

mysqlcheck 是 **MySQL** 发行版的组成部分，用于表维护和修复操作。

# INSTALL

```apk: sudo apk add mariadb-client```

```zypper: sudo zypper install mariadb-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mysql](/man/mysql)(1), [mysqladmin](/man/mysqladmin)(1), [mysqldump](/man/mysqldump)(1)
