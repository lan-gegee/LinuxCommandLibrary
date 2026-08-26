# TAGLINE

交互式 GPT 分区工具

# TLDR

**列出**分区

```sudo gdisk -l```

启动**交互式**分区操作程序

```sudo gdisk /dev/sdX```

# INTERACTIVE COMMANDS

**?**
> 打开帮助菜单

**p**
> 打印分区表

**n**
> 添加新分区

**d**
> 删除分区

**t**
> 更改分区类型

**c**
> 更改分区名称

**w**
> 将分区表写入磁盘并退出

**q**
> 不保存更改直接退出

# SYNOPSIS

**gdisk** [_options_] _device_

# PARAMETERS

**-l**, **--list**
> 列出所有设备的分区表然后退出

**device**
> 要分区的设备（例如 /dev/sda、/dev/nvme0n1）

# DESCRIPTION

**gdisk** 是一个交互式 GPT（GUID 分区表）分区工具，类似于 fdisk，但专为 GPT 磁盘设计。它可以在现代 UEFI 系统上创建、删除和修改分区。

GPT 是取代 MBR（主引导记录）的现代分区方案，支持大于 2TB 的磁盘以及超过 4 个的主分区（最多 128 个）。gdisk 同时维护主分区表和备份分区表以实现冗余。

gdisk 还可以将 MBR 磁盘转换为 GPT（用 **sgdisk** 可以反向转换），不过此操作需谨慎进行并做好备份。

# CAVEATS

需要 root 权限。更改只有在使用 **w** 命令时才会写入磁盘。MBR 与 GPT 之间的转换如果操作不当可能导致无法启动。分区前务必备份重要数据。

# HISTORY

gdisk（GPT fdisk）由 Roderick W. Smith 创建，于 **2009 年**前后首次发布。随着 UEFI 和 GPT 成为现代系统的标准，它被开发为一个界面类似经典 fdisk 的文本模式 GPT 分区工具。

# INSTALL

```apt: sudo apt install gdisk```

```dnf: sudo dnf install gdisk```

```pacman: sudo pacman -S gptfdisk```

```apk: sudo apk add gptfdisk```

```zypper: sudo zypper install gptfdisk```

```brew: brew install gptfdisk```

```nix: nix profile install nixpkgs#gptfdisk```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fdisk](/man/fdisk)(8), [parted](/man/parted)(8), [cfdisk](/man/cfdisk)(8), [sgdisk](/man/sgdisk)(8)

# RESOURCES

```[Homepage](https://www.rodsbooks.com/gdisk/)```

```[Source code](https://sourceforge.net/projects/gptfdisk/)```

<!-- verified: 2026-07-15 -->
