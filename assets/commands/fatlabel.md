# TAGLINE

FAT 文件系统卷标工具

# TLDR

**读取** FAT 文件系统的卷标

```fatlabel [/dev/sda1]```

**写入**新卷标

```fatlabel [/dev/sdc3] "[new_label]"```

# SYNOPSIS

**fatlabel** _device_ [_label_]

# DESCRIPTION

**fatlabel** 用于获取或设置 FAT 文件系统的卷标。不带卷标参数时，显示当前卷标；带卷标参数时，设置新卷标。

它是 dosfstools 软件包的一部分，该软件包用于管理 FAT 文件系统。

# PARAMETERS

_device_
> FAT 分区设备

_label_
> 新卷标（可选）

# CAVEATS

FAT 卷标限制为 11 个字符。写入时要求文件系统未挂载。dosfstools 软件包的一部分。

# INSTALL

```apt: sudo apt install dosfstools```

```dnf: sudo dnf install dosfstools```

```pacman: sudo pacman -S dosfstools```

```apk: sudo apk add dosfstools```

```zypper: sudo zypper install dosfstools```

```brew: brew install dosfstools```

```nix: nix profile install nixpkgs#dosfstools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dosfslabel](/man/dosfslabel)(8), [e2label](/man/e2label)(8), [mlabel](/man/mlabel)(1)

# RESOURCES

```[Source code](https://github.com/dosfstools/dosfstools)```

<!-- verified: 2026-07-15 -->
