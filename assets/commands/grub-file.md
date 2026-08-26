# TAGLINE

检查引导映像文件类型

# TLDR

检查文件是否为 **ARM EFI** 映像

```grub-file --is-arm-efi [path/to/file]```

检查文件是否为 **i386 EFI** 映像

```grub-file --is-i386-efi [path/to/file]```

检查文件是否为 **x86_64 EFI** 映像

```grub-file --is-x86_64-efi [path/to/file]```

检查文件是否为 **ARM Linux** 内核

```grub-file --is-arm-linux [path/to/file]```

检查文件是否为 **x86 Linux** 内核（32 位或 64 位）

```grub-file --is-x86-linux [path/to/file]```

检查文件是否为 **x86 Multiboot2** 内核

```grub-file --is-x86-multiboot2 [path/to/file]```

检查文件是否为 **x86_64 XNU**（macOS）内核

```grub-file --is-x86_64-xnu [path/to/file]```

# SYNOPSIS

**grub-file** _--is-TYPE_ _file_

# PARAMETERS

**--is-arm-efi**
> 检查是否为 ARM EFI 映像

**--is-arm64-efi**
> 检查是否为 ARM64 EFI 映像

**--is-i386-efi**
> 检查是否为 i386 EFI 映像

**--is-x86_64-efi**
> 检查是否为 x86_64 EFI 映像

**--is-arm-linux**
> 检查是否为 ARM Linux 内核

**--is-arm64-linux**
> 检查是否为 ARM64 Linux 内核

**--is-x86-linux**
> 检查是否为 x86 Linux 内核（同时覆盖 32 位和 64 位）

**--is-x86-linux32**
> 检查是否为使用仅 32 位引导协议的 x86 Linux 内核

**--is-x86_64-xnu**
> 检查是否为 macOS（XNU）x86_64 内核

**--is-x86-multiboot**
> 检查是否为 Multiboot 映像

**--is-x86-multiboot2**
> 检查是否为 Multiboot2 映像

# DESCRIPTION

**grub-file** 检查某个文件是否是特定类型的可引导映像。它通过检查文件头和签名来识别内核映像、EFI 应用程序及其他可引导格式。

如果文件匹配指定类型，命令返回退出码 0（成功），否则返回 1（失败）。这在脚本中可用于验证引导映像或确定正确的引导方式。

# CAVEATS

只检查文件类型签名；不会验证该映像是否真的可以启动或有效。某些特殊或自定义内核可能无法被正确识别。

# HISTORY

grub-file 属于 GRUB 2，提供了一个映像类型检测工具。它在安装和配置期间很有用，可确保为目标架构配置正确的引导加载程序。

# INSTALL

```apt: sudo apt install grub-common```

```pacman: sudo pacman -S grub```

```apk: sudo apk add grub```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grub-install](/man/grub-install)(8), [grub-probe](/man/grub-probe)(8), [file](/man/file)(1)

# RESOURCES

```[Homepage](https://www.gnu.org/software/grub/)```

```[Source code](https://git.savannah.gnu.org/cgit/grub.git)```

```[Documentation](https://www.gnu.org/software/grub/manual/grub/grub.html)```

<!-- verified: 2026-07-17 -->
