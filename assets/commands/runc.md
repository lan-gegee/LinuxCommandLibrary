# TAGLINE

底层 OCI 容器运行时

# TLDR

**运行容器**

```runc run [container-id]```

**创建容器**

```runc create [container-id]```

**启动容器**

```runc start [container-id]```

**列出容器**

```runc list```

**杀死容器**

```runc kill [container-id]```

**删除容器**

```runc delete [container-id]```

**在运行中的容器内执行命令**

```runc exec [container-id] [command]```

**显示容器状态**

```runc state [container-id]```

**生成 OCI spec 文件**

```runc spec```

**显示容器中运行的进程**

```runc ps [container-id]```

# SYNOPSIS

**runc** [_options_] _command_ [_args_...]

# DESCRIPTION

**runc** 是一个按照 OCI 规范启动和运行容器的 CLI 工具。它是开放容器倡议（Open Container Initiative）运行时规范的参考实现。

该工具提供底层的容器运行时功能，被 Docker、containerd 以及其他容器平台使用。

# PARAMETERS

**run** _id_
> 创建并启动容器。

**create** _id_
> 创建容器。

**start** _id_
> 启动已创建的容器。

**list**
> 列出容器。

**state** _id_
> 输出容器状态。

**kill** _id_ [_signal_]
> 向容器发送信号。

**delete** _id_
> 删除容器。

**exec** _id_ _cmd_
> 在容器内执行新进程。

**pause** _id_
> 暂停容器内的所有进程。

**resume** _id_
> 恢复之前暂停的进程。

**ps** _id_
> 显示容器内运行的进程。

**events** _id_
> 显示容器事件（OOM、CPU、内存、I/O 统计）。

**update** _id_
> 更新容器的资源约束。

**checkpoint** _id_
> 对运行中的容器做检查点。

**restore** _id_
> 从之前的检查点恢复容器。

**spec**
> 生成新的 OCI spec 文件（config.json）。

**--root** _dir_
> 存放容器状态的根目录（应位于 tmpfs 上）。

**--debug**
> 启用调试日志。

**--log** _path_
> 设置日志文件路径（默认：stderr）。

**--log-format** _text|json_
> 设置日志格式（默认：text）。

**--systemd-cgroup**
> 启用 systemd cgroup 支持。

**--rootless** _true|false|auto_
> 启用或禁用 rootless 模式（默认：auto）。

# CAVEATS

需要 OCI bundle。属于底层工具——通常不直接使用。完整功能需要 root 权限。容器必须正确配置。

# HISTORY

**runc** 由 Docker 及其他方于 **2015 年**作为**开放容器倡议**（Open Container Initiative，OCI）的一部分开发。它标准化了容器运行时行为，使各容器平台之间能够互操作。

# INSTALL

```apt: sudo apt install runc```

```dnf: sudo dnf install runc```

```pacman: sudo pacman -S runc```

```apk: sudo apk add runc```

```zypper: sudo zypper install runc```

```brew: brew install runc```

```nix: nix profile install nixpkgs#runc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [containerd](/man/containerd)(8), [podman](/man/podman)(1), [crun](/man/crun)(1)
