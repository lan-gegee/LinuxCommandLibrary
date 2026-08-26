# TAGLINE

基于容器的 Ceph 集群部署

# TLDR

**引导（bootstrap）**一个新的 Ceph 集群

```sudo cephadm bootstrap --mon-ip [monitor_ip]```

向集群**添加**新主机

```sudo cephadm add-host [hostname] [ip_address]```

**部署**指定服务

```sudo cephadm deploy [service_type] --name [service_name]```

检查集群服务的**状态**

```sudo cephadm shell -- ceph -s```

进入 Ceph 容器内的 **shell**

```sudo cephadm shell```

从集群中**移除**服务

```sudo cephadm rm-service [service_type] --name [service_name]```

# SYNOPSIS

**cephadm** [_options_] _command_ [_arguments_]

# DESCRIPTION

**cephadm** 使用容器部署和管理 Ceph 分布式存储集群（首选 Podman，也支持 Docker）。它是现代的 Ceph 编排工具，取代了 ceph-deploy 和 ceph-ansible 等较老的部署方式。

该工具处理完整的集群生命周期：在单个节点上引导新集群、添加主机、部署守护进程（monitor、OSD、manager、网关）以及升级集群。每个 Ceph 守护进程运行在自己的容器中，从而提供隔离性并简化升级。

`bootstrap` 命令创建一个带 monitor 和 manager 的初始单节点集群，生成管理员凭证，并为后续操作设置编排器。`shell` 命令提供一个位于 Ceph 容器内的交互环境，所有管理工具均可用。

# SUBCOMMANDS

**bootstrap**
> 初始化新的 Ceph 集群

**add-host**
> 向集群添加主机

**rm-host**
> 从集群移除主机

**deploy**
> 部署守护进程

**rm-daemon**
> 移除守护进程

**shell**
> 进入 Ceph 容器内的交互式 shell

**enter**
> 在已有的 Ceph 容器内运行命令

**ls**
> 列出此主机上运行的所有 Ceph 守护进程

**ps**
> 显示守护进程状态（`ls --no-extra-info` 的别名）

**check-host**
> 检查主机前提条件（软件包、时间同步、容器运行时）

**prepare-host**
> 安装缺失的前提条件

**gather-facts**
> 收集主机清单信息

**adopt**
> 接管来自旧式（非 cephadm）部署的守护进程

**logs**
> 查看守护进程日志

**rm-cluster**
> 销毁本地集群状态（危险操作）

# PARAMETERS

**--mon-ip** _ip_
> 引导时使用的 monitor IP 地址

**--cluster-network** _CIDR_
> 将 OSD 复制网络限制到给定的子网。

**--ssh-user** _USER_
> cephadm SSH 连接远程主机所用的用户（默认 `root`）。

**--initial-dashboard-user**, **--initial-dashboard-password**
> 引导过程中创建的 Ceph Dashboard 凭证。

**--skip-dashboard**
> 不启用 dashboard。

**--fsid** _UUID_
> 复用现有的集群 FSID 而不是重新生成。

**--name** _name_
> 服务或守护进程名称

**--image** _image_
> 要使用的容器镜像

**--docker**
> 强制使用 Docker 而不是 Podman。

**-v**, **--verbose**
> 增加日志详细程度。

# CAVEATS

需要容器运行时（首选 Podman，也支持 Docker）。引导过程会创建初始管理员凭证。服务通过编排器管理，而非直接管理。

# INSTALL

```apt: sudo apt install cephadm```

```dnf: sudo dnf install cephadm```

```apk: sudo apk add ceph18-cephadm```

```zypper: sudo zypper install cephadm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ceph](/man/ceph)(8), [podman](/man/podman)(1)
