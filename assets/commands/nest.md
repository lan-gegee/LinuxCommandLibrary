# TAGLINE

NestJS——渐进式 Node 框架的 CLI

# TLDR

**创建新项目**

```nest new [project-name]```

**生成控制器**

```nest generate controller [name]```

**生成服务**

```nest generate service [name]```

**生成模块**

```nest generate module [name]```

**生成资源**（完整 CRUD）

```nest generate resource [name]```

**启动开发服务器**

```nest start --watch```

**构建生产版本**

```nest build```

**显示帮助**

```nest --help```

# SYNOPSIS

**nest** [_new_] [_generate_] [_start_] [_build_] [_options_] [_args_]

# PARAMETERS

**new** _NAME_
> 创建新项目。

**generate**, **g** _TYPE_ _NAME_
> 生成组件。

**start**
> 启动应用。

**build**
> 构建应用。

**info**
> 显示项目信息。

**add** _LIBRARY_
> 添加 NestJS 库。

**--watch**, **-w**
> 开发用的监视模式。

**--prod**
> 构建生产版本。

**--flat**
> 不为生成的文件创建目录。

**--spec**
> 生成 spec 测试文件（默认 true）。

**--no-spec**
> 跳过 spec 文件生成。

**--dry-run**, **-d**
> 只报告将要执行的操作而不写入。

**--skip-git**
> 跳过 git 初始化。

# DESCRIPTION

**nest** 是 NestJS 的 CLI，NestJS 是用于构建服务端应用的渐进式 Node.js 框架。它按照 NestJS 约定生成项目和组件。

新项目包含 TypeScript 配置、测试环境设置和 NestJS 模块结构。生成器可创建控制器、服务、模块等组件。

资源生成器会创建完整的 CRUD 功能，包括控制器、服务、DTO 和实体。它可以生成 REST、GraphQL 或 WebSocket 资源。

开发服务器支持热重载。代码变更会触发自动重启。生产构建则针对部署进行优化。

模块化架构将关注点分离到各模块中，每个模块包含相关的控制器、服务和提供者。CLI 会维护这种结构。

NestJS 支持 Express 或 Fastify 作为底层 HTTP 服务器，通过装饰器实现路由和依赖注入。

# CAVEATS

需要 Node.js 16 及以上版本。生成的代码使用 TypeScript。某些功能需要额外的软件包。装饰器和依赖注入有一定学习曲线。

# HISTORY

**NestJS** 由 **Kamil Myśliwiec** 于 **2017 年**创建，其架构灵感来自 Angular。它把 Angular 风格的依赖注入和装饰器引入 Node.js 后端开发。该 CLI 提供类似 Rails 的代码生成能力。

# INSTALL

```dnf: sudo dnf install nest```

```brew: brew install nest```

```nix: nix profile install nixpkgs#nest```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[node](/man/node)(1), [npm](/man/npm)(1), [express](/man/express)(1)
