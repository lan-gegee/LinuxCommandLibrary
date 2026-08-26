# TAGLINE

Cradle PHP 框架的 CLI

# TLDR

**安装 Cradle 框架**

```cradle install```

**安装并强制覆盖文件**

```cradle install -f```

**创建新模块**

```cradle make:module [module_name]```

**运行数据库迁移**

```cradle migrate```

**从数据库表生成模型**

```cradle make:model [table_name]```

**启动开发服务器**

```cradle serve```

**清除应用缓存**

```cradle cache:clear```

# SYNOPSIS

**cradle** _command_ [_options_] [_arguments_]

# PARAMETERS

**install**
> 安装 Cradle 框架及其依赖。支持用 `-f`/`--force` 覆盖文件，以及 `--skip-sql`、`--skip-versioning`、`--skip-mkdir`、`--skip-chmod`。

**serve**
> 启动内置的开发服务器。

**migrate**
> 运行数据库迁移。

**make:module** _NAME_
> 生成新模块的脚手架。

**make:model** _TABLE_
> 从数据库表生成模型。

**make:controller** _NAME_
> 生成新的控制器。

**cache:clear**
> 清除应用缓存。

**queue:work**
> 处理队列中的任务。

**connect** _NAME_
> 连接到已配置的服务器。

**--help**
> 显示某个命令的帮助信息。

# DESCRIPTION

**Cradle** 是一个面向快速应用开发的 PHP 框架，注重模块化与开发者体验。该 CLI 工具提供用于脚手架生成、数据库管理和开发服务器操作的命令。

框架采用事件驱动架构，允许组件之间保持松耦合。模块可以独立开发，再插入到应用中使用。make 系列命令会按照框架约定生成样板代码。

Cradle CLI 承担常见开发任务，包括数据库迁移、根据现有 schema 生成模型以及缓存管理。借助内置服务器，本地开发无需配置外部 Web 服务器即可快速开始。

# CAVEATS

需要 PHP 7.4+ 和 Composer。数据库命令需要在框架设置中进行正确配置。开发服务器不适合用于生产环境。

# HISTORY

Cradle 是作为一个强调事件驱动编程和模块化的现代 PHP 框架而开发的。它源于 PHP 开发社区对兼顾约定与灵活性的框架的需求——既提供结构，又不过度施加约束。

# SEE ALSO

[composer](/man/composer)(1), [php](/man/php)(1), [artisan](/man/artisan)(1)
