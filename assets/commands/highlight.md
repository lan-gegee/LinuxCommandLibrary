# TAGLINE

将源代码转换为带语法高亮的格式化输出

# TLDR

**对源代码进行语法高亮**

```highlight [file.py]```

**输出为 HTML**

```highlight -O html [file.py] > [file.html]```

**输出为 ANSI**（终端）

```highlight -O ansi [file.py]```

**指定语言**

```highlight --syntax=[python] [file]```

**使用指定主题**

```highlight --style=[molokai] [file.py]```

**列出支持的语言**

```highlight --list-scripts=langs```

**列出可用主题**

```highlight --list-scripts=themes```

# SYNOPSIS

**highlight** [_options_] [_files_...]

# DESCRIPTION

**highlight** 将源代码转换为带语法高亮的格式化输出。它支持超过 250 种编程语言和标记语言，可输出为 HTML、XHTML、RTF、ODT、TeX、LaTeX、SVG、Pango、BBCode 以及 ANSI/终端转义序列（包括 256 色和 truecolor）。

该工具适用于文档编写、演示文稿，以及生成带正确语法配色的可打印源代码清单。

# PARAMETERS

**-O**, **--out-format** _format_
> 输出格式：html、xhtml、latex、tex、rtf、odt、ansi、xterm256、truecolor、bbcode、pango、svg。

**-S**, **--syntax** _lang_
> 指定源语言，无法从文件后缀推断时需要此选项。

**-s**, **--style** _name_
> 颜色主题（使用 Base16 主题需加 "base16/" 前缀）。

**-l**, **--line-numbers**
> 包含行号。

**-i**, **--input** _file_
> 输入文件。

**-o**, **--output** _file_
> 输出文件。

**--list-scripts** _type_
> 列出 langs、themes 或 plugins。

**-f**, **--fragment**
> 省略文档头。

**--inline-css**
> 将 CSS 内嵌到 HTML 中。

**-a**, **--anchors**
> 为行号附加锚点（仅限 HTML）。

**-B**, **--batch-recursive** _wildcard_
> 递归转换所有匹配通配符的文件。

**--stdout**
> 批量模式下将输出写入 stdout 而不是文件。

**-t**, **--replace-tabs** _num_
> 用指定数量的空格替换制表符。

**-u**, **--encoding** _enc_
> 设置与输入文件编码一致的输出编码。

**--config-file** _file_
> 自定义语言定义文件或主题文件的路径。

# CAVEATS

语言检测可能需要提示。主题外观随输出格式而异。部分语言的支持有限。

# HISTORY

**highlight** 由 **Andre Simon** 创建，是一款通用的源代码高亮工具。自 **2002 年**起持续活跃开发，不断增加语言支持和输出格式。

# INSTALL

```apt: sudo apt install highlight```

```dnf: sudo dnf install highlight```

```pacman: sudo pacman -S highlight```

```apk: sudo apk add highlight```

```zypper: sudo zypper install highlight```

```brew: brew install highlight```

```nix: nix profile install nixpkgs#highlight```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pygmentize](/man/pygmentize)(1), [bat](/man/bat)(1), [source-highlight](/man/source-highlight)(1), [vim](/man/vim)(1)

# RESOURCES

```[Source code](https://gitlab.com/saalen/highlight)```

```[Documentation](http://andre-simon.de/doku/highlight/en/highlight.php)```

<!-- verified: 2026-07-19 -->
