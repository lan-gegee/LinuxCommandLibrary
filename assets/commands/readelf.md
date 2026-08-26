# TAGLINE

显示 ELF 二进制文件的信息

# TLDR

显示 ELF 文件的**全部信息**

```readelf -a /path/to/binary```

显示所有**头部**（文件头、程序头和节头）

```readelf -e /path/to/binary```

显示**符号表**

```readelf -s /path/to/binary```

显示**动态符号表**

```readelf --dyn-syms /path/to/binary```

显示**节头**

```readelf -S /path/to/binary```

显示**重定位**条目

```readelf -r /path/to/binary```

以十六进制字节显示某个**节**的内容

```readelf -x .text /path/to/binary```

以可打印字符串显示某个**节**的内容

```readelf -p .rodata /path/to/binary```

# SYNOPSIS

**readelf** [_options_] _elffile_...

# DESCRIPTION

**readelf** 显示一个或多个 ELF（Executable and Linkable Format）目标文件的信息。它同时支持 32 位和 64 位 ELF 文件，且独立于 BFD 库运行，可对二进制文件进行详细分析。

# PARAMETERS

**-a, --all**
> 显示全部信息

**-h, --file-header**
> 显示 ELF 文件头

**-l, --program-headers**
> 显示程序（段）头

**-S, --section-headers**
> 显示节头

**-e, --headers**
> 显示所有头部（文件、程序、节）

**-s, --symbols**
> 显示符号表条目

**--dyn-syms**
> 显示动态符号表

**-r, --relocs**
> 显示重定位节

**-d, --dynamic**
> 显示 dynamic 节内容

**-n, --notes**
> 显示 NOTE 段/节

**-V, --version-info**
> 显示版本节

**-x** _section_, **--hex-dump=**_section_
> 以十六进制字节显示节内容

**-p** _section_, **--string-dump=**_section_
> 以可打印字符串显示节内容

**-u, --unwind**
> 显示展开（unwind）表信息

**-w, --debug-dump**
> 显示 DWARF 调试节

**-I, --histogram**
> 显示符号表桶列表长度的直方图

**-W, --wide**
> 允许宽输出（不在 80 列处折行）

**-C, --demangle**
> 将低级符号名解码（反修饰）为用户级名称

**-z, --decompress**
> 在显示节内容之前先解压

**-H, --help**
> 显示用法信息

# CAVEATS

与 objdump 不同，readelf 独立于 BFD 库运行，输出可能有所不同。它只处理 ELF 格式文件，且不能反汇编代码。

# HISTORY

**readelf** 属于 GNU **binutils** 软件包。在 ELF 专属信息方面，它比 objdump 提供更详细的分析。

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

[objdump](/man/objdump)(1), [nm](/man/nm)(1), [strings](/man/strings)(1), [strip](/man/strip)(1), [size](/man/size)(1), [elf](/man/elf)(5)
