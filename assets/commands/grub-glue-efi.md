# TAGLINE

合并 32 位与 64 位 EFI 二进制文件

# TLDR

**粘合 EFI 二进制文件**

```grub-glue-efi -3 [ia32.efi] -6 [x64.efi] -o [boot.efi]```

**创建 fat 二进制文件**

```grub-glue-efi --input32 [grub32.efi] --input64 [grub64.efi] --output [grub.efi]```

# SYNOPSIS

**grub-glue-efi** [_options_]

# PARAMETERS

**-3**, **--input32** _FILE_
> 32 位 EFI 输入。

**-6**, **--input64** _FILE_
> 64 位 EFI 输入。

**-o**, **--output** _FILE_
> 输出文件。

**-v**, **--verbose**
> 打印详细消息。

**--help**
> 显示帮助信息。

# DESCRIPTION

**grub-glue-efi** 处理 ia32 和 amd64 EFI 映像，并按 Apple 格式将它们粘合在一起，从两个 EFI 二进制文件创建一个 Apple fat EFI 二进制文件。这样，单个文件便可在配备 32 位或 64 位 EFI 固件的系统上启动。

该工具主要用于为 GRUB 引导加载程序创建通用 EFI 二进制文件，适用于必须在多样化硬件上启动的可移动介质。

# CAVEATS

属于 GRUB 软件包。需要两种架构的二进制文件。仅用于特殊的引导加载程序场景。

# HISTORY

grub-glue-efi 作为 **GNU GRUB** 的一部分开发，用于支持通用 EFI 启动介质的制作。

# INSTALL

```apt: sudo apt install grub-common```

```pacman: sudo pacman -S grub```

```apk: sudo apk add grub```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grub](/man/grub)(8), [grub-install](/man/grub-install)(8)
