# TAGLINE

在 Fly.io 平台上部署应用的 CLI 工具

# TLDR

**启动新应用**

```flyctl launch```

**部署应用**

```flyctl deploy```

**列出应用**

```flyctl apps list```

**查看日志**

```flyctl logs```

**SSH 进入机器**

```flyctl ssh console```

**检查应用状态**

```flyctl status```

**管理密钥**

```flyctl secrets set [KEY=VALUE]```

# SYNOPSIS

**flyctl** _command_ [_options_] [_arguments_]

# PARAMETERS

_COMMAND_
> 操作类型：launch、deploy、apps、logs、ssh 等。

**launch**
> 创建并部署新应用。

**deploy**
> 部署当前目录。

**apps** _SUBCMD_
> 管理应用程序。

**logs**
> 查看应用日志。

**ssh** _SUBCMD_
> 通过 SSH 访问机器。

**secrets** _SUBCMD_
> 管理密钥/环境变量。

**scale** _SUBCMD_
> 调整资源。

**status**
> 显示应用部署状态。

**--help**
> 显示帮助信息。

**-t**, **--access-token** _TOKEN_
> Fly API 访问令牌。

**--verbose**
> 详细输出。

**--debug**
> 打印额外的日志和跟踪信息。

# DESCRIPTION

**flyctl**（也可用 fly 命名调用）是 Fly.io 的命令行界面，Fly.io 是一个在边缘基础设施上全球部署应用的平台。它管理应用程序、部署和平台资源。

该工具可部署 Docker 容器或从源码构建，并分发到 Fly 的全球网络。它处理密钥、卷、扩缩容和网络配置。

flyctl 让你可以完全通过命令行控制整个平台，从初始启动到生产环境管理。

# CONFIGURATION

**fly.toml**
> 应用配置文件，定义服务、区域、构建设置和环境变量。

# CAVEATS

需要 Fly.io 账户。使用会产生费用。某些功能取决于所在区域。

# HISTORY

flyctl 是 **Fly.io** 的 CLI，该平台于 2017 年上线，专注于边缘部署。它使用轻量级虚拟机将应用部署在离全球用户更近的位置。

# INSTALL

```brew: brew install flyctl```

```nix: nix profile install nixpkgs#flyctl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [heroku](/man/heroku)(1), [railway](/man/railway)(1)
