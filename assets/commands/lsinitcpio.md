# TAGLINE

检查 mkinitcpio initramfs 镜像的内容

# TLDR

**列出** initramfs 镜像内的文件

```lsinitcpio /boot/initramfs-linux.img```

**分析**镜像（内核版本、模块、二进制文件、早期 CPIO）

```lsinitcpio --analyze /boot/initramfs-linux.img```

显示构建该镜像所用的**配置**

```lsinitcpio --config /boot/initramfs-linux.img```

将镜像**解压**到当前目录

```lsinitcpio --extract /boot/initramfs-linux.img```

以**详细**的长格式列出内容

```lsinitcpio -v /boot/initramfs-linux.img```

仅列出或解压**早期 CPIO** 段

```lsinitcpio --early /boot/initramfs-linux.img```

仅列出或解压**主 CPIO** 段

```lsinitcpio --cpio /boot/initramfs-linux.img```

# SYNOPSIS

**lsinitcpio** [*action*] [*options*] *image*

# DESCRIPTION

**lsinitcpio** 用于检查由 **mkinitcpio** 生成的 initcpio（initramfs）镜像的内容。不带任何动作标志时会列出镜像中存储的文件。它是 Arch Linux 及相关发行版上 mkinitcpio 软件包的一部分，可用于验证构建镜像后包含了哪些钩子（hook）、模块和二进制文件。

镜像可能包含一个早期 CPIO 归档（微码、早期固件），其后是主压缩 CPIO。**--early** 和 **--cpio** 选项可将列表或解压操作限制在其中一段。

# ACTIONS

**-a**, **--analyze**

> 分析镜像并打印人类可读的摘要（内核版本、是否含早期 CPIO、包含的模块和二进制文件等元数据）。

**-c**, **--config**

> 显示给定镜像的构建配置文件。

**-l**, **--list**

> 列出归档内容。这是默认动作。传入 **-v** 可获得长格式输出。

**-x**, **--extract**

> 将给定镜像解压到当前工作目录。

# OPTIONS

**-h**, **--help**

> 打印可用命令行开关的简要概览。

**-n**, **--nocolor**

> 禁用彩色输出。

**-V**, **--version**

> 显示版本信息。

**-v**, **--verbose**

> 输出更详细。列表采用长格式；解压时打印正在写入的文件。

**--cpio**

> 仅列出或解压主 CPIO 镜像。

**--early**

> 仅在存在时列出或解压早期 CPIO 镜像。早期 CPIO 镜像详见 **mkinitcpio**(8)。

# CAVEATS

需要将 initramfs 路径作为参数（不像某些发行版工具会默认使用当前运行内核的镜像）。解压会写入当前目录并可能覆盖已有文件；请在空目录或专用目录中运行。属于 Arch Linux **mkinitcpio** 软件包的一部分，并非所有发行版都提供独立工具。

# SEE ALSO

[mkinitcpio](/man/mkinitcpio)(8), [lsinitrd](/man/lsinitrd)(1), [dracut](/man/dracut)(8), [cpio](/man/cpio)(1)

# RESOURCES

```[Source code](https://gitlab.archlinux.org/archlinux/mkinitcpio/mkinitcpio)```

```[Homepage](https://wiki.archlinux.org/title/Mkinitcpio)```

```[Documentation](https://man.archlinux.org/man/lsinitcpio.1)```

<!-- verified: 2026-07-19 -->
