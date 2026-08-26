# TAGLINE

管理磁盘分区的程序

# TLDR

列出**所有块设备**上的分区

```sudo parted -l```

创建**新的分区表**

```sudo parted /dev/sdX mklabel gpt```

创建**引导分区和系统分区**

```sudo parted /dev/sdX -s mklabel gpt mkpart "boot" 0% 500MiB mkpart "system" 500MiB 100%```

为分区设置 **boot 标志**

```sudo parted /dev/sdX set 1 boot on```

进入**交互模式**

```sudo parted /dev/sdX```

打印**分区信息**

```sudo parted /dev/sdX print```

# SYNOPSIS

**parted** [_options_] [_device_ [_command_ [_options_]...]]

# DESCRIPTION

**parted** 是一个管理磁盘分区的程序。它支持多种分区表格式，包括 MS-DOS（MBR）和 GPT。它可以用来为新操作系统腾出空间、重新组织磁盘的使用，以及把数据复制到新硬盘。

# PARAMETERS

**-h**, **--help**
> 显示帮助信息。

**-l**, **--list**
> 列出所有块设备上的分区布局。

**-m**, **--machine**
> 以机器可解析的格式输出。

**-j**, **--json**
> 显示 JSON 输出。

**-s**, **--script**
> 从不提示用户干预。

**-f**, **--fix**
> 在脚本模式下对异常自动回答 "fix"。

**-v**, **--version**
> 显示版本信息。

**-a**, **--align** _TYPE_
> 设置新分区的对齐方式（none、cylinder、minimal、optimal）。

# COMMANDS

**mklabel TYPE**
> 创建新的分区表（gpt、msdos 等）

**mkpart NAME START END**
> 创建新分区，可选指定文件系统类型

**print**
> 显示分区表

**rm NUMBER**
> 按编号删除分区

**select DEVICE**
> 选择要编辑的设备

**set NUMBER FLAG STATE**
> 更改分区标志（boot、raid、lvm、esp 等）

**name NUMBER NAME**
> 设置分区名称（仅限 GPT）

**resizepart NUMBER END**
> 修改分区的结束位置

**rescue START END**
> 恢复丢失的分区

**type NUMBER TYPE**
> 设置分区类型 ID（MBR）或 UUID（GPT）

**unit UNIT**
> 设置显示/输入单位（s、B、kB、MB、GB、TB、%）

# CAVEATS

Parted 会直接修改分区表，且更改立即生效。修改分区前务必备份重要数据。在脚本中使用 **-s** 标志可以避免交互式提示。

# HISTORY

**parted** 是 GNU Parted 软件包的一部分，由 Andrew Clausen 于 1999 年首次发布。它的设计目标是处理比传统 fdisk 更大的磁盘和更多的分区类型。

# INSTALL

```apt: sudo apt install parted```

```dnf: sudo dnf install parted```

```pacman: sudo pacman -S parted```

```apk: sudo apk add parted```

```zypper: sudo zypper install parted```

```nix: nix profile install nixpkgs#parted```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fdisk](/man/fdisk)(8), [gdisk](/man/gdisk)(8), [mkfs](/man/mkfs)(8), [partprobe](/man/partprobe)(8)
