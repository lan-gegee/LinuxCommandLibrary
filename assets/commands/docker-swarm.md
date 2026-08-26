# TAGLINE

Docker 原生集群与编排

# TLDR

**初始化一个 swarm**

```docker swarm init```

**初始化时指定通告地址**

```docker swarm init --advertise-addr [ip:port]```

**以工作节点身份加入 swarm**

```docker swarm join --token [token] [manager:port]```

**获取加入令牌**

```docker swarm join-token [worker|manager]```

**离开 swarm**

```docker swarm leave```

**以管理节点身份强制离开**

```docker swarm leave --force```

**更新 swarm 配置**

```docker swarm update --autolock=[true]```

# SYNOPSIS

**docker** **swarm** _command_ [_options_]

# SUBCOMMANDS

**init**
> 初始化一个 swarm。

**join**
> 以节点身份加入 swarm。

**join-token**
> 管理加入令牌。

**leave**
> 离开 swarm。

**update**
> 更新 swarm 配置。

**ca**
> 管理 swarm CA。

**unlock**
> 解锁 swarm。

**unlock-key**
> 管理解锁密钥。

# DESCRIPTION

**docker swarm** 管理 Docker Swarm 集群。Swarm 模式提供原生集群能力、服务编排、负载均衡以及节点之间的安全通信。

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

[docker-node](/man/docker-node)(1), [docker-service](/man/docker-service)(1)

# RESOURCES

```[Source code](https://github.com/docker/cli)```

```[Documentation](https://docs.docker.com/reference/cli/docker/)```

<!-- verified: 2026-07-11 -->
