# TAGLINE

TypeORM 数据库迁移与实体命令行工具

# TLDR

**初始化项目**

```typeorm init```

**生成迁移**

```typeorm migration:generate -n [MigrationName]```

**执行迁移**

```typeorm migration:run```

**回滚迁移**

```typeorm migration:revert```

**创建实体**

```typeorm entity:create -n [EntityName]```

**同步架构**

```typeorm schema:sync```

# SYNOPSIS

**typeorm** _command_ [_-n name_] [_options_]

# PARAMETERS

**init**
> 初始化项目。

**migration:generate**
> 生成迁移。

**migration:run**
> 执行迁移。

**migration:revert**
> 回滚最近一次迁移。

**entity:create**
> 创建实体。

**schema:sync**
> 同步数据库。

# DESCRIPTION

**typeorm** 是 TypeORM 的命令行界面。TypeORM 是一个支持 PostgreSQL、MySQL、SQLite 及其他数据库的 TypeScript 和 JavaScript ORM。它提供管理数据库迁移、生成实体脚手架和同步架构更改的工具。

迁移将数据库架构变更记录为可应用、可回滚的版本化文件。**migration:generate** 命令通过比较当前实体与数据库状态自动生成迁移文件。架构同步提供了一种更简单的方式，直接更新数据库以匹配实体定义。

该 CLI 还支持用样板配置和实体文件初始化新项目。

# CAVEATS

需要 TypeScript/Node.js。需要配置文件。需要数据库连接。

# HISTORY

**TypeORM** 是面向 TypeScript 和 JavaScript 的 ORM，其 CLI 提供数据库管理操作。

# SEE ALSO

[prisma](/man/prisma)(1), [knex](/man/knex)(1), [sequelize](/man/sequelize)(1)
