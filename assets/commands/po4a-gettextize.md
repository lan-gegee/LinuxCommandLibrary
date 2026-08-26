# TLDR

# TAGLINE

将可翻译的字符串提取为 PO 文件

# TLDR

**转换**文本文件为 PO 格式

```po4a-gettextize --format [text] --master [path/to/master.txt] --po [path/to/result.po]```

**列出**所有可用格式

```po4a-gettextize --help-format```

**将**文本文件连同已翻译的文档一起转换为 PO 文件

```po4a-gettextize --format [text] --master [path/to/master.txt] --localized [path/to/translated.txt] --po [path/to/result.po]```

# SYNOPSIS

**po4a-gettextize** [_options_] **-f** _format_ **-m** _master_ **-p** _po_

# PARAMETERS

**-f, --format _format_**
> 主文档的格式（text、pod、man、sgml、xml 等）

**-m, --master _file_**
> 原始（主）文档的路径

**-p, --po _file_**
> 生成的 PO 文件的输出路径

**-l, --localized _file_**
> 已有的译文（可多次指定）

**--help-format**
> 列出可用的文档格式

**-M, --master-charset _charset_**
> 主文档的字符集

**-L, --localized-charset _charset_**
> 本地化文档的字符集

# DESCRIPTION

**po4a-gettextize** 从文档文件中提取可翻译的字符串，并创建适合翻译的 PO（Portable Object）文件。它是 **po4a**（PO for anything）套件的一部分，该套件让 gettext 方法论可用于文档翻译。

如果通过 **-l** 选项提供了已有译文，该工具会尝试将已翻译的字符串与原文匹配，并用现有译文预先填充 PO 文件。

# CAVEATS

由于自动匹配可能不完美，生成的 PO 文件应由译者审阅。提供已有译文时，两份文档必须具有相同的结构才能正确对齐。

# INSTALL

```dnf: sudo dnf install po4a```

```pacman: sudo pacman -S po4a```

```apk: sudo apk add po4a```

```zypper: sudo zypper install po4a```

```brew: brew install po4a```

```nix: nix profile install nixpkgs#po4a```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[po4a](/man/po4a)(1), [po4a-translate](/man/po4a-translate)(1), [po4a-updatepo](/man/po4a-updatepo)(1), [msginit](/man/msginit)(1)
