# TAGLINE

带编译期检查的 Rust SQL 工具集

# TLDR

**创建数据库**

```sqlx database create```

**运行迁移**

```sqlx migrate run```

**创建迁移**

```sqlx migrate add [migration_name]```

**回滚迁移**

```sqlx migrate revert```

**准备离线数据**

```sqlx prepare```

**检查查询**

```sqlx prepare --check```

# SYNOPSIS

**sqlx** _command_ [_options_]

# PARAMETERS

**database**
> 数据库操作。

**migrate**
> 迁移命令。

**prepare**
> 为离线模式做准备。

**--database-url** _URL_
> 连接字符串。

**add**
> 添加迁移。

**run**
> 运行迁移。

# DESCRIPTION

**sqlx** 是 SQLx（Rust SQL 工具集）的命令行工具，提供数据库迁移管理和编译期查询验证。它支持 PostgreSQL、MySQL、MariaDB 和 SQLite。

迁移系统会创建带版本的 SQL 脚本来跟踪模式变更，并提供创建、运行和回滚迁移的命令。**prepare** 命令将查询元数据缓存到 JSON 文件，从而在 Rust 代码中对 SQL 查询进行编译期类型检查，构建期间无需连接真实数据库。

所有操作都需要 **DATABASE_URL** 环境变量或 **.env** 文件指定数据库连接字符串。

# CONFIGURATION

**DATABASE_URL**
> 指定数据库连接字符串的环境变量（例如 postgres://user:pass@host/db、sqlite:data.db）。

**.env**
> 可定义 DATABASE_URL 的项目级文件；sqlx 命令会自动加载它。

# CAVEATS

面向 Rust 开发的工具。需要 DATABASE_URL。支持编译期检查。

# HISTORY

**sqlx** 是一个 Rust SQL 工具集，提供编译期检查的查询和数据库迁移能力。

# INSTALL

```apk: sudo apk add sqlx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[diesel](/man/diesel)(1), [psql](/man/psql)(1), [sqlite3](/man/sqlite3)(1)
