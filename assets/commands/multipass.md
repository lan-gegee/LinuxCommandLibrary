# TAGLINE

面向 Ubuntu 实例的轻量级虚拟机管理器

# TLDR

**启动新的 Ubuntu 实例**

```multipass launch --name [myvm]```

**以特定 Ubuntu 版本启动**

```multipass launch [22.04] --name [myvm]```

**以自定义资源启动**

```multipass launch --name [myvm] --cpus [2] --memory [4G] --disk [20G]```

**列出所有实例**

```multipass list```

**在实例中打开 Shell**

```multipass shell [instance_name]```

**在实例中执行命令**

```multipass exec [instance_name] -- [command]```

**停止实例**

```multipass stop [instance_name]```

**删除并清除实例**

```multipass delete [instance_name] && multipass purge```

# SYNOPSIS

**multipass** _command_ [_options_] [_arguments_]

# PARAMETERS

**launch** [_image_]
> 创建并启动新实例。

**list**, **ls**
> 列出所有实例。

**shell** _instance_
> 在实例中打开 Shell。

**exec** _instance_ **--** _command_
> 在实例中运行命令。

**start** _instance_
> 启动已停止的实例。

**stop** _instance_
> 停止运行中的实例。

**restart** _instance_
> 重启实例。

**delete** _instance_
> 删除实例（purge 之前可恢复）。

**purge**
> 永久移除已删除的实例。

**recover** _instance_
> 恢复已删除的实例。

**info** _instance_
> 显示实例详情。

**mount** _source_ _instance:target_
> 将宿主机目录挂载到实例中。

**umount** _mount_
> 卸载目录。

**transfer** _source_ _destination_
> 在宿主机和实例之间复制文件。

**find**
> 列出可用的镜像。

**--name** _NAME_
> 实例名称。

**--cpus** _NUM_
> CPU 数量。

**--memory** _SIZE_
> 内存分配（如 2G）。

**--disk** _SIZE_
> 磁盘大小（如 10G）。

**--cloud-init** _FILE_
> cloud-init 配置文件。

**--network** _SPEC_
> 为实例添加网络接口。

**--bridged**
> 添加一个桥接到默认网桥的网络接口。

# DESCRIPTION

**Multipass** 是一款面向 Ubuntu 实例的轻量级虚拟机管理器。它由 Canonical 开发，提供在 Linux、macOS 和 Windows 上快速启动 Ubuntu 虚拟机的方式，针对云风格的工作流做了优化。

实例从缓存的云镜像快速启动。虚拟机监控后端因平台而异：Linux 上为 QEMU 或 LXD，macOS 上为 QEMU（配合 Hypervisor.framework），Windows 上为 Hyper-V。实例通过 DHCP 组网，开箱即可与宿主机连通。

cloud-init 支持实现自动化配置。你可以在首次启动时传入 cloud-init YAML 来安装软件包、配置用户、运行脚本等——在本地复刻云端部署工作流。

挂载功能可在实例与宿主机之间共享目录，对开发很有用。文件传输双向可用。多个实例可以同时运行，上限取决于系统资源。

该工具特别适合测试 Ubuntu 服务器配置、在本地开发云应用，以及创建快速的一次性开发环境。

# CAVEATS

以 Ubuntu 镜像为主，不过也可以通过 URL 使用其他镜像。需要硬件虚拟化支持。可能出现虚拟机监控程序冲突（VirtualBox、Docker Desktop）。默认实例资源较少（1 CPU、1 GB 内存、5 GB 磁盘）。网络网桥配置因后端而异。部分功能需要特定的虚拟机监控后端。

# HISTORY

**Multipass** 由 **Canonical** 开发，约于 **2017 年**发布，旨在跨平台提供流畅的 Ubuntu 虚拟机体验。它源自人们对快速、一致的 Ubuntu 开发测试环境的需求。该项目强调简洁而非完整的虚拟化功能，面向需要 Ubuntu 实例但不想处理复杂 VM 管理的开发者。

# INSTALL

```aur: yay -S multipass```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lxc](/man/lxc)(1), [vagrant](/man/vagrant)(1), [docker](/man/docker)(1), [qemu](/man/qemu)(1)
