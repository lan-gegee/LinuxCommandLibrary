# TAGLINE

MAME Compressed Hunks of Data 管理器

# TLDR

**显示 CHD 文件信息**

```chdman info -i [path/to/image.chd]```

**校验 CHD 文件完整性**

```chdman verify -i [path/to/image.chd]```

**从 CD 镜像创建 CHD（bin/cue）**

```chdman createcd -i [path/to/image.cue] -o [path/to/output.chd]```

**从原始硬盘镜像创建 CHD**

```chdman createhd -i [path/to/image.img] -o [path/to/output.chd]```

**从 CHD 提取 CD 镜像**

```chdman extractcd -i [path/to/image.chd] -o [path/to/output.cue]```

**从 CHD 提取原始硬盘镜像**

```chdman extracthd -i [path/to/image.chd] -o [path/to/output.img]```

**以不同压缩方式复制 CHD**

```chdman copy -i [path/to/input.chd] -o [path/to/output.chd] -c [lzma,zlib,huff,flac]```

# SYNOPSIS

**chdman** _command_ [**-i** _input_] [**-o** _output_] [**-c** _compression_] [_options..._]

# DESCRIPTION

**chdman** 是 MAME Compressed Hunks of Data（CHD）管理器。CHD 是一种专为 MAME 及其他模拟器所用磁盘镜像设计的无损压缩格式，支持硬盘、CD-ROM、LaserDisc 和 GD-ROM。

该格式在保持数据完全完整的同时提供高效压缩，非常适合归档游戏介质。CHD 支持基于父镜像的增量压缩，以减少相似版本的存储占用。

# PARAMETERS

**info**
> 显示 CHD 头部信息

**verify**
> 校验 MD5/SHA1 校验和

**createcd**
> 从 CD 镜像创建 CHD（cue/bin、toc/bin、gdi）

**createhd**
> 从原始硬盘镜像创建 CHD

**createraw**
> 从原始数据文件创建 CHD

**createld**
> 从 LaserDisc 镜像创建 CHD

**extractcd**
> 从 CHD 提取 CD 镜像

**extracthd**
> 从 CHD 提取硬盘镜像

**copy**
> 复制 CHD，可选择重新压缩

**-i** _file_
> 输入文件

**-o** _file_
> 输出文件

**-c** _algorithms_
> 压缩：none，或最多四个逗号分隔的算法（默认：lzma,zlib,huff,flac）

**--outputparent** _file_
> 创建增量 CHD，仅存储与父文件的差异

# CAVEATS

Hunk 大小必须在 16 字节到 1 MiB 之间。3DO、Dreamcast、PlayStation、Saturn、Mega CD、Neo-Geo CD、PC Engine CD 等平台的模拟器均支持 CHD 格式。

# HISTORY

CHD 是作为 **MAME**（Multiple Arcade Machine Emulator）项目的一部分开发的，旨在为磁盘镜像提供高效的无损压缩，同时精确保留数据以实现准确模拟。

# INSTALL

```apt: sudo apt install mame-tools```

```dnf: sudo dnf install mame-tools```

```pacman: sudo pacman -S mame-tools```

```zypper: sudo zypper install mame-tools```

```nix: nix profile install nixpkgs#mame-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mame](/man/mame)(6)

# RESOURCES

```[Source code](https://github.com/mamedev/mame)```

```[Documentation](https://docs.mamedev.org/tools/chdman.html)```

<!-- verified: 2026-06-22 -->
