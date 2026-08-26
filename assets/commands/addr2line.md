# TAGLINE

将地址转换为源文件位置

# TLDR

根据指令地址显示**文件名和行号**

```addr2line -e [path/to/executable] [address]```

显示**函数名**、文件名和行号

```addr2line -e [path/to/executable] -f [address]```

为 C++ 代码**还原**修饰过的函数名

```addr2line -e [path/to/executable] -f -C [address]```

**美化打印**含内联帧的结果

```addr2line -e [path/to/executable] -f -C -i -p [address]```

**从标准输入读取地址**（例如来自栈回溯）

```cat [addresses.txt] | addr2line -e [path/to/executable] -f -C```

# SYNOPSIS

**addr2line** [_-e executable_] [_-f_] [_-C_] [_-s_] [_-i_] [_address_...]

# DESCRIPTION

**addr2line** 将地址转换为文件名和行号。给定可执行文件或可重定位目标中的一个地址，它会利用调试信息找出与之关联的文件名和行号。

这对于解读崩溃转储以及来自栈回溯的调试信息特别有用。

# PARAMETERS

**-e, --exe executable**
> 指定要分析的可执行文件

**-f, --functions**
> 除文件和行号信息外还显示函数名

**-C, --demangle**
> 将底层符号名解码（还原）为用户级名称（对 C++ 很有用）

**-s, --basenames**
> 只显示每个文件名的基础名称，而不是完整路径

**-i, --inlines**
> 如果地址属于内联函数，则同时打印调用者信息

**-p, --pretty-print**
> 以人类可读的格式打印输出

**-a, --addresses**
> 在函数名、文件和行号之前显示地址

**-j, --section** _NAME_
> 将输入地址视为指定节内的偏移量。

**--target** _BFDNAME_
> 指定目标文件的二进制格式（默认自动检测）。

**-r, --no-recurse-limit**
> 禁用符号还原器的递归限制。

# CAVEATS

要求可执行文件编译时带有调试信息（例如 gcc 的 **-g** 标志）。已剥离（strip）的可执行文件无法给出有用的输出。

# HISTORY

属于 **GNU Binutils**，这是一套用于处理目标文件和可执行文件的二进制工具集合。

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

[objdump](/man/objdump)(1), [nm](/man/nm)(1), [readelf](/man/readelf)(1)
