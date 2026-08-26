# TAGLINE

通过读取卷描述符显示 ISO 9660 文件系统映像的大小

# TLDR

显示 ISO 文件的**大小**

```isosize [path/to/file.iso]```

显示**块数量**和块大小

```isosize -x [path/to/file.iso]```

显示大小除以**指定数字**后的结果

```isosize -d [number] [path/to/file.iso]```

# SYNOPSIS

**isosize** [_options_] _file_

# PARAMETERS

**-x**, **--sectors**
> 显示块数量和块大小，而不是总字节数

**-d**, **--divisor** _NUM_
> 用大小除以指定的数字（不能与 -x 同用）

# DESCRIPTION

**isosize** 通过读取卷描述符来显示 ISO 9660 文件系统映像的大小。与报告文件大小的工具不同，isosize 报告的是存储在 ISO 头部中的实际文件系统大小。

当 ISO 映像文件被填充过空间，或在确定将映像写入介质所需的精确大小时，这个工具会很有用。

# CAVEATS

只对有效的 ISO 9660 映像有效。报告的是卷描述符中记录的大小，如果映像曾被截断或填充过，该大小可能与文件大小不同。

# HISTORY

isosize 是 util-linux 软件包的一部分，提供了一个查询 ISO 映像大小的简单工具。它通过读取 ISO 9660 主卷描述符来确定大小。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add util-linux-misc```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[isoinfo](/man/isoinfo)(1), [genisoimage](/man/genisoimage)(1), [du](/man/du)(1)
