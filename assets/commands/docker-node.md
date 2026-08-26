# TAGLINE

管理 Docker Swarm 集群节点

# TLDR

**列出 swarm 节点**

```docker node ls```

**查看节点**，以易读格式显示

```docker node inspect --pretty [node]```

**列出节点上正在运行的任务**

```docker node ps [node]```

**将节点提升为管理节点**

```docker node promote [node]```

**将管理节点降级为工作节点**

```docker node demote [node]```

**排空（drain）** 一个节点（停止调度任务）

```docker node update --availability drain [node]```

**为节点添加标签**

```docker node update --label-add [key=value] [node]```

**从 swarm 中移除**节点

```docker node rm [node]```

# SYNOPSIS

**docker** **node** _command_ [_options_]

# SUBCOMMANDS

**ls**
> 列出 swarm 中的节点。

**inspect**
> 显示详细的节点信息。

**update**
> 更新节点。

**promote**
> 将节点提升为管理节点。

**demote**
> 将管理节点降级为工作节点。

**rm**
> 从 swarm 中移除节点。

**ps**
> 列出节点上运行的任务。

# DESCRIPTION

**docker node** 用于管理 Swarm 节点。节点是参与 swarm 集群的 Docker 主机。该命令仅在 Docker 守护进程以 swarm 模式运行时可用。管理节点负责协调集群操作，工作节点负责执行任务。节点管理包括控制可用性（active、pause、drain）、用于任务放置约束的标签，以及角色分配（manager/worker）。

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

[docker-swarm](/man/docker-swarm)(1), [docker-service](/man/docker-service)(1)
