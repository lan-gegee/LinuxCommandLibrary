# TAGLINE

生成字体文件的优化子集

# TLDR

将字体子集化为 **Basic Latin** 码点

```fonttools subset [path/to/font.ttf] --unicodes=U+0000-007F```

以显式的**输出路径**写出子集

```fonttools subset [path/to/font.ttf] --unicodes=U+0000-007F --output-file=[path/to/subset.ttf]```

输出 **WOFF2** 而非 TTF

```fonttools subset [path/to/font.ttf] --unicodes=U+0000-007F --flavor=woff2```

仅保留选定的 OpenType **排版特性**

```fonttools subset [path/to/font.ttf] --unicodes=U+0000-007F --layout-features=onum,kern```

# SYNOPSIS

**fonttools subset** [_options_] _font-file_

# PARAMETERS

**--unicodes=**_RANGE_
> 要包含的 Unicode 码点（例如 U+0000-007F 表示 Basic Latin）

**--flavor=**_FORMAT_
> 输出格式：**woff**、**woff2**，或省略以保持原格式

**--layout-features=**_LIST_
> 以逗号分隔的要保留的 OpenType 特性（如 kern,liga,onum）

**--output-file=**_PATH_
> 指定输出文件名；默认为输入名加 .subset 后缀

**--text=**_STRING_
> 仅包含给定文本所需的字形

**--text-file=**_FILE_
> 包含指定文件中文本所需的字形

**--no-hinting**
> 移除 hinting 指令以减小文件体积

**--desubroutinize**
> 从 CFF 字体中移除子例程

# DESCRIPTION

**fonttools subset** 通过只包含指定的字形、Unicode 范围或 OpenType 特性来生成字体文件的优化子集。这对 Web 字体优化至关重要，可通过移除未使用的字符显著缩小文件体积。

该工具支持 TrueType（.ttf）、OpenType（.otf）、WOFF 和 WOFF2 格式。子集化过程中可用 **--flavor** 选项在格式之间转换。

常见用例包括创建特定语言的子集、仅含拉丁字符的 Web 优化字体，或包含特定图标的图标字体。

# CAVEATS

WOFF2 输出需要 **brotli** Python 软件包。如果被依赖的字形被排除，某些复杂的 OpenType 特性可能无法正确子集化。务必对子集化后的字体进行充分测试。

# INSTALL

```dnf: sudo dnf install fonttools```

```apk: sudo apk add py3-fonttools```

```brew: brew install fonttools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fonttools](/man/fonttools)(1)
