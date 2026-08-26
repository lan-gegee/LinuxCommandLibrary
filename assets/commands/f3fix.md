# TAGLINE

修复假冒闪存盘的分区表

# TLDR

**修复虚假闪存**容量

```f3fix --last-sec [size] [/dev/sdb]```

**计算正确的大小**

```f3fix --last-sec $(f3probe --destructive [/dev/sdb] | grep 'last usable sector')```

**使用指定**扇区修复

```f3fix --last-sec [1953125] [/dev/sdb]```

# SYNOPSIS

**f3fix** [_options_] _device_

# PARAMETERS

_DEVICE_
> 要修复的块设备（如 /dev/sdb）。

**--last-sec** _SECTOR_
> 设置最后一个可用扇区的编号。

**--help**
> 显示帮助信息。

# DESCRIPTION

**f3fix** 创建一个与假冒闪存盘真实容量相符的分区。它是 F3（Fight Flash Fraud）工具集的一部分，在 f3probe 识别出假冒设备的实际大小后使用。

假冒闪存盘报告的容量大于其实际容量，会导致数据丢失。f3fix 创建一个限制在真实可用空间内的分区，防止向超出实际存储容量的区域写入数据。

该工具会修改分区表以反映真实容量，使设备能够按其实际大小安全使用。

# CAVEATS

需要 root 权限。会破坏现有分区表。只能在 f3probe 确定真实容量之后使用。设备必须已卸载。

# HISTORY

f3fix 是 **F3**（Fight Flash Fraud）项目的一部分，该项目旨在打击假冒闪存。该工具集帮助识别虚假容量闪存盘并安全地使用它们，这类产品在网上购物平台十分常见。

# INSTALL

```apt: sudo apt install f3```

```dnf: sudo dnf install f3```

```apk: sudo apk add f3-extra```

```zypper: sudo zypper install f3```

```brew: brew install f3```

```nix: nix profile install nixpkgs#f3```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[f3probe](/man/f3probe)(1), [f3read](/man/f3read)(1), [f3write](/man/f3write)(1), [fdisk](/man/fdisk)(1)

# RESOURCES

```[Source code](https://github.com/AltraMayor/f3)```

<!-- verified: 2026-07-15 -->
