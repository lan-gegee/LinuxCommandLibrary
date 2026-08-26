# TAGLINE

创建可引导的 GRUB 救援镜像

# TLDR

从当前目录创建**可引导 ISO**

```grub-mkrescue --output [grub.iso] .```

使用**自定义目录**中的 GRUB 文件创建 ISO

```grub-mkrescue --directory [/usr/lib/grub/i386-pc] --output [grub.iso] [path/to/source]```

构建镜像时对 GRUB 文件进行**压缩**

```grub-mkrescue --compress [xz|gz|lzo|no] --output [grub.iso] [path/to/source]```

向镜像中**预加载**指定的 GRUB 模块

```grub-mkrescue --modules "[part_gpt iso9660]" --output [grub.iso] [path/to/source]```

显示**帮助**

```grub-mkrescue --help```

# SYNOPSIS

**grub-mkrescue** [_options_] [_source_]

# PARAMETERS

**--output** _FILE_
> 将生成的镜像写入指定文件

**--directory** _DIR_
> 使用指定目录中的 GRUB 文件

**--compress** _TYPE_
> 使用 xz、gz、lzo 压缩 GRUB 文件，no 表示禁用压缩

**--modules** _MODULES_
> 向镜像中预加载指定的 GRUB 模块

**--disable-cli**
> 在生成的镜像中禁用 GRUB 命令行界面

**--version**
> 显示版本信息

# DESCRIPTION

**grub-mkrescue** 以 GRUB 作为引导加载程序，创建可引导的 CD、USB 或软盘镜像。它生成的是混合镜像，既可以从 BIOS 系统启动，也可以从 UEFI 系统启动。

该命令将源目录内容与必要的 GRUB 文件打包在一起，制作成可引导的救援或安装介质。可以使用 -- 分隔符向底层的 xorriso 工具传递额外选项。

# CAVEATS

创建 ISO 需要已安装 xorriso。生成的镜像默认为混合镜像，适用于光盘和 USB 驱动器。某些 BIOS/UEFI 组合可能需要预加载特定模块。

# HISTORY

grub-mkrescue 是 GRUB 2（GRand Unified Bootloader）的一部分，GRUB 2 是 GNU GRUB Legacy 的后继者。GRUB 2 的开发始于 **2002 年**前后，到 2009 年已成为大多数 Linux 发行版的默认引导加载程序。

# INSTALL

```apt: sudo apt install grub-common```

```pacman: sudo pacman -S grub```

```apk: sudo apk add grub```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grub-install](/man/grub-install)(8), [grub-mkconfig](/man/grub-mkconfig)(8), [mkisofs](/man/mkisofs)(8)
