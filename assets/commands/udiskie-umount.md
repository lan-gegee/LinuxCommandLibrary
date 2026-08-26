# TAGLINE

安全卸载可移动设备

# TLDR

**卸载**设备

```udiskie-umount [path/to/mount]```

卸载并**切断** USB 供电

```udiskie-umount --detach [path/to/mount]```

**弹出**光驱

```udiskie-umount --eject [path/to/mount]```

# SYNOPSIS

**udiskie-umount** [_OPTIONS_] _PATH_...

# PARAMETERS

**--detach**
> 卸载并给设备断电

**--eject**
> 弹出光盘介质

**--help**
> 显示帮助信息

# DESCRIPTION

**udiskie-umount** 使用 udiskie 和 udisks2 手动卸载设备。它能安全地卸载可移动介质，还可以选择为 USB 设备断电或弹出光驱。

路径既可以是设备路径（如 /dev/sdb1），也可以是挂载点。

# CAVEATS

设备不能正被任何进程使用。分离 USB 设备会将其完全断电。弹出操作仅适用于光驱。

# INSTALL

```dnf: sudo dnf install udiskie```

```pacman: sudo pacman -S udiskie```

```apk: sudo apk add udiskie```

```zypper: sudo zypper install udiskie```

```nix: nix profile install nixpkgs#udiskie```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[udiskie](/man/udiskie)(1), [udiskie-mount](/man/udiskie-mount)(1), [udisksctl](/man/udisksctl)(1)
