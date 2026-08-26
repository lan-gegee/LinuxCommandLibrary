# TAGLINE

Supabase 本地开发与部署 CLI

# TLDR

**初始化项目**

```supabase init```

**启动本地开发环境**

```supabase start```

**停止本地服务**

```supabase stop```

**生成类型定义**

```supabase gen types typescript --local```

**创建迁移**

```supabase migration new [migration_name]```

**应用迁移**

```supabase db push```

**链接到项目**

```supabase link --project-ref [project-id]```

**查看状态**

```supabase status```

# SYNOPSIS

**supabase** _command_ [_options_]

# PARAMETERS

**init**
> 初始化项目。

**start**
> 启动本地堆栈。

**stop**
> 停止本地堆栈。

**link**
> 链接到远程项目。

**db push**
> 推送迁移。

**gen types**
> 生成类型定义。

**migration new** _NAME_
> 创建迁移。

**status**
> 显示状态。

**--project-ref** _ID_
> 项目引用 ID。

# DESCRIPTION

**supabase** 是用于管理 Supabase 项目的命令行界面。Supabase 是构建在 PostgreSQL 之上的开源 Firebase 替代品。该 CLI 提供本地开发、数据库迁移管理、类型生成以及部署到托管 Supabase 项目的工具。

本地开发环境通过 Docker 运行完整的 Supabase 堆栈，包括 PostgreSQL、认证服务、对象存储、实时订阅和 Edge Functions。这样无需远程项目就能在与生产环境等同的环境中开发和测试。

数据库迁移将 schema 变更纳入版本控制。CLI 可以从数据库 schema 生成 TypeScript 类型，实现类型安全的客户端代码。link 操作将本地项目连接到托管的 Supabase 实例，以便将迁移和 Edge Functions 部署到生产环境。

# CAVEATS

本地开发需要 Docker。项目必须存在于 Supabase 上。受免费套餐限制约束。

# HISTORY

**Supabase** 是一个开源的 Firebase 替代品，于 **2020 年**推出。该 CLI 支持本地开发和自托管。

# INSTALL

```brew: brew install supabase```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [psql](/man/psql)(1), [firebase](/man/firebase)(1)
