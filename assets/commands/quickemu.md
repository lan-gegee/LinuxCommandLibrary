# TAGLINE

创建和运行优化过的 QEMU 虚拟机

# TLDR

从配置文件**运行**虚拟机

```quickemu --vm [file.conf]```

运行且**不提交更改**

```quickemu --status-quo --vm [file.conf]```

以指定显示后端**全屏**运行

```quickemu --fullscreen --display [sdl] --vm [file.conf]```

创建/恢复/删除**快照**

```quickemu --snapshot [create|apply|delete] [tag] --vm [file.conf]```

列出**快照**

```quickemu --snapshot info --vm [file.conf]```

**删除**虚拟机

```quickemu --delete-vm --vm [file.conf]```

# SYNOPSIS

**quickemu** [**--vm** _config_] [**--display** _backend_] [**--snapshot** _action_] [_options_]

# PARAMETERS

**--vm _config_**
> 虚拟机配置文件

**--status-quo**
> 不将更改提交到磁盘

**--fullscreen**
> 以全屏模式启动

**--display _backend_**
> 显示后端：sdl、gtk、spice、spice-app、none

**--sound-card _card_**
> 声卡：intel-hda、ac97、es1370、sb16、none

**--snapshot _action_ _tag_**
> 快照操作：create、apply、delete、info

**--delete-vm**
> 删除虚拟机及其配置

**--delete-disk**
> 删除磁盘镜像和 EFI 变量

**--shortcut**
> 创建桌面快捷方式

# DESCRIPTION

**quickemu** 只需极少的配置即可创建和管理优化过的 QEMU 虚拟机。它会根据客户机操作系统自动配置显示、音频、USB 直通和共享文件夹。

虚拟机通过简单的配置文件定义，只需指定操作系统类型和磁盘镜像。复杂的 QEMU 命令行选项由工具在内部处理。

# CAVEATS

需要 QEMU 及相关软件包。部分功能需要 KVM 支持。要获得最佳集成效果可能需要安装增强组件。macOS 客户机有特殊要求。

# HISTORY

**quickemu** 由 **Martin Wimpress** 创建，旨在简化 QEMU 虚拟机管理。它源自用于测试 Linux 发行版的脚本，后来发展成一套完整的虚拟机工具。

# INSTALL

```apt: sudo apt install quickemu```

```dnf: sudo dnf install quickemu```

```nix: nix profile install nixpkgs#quickemu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[quickget](/man/quickget)(1), [qemu](/man/qemu)(1), [virt-manager](/man/virt-manager)(1)
