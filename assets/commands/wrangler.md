# TAGLINE

Cloudflare Workers CLI 工具

# TLDR

**创建新的 Worker 项目**

```wrangler init [project-name]```

**启动本地开发服务器**

```wrangler dev```

**将 Worker 部署到 Cloudflare**

```wrangler deploy```

**登录 Cloudflare 账户**

```wrangler login```

**列出 KV 命名空间**

```wrangler kv namespace list```

**创建 KV 命名空间**

```wrangler kv namespace create [namespace-name]```

实时**追踪 Worker 日志**

```wrangler tail [worker-name]```

从配置**生成类型定义**

```wrangler types```

# SYNOPSIS

**wrangler** _command_ [_subcommand_] [_options_]

# PARAMETERS

**init** [_name_]
> 创建新的 Worker 项目，名称可选。

**dev**
> 启动支持热重载的本地开发服务器。

**deploy**
> 将 Worker 部署到 Cloudflare 全球网络。

**publish**
> deploy 的别名（已废弃）。

**login**
> 通过浏览器向 Cloudflare 账户进行身份验证。

**logout**
> 撤销本地身份验证。

**whoami**
> 显示当前登录用户的信息。

**tail** [_worker_]
> 流式查看已部署 Worker 的实时日志。

**kv namespace** _action_
> 管理 Workers KV 命名空间（list、create、delete）。

**kv key** _action_
> 管理 KV 键值对（put、get、delete、list）。

**r2 bucket** _action_
> 管理 R2 存储桶。

**d1** _action_
> 管理 D1 数据库。

**secret put** _name_
> 创建或更新加密的密钥。

**types**
> 根据 wrangler.toml 配置生成 TypeScript 类型。

**--config** _file_
> 指定配置文件路径。

**--env** _environment_
> 以指定环境为目标。

# DESCRIPTION

**Wrangler** 是 Cloudflare 开发者平台的命令行界面，用于创建、开发、测试和部署 Cloudflare Workers，并管理 KV 存储、R2 对象存储、D1 数据库和 Queues 等相关服务。

该工具提供一个模拟 Cloudflare Workers 运行时的本地开发服务器，无需部署到生产环境即可快速迭代。它负责打包 JavaScript 和 TypeScript 代码、管理密钥以及配置到其他 Cloudflare 服务的绑定。

配置通过项目根目录下的 wrangler.toml（或 wrangler.json）管理，定义 Worker 的名称、入口文件、兼容性设置和服务绑定。Wrangler 支持多环境，便于预发布与生产部署。

# CAVEATS

需要 Node.js 18 或更高版本。本地开发环境可能与生产环境的 Cloudflare 边缘运行时存在细微差异。某些功能需要相应套餐级别的 Cloudflare 账户。API 操作受速率限制约束。

# HISTORY

**Wrangler** 最初由 **Cloudflare** 于 **2019 年**开发，用于支持 Workers 无服务器平台。版本 1 使用 Rust 编写，而 **Wrangler 2**（于 **2022 年**发布）改用 TypeScript 重写，以便更好地融入 JavaScript 生态。该工具是开源 workers-sdk 仓库的一部分，目前仍在活跃开发并频繁发布新版本。

# INSTALL

```pacman: sudo pacman -S wrangler```

```nix: nix profile install nixpkgs#wrangler```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npx](/man/npx)(1), [node](/man/node)(1), [miniflare](/man/miniflare)(1)
