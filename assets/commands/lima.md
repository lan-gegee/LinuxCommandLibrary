# TAGLINE

在 macOS 上运行 Linux 虚拟机

# TLDR

**创建默认虚拟机**

```limactl create```

**启动虚拟机**

```limactl start [default]```

**停止虚拟机**

```limactl stop [default]```

**进入虚拟机 Shell**

```limactl shell [default]```

**列出虚拟机**

```limactl list```

**删除虚拟机**

```limactl delete [default]```

# SYNOPSIS

**limactl** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 要执行的子命令。

**create** [_INSTANCE_]
> 创建新的虚拟机实例。

**start** _INSTANCE_
> 启动虚拟机实例。

**stop** _INSTANCE_
> 停止虚拟机实例。

**shell** _INSTANCE_
> 在实例中打开 shell。

**list**
> 列出所有实例。

**delete** _INSTANCE_
> 删除实例。

**--help**
> 显示帮助信息。

# DESCRIPTION

**lima**（Linux Machines）在 macOS 上运行 Linux 虚拟机。它提供自动文件共享和端口转发功能。

该工具使用 QEMU 进行虚拟化。常用于在 macOS 上运行 containerd 和 Docker。

# CAVEATS

专注于 macOS。需要 QEMU。运行虚拟机会占用大量资源。

# HISTORY

Lima 由 **Akihiro Suda** 创建，旨在 macOS 上提供具有无缝集成体验的轻量级 Linux 虚拟机。

# INSTALL

```zypper: sudo zypper install lima```

```brew: brew install lima```

```nix: nix profile install nixpkgs#lima```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [nerdctl](/man/nerdctl)(1), [colima](/man/colima)(1)
