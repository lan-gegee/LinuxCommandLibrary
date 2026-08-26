# TAGLINE

通过 udisks2 挂载可移动设备

# TLDR

挂载**所有**可处理的设备

```udiskie-mount -a```

挂载**指定**设备

```udiskie-mount [/dev/sdX1]```

以**详细输出**模式挂载

```udiskie-mount --verbose [/dev/sdX1]```

# SYNOPSIS

**udiskie-mount** [_OPTIONS_] [_DEVICE_...]

# PARAMETERS

**-a, --all**
> 挂载所有可处理的设备

**--verbose**
> 启用详细输出

**--help**
> 显示帮助信息

# DESCRIPTION

**udiskie-mount** 使用 udiskie 和 udisks2 手动挂载设备。它提供命令行界面来挂载可移动设备，且不需要 root 权限。

设备会被挂载到 udisks2 管理的标准位置，通常位于 /run/media/USERNAME/ 下。

# CAVEATS

需要 udisks2 守护进程。设备必须被 udisks2 识别。某些加密设备需要额外配置才能弹出密码提示。

# INSTALL

```dnf: sudo dnf install udiskie```

```pacman: sudo pacman -S udiskie```

```apk: sudo apk add udiskie```

```zypper: sudo zypper install udiskie```

```nix: nix profile install nixpkgs#udiskie```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[udiskie](/man/udiskie)(1), [udiskie-umount](/man/udiskie-umount)(1), [udisksctl](/man/udisksctl)(1)
