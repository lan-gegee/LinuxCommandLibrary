# TAGLINE

Rust ORM 命令行工具

# TLDR

**初始化数据库**（不存在则创建）

```diesel setup```

**生成新的迁移**

```diesel migration generate [migration_name]```

**执行待运行的迁移**

```diesel migration run```

**回滚最近一次迁移**

```diesel migration revert```

**打印当前 schema**

```diesel print-schema```

**从数据库生成 schema.rs**

```diesel print-schema > src/schema.rs```

**检查迁移状态**

```diesel migration list```

# SYNOPSIS

**diesel** _command_ [_options_]

# PARAMETERS

**setup**
> 创建数据库并运行迁移。

**migration generate** _name_
> 创建新的迁移文件。

**migration run**
> 运行所有待执行的迁移。

**migration revert**
> 回滚最近一次迁移。

**migration redo**
> 回滚并重新运行最近一次迁移。

**migration list**
> 列出所有迁移及其状态。

**print-schema**
> 以 Rust 代码形式输出数据库 schema。

**database setup**
> 创建数据库。

**database reset**
> 删除并重建数据库。

**--database-url** _url_
> 数据库连接 URL。

**--config-file** _file_
> diesel.toml 的路径。

**--migration-dir** _dir_
> 存放迁移的目录。

# DESCRIPTION

**Diesel CLI** 是 Diesel ORM 的命令行工具。Diesel 是一个安全、可扩展的 Rust ORM 和查询构建器。该工具管理数据库迁移，并生成表示数据库 schema 的 Rust 代码。

迁移是 migrations 目录中的 SQL 文件，包含用于应用和回滚更改的 "up" 和 "down" 文件。CLI 会在数据库表中跟踪已应用的迁移。

**print-schema** 命令会内省数据库并生成 Rust 代码（schema.rs），Diesel 用它进行编译期查询校验。这确保查询会针对实际数据库结构进行类型检查。

# CONFIGURATION

**diesel.toml**：
```toml
[print_schema]
file = "src/schema.rs"
with_docs = true

[migrations_directory]
dir = "migrations"
```

# CAVEATS

需要数据库驱动库（PostgreSQL 用 libpq，MySQL 用 libmysqlclient）。必须设置 DATABASE_URL 环境变量或 --database-url。schema 生成需要可访问的数据库。迁移 SQL 因数据库后端而异。

# HISTORY

Diesel 由 **Sean Griffin**（同时也是 Ruby on Rails 的贡献者）创建，于 **2015** 年首次发布。其设计目标是利用 Rust 的类型系统保障数据库安全。该 CLI 工具提供了类似 ActiveRecord 或 Knex 的迁移管理功能。Diesel 已成为最受欢迎的 Rust 数据库库之一。

# INSTALL

```brew: brew install diesel```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sqlx](/man/sqlx)(1), [cargo](/man/cargo)(1)
