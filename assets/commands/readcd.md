# TAGLINE

读取 CD/DVD 光盘数据

# TLDR

**读取** CD 并复制为 ISO 文件

```readcd dev=/dev/sr0 f=[path/to/file.iso]```

**列出**可用的 SCSI/光驱设备

```readcd -scanbus```

**读取**指定范围的扇区

```readcd dev=/dev/sr0 sectors=[0]-[10000] f=[out.bin]```

以降低的速度**读取**以提高可靠性

```readcd dev=/dev/sr0 speed=[4] f=[file.iso]```

**制作完整克隆**，包括子通道数据和 TOC

```readcd dev=/dev/sr0 -clone f=[disc.img]```

# SYNOPSIS

**readcd** [_options_] dev=_device_ f=_file_

# PARAMETERS

**dev=**_device_
> 要读取的 CD/DVD/BluRay 设备（如 /dev/sr0 或 1,0,0 这类 SCSI 表示法）。

**f=**_file_
> 读取操作的输出文件（写入时为输入文件）。用 '-' 表示 stdout/stdin。

**sectors=**_range_
> 要读取的扇区范围，如 150-10000（结束扇区不包含在内）。

**speed=**_n_
> 以单速的倍数表示的读取速度（CD 单速为 150 KB/s）。较低的速度可以改善读取效果。

**retries=**_n_
> 对不可读扇区的高层重试次数。默认为 128。

**-clone**
> 读取整张光盘，包括所有子通道数据和完整目录表（TOC）（保存时附带 .toc 文件）。

**-fulltoc**
> 获取并以十六进制打印完整目录表。

**-c2scan**
> 扫描光盘中的 C2（无法纠正）错误。

**-w**
> 切换到写入模式（仅限 DVD-RAM）。

**-scanbus**
> 列出所有可用的 SCSI 设备。

**-v**
> 提高详细程度，报告读取进度。

# DESCRIPTION

**readcd** 读取 CD、DVD 和 BluRay 介质的数据，通常用于创建物理光盘的 ISO 镜像或原始转储。它也可以写回数据，但仅限于 DVD-RAM 介质（配合 **-w**）。

该工具直接访问原始光盘数据，支持重试、扇区范围和完整克隆（子通道数据加 TOC），适合制作介质的精确副本。

# CAVEATS

需要对光驱设备的读取权限。某些带拷贝保护的光盘可能无法正确读取。

# HISTORY

属于 **cdrtools**（部分发行版为 cdrkit）的一部分，提供 CD/DVD 刻录和读取工具。

# INSTALL

```apk: sudo apk add cdrkit```

```zypper: sudo zypper install readcd```

```nix: nix profile install nixpkgs#cdrkit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cdrecord](/man/cdrecord)(1), [dd](/man/dd)(1), [wodim](/man/wodim)(1)
