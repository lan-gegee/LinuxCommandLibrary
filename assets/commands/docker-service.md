# TAGLINE

管理 Docker Swarm 中的容器化服务

# TLDR

**创建一个服务**

```docker service create --name [name] [image]```

**列出服务**

```docker service ls```

**查看一个服务**

```docker service inspect [service]```

**伸缩一个服务**

```docker service scale [service]=[replicas]```

**更新服务镜像**

```docker service update --image [image]:[tag] [service]```

**查看服务日志**

```docker service logs [service]```

**删除一个服务**

```docker service rm [service]```

# SYNOPSIS

**docker** **service** _command_ [_options_]

# SUBCOMMANDS

**create**
> 创建一个新服务。

**ls**
> 列出服务。

**inspect**
> 显示详细信息。

**update**
> 更新服务。

**scale**
> 伸缩服务。

**logs**
> 获取服务日志。

**ps**
> 列出服务的任务。

**rm**
> 删除服务。

**rollback**
> 将服务回滚到上一个规格。

# COMMON OPTIONS

**--replicas** _n_（create/scale）
> 要运行的副本任务数量。

**--mode** _mode_（create）
> **replicated**（默认）或 **global**（每个节点一个任务）。

**--publish** _published:target_（create）
> 对外发布端口（例如 `8080:80`）。

**--network** _name_（create）
> 将服务连接到 swarm overlay 网络。

**--env**, **-e** _KEY=VAL_（create/update）
> 设置环境变量。

**--constraint** _expr_（create）
> 放置约束（例如 `node.role==worker`）。

**--update-parallelism** _n_ / **--update-delay** _dur_（create/update）
> 滚动更新的并发数以及批次之间的延迟。

# DESCRIPTION

**docker service** 管理 Swarm 服务。服务是对一组容器应如何在 swarm 中运行的声明，包括镜像、副本数量、网络、挂载、secrets、资源限制和更新策略。Swarm 编排器在集群节点上调度任务（容器实例）并维持期望状态，替换失败的任务并通过路由网格（routing mesh）转发流量。

服务命令仅在已加入 swarm 的 Docker 主机上可用；使用前需先执行 **docker swarm init** 初始化。更新默认以滚动更新方式应用，并可使用 **rollback** 回退到上一个服务规格。

# CAVEATS

需要 swarm 模式（**docker swarm init** / **join**）。单主机工作负载请改用 **docker run** 或 **docker compose**。使用 **--update-parallelism 0** 的滚动更新会一次性替换所有任务，可能导致停机。

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

[docker-swarm](/man/docker-swarm)(1), [docker-node](/man/docker-node)(1), [docker](/man/docker)(1), [docker-compose](/man/docker-compose)(1)
