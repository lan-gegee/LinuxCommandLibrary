# TAGLINE

Node.js 生产环境进程管理器

# TLDR

**启动应用**

```pm2 start [app.js]```

**以指定名称启动**

```pm2 start [app.js] --name "[app_name]"```

**列出进程**

```pm2 list```

**停止进程**

```pm2 stop [name|id]```

**重启进程**

```pm2 restart [name|id]```

**查看日志**

```pm2 logs```

**监视进程**

```pm2 monit```

# SYNOPSIS

**pm2** [_command_] [_options_]

# PARAMETERS

**start** _APP_
> 启动应用。

**stop** _ID_
> 停止进程。

**restart** _ID_
> 重启进程。

**list**
> 列出进程。

**logs**
> 查看日志。

**monit**
> 监视仪表盘。

**--name** _NAME_
> 进程名称。

# DESCRIPTION

**pm2** 是面向 Node.js 应用的生产环境进程管理器。它让应用持续运行，崩溃时自动重启，通过集群模式内置负载均衡，并提供集中式日志管理。

该工具提供监视仪表盘（**monit**）、进程列表、日志查看以及用于开机自启的启动脚本生成功能。它可以同时管理多个应用，每个应用都可以独立配置实例数、环境变量和重启策略。

# CONFIGURATION

**ecosystem.config.js**
> 应用配置文件，定义进程、环境变量和部署设置。

**~/.pm2/**
> PM2 主目录，存放日志、进程数据库和模块数据。

**PM2_HOME**
> 用于覆盖默认 PM2 主目录的环境变量。

# CAVEATS

仅适用于 Node.js。需要 npm install。基于守护进程运行。

# HISTORY

PM2 为 **生产环境的 Node.js** 进程管理而生。

# INSTALL

```pacman: sudo pacman -S pm2```

```nix: nix profile install nixpkgs#pm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[node](/man/node)(1), [forever](/man/forever)(1), [nodemon](/man/nodemon)(1)
