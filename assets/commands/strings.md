# TAGLINE

从二进制文件中提取可打印文本

# TLDR

在文件中**查找可打印字符串**

```strings [file]```

**查找**最小长度的字符串

```strings -n [10] [file]```

在每个字符串前**打印文件名**

```strings -f [file1] [file2]```

**打印每个字符串的偏移量**

```strings -t d [file]```

以十六进制**打印偏移量**

```strings -t x [file]```

**搜索整个文件**（不只是数据段）

```strings -a [file]```

**按指定编码搜索**

```strings -e l [file]```

**扫描多个文件**

```strings [*.bin]```

# SYNOPSIS

**strings** [_options_] _file_...

# DESCRIPTION

**strings** 查找并打印文件中的可打印字符序列，通常用于二进制文件。默认情况下，它查找至少由 4 个连续可打印字符组成、后跟不可打印字符的序列。

该工具常用于检查二进制文件、从可执行文件中提取文本、查找内嵌消息以及进行基本的取证分析。它可以揭示版本字符串、错误消息和其他内嵌文本。

strings 不关心文件的结构，只是扫描字符序列，因此在文件格式未知或不重要时非常有用。

# PARAMETERS

**-a**, **--all**
> 扫描整个文件，而不只是数据段。

**-f**, **--print-file-name**
> 在每个字符串前打印文件名。

**-n** _min_, **--bytes=** _min_
> 最小字符串长度（默认为 4）。

**-t** _format_, **--radix=** _format_
> 打印偏移量（o=八进制，d=十进制，x=十六进制）。

**-e** _encoding_
> 字符编码（s=7 位，S=8 位，b/l=16 位，B/L=32 位）。

**-o**
> 以八进制打印偏移量（等同于 -t o）。

**-T** _bfdname_, **--target=** _bfdname_
> 指定二进制格式。

# CAVEATS

结果包含任何形式的字符序列，未必是有意义的文本。二进制数据中误报很常见。无法判断所找到字符串的上下文或用途。某些字符串可能是不完整的或具有误导性的。

# HISTORY

**strings** 自早期 Unix 版本就已存在，起源于 **1970 年代**贝尔实验室的 **Version 6 Unix**。GNU 版本是 **binutils** 的一部分。该工具至今仍是二进制分析的重要工具，常用于安全研究和逆向工程。

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

[file](/man/file)(1), [hexdump](/man/hexdump)(1), [od](/man/od)(1), [xxd](/man/xxd)(1)
