# TAGLINE

通过 FUSE 挂载 iOS 设备文件系统

# TLDR

**挂载 iOS 设备**

```ifuse [/mnt/iphone]```

**挂载应用文档目录**

```ifuse --documents [com.app.id] [/mnt/app]```

**挂载指定设备**

```ifuse -u [udid] [/mnt/device]```

**卸载**

```fusermount -u [/mnt/iphone]```

# SYNOPSIS

**ifuse** [_options_] _mountpoint_

# PARAMETERS

_MOUNTPOINT_
> 挂载点目录。

**-u** _UDID_
> 目标设备。

**--documents** _APPID_
> 挂载应用文档目录。

**--container** _APPID_
> 挂载应用沙盒容器。

**-o** _OPTIONS_
> FUSE 选项。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ifuse** 通过 FUSE 挂载 iOS 设备的文件系统。它提供对设备存储、应用文档和容器的访问。

该工具要求设备已完成配对，并使用 AFC 协议。它让你无需 iTunes 或第三方应用即可传输文件。

# CAVEATS

属于 libimobiledevice。设备必须已配对。只能访问可访问的区域。

# HISTORY

ifuse 是 **libimobiledevice** 的组成部分，用于在 Linux 上访问 iOS 文件系统。

# INSTALL

```apt: sudo apt install ifuse```

```dnf: sudo dnf install ifuse```

```pacman: sudo pacman -S ifuse```

```apk: sudo apk add ifuse```

```zypper: sudo zypper install ifuse```

```brew: brew install ifuse```

```nix: nix profile install nixpkgs#ifuse```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[idevice_id](/man/idevice_id)(1), [idevicepair](/man/idevicepair)(1), [fusermount](/man/fusermount)(1)
