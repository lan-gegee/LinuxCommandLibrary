# TAGLINE

具有类型安全数据库访问的 Node.js ORM

# TLDR

**初始化 Prisma**

```npx prisma init```

**生成客户端**

```npx prisma generate```

**运行迁移**

```npx prisma migrate dev```

**将 schema 推送到数据库**

```npx prisma db push```

**打开 Prisma Studio**

```npx prisma studio```

# SYNOPSIS

**prisma** _command_ [_options_]

# PARAMETERS

**init**
> 在项目中初始化 Prisma。

**generate**
> 生成 Prisma Client。

**migrate dev**
> 创建并应用迁移。

**migrate deploy**
> 应用待处理的迁移。

**db push**
> 不经迁移直接推送 schema。

**db pull**
> 内省数据库。

**studio**
> 打开可视化编辑器。

**format**
> 格式化 schema 文件。

# DESCRIPTION

**Prisma** 是面向 Node.js 和 TypeScript 的新一代 ORM。它提供类型安全的数据库访问、自动化迁移以及可视化数据库浏览器。

# EXAMPLES

```bash
# Initialize new project
npx prisma init

# After schema changes
npx prisma generate

# Development migration
npx prisma migrate dev --name add_users

# Production deployment
npx prisma migrate deploy

# Reset database
npx prisma migrate reset

# Introspect existing DB
npx prisma db pull
```

# SCHEMA EXAMPLE

```prisma
model User {
  id    Int     @id @default(autoincrement())
  email String  @unique
  name  String?
  posts Post[]
}
```

# CAVEATS

需要 Node.js。schema 位于 schema.prisma。修改 schema 后需重新生成。

# HISTORY

Prisma 由 **Johannes Schickling** 和 **Søren Bramer Schmidt** 于 2016 年创立，由 Graphcool 演化而来。

# SEE ALSO

[sequelize](/man/sequelize)(1), [typeorm](/man/typeorm)(1), [knex](/man/knex)(1)
