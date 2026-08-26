# TAGLINE

管理容器网络与连接

# TLDR

**列出网络**

```docker network ls```

**创建一个网络**

```docker network create [name]```

**创建带子网的 bridge 网络**

```docker network create --driver bridge --subnet [192.168.1.0/24] [name]```

**将容器连接到网络**

```docker network connect [network] [container]```

**断开容器连接**

```docker network disconnect [network] [container]```

**查看网络详情**

```docker network inspect [network]```

**删除网络**

```docker network rm [network]```

# SYNOPSIS

**docker** **network** _command_ [_options_]

# SUBCOMMANDS

**ls**
> 列出网络。

**create**
> 创建一个网络。

**rm**
> 删除网络。

**inspect**
> 显示详细信息。

**connect**
> 将容器连接到网络。

**disconnect**
> 将容器从网络断开。

**prune**
> 删除未使用的网络。

# DESCRIPTION

**docker network** 用于管理 Docker 网络。网络使容器之间能够相互通信，支持 bridge、host、overlay 和 macvlan 等驱动。同一用户自定义网络中的容器可以使用容器名作为主机名相互通信，从而提供服务发现功能。自定义网络可以隔离容器，比默认的 bridge 网络具有更好的安全性。

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

[docker-run](/man/docker-run)(1), [docker-compose](/man/docker-compose)(1)

# RESOURCES

```[Source code](https://github.com/docker/cli)```

```[Documentation](https://docs.docker.com/reference/cli/docker/)```

<!-- verified: 2026-07-11 -->
