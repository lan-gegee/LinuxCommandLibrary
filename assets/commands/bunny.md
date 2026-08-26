# TAGLINE

bunny.net 官方命令行界面

# TLDR

**认证** CLI 并绑定你的 bunny.net 账户

```bunny login```

**部署**当前项目为 Magic Containers 应用

```bunny apps deploy```

**列出**你账户中的数据库

```bunny db list```

**通过 shell 安装脚本安装** CLI

```curl -fsSL https://cli.bunny.net/install.sh | sh```

**通过 npm 全局安装** CLI

```npm install -g @bunny.net/cli```

**显示**帮助并列出可用的子命令

```bunny --help```

# SYNOPSIS

**bunny** _command_ [_subcommand_] [_options_]

# PARAMETERS

**login**
> 将本地 CLI 与 bunny.net 账户进行认证；令牌会存储在本地供后续命令使用。

**apps deploy**
> 构建当前项目并部署到 **Magic Containers**。自动预置基础设施、全球扩缩容并路由流量。

**db list**
> 列出活跃账户关联的数据库（包括 bunny.net 的边缘数据库产品）。

**--help**, **-h**
> 打印 CLI 或特定子命令的帮助信息。

**--version**
> 打印版本信息。

# DESCRIPTION

**bunny** 是 **bunny.net** 的官方命令行客户端，提供对该平台开发者工具集的终端访问：**Magic Containers**、边缘数据库、存储桶、边缘脚本、DNS 区域和 CDN pull zone。它使用 **TypeScript** 实现，既以独立二进制文件分发，也以 npm 软件包 **@bunny.net/cli** 的形式发布。

该 CLI 的主要工作流包括登录、将应用部署到 Magic Containers（它会自动预置全球分布的运行时），以及管理数据库等配套资源。它是 bunny.net 迈向统一开发者体验的一部分，与之相伴的还有 **@bunny.net/api** 类型安全 SDK 和一键模板。

# CAVEATS

该 CLI 相对较新且仍在演进中——子命令和标志可能在版本之间发生变化。**bunny** 是 **BunnyWay/cli** 发布的二进制名称；还有几个不相关的社区项目也称自己为 "bunny CLI"（例如 **own3d/bunny-cli**、**straticus1/bunny-cli** 和 **simplesurance/bunny-cli**），每个都有各自的命令集。在排查问题前请确认安装的是哪个软件包。

# CONFIGURATION

执行 **bunny login** 后，凭据会被持久化到用户主目录（通常位于 **$XDG_CONFIG_HOME/bunny** 或 **~/.config/bunny** 下）。用于非交互式自动化的 API 令牌可通过各子命令定义的环境变量提供。

# HISTORY

**bunny** 由 **bunny.net** 在 GitHub 的 **BunnyWay/cli** 单体仓库中发布。它于 **2024 年**推出，旨在通过单一的可脚本化 CLI 暴露公司的开发者平台——尤其是 **Magic Containers** 产品。

# SEE ALSO

[curl](/man/curl)(1), [docker](/man/docker)(1), [flyctl](/man/flyctl)(1), [wrangler](/man/wrangler)(1)
