# TAGLINE

旧内核清理工具

# TLDR

**列出**所有内核文件

```sudo eclean-kernel -l```

只保留最新的 **2 个**内核

```sudo eclean-kernel -n 2```

**预览**将被移除的内容

```sudo eclean-kernel -p -n 2```

带**确认**地移除内核

```sudo eclean-kernel -A -n 2```

移除所有**未被引导程序引用**的内核

```sudo eclean-kernel -a```

# SYNOPSIS

**eclean-kernel** [_options_]

# DESCRIPTION

**eclean-kernel** 移除 Gentoo Linux 中的旧内核。它会清理内核镜像、模块及相关文件，同时保留指定数量的近期内核。

随着时间推移，/boot 和 /lib/modules 会积累升级产生的旧内核版本，占用大量磁盘空间。这对引导分区较小的系统尤其成问题。eclean-kernel 自动识别并删除旧的内核文件，同时保护正在运行的内核和可配置数量的近期版本。

该工具处理所有与内核相关的组件，包括内核镜像、System.map、initramfs、配置文件和模块目录。它比手动删除更安全，因为它理解内核依赖关系，避免误删关键文件。

# PARAMETERS

**-l, --list-kernels**
> 列出所有已安装的内核并退出

**-n** _NUM_
> 保留 N 个最新内核

**-A, --ask**
> 移除每个内核前先询问

**-a, --all**
> 移除所有未被引导程序引用的内核

**-d, --destructive**
> 破坏模式：即使被引导程序引用也移除内核

**-p, --pretend**
> 打印将要移除的内核并退出

**-b, --bootloader** _BOOTLOADER_
> 所使用的引导程序（auto、lilo、grub2、grub、yaboot、symlinks）

**-x, --exclude** _KERNEL_
> 排除特定内核不移除

**--no-bootloader-update**
> 移除后不更新引导程序配置

# CAVEATS

仅限 Gentoo。务必至少保留一个可用内核。当前正在运行的内核会受到保护。

# SEE ALSO

[eclean](/man/eclean)(1), [emerge](/man/emerge)(1)
