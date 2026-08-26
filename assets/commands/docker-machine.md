# TAGLINE

在虚拟机上创建和管理 Docker 主机

# TLDR

**列出机器**

```docker-machine ls```

**创建一台机器**

```docker-machine create --driver [virtualbox] [name]```

**启动一台机器**

```docker-machine start [name]```

**停止一台机器**

```docker-machine stop [name]```

**获取机器 IP**

```docker-machine ip [name]```

**通过 SSH 连接到机器**

```docker-machine ssh [name]```

**为机器设置环境变量**

```eval $(docker-machine env [name])```

# SYNOPSIS

**docker-machine** _command_ [_options_] [_args_]

# SUBCOMMANDS

**ls**
> 列出机器。

**create**
> 创建一台机器。

**start**
> 启动一台机器。

**stop**
> 停止一台机器。

**rm**
> 删除一台机器。

**ssh**
> 通过 SSH 连接到机器。

**ip**
> 获取机器的 IP 地址。

**env**
> 显示环境变量。

**status**
> 获取机器状态。

**inspect**
> 查看机器信息。

# DESCRIPTION

**docker-machine** 用于在本地虚拟机管理程序或云服务商上创建和管理 Docker 主机，支持在远程机器上运行 Docker Engine。它将创建虚拟机、安装 Docker 以及配置 Docker 客户端连接的过程自动化。支持多种驱动，包括 VirtualBox、VMware、AWS、Azure 和 Digital Ocean。

# CAVEATS

Docker Machine 已被弃用。现在管理 Docker 环境首选 Docker Desktop 或云原生解决方案。

# INSTALL

```pacman: sudo pacman -S docker-machine```

```brew: brew install docker-machine```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [docker-context](/man/docker-context)(1)

# RESOURCES

```[Source code](https://github.com/docker/machine)```

<!-- verified: 2026-07-11 -->
