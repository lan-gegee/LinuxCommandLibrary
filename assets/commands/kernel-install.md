# TAGLINE

管理启动分区中的内核映像

# TLDR

向引导加载程序**添加**内核和 initramfs

```sudo kernel-install add [kernel-version] [kernel-image] [path/to/initrd]```

从引导加载程序**移除**内核

```sudo kernel-install remove [kernel-version]```

**检查**配置和自动检测的路径

```sudo kernel-install inspect [kernel-image]```

# SYNOPSIS

**kernel-install** _command_ [_options_]

# PARAMETERS

**add** _VERSION_ _KERNEL_ [_INITRD_...]
> 将内核和可选的 initramfs 映像添加到启动分区

**remove** _VERSION_
> 从启动分区移除内核及相关文件

**inspect** [_KERNEL_]
> 显示已配置和自动检测的路径

# DESCRIPTION

**kernel-install** 管理启动分区中的内核映像。它是 systemd 的一部分，为 systemd-boot 及其他引导加载程序处理内核映像的安装和移除。

该工具运行插件（install.d 脚本）来完成复制文件、生成引导加载程序条目和更新 initramfs 等任务。它与 Boot Loader Specification 集成。

# CAVEATS

需要 root 权限。行为取决于已安装的插件。与 systemd-boot 配合效果最佳，但也可以通过插件支持其他引导加载程序。

# HISTORY

kernel-install 是 systemd 的一部分，提供管理内核安装的标准化方式。它实现了用于可移植启动配置的 Boot Loader Specification。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bootctl](/man/bootctl)(1), [dracut](/man/dracut)(8)
