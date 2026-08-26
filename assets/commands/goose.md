# TAGLINE

数据库迁移工具

# TLDR

**创建**新的迁移

```goose create [migration-name] [sql|go]```

**应用**迁移

```goose up```

**回滚**上一次迁移

```goose down```

**检查**迁移状态

```goose status```

# SYNOPSIS

**goose** [_options_] _command_

# PARAMETERS

**up**
> 执行向上迁移

**up-by-one**
> 向上迁移一个版本

**down**
> 执行向下回退

**down-to** _VERSION_
> 回退到指定版本

**status**
> 显示迁移状态

**create** _NAME_ _TYPE_
> 创建新迁移（sql 或 go）

**fix**
> 为迁移文件应用连续顺序编号

**version**
> 打印 goose 版本

**-dir** _DIR_
> 迁移文件所在目录（默认：migrations）

**-table** _TABLE_
> 迁移记录表名（默认：goose_db_version）

**-s, --allow-missing**
> 允许存在缺失的迁移

**-v, --version**
> 显示版本并退出

**-h, --help**
> 显示帮助并退出

# DESCRIPTION

**goose** 是一个数据库迁移工具，同时支持 SQL 和 Go 两种迁移形式。它通过给迁移文件建立版本顺序并跟踪哪些迁移已经应用，来管理数据库模式的变更。

该工具支持 PostgreSQL、MySQL、SQLite、SQL Server 等多种数据库，为模式迁移提供一致的接口。

# DATABASE DRIVERS

支持的数据库：
- PostgreSQL
- MySQL/MariaDB
- SQLite3
- SQL Server
- ClickHouse
- Redshift
- TiDB
- Turso

# CAVEATS

需要数据库连接。迁移文件必须遵循命名约定。向下回退的迁移应经过仔细测试。并发执行迁移时可能需要加锁。

# HISTORY

**goose** 的设计目标是一个语言无关的迁移工具，同时支持 SQL 和基于 Go 的迁移，填补了 Go 开发者在数据库迁移方面的空白。

# INSTALL

```dnf: sudo dnf install goose```

```brew: brew install goose```

```nix: nix profile install nixpkgs#goose```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[migrate](https://github.com/golang-migrate/migrate), [dbmate](https://github.com/amacneil/dbmate), [flyway](https://flywaydb.org/), [liquibase](https://www.liquibase.org/)
