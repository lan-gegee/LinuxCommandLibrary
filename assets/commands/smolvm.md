# TAGLINE

构建和运行轻量、可移植的虚拟机

# TLDR

在临时虚拟机中**运行命令**

```smolvm machine run [command]```

在临时虚拟机中**启动交互式 Shell**

```smolvm machine run -it```

**创建**持久化虚拟机

```smolvm machine create [name]```

创建启用网络的**虚拟机**

```smolvm machine create [name] --net```

在已有虚拟机中**执行命令**

```smolvm machine exec [name] [command]```

**启动**已停止的虚拟机

```smolvm machine start [name]```

**停止**运行中的虚拟机

```smolvm machine stop [name]```

将虚拟机**打包**成可移植的可执行文件

```smolvm pack create [name] -o [output]```

# SYNOPSIS

**smolvm** \<command\> [_options_]

# PARAMETERS

**machine run** [_command_]
> 在临时虚拟机中执行命令，退出后即清理

**machine run -it**
> 在临时虚拟机中启动交互式 Shell

**machine create** _name_ [_--net_] [_--image image_] [_--cpus n_] [_--mem size_]
> 创建持久化虚拟机

**machine start** _name_
> 启动已停止的虚拟机

**machine stop** _name_
> 停止运行中的虚拟机

**machine exec** _name_ _command_
> 在已有虚拟机中运行命令

**pack create** _name_ [_-o path_] [_-s smolfile_]
> 将工作负载打包为可移植、自包含的可执行文件

**--net**
> 启用网络访问（默认禁用；仅支持 TCP/UDP，不支持 ICMP）

**--image** _image_
> 指定基础 Linux 镜像

**--cpus** _n_
> 覆盖 vCPU 数量（默认：4）

**--mem** _size_
> 覆盖内存分配（默认：8 GiB）

**--ssh-agent**
> 将宿主机 SSH 密钥转发进虚拟机

**--allow-host** _domain_
> 将出站流量限制到特定域名

**-o** _path_
> 打包产物的输出路径

**-s** _smolfile_
> 使用 Smolfile 配置

# DESCRIPTION

**smolvm** 是一个 CLI 工具，用于构建和运行可移植、轻量、自包含的虚拟机，具备亚秒级冷启动和弹性内存占用。每个工作负载都拥有真正的硬件隔离——在 **Hypervisor.framework**（macOS）或 **KVM**（Linux）上运行自己的内核。

虚拟机可以打包成单个 **.smolmachine** 文件，并在任何受支持的平台上还原。所有依赖都已预先内置，无需安装步骤或运行时下载，启动时间不到 200ms。内存通过 virtio balloon 实现弹性管理——宿主机只为客户机实际使用的部分提交资源，其余自动回收。

网络访问需要显式开启且默认禁用，为沙箱运行不受信任的代码提供了强大的安全边界。宿主机的文件系统、网络和凭据均由虚拟机监控程序边界隔离。

# CAVEATS

网络仅支持 TCP/UDP 且必须显式开启；不支持 ICMP。卷挂载仅支持目录，不支持单个文件。在 macOS 上，二进制文件必须带有 Hypervisor.framework 权限签名。在 Linux 上需要 KVM 访问权限。该工具用 Rust 编写，目前支持 macOS（Apple Silicon 和 Intel）以及 Linux（x86_64 和 aarch64）。

# HISTORY

smolvm 由 **Smol Machines** 创建，使用 **Rust** 编写。其开发目的是为开发者提供快速、隔离的虚拟机环境，默认优先保证安全性，从而能够安全地运行不受信任的代码并构建可重现的环境，同时避免传统虚拟化的开销。

# INSTALL

```pacman: sudo pacman -S smolvm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qemu](/man/qemu)(1), [docker](/man/docker)(1), [podman](/man/podman)(1)
