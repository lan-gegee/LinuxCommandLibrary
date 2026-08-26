# TAGLINE

管理 Docker 守护进程连接上下文

# TLDR

**列出上下文**

```docker context ls```

**显示当前上下文**

```docker context show```

**创建新上下文**

```docker context create [name] --docker "host=ssh://[user@host]"```

**切换到某个上下文**

```docker context use [name]```

**移除上下文**

```docker context rm [name]```

**查看上下文详情**

```docker context inspect [name]```

# SYNOPSIS

**docker** **context** _command_ [_options_]

# SUBCOMMANDS

**ls**
> 列出上下文。

**show**
> 打印当前上下文。

**create**
> 创建新上下文。

**use**
> 设置当前上下文。

**rm**
> 移除上下文。

**inspect**
> 显示详细信息。

**update**
> 更新上下文。

**export**
> 导出上下文。

**import**
> 导入上下文。

# DESCRIPTION

**docker context** 管理 Docker 上下文。上下文是存储不同 Docker 引擎连接信息的配置档案。借助上下文，可以在本地、远程和云端 Docker 主机之间无缝切换，而无需手动重新配置连接设置。

每个上下文包含端点信息、TLS 证书以及与 Docker 守护进程通信所需的其他元数据。这对需要同时使用多个 Docker 环境的开发者和运维人员特别有用，例如本地开发、预发布服务器和生产集群。

名为 "default" 的默认上下文通过 Unix 套接字连接本地 Docker 守护进程。可以创建额外的上下文，通过 SSH、TCP 或其他协议连接远程 Docker 主机。

# CONFIGURATION

**~/.docker/contexts**
> 存储自定义上下文的元数据和 TLS 证书的目录。

# INSTALL

```apt: sudo apt install docker-cli```

```dnf: sudo dnf install docker-cli```

```pacman: sudo pacman -S docker```

```apk: sudo apk add docker-cli```

```zypper: sudo zypper install docker```

```brew: brew install docker```

```nix: nix profile install nixpkgs#docker```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [docker-machine](/man/docker-machine)(1)

# RESOURCES

```[Source code](https://github.com/docker/cli)```

```[Documentation](https://docs.docker.com/reference/cli/docker/)```

<!-- verified: 2026-07-11 -->
