# TAGLINE

在 Railway 平台上部署和管理应用

# TLDR

**登录 Railway**

```railway login```

**初始化新项目**

```railway init```

**关联到已有的 Railway 项目**

```railway link```

**部署当前目录**

```railway up```

**带 Railway 环境变量运行命令**

```railway run [command]```

**打开带 Railway 环境变量的 Shell**

```railway shell```

**查看项目日志**

```railway logs```

**在 Railway 控制台中打开项目**

```railway open```

# SYNOPSIS

**railway** _command_ [_options_]

# PARAMETERS

**login**
> 向 Railway 进行身份验证

**logout**
> 退出 Railway 登录

**init**
> 创建新的 Railway 项目

**link**
> 将当前目录关联到已有的 Railway 项目

**up**
> 将当前目录部署到 Railway

**run** _command_
> 注入 Railway 环境变量运行本地命令

**shell**
> 打开带 Railway 环境变量的新 Shell

**logs**
> 查看部署日志

**open**
> 在 Railway 网页控制台中打开项目

**status**
> 显示已关联项目的状态

**variables**
> 管理环境变量

**service**
> 管理项目内的服务

**volume**
> 管理持久化卷

**domain**
> 管理自定义域名

**ssh**
> 打开到已部署服务的 SSH 会话

**--help**, **-h**
> 显示帮助信息

**--version**, **-v**
> 显示版本号

# DESCRIPTION

**railway** 是 Railway 的命令行界面。Railway 是一个用于部署和托管应用的云平台。它让开发者能够直接从终端部署代码、管理环境变量并与 Railway 项目交互。

该 CLI 通过自动检测项目类型并配置构建设置来支持零配置部署。它与 git 工作流集成，可以从本地目录或已连接的仓库进行部署。

一个关键特性是能够使用 **railway run** 在本地以生产环境变量运行开发，确保开发环境与已部署环境的一致性。

# CONFIGURATION

**~/.railway/config.json**
> 本地身份验证和项目关联配置，存储 API 令牌和项目引用。

**RAILWAY_TOKEN**
> 用于 API 身份验证的环境变量，适用于无法交互式登录的 CI/CD 流水线。

# CAVEATS

需要 Railway 账号并通过 **railway login** 完成认证后，大多数命令才能使用。

目录必须先通过 **railway link** 关联或通过 **railway init** 初始化，才能在其中使用部署命令。

免费套餐有资源限制。请查阅 Railway 的定价文档了解部署限制和使用配额。

# HISTORY

Railway 成立于 **2020 年**，是传统平台即服务（PaaS）提供商的现代替代品。CLI 与平台同步开发，旨在以最少的配置提供对开发者友好的部署体验。该工具开源并在 GitHub 上持续维护。

# INSTALL

```pacman: sudo pacman -S railway```

```apk: sudo apk add railway```

```brew: brew install railway```

```nix: nix profile install nixpkgs#railway```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [heroku](/man/heroku)(1), [fly](/man/fly)(1), [vercel](/man/vercel)(1)
