# TAGLINE

快速的 OCI 容器运行时

# TLDR

从 OCI bundle **运行容器**

```crun run [container_id]```

**创建容器**但不启动

```crun create [container_id]```

**启动已创建的容器**

```crun start [container_id]```

**列出运行中的容器**

```crun list```

在运行中的容器内**执行命令**

```crun exec [container_id] [command]```

**删除容器**

```crun delete [container_id]```

**获取容器状态**

```crun state [container_id]```

**暂停容器内的所有进程**

```crun pause [container_id]```

**显示**容器中运行的进程

```crun ps [container_id]```

# SYNOPSIS

**crun** [_global-options_] _command_ [_command-options_] [_arguments_]

# PARAMETERS

**run** _ID_
> 基于 OCI bundle 创建并启动容器。

**create** _ID_
> 创建容器但不启动。

**start** _ID_
> 启动先前创建的容器。

**exec** _ID_ _CMD_
> 在运行中的容器内执行命令。

**delete** _ID_
> 删除容器。

**kill** _ID_ [_SIGNAL_]
> 向容器的 init 进程发送信号。

**list**
> 列出容器。

**state** _ID_
> 输出容器的状态。

**pause** _ID_
> 暂停容器内的所有进程。

**resume** _ID_
> 恢复容器内的进程。

**ps** _ID_
> 显示容器中运行的进程。

**update** _ID_
> 更新容器的资源限制。

**spec**
> 生成新的 OCI bundle 规范文件。

**checkpoint** _ID_
> 使用 CRIU 对运行中的容器做检查点。

**--root** _DIR_
> 存放容器状态的根目录。

**--debug**
> 产生详细输出。

**--log**=_DESTINATION_
> 定义错误和警告消息的目标位置（file:PATH、journald:ID 或 syslog:ID）。

**--systemd-cgroup**
> 使用 systemd 配置 cgroup。

**--cgroup-manager**=_MANAGER_
> 指定 cgroup 管理器（cgroupfs、systemd 或 disabled）。

# DESCRIPTION

**crun** 是一个用 C 编写、速度快且内存占用低的 OCI 容器运行时。它完全兼容 OCI（开放容器倡议）运行时规范，可以作为 runc 的直接替代品。

crun 实现了全部必需的 OCI 运行时操作，包括容器创建、执行和生命周期管理。它支持 Linux 命名空间、cgroups v1 与 v2、seccomp 等容器隔离特性。

该运行时的设计目标是轻量高效，与基于 Go 的运行时相比，启动时间显著更快，内存占用更低。Podman 和 Buildah 等容器引擎都在使用它。

# CAVEATS

需要 root 权限或适当的 user namespace 配置。OCI bundle 必须正确配置 config.json 和 rootfs。crun 操作的是 OCI bundle，而非直接操作容器镜像。

# HISTORY

crun 由 Red Hat 的 Giuseppe Scrivano 开发，作为 runc 的更快替代方案。它于约 **2019** 年首次发布，凭借性能优势获得广泛采用。它已成为 Podman 的默认运行时，并通过 CRI-O 得到 Kubernetes 支持。

# INSTALL

```apt: sudo apt install crun```

```dnf: sudo dnf install crun```

```pacman: sudo pacman -S crun```

```apk: sudo apk add crun```

```zypper: sudo zypper install crun```

```brew: brew install crun```

```nix: nix profile install nixpkgs#crun```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[runc](/man/runc)(1), [podman](/man/podman)(1), [buildah](/man/buildah)(1), [containerd](/man/containerd)(1), [docker](/man/docker)(1)
