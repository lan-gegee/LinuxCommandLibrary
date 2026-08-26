# TAGLINE

拼写检查器和形态分析器

# TLDR

**检查拼写**

```hunspell [file.txt]```

**使用指定词典**

```hunspell -d [en_US] [file.txt]```

**列出拼写错误**

```hunspell -l [file.txt]```

**通过管道输入**

```echo "teh quikc fox" | hunspell -a```

**以批处理模式检查**

```hunspell -a < [file.txt]```

# SYNOPSIS

**hunspell** [_-aDGhHlmnrstvwX_] [_-d_ _dict_[,_dict2_,...]] [_-i_ _enc_] [_-p_ _dict_] [_files_]

# PARAMETERS

_FILES_
> 要检查的文件（文本、HTML、XML、TeX/LaTeX、nroff/troff 或 OpenDocument）。

**-d** _dict_[,_dict2_,...]
> 要使用的词典（可多个），按基础名称指定。

**-p** _dict_
> 个人词典的路径。

**-l**
> 列出输入中拼写错误的单词（每行一个）。

**-a**
> 兼容 Ispell 的管道模式；供编辑器和其他程序使用。

**-D**
> 显示检测到的词典路径、搜索路径以及可用词典。

**-G**
> 只打印正确的单词或行。

**-L**
> 打印包含拼写错误单词的行。

**-H**
> 输入为 HTML/SGML。

**-X**
> 输入为 XML。

**-t**
> 输入为 TeX 或 LaTeX。

**-n**
> 输入为 nroff/troff。

**-O**
> 输入为 OpenDocument（ODF 或 Flat ODF）。

**-s**
> 对输入中的单词进行词干提取。

**-m**
> 分析单词形态和词缀数据。

**-i** _enc_
> 设置输入编码。

**--check-url**
> 同时检查 URL、电子邮件地址和文件路径。

**-v**, **--version**
> 打印版本号。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**Hunspell** 是一个拼写检查器和形态分析器。它是许多应用程序的默认拼写检查器，包括 LibreOffice、OpenOffice、Firefox、Thunderbird 和 Chrome。

该工具借助 Myspell/Hunspell 格式的词典文件支持多种语言，并且比老一代拼写检查器更好地理解复合词和复杂形态。它既可以交互式地检查文件，也可以在列表模式（**-l**）或编辑器及其他程序使用的 ispell 兼容管道模式（**-a**）下工作。输入格式过滤器（**-H**、**-X**、**-t**、**-n**、**-O**）会在检查前剥离标记。

# CAVEATS

每种语言的词典都需要单独安装（例如 **hunspell-en-us**）。设计上可作为 ispell/myspell 的直接替代品。通过 **-p** 支持每用户个人词典。

# HISTORY

Hunspell 由 **László Németh** 创建，是一款经过改进的 ispell/myspell 兼容拼写检查器，在 Unicode、复合词和形态学方面支持更好。它目前仍在活跃维护，是大多数主流开源办公套件和浏览器背后的拼写检查引擎。

# INSTALL

```apt: sudo apt install hunspell```

```dnf: sudo dnf install hunspell```

```pacman: sudo pacman -S hunspell```

```apk: sudo apk add hunspell```

```zypper: sudo zypper install hunspell```

```brew: brew install hunspell```

```nix: nix profile install nixpkgs#hunspell```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aspell](/man/aspell)(1), [ispell](/man/ispell)(1), [spell](/man/spell)(1)

# RESOURCES

```[Source code](https://github.com/hunspell/hunspell)```

```[Homepage](https://hunspell.github.io/)```

<!-- verified: 2026-07-19 -->
