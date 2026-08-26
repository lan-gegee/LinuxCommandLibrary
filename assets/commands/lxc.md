# TAGLINE

通过 LXD REST API 管理 Linux 容器

# TLDR

**列出**容器

```lxc list [match_string]```

列出**镜像**

```lxc image list [remote:][match_string]```

从镜像**创建**容器

```lxc init [remote:]image [container]```

**启动**容器

```lxc start [remote:]container```

**停止**容器

```lxc stop [remote:]container```

查看容器**信息**

```lxc info [remote:]container```

创建**快照**

```lxc snapshot [remote:]container [snapshot_name]```

在容器内**执行**命令

```lxc exec [remote:]container [command]```

**启动**容器（创建 + 启动）

```lxc launch [remote:]image [container]```

# SYNOPSIS

**lxc** _command_ [_options_]

# DESCRIPTION

**lxc** 通过 LXD REST API 管理 Linux 容器。它提供友好的用户界面，用于创建、管理系统容器与虚拟机并与之交互。

# PARAMETERS

**list**
> 列出容器

**image list**
> 列出可用的镜像

**init**
> 从镜像创建容器

**start**
> 启动容器

**stop**
> 停止容器

**info**
> 显示容器详情

**snapshot**
> 创建容器快照

**exec**
> 在容器内执行命令

**launch**
> 创建并启动容器（相当于 init + start）

**delete**
> 删除容器

**copy**
> 复制容器

**move**
> 在服务器之间移动容器

**file** push|pull
> 向容器传输文件或从容器取回文件

**config**
> 管理容器配置

**profile**
> 管理容器 profile

**network**
> 管理网络

**storage**
> 管理存储池和存储卷

**remote**
> 管理远程服务器

**--debug**
> 显示所有调试消息

**--force-local**
> 强制使用本地 unix 套接字

**-h**, **--help**
> 打印帮助

**--project** _PROJECT_
> 覆盖源项目

**-q**, **--quiet**
> 不显示进度信息

**-v**, **--verbose**
> 显示所有信息类消息

# CAVEATS

需要 LXD 守护进程处于运行状态（用 lxd init 配置）。容器名称可以加上远程服务器名作为前缀，以便进行集群操作。可同时管理系统容器和虚拟机。注意 lxc（LXD 客户端）与较旧的 lxc-* 工具（liblxc）是不同的东西。

# HISTORY

**lxc** 是 LXD 的命令行客户端，由 **Canonical** 自 **2014 年**起开发，作为新一代容器管理器。LXD 提供系统容器（类似于轻量级虚拟机）和虚拟机，并通过 REST API 进行管理，lxc 客户端正是与该 API 通信。

# INSTALL

```apt: sudo apt install lxd-client```

```dnf: sudo dnf install lxc```

```pacman: sudo pacman -S lxc```

```zypper: sudo zypper install lxc```

```brew: brew install lxc```

```nix: nix profile install nixpkgs#lxc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lxc-attach](/man/lxc-attach)(1), [lxc-start](/man/lxc-start)(1), [docker](/man/docker)(1), [podman](/man/podman)(1)
