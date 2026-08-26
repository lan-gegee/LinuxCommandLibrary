# TAGLINE

从目标文件中移除符号

# TLDR

**剥离**文件中的全部符号（就地修改）

```strip [path/to/file]```

剥离后保存到**输出文件**

```strip [path/to/input] -o [path/to/output]```

仅剥离**调试符号**

```strip -d [path/to/file.o]```

剥离**不需要的**符号

```strip --strip-unneeded [path/to/file]```

**保留**特定符号

```strip -K [symbol_name] [path/to/file]```

**移除**特定节区

```strip -R [section_name] [path/to/file]```

只保留**调试**信息

```strip --only-keep-debug [path/to/file]```

# SYNOPSIS

**strip** [_OPTIONS_] _objfile_...

# PARAMETERS

**-s, --strip-all**
> 移除所有符号

**-g, -S, -d, --strip-debug**
> 仅移除调试符号

**--strip-unneeded**
> 移除重定位不需要的符号

**--only-keep-debug**
> 仅保留调试节区

**-K, --keep-symbol** _name_
> 保留特定符号（可重复）

**-N, --strip-symbol** _name_
> 移除特定符号（可重复）

**-R, --remove-section** _name_
> 移除指定名称的节区（允许使用通配符）

**--keep-section** _pattern_
> 保留匹配的节区

**-x, --discard-all**
> 移除所有非全局符号

**-X, --discard-locals**
> 移除编译器生成的局部符号

**-o** _file_
> 将输出写入文件（仅限单个输入）

**-p, --preserve-dates**
> 保留访问/修改时间戳

**-D, --enable-deterministic-archives**
> 归档中的 UID/GID/时间戳使用零值

**--strip-dwo**
> 移除 DWARF .dwo 节区（拆分调试信息）

**--strip-section-headers**
> 剥离 ELF 节区头（仅限 ELF 文件）

**--remove-relocations** _pattern_
> 从匹配的节区中移除重定位信息

**--keep-file-symbols**
> 保留标识源文件名的符号

**--keep-section-symbols**
> 保留标识节区名的符号

**-M, --merge-notes**
> 合并并移除 ELF 文件中的重复 note

**-w, --wildcard**
> 允许在 -K 和 -N 的符号名中使用 Shell 风格通配符

**-v, --verbose**
> 列出所有处理过的文件

**--help**
> 显示帮助

**--version**
> 显示版本

# DESCRIPTION

**strip** 从目标文件和可执行文件中移除符号和其他数据，减小文件体积并增加逆向工程的难度。默认情况下它就地修改文件。归档（.a 文件）也可以被剥离。

发布构建通常剥离调试符号以缩小二进制体积，同时保持功能不变。**--only-keep-debug** 选项会生成单独的调试文件供调试器使用，而生产二进制保持精简。

# CAVEATS

strip 会就地修改文件；如有需要请备份原始文件。过度剥离可能破坏动态链接或调试能力。对可能被链接的库应使用 **--strip-debug**。剥离后静态分析和调试都会变得困难。

# HISTORY

**strip** 是 GNU **binutils** 的一部分，binutils 是由自由软件基金会维护的二进制工具集合。该命令起源于 **1970 年代**贝尔实验室的早期 Unix，用于在存储受限的系统上缩减可执行文件体积。GNU binutils 提供了 Linux 上使用的现代实现。

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

[objcopy](/man/objcopy)(1), [objdump](/man/objdump)(1), [readelf](/man/readelf)(1), [nm](/man/nm)(1), [ar](/man/ar)(1), [size](/man/size)(1)
