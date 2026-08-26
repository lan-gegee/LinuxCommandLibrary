# TAGLINE

Ghost 发布平台的命令行界面

# TLDR

**在开发模式下启动 Ghost**

```ghost start```

**在生产模式下启动**

```ghost start --production```

**停止 Ghost**

```ghost stop```

**重启 Ghost**

```ghost restart```

**查看状态**

```ghost status```

**安装 Ghost**

```ghost install```

**更新 Ghost**

```ghost update```

# SYNOPSIS

**ghost** _command_ [_options_]

# SUBCOMMANDS

**install**
> 安装 Ghost。

**start**
> 启动 Ghost。

**stop**
> 停止 Ghost。

**restart**
> 重启 Ghost。

**status**
> 显示状态。

**update**
> 更新 Ghost。

**setup**
> 配置 Ghost。

**config**
> 查看/设置配置。

**log**
> 查看日志。

**doctor**
> 检查安装状况。

**run**
> 不经进程管理器直接启动 Ghost（用于调试）。

**backup**
> 创建站点数据的 zip 备份。

**uninstall**
> 移除 Ghost 安装及其数据。

# PARAMETERS

**--production**
> 以生产模式运行。

**-D**, **--development**
> 以开发模式运行。

**-d**, **--dir** _path_
> 安装目录。

**--enable**
> 服务器重启时自动重启 Ghost。

**--no-prompt**
> 跳过确认提示。

# DESCRIPTION

**ghost** 是 Ghost 的命令行界面。Ghost 是一个基于 Node.js 构建的现代开源发布平台。该 CLI 为 Ghost 安装提供完整的生命周期管理，包括初始设置、更新、配置和进程管理。

CLI 可以自动完成数据库设置、SSL 证书安装、systemd 服务配置以及 nginx 反向代理搭建。它会在更新期间处理数据库迁移，并通过 doctor 命令提供诊断功能。

# CONFIGURATION

**config.production.json**
> 生产环境配置，涵盖数据库、URL、邮件和服务器等设置。

**config.development.json**
> 开发环境配置。

# INSTALL

```nix: nix profile install nixpkgs#ghost```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[node](/man/node)(1), [npm](/man/npm)(1), [nginx](/man/nginx)(1), [systemctl](/man/systemctl)(1)
