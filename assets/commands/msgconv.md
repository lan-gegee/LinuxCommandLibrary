# TAGLINE

在多种字符编码之间转换 PO 文件

# TLDR

**转换 PO 文件编码**

```msgconv -t [UTF-8] [input.po] -o [output.po]```

**转换为特定编码**

```msgconv --to-code=[ISO-8859-1] [file.po]```

**转换并输出到 stdout**

```msgconv -t [UTF-8] [input.po]```

**强制转换**

```msgconv --force [input.po] -o [output.po]```

# SYNOPSIS

**msgconv** [_options_] [_inputfile_]

# PARAMETERS

_INPUTFILE_
> 要转换的 PO 文件。

**-t** _ENCODING_
> 目标编码。

**--to-code** _ENCODING_
> 目标字符编码。

**-o** _FILE_
> 输出文件。

**--force**
> 强制转换。

**--help**
> 显示帮助信息。

# DESCRIPTION

**msgconv** 在多种字符编码之间转换 PO 文件。它是 GNU gettext 的一部分。

该工具处理翻译文件的编码，并在转换过程中保留消息结构。

# CAVEATS

属于 gettext-tools。不兼容的编码转换可能丢失数据。推荐使用 UTF-8。

# HISTORY

msgconv 是 **GNU gettext** 的一部分，自 1995 年起提供国际化工具。

# INSTALL

```apt: sudo apt install gettext```

```dnf: sudo dnf install gettext```

```pacman: sudo pacman -S gettext```

```apk: sudo apk add gettext```

```brew: brew install gettext```

```nix: nix profile install nixpkgs#gettext```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[msgen](/man/msgen)(1), [msgfmt](/man/msgfmt)(1), [msgmerge](/man/msgmerge)(1)
