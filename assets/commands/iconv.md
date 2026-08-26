# TAGLINE

将文本文件从一种字符编码转换为另一种

# TLDR

**转换文件**，从 UTF-8 到 ISO-8859-1

```iconv -f UTF-8 -t ISO-8859-1 [input.txt] > [output.txt]```

**就地转换文件**（借助临时文件）

```iconv -f UTF-8 -t ASCII//TRANSLIT [input.txt] -o [output.txt]```

**列出可用编码**

```iconv -l```

**以音译方式转换**（近似字符）

```iconv -f UTF-8 -t ASCII//TRANSLIT [input.txt]```

**忽略错误进行转换**

```iconv -f UTF-8 -t ASCII//IGNORE [input.txt]```

**从 Windows 代码页转换**

```iconv -f CP1252 -t UTF-8 [windows.txt]```

**从 stdin 转换**

```cat [file.txt] | iconv -f UTF-8 -t UTF-16```

# SYNOPSIS

**iconv** [_options_] [**-f** _encoding_] [**-t** _encoding_] [_file_...]

# DESCRIPTION

**iconv** 将文本文件从一种字符编码转换为另一种。它以源编码读取输入，以目标编码写出输出，处理不同字符集之间的字符映射。

该工具支持数百种编码，包括 UTF-8、ISO-8859 系列、Windows 代码页、亚洲编码以及遗留格式。特殊后缀 //TRANSLIT（近似转换）和 //IGNORE（跳过无法转换的字符）可以改变转换行为。

iconv 对于处理来自不同系统的文件、迁移遗留数据，以及确保文本在具有不同默认编码的平台之间正确显示都不可或缺。

# PARAMETERS

**-f** _encoding_, **--from-code=** _encoding_
> 源编码。

**-t** _encoding_, **--to-code=** _encoding_
> 目标编码。

**-l**, **--list**
> 列出可用的编码。

**-o** _file_, **--output=** _file_
> 输出文件。

**-c**
> 静默丢弃无法转换的字符。

**-s**, **--silent**
> 抑制警告。

**--verbose**
> 打印进度信息。

**//TRANSLIT**
> 对无法转换的字符进行音译。

**//IGNORE**
> 跳过无法转换的字符。

# CAVEATS

并非所有字符映射都是可逆的。某些字符可能丢失或被近似替代。现代系统建议使用 UTF-8 作为目标编码。编码检测不是自动的（未知时先用 chardet）。不要转换二进制文件。

# HISTORY

**iconv** 是 **POSIX 标准**的一部分，在 glibc（GNU libc）及其他 C 库中都有实现。自 **1992 年**的 **POSIX.2** 起，字符转换功能就已标准化。GNU 实现支持大量编码，是大多数 Linux 系统上常见的版本。

# INSTALL

```apt: sudo apt install libc-bin```

```apk: sudo apk add musl-utils```

```nix: nix profile install nixpkgs#iconv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[chardet](/man/chardet)(1), [file](/man/file)(1), [recode](/man/recode)(1), [uconv](/man/uconv)(1)
