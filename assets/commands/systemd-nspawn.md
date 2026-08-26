# TAGLINE

轻量级命名空间容器

# TLDR

在容器中**运行**命令

```systemd-nspawn -D [path/to/container_root]```

在容器中**运行**完整 Linux 操作系统（引导启动）

```systemd-nspawn -b -D [path/to/container_root]```

借助桩 init 进程以 PID 2 身份**运行**命令

```systemd-nspawn -D [path/to/container_root] -a```

**指定**机器名称和主机名

```systemd-nspawn -M [container_name] --hostname [hostname] -D [path/to/container_root]```

# SYNOPSIS

**systemd-nspawn** [_options_] [_command_] [_arguments_]

# PARAMETERS

**-D, --directory _path_**
> 容器的根目录

**-b, --boot**
> 引导启动容器的 init 系统

**-M, --machine _name_**
> 设置机器名称

**-a, --as-pid2**
> 使用桩 init 以 PID 2 身份运行命令

**--hostname _name_**
> 设置容器主机名

**-u, --user _user_**
> 以指定用户身份运行

**--bind _src:dest_**
> 将宿主机路径绑定挂载到容器中

**-n, --network-veth**
> 创建虚拟以太网链路

**--private-network**
> 与宿主网络断开连接

# DESCRIPTION

**systemd-nspawn** 在轻量级容器中启动一个命令或完整的操作系统。它使用 Linux 命名空间和 cgroups 进行隔离，但比 Docker 这类完整的容器方案更简单。

该工具适用于测试、构建软件包以及运行相互隔离的服务。配合 **--boot** 可以运行完整的 init 系统，因此也适合作为系统容器使用。

# CAVEATS

需要 root 权限。容器文件系统必须包含完整的操作系统，或至少包含所需的二进制文件。网络隔离需要额外的配置。本命令是 systemd 套件的一部分。

# INSTALL

```apt: sudo apt install systemd-container```

```dnf: sudo dnf install systemd-container```

```zypper: sudo zypper install systemd-container```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[machinectl](/man/machinectl)(1), [systemd-detect-virt](/man/systemd-detect-virt)(1), [systemd-dissect](/man/systemd-dissect)(1), [chroot](/man/chroot)(1)
