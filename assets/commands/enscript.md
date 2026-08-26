# TAGLINE

将文本文件转换为 PostScript 以便打印

# TLDR

**打印文件到默认打印机**

```enscript [file]```

**生成 PostScript 输出**

```enscript -o [output.ps] [file]```

**按双栏打印**

```enscript -2 [file]```

**带语法高亮打印**

```enscript -E [file.c]```

**横向打印**

```enscript -r [file]```

**带页眉打印**

```enscript -b "[Header Text]" [file]```

**打印行号**

```enscript -C [file]```

# SYNOPSIS

**enscript** [_options_] [_file_...]

# PARAMETERS

**-o** _file_
> 输出到文件而非打印机。

**-E** [_lang_]
> 语法高亮。

**-2**
> 双栏输出。

**-r**
> 横向（landscape）方向。

**-b** _header_
> 页眉。

**-C**
> 打印行号。

**-f** _font_
> 正文字体。

**-F** _font_
> 页眉字体。

**-p** _printer_
> 选择打印机。

**--color**
> 彩色输出。

# DESCRIPTION

**enscript** 将文本文件转换为 PostScript、HTML 或 RTF，用于打印或查看。它提供高级格式化功能，包括多栏输出、页眉、页脚以及对众多编程语言的语法高亮。

该工具广泛用于生成美观专业的源代码和文档打印稿。它能自动检测文件类型并应用相应的语法高亮，使代码在打印后更具可读性。

enscript 支持通过配置文件和命令行选项进行定制，可控制字体、页面布局、边框和输出格式。它在开发环境中尤其适合代码评审和文档打印。

# CONFIGURATION

**/etc/enscript.cfg**
> 全局系统配置文件，用于默认设置。

**~/.enscriptrc**
> 用户专属配置文件，用于个人偏好设置。

# INSTALL

```apt: sudo apt install enscript```

```dnf: sudo dnf install enscript```

```pacman: sudo pacman -S enscript```

```apk: sudo apk add enscript```

```zypper: sudo zypper install enscript```

```brew: brew install enscript```

```nix: nix profile install nixpkgs#enscript```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lpr](/man/lpr)(1)
