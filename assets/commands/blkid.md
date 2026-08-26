# TAGLINE

识别块设备属性

# TLDR

以属性列表形式列出**所有**块设备

```sudo blkid```

以**表格**形式列出所有分区（包括挂载点）

```sudo blkid -o list```

获取指定分区的 **UUID**

```sudo blkid -s UUID -o value [/dev/sdXY]```

获取分区的**文件系统类型**

```sudo blkid -s TYPE -o value [/dev/sdXY]```

按**标签（label）**查找设备

```sudo blkid -L [mylabel]```

按 **UUID** 查找设备

```sudo blkid -U [uuid]```

绕过缓存**探测**设备

```sudo blkid -p [/dev/sdXY]```

# SYNOPSIS

**blkid** [_-o format_] [_-s tag_] [_device_...]

# DESCRIPTION

**blkid** 列出所有已识别的分区及其属性，包括通用唯一标识符（UUID）、文件系统类型和标签。它使用 libblkid 库来定位和识别块设备。

# PARAMETERS

**-o, --output format**
> 输出格式：full、value、list、device、udev、export

**-s, --match-tag tag**
> 只显示指定的标签（UUID、TYPE、LABEL 等）

**-c, --cache-file file**
> 从指定的缓存文件读取而非默认文件

**-g, --garbage-collect**
> 对 blkid 缓存执行垃圾回收

**-l, --list-one**
> 只查找一个匹配参数的设备

**-L, --label label**
> 按文件系统标签查找设备

**-U, --uuid uuid**
> 按文件系统 UUID 查找设备

**-p, --probe**
> 底层超级块探测模式（绕过缓存）

**-i, --info**
> 打印 I/O 限制信息（扇区大小等）

**-t, --match-token** _NAME=value_
> 搜索具有名为 NAME 且值为指定值的令牌的块设备

**-n, --match-types** _list_
> 将探测限制在逗号分隔的超级块类型列表内

**-u, --usages** _list_
> 将探测限制在逗号分隔的用途类型列表内（filesystem、raid、crypto、other）

# CONFIGURATION

**/etc/blkid.tab**
> 默认缓存文件，存储之前检测到的块设备属性。

**/run/blkid/blkid.tab**
> 使用 tmpfs 作为 /run 的系统上的运行时缓存位置。

# CAVEATS

输出格式随选项而异。不带参数运行会显示所有块设备。结果可能来自缓存；使用 **-p** 可实时探测。

# HISTORY

属于 **util-linux** 软件包。开发目的是为识别块设备属性提供统一接口。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add blkid```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lsblk](/man/lsblk)(8), [findfs](/man/findfs)(8), [mount](/man/mount)(8), [fdisk](/man/fdisk)(8)
