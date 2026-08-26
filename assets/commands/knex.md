# TAGLINE

Node 的 SQL 查询构建器

# TLDR

**初始化 Knex 项目**

```npx knex init```

**创建迁移**

```npx knex migrate:make [migration_name]```

**执行迁移**

```npx knex migrate:latest```

**回滚迁移**

```npx knex migrate:rollback```

**创建种子文件**

```npx knex seed:make [seed_name]```

**运行种子文件**

```npx knex seed:run```

**显示迁移状态**

```npx knex migrate:status```

# SYNOPSIS

**npx knex** _command_ [_options_]

# PARAMETERS

**init**
> 创建 knexfile.js 配置文件。

**migrate:make** _name_
> 创建新迁移。

**migrate:latest**
> 执行待处理的迁移。

**migrate:rollback**
> 撤销最近一批迁移。

**migrate:status**
> 显示迁移状态。

**seed:make** _name_
> 创建种子文件。

**seed:run**
> 运行种子文件。

**migrate:up** [_filename_]
> 执行下一个待处理迁移（或指定名称的迁移）。

**migrate:down** [_filename_]
> 回滚最近一次已完成的迁移（或指定名称的迁移）。

**migrate:list**
> 列出已完成和待处理的迁移。

**migrate:unlock**
> 强制释放迁移锁（在迁移运行崩溃后使用）。

**--env** _ENVIRONMENT_
> 选择要使用的 **knexfile** 配置段（默认：_development_，或 **NODE_ENV**）。

**--knexfile** _PATH_
> 指定自定义的 knexfile 路径。

**--client** _DIALECT_
> 覆盖数据库客户端方言。

**--debug**
> 在 SQL 语句执行时将其打印出来。

# DESCRIPTION

**Knex.js** 是 Node.js 的 SQL 查询构建器。该 CLI 管理数据库迁移和种子数据，为模式变更提供版本控制。

Knex 支持 PostgreSQL、MySQL、SQLite3 等数据库。迁移定义模式变更；种子填充测试数据。

# KNEXFILE EXAMPLE

```javascript
module.exports = {
  development: {
    client: 'postgresql',
    connection: {
      database: 'mydb',
      user: 'user',
      password: 'password'
    },
    migrations: {
      tableName: 'knex_migrations'
    }
  }
};
```

# CAVEATS

执行迁移需要数据库连接。回滚可能导致数据丢失。种子文件的执行顺序没有保证。请先在副本上测试迁移。

# HISTORY

Knex 由 **Tim Griesser** 创建，是 Node.js 上灵活的 SQL 查询构建器。它是 Objection.js 等 ORM 的基础。

# SEE ALSO

[node](/man/node)(1), [prisma](/man/prisma)(1), [sequelize](/man/sequelize)(1)
