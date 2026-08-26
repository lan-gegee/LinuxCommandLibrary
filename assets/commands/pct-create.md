# TAGLINE

在 Proxmox VE 中基于模板镜像创建新的 LXC 容器

# TLDR

创建指定磁盘大小的容器

```pct create 100 local:vztmpl/distro.tar.zst --rootfs local-lvm:4```

创建带 **memory** 限制的容器

```pct create 100 local:vztmpl/distro.tar.zst --rootfs local-lvm:4 --memory 8192```

创建指定 **hostname** 和密码的容器

```pct create 100 local:vztmpl/distro.tar.zst --rootfs local-lvm:4 --hostname name --password pass```

创建带 **network** 配置的容器

```pct create 100 local:vztmpl/distro.tar.zst --rootfs local-lvm:4 --net0 name=eth0,bridge=vmbr0,ip=dhcp```

创建带 CPU 和 swap 限制的**非特权**容器

```pct create 100 local:vztmpl/distro.tar.zst --rootfs local-lvm:4 --unprivileged 1 --cores 2 --swap 512```

创建并立即**启动**

```pct create 100 local:vztmpl/distro.tar.zst --rootfs local-lvm:4 --start```

# SYNOPSIS

**pct create** _vmid_ _template_ [_OPTIONS_]

# DESCRIPTION

**pct create** 在 Proxmox VE 中基于模板镜像创建新的 LXC 容器。它会在创建过程中配置存储、网络、资源及其他容器属性。

# PARAMETERS

**vmid**
> 新容器的数字 ID

**template**
> 容器模板的路径（例如 local:vztmpl/distro.tar.zst）

**--rootfs** _storage:size_
> 根文件系统的存储与大小（单位为 GB）

**--memory** _megabytes_
> 内存限制（单位为 MB）

**--hostname** _name_
> 容器主机名

**--password** _password_
> 容器的 root 密码

**--net**_N_ _config_
> 网络接口配置

**--cores** _number_
> 分配给容器的 CPU 核心数

**--swap** _megabytes_
> swap 内存限制（单位为 MB）（默认：512）

**--unprivileged** _0|1_
> 创建为非特权容器（1，出于安全考虑推荐使用）

**--ssh-public-keys** _filepath_
> 用于 root 用户认证的 SSH 公钥

**--features** _list_
> 启用 nesting、keyctl、fuse、mknod 等特性

**--start** _0|1_
> 创建后启动容器（默认：0）。

**--onboot** _0|1_
> 系统启动时启动容器（默认：0）。

**--storage** _storage_
> 容器的默认存储（默认：local）。

**--nameserver** _ip_
> 容器的 DNS 服务器 IP 地址。

**--ostype** _type_
> 操作系统类型（例如 debian、ubuntu、centos、alpine、archlinux、fedora、gentoo、opensuse、unmanaged）。

# CAVEATS

模板必须先下载或上传到 Proxmox 存储中。容器 ID 在整个集群内必须唯一。对于要在内部运行 Docker 或其他容器的容器，需启用 nesting 特性。

# HISTORY

**pct create** 是用于管理 LXC 容器的 **Proxmox VE** 虚拟化平台的一部分。

# SEE ALSO

[pct](/man/pct)(1), [pct-clone](/man/pct-clone)(1), [pct-enter](/man/pct-enter)(1), [pct-destroy](/man/pct-destroy)(1)
