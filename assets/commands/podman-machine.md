# TAGLINE

管理 Podman 的虚拟机

# TLDR

**以自定义资源初始化新机器**

```podman machine init --cpus [4] --memory [4096] --disk-size [50]```

**初始化并立即启动**

```podman machine init --now```

**启动机器**

```podman machine start```

**列出机器**

```podman machine list```

**SSH 进入机器**

```podman machine ssh```

**以 JSON 查看机器详情**

```podman machine inspect```

**修改已停止机器的资源**

```podman machine set --cpus [8] --memory [8192]```

**移除机器**

```podman machine rm```

# SYNOPSIS

**podman** **machine** _command_ [_options_]

# PARAMETERS

**init**
> 初始化新的虚拟机。

**start**
> 启动虚拟机。

**stop**
> 停止虚拟机。

**list**
> 列出虚拟机。

**ssh**
> SSH 进入虚拟机。

**inspect**
> 以 JSON 显示机器配置。

**set**
> 修改已停止机器的设置（CPU、内存、磁盘、rootful）。

**rm**
> 移除虚拟机。

**info**
> 显示机器主机信息（架构、操作系统、VM 提供程序）。

**reset**
> 移除所有机器、配置和缓存的镜像。

**os** apply|upgrade
> 管理 VM 操作系统镜像。

**--cpus** _n_
> CPU 数量（init、set）。

**--memory** _mb_
> 内存大小，单位 MiB（init、set）。

**--disk-size** _gb_
> 磁盘大小，单位 GiB（init、set —— 仅可扩大）。

**--rootful**
> 偏好 rootful 容器执行方式（init、set）。

**--now**
> init 后立即启动机器。

**--volume** _src:dst_
> 将主机目录挂载进 VM（init）。

# DESCRIPTION

**podman machine** 管理 Linux 虚拟机，用于在 macOS 和 Windows 上运行 Podman。由于容器需要 Linux 内核，该命令会创建并管理一个运行 Podman 服务的 VM。

VM 提供程序根据平台自动选择：macOS 上是 Apple Hypervisor，Windows 上是 WSL 或 Hyper-V，Linux 上是 QEMU。可在 init 时用 `--provider` 覆盖。`set` 子命令允许修改已停止机器的 CPU、内存和磁盘。

# CAVEATS

所有 machine 命令仅支持无根模式。`set` 子命令要求机器处于停止状态。磁盘大小只能扩大，不能缩小。某些 `set` 选项（--cpus、--memory、--disk-size）仅限 QEMU 使用。

# INSTALL

```dnf: sudo dnf install podman-machine```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[podman](/man/podman)(1), [docker-machine](/man/docker-machine)(1)
