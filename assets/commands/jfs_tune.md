# TAGLINE

调整 JFS 文件系统的参数

# TLDR

**显示**文件系统信息

```sudo jfs_tune [/dev/sda1]```

设置卷标

```sudo jfs_tune -L [label] [/dev/sda1]```

更改 UUID

```sudo jfs_tune -U [random] [/dev/sda1]```

列出文件系统选项

```jfs_tune -l [/dev/sda1]```

# SYNOPSIS

**jfs_tune** [_options_] _device_

# PARAMETERS

_DEVICE_
> JFS 文件系统设备。

**-L** _LABEL_
> 设置卷标。

**-U** _UUID_
> 设置或生成 UUID。

**-l**
> 列出文件系统信息。

**-J** _OPTIONS_
> 外部日志选项。

**--help**
> 显示帮助信息。

# DESCRIPTION

**jfs_tune** 调整 JFS 文件系统的参数。它可以设置卷标、UUID 及其他文件系统元数据。

该工具只作用于未挂载的文件系统。它类似于 ext 文件系统上的 tune2fs。

# CAVEATS

仅适用于 JFS 文件系统。使用前需卸载。这是 Linux 工具。

# HISTORY

jfs_tune 是 **jfsutils** 的一部分，为从 IBM AIX 移植的 JFS 文件系统提供管理工具。

# INSTALL

```apt: sudo apt install jfsutils```

```dnf: sudo dnf install jfsutils```

```pacman: sudo pacman -S jfsutils```

```apk: sudo apk add jfsutils```

```zypper: sudo zypper install jfsutils```

```nix: nix profile install nixpkgs#jfsutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tune2fs](/man/tune2fs)(8)
