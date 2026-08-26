# TAGLINE

从二进制文件中提取可打印字符串

# TLDR

**从二进制文件提取字符串**

```llvm-strings [file]```

**设置最小字符串长度**

```llvm-strings -n [8] [file]```

**随字符串一起打印文件偏移量**

```llvm-strings -t x [file]```

**处理所有节**

```llvm-strings -a [file]```

# SYNOPSIS

**llvm-strings** [_options_] [_file_...]

# PARAMETERS

**-n** _length_
> 最小字符串长度（默认 4）。

**-t** _format_
> 打印偏移量（d=十进制，o=八进制，x=十六进制）。

**-a**, **--all**
> 扫描整个文件，而不仅是数据节。

# DESCRIPTION

**llvm-strings** 从二进制文件中提取可打印字符串。它是 GNU strings 的直接替代品。可用于分析可执行文件、查找内嵌文本以及逆向工程。

# INSTALL

```apt: sudo apt install llvm```

```dnf: sudo dnf install llvm```

```pacman: sudo pacman -S llvm```

```apk: sudo apk add llvm```

```zypper: sudo zypper install llvm```

```brew: brew install llvm```

```nix: nix profile install nixpkgs#llvm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[strings](/man/strings)(1), [llvm-objdump](/man/llvm-objdump)(1)
