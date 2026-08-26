# TAGLINE

无需 root 卸载可移动设备

# TLDR

**卸载设备**

```pumount [/dev/sdb1]```

**按挂载点卸载**

```pumount [/media/usb]```

**按标签卸载**

```pumount [LABEL]```

**延迟卸载**

```pumount --lazy [/dev/sdb1]```

# SYNOPSIS

**pumount** [_options_] _device_|_directory_

# PARAMETERS

**-l**, **--lazy**
> 延迟卸载（立即分离文件系统，待不再繁忙时清理）。请谨慎使用，可能导致数据丢失。

**--luks-force**
> 即使 pmount 未打开该设备，也强制关闭 LUKS。

**-d**, **--debug**
> 启用详细的调试消息。

**--version**
> 打印版本号并退出。

# DESCRIPTION

**pumount** 是 pmount 的配套工具，用于在没有 root 权限的情况下卸载可移动设备。它是标准 umount 的一个封装，允许普通用户在 /etc/fstab 中没有对应条目的情况下卸载可移动设备。它支持加密的 dm-crypt/LUKS 卷并确保正确清理。它还支持卸载被强行拔出的设备。

# CAVEATS

仅适用于由 pmount 挂载的设备。不处理 fstab 挂载项。对于繁忙的设备可能需要 --lazy。

# HISTORY

pumount 是 **Martin Pitt** 的 **pmount** 的一部分，为可移动介质提供非 root 卸载能力。

# INSTALL

```apt: sudo apt install pmount```

```dnf: sudo dnf install pmount```

```nix: nix profile install nixpkgs#pmount```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pmount](/man/pmount)(1), [umount](/man/umount)(8), [udisksctl](/man/udisksctl)(1)
