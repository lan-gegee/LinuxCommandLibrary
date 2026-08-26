# TAGLINE

列出二进制目标文件的段大小

# TLDR

显示可执行文件的段大小

```size [path/to/file]```

以八进制显示大小

```size -o [path/to/file]```

以十进制显示大小

```size -d [path/to/file]```

以十六进制显示大小

```size -x [path/to/file]```

显示多个文件的总计

```size -t [path/to/file1] [path/to/file2]```

使用 System V 输出格式

```size -A [path/to/file]```

# SYNOPSIS

**size** [**-A**|**-B**|**-G**] [**-d**|**-o**|**-x**] [**-t**] [_objfile_...]

# PARAMETERS

**-A, --format=sysv**
> 使用 System V 输出格式（详细的段列表）

**-B, --format=berkeley**
> 使用 Berkeley 输出格式（默认：text、data、bss、total）

**-G, --format=gnu**
> 使用 GNU 输出格式

**-d, --radix=10**
> 以十进制显示大小

**-o, --radix=8**
> 以八进制显示大小

**-x, --radix=16**
> 以十六进制显示大小

**-t, --totals**
> 显示所有列出目标文件的汇总总计

**--common**
> 将 common 符号计入 bss 大小

**--target** _bfdname_
> 指定文件的目标代码格式

**-V, --version**
> 显示版本信息

**-h, --help**
> 显示帮助信息

# DESCRIPTION

**size** 列出二进制目标文件的各段大小和总大小。对于每个目标文件，它会显示 text（代码）、data 和 bss（未初始化数据）段的大小，以及以字节和十六进制表示的总大小。

默认的 Berkeley 格式为每个文件显示简洁的单行输出。System V 格式提供所有段的详细列表。未指定文件时，默认检查 **a.out**。

# CAVEATS

只能处理受支持格式（ELF、COFF 等）的目标文件和可执行文件。静态库会显示其中每个目标模块的大小。结果可能因编译选项和链接方式而异。

# HISTORY

**size** 是 GNU **binutils** 的一部分，这是自由软件基金会维护的二进制工具集。该命令起源于 **20 世纪 70 年代**贝尔实验室的早期 Unix 系统，此后一直是标准的开发工具。GNU binutils 为各种平台提供了兼容的实现。

# INSTALL

```apt: sudo apt install binutils```

```dnf: sudo dnf install binutils```

```pacman: sudo pacman -S binutils```

```apk: sudo apk add binutils```

```zypper: sudo zypper install binutils```

```brew: brew install binutils```

```nix: nix profile install nixpkgs#binutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[objdump](/man/objdump)(1), [readelf](/man/readelf)(1), [nm](/man/nm)(1), [strip](/man/strip)(1)
