# TAGLINE

管理可移植的虚拟开发环境

# TLDR

**用基础 box 初始化新的 Vagrantfile**

```vagrant init [ubuntu/jammy64]```

**启动并预配置虚拟机**

```vagrant up```

**通过 SSH 连接运行中的虚拟机**

```vagrant ssh```

**停止运行中的虚拟机**

```vagrant halt```

**销毁虚拟机并移除所有资源**

```vagrant destroy```

**显示所有虚拟机的状态**

```vagrant status```

**挂起虚拟机**（将状态保存到磁盘）

```vagrant suspend```

**显示整个系统中所有 Vagrant 虚拟机**

```vagrant global-status```

# SYNOPSIS

**vagrant** _command_ [_options_]

# PARAMETERS

**init** [_BOX_]
> 初始化新的 Vagrantfile，可选指定基础 box。

**up** [_NAME_]
> 启动并预配置虚拟机。在多机环境中可选择指定机器名称。

**ssh** [_NAME_]
> 通过 SSH 连接运行中的虚拟机。

**halt** [_NAME_]
> 优雅地停止运行中的虚拟机。

**destroy** [_NAME_]
> 移除虚拟机及其所有资源。

**reload** [_NAME_]
> 重启虚拟机并重新加载 Vagrantfile 配置。

**suspend** [_NAME_]
> 暂停运行中的虚拟机，保存其当前状态。

**resume** [_NAME_]
> 恢复之前挂起的虚拟机。

**provision** [_NAME_]
> 在运行中的虚拟机上执行已配置的预配置器。

**status** [_NAME_]
> 显示当前环境中虚拟机的状态。

**global-status**
> 显示整个系统中所有 Vagrant 虚拟机的状态。

**snapshot push**
> 保存当前虚拟机状态的快照。

**snapshot pop**
> 恢复最近一次的快照。

**validate**
> 检查 Vagrantfile 的语法错误。

**package**
> 将运行中的虚拟机打包为可复用的 box。

**plugin install** _NAME_
> 安装 Vagrant 插件。

**box add** _BOX_
> 下载并添加 box 镜像。

**box list**
> 列出本地可用的 box。

**box remove** _BOX_
> 移除本地存储的 box。

**--provider** _NAME_
> 指定提供者（virtualbox、vmware 等）。

**-f**, **--force**
> 不经确认强制执行操作。

**-h**, **--help**
> 显示任意命令的帮助信息。

# DESCRIPTION

**vagrant** 管理可移植的虚拟开发环境。它自动完成虚拟机的创建、配置和预配置。

Vagrantfile 定义虚拟机配置。它指定基础 box、网络设置、共享文件夹和预配置脚本。

Box 是基础镜像。许多镜像可在 Vagrant Cloud 上获取。也可以创建并共享自定义 box。

提供者负责虚拟化。默认为 VirtualBox，同时支持 VMware、Hyper-V、Docker 以及云端提供者。

预配置器在虚拟机启动后进行配置。支持 Shell 脚本、Ansible、Puppet 和 Chef。

多机环境在一个 Vagrantfile 中定义多台虚拟机。它们可以建模集群等复杂环境。

# CAVEATS

需要虚拟化软件。大型 box 需要下载时间和磁盘空间。提供者特有的功能可能有所差异。

# HISTORY

**Vagrant** 由 **Mitchell Hashimoto** 于 **2010 年**创建，后由 **HashiCorp** 继续开发。它革新了开发环境管理方式，使环境的可复现搭建成为可能。

# INSTALL

```apt: sudo apt install vagrant```

```dnf: sudo dnf install vagrant```

```nix: nix profile install nixpkgs#vagrant```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vboxmanage](/man/vboxmanage)(1), [docker](/man/docker)(1), [ansible](/man/ansible)(1), [packer](/man/packer)(1), [ssh](/man/ssh)(1)
