# TAGLINE

从 PO 文件生成已翻译的文档

# TLDR

**将已翻译的 PO 文件转换回文档**

```po4a-translate -f [text] -m [path/to/master.doc] -p [path/to/result.po] -l [path/to/translated.txt]```

**要求至少 90% 翻译完成才生成输出**

```po4a-translate -f [man] -m [path/to/master.1] -p [path/to/result.po] -l [path/to/translated.1] -k 90```

**在输出中附加译者署名附录**

```po4a-translate -f [text] -m [path/to/master.doc] -p [path/to/result.po] -l [path/to/translated.txt] -a [path/to/addendum]```

**列出所有可用格式**

```po4a-translate --help-format```

# SYNOPSIS

**po4a-translate** [_options_] **-f** _format_ **-m** _master_ **-p** _po_ **-l** _localized_

# PARAMETERS

**-f**, **--format** _format_
> 主文档的格式（text、pod、man、sgml、xml 等）

**-m**, **--master** _file_
> 原始（主）文档的路径。

**-p**, **--po** _file_
> 已翻译 PO 文件的路径。

**-l**, **--localized** _file_
> 已翻译文档的输出路径。

**-k**, **--keep** _percent_
> 生成输出所需的最低翻译百分比（默认：80）。

**-a**, **--addendum** _file_
> 向已翻译文档追加补充内容（如译者署名）。可多次指定。

**-o**, **--option** _key=value_
> 向格式插件传递额外参数。

**-w**, **--width** _columns_
> 换行列数（默认：76）。设为 0 或负数可禁用换行。

**-M**, **--master-charset** _charset_
> 主文档的字符集。

**-L**, **--localized-charset** _charset_
> 输出文档的字符集。

**-A**, **--addendum-charset** _charset_
> 附录文件的字符集。

**--help-format**
> 列出可用的文档格式。

**-v**, **--verbose**
> 提高输出的详细程度。

**-d**, **--debug**
> 输出调试信息。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本信息。

# DESCRIPTION

**po4a-translate** 将已翻译的 PO 文件转换回原始文档格式。它接收主文档和包含译文的 PO 文件（通常由 po4a-gettextize 创建），然后生成文档的本地化版本。

该工具是 **po4a**（PO for anything）套件的一部分，帮助使用 gettext 方法论维护文档翻译。这样译者可以基于 PO 文件工作，而最终输出仍保留原始文档格式。

# CAVEATS

PO 文件必须是 **po4a-gettextize** 从同一主文档生成的 POT 文件的翻译。默认情况下翻译完成度须达到至少 80% 才会生成输出；使用 **-k** 调整此阈值。根据文档格式的不同，排版可能与原文略有差异。

# INSTALL

```dnf: sudo dnf install po4a```

```pacman: sudo pacman -S po4a```

```apk: sudo apk add po4a```

```zypper: sudo zypper install po4a```

```brew: brew install po4a```

```nix: nix profile install nixpkgs#po4a```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[po4a](/man/po4a)(1), [po4a-gettextize](/man/po4a-gettextize)(1), [po4a-updatepo](/man/po4a-updatepo)(1), [msgfmt](/man/msgfmt)(1), [xgettext](/man/xgettext)(1), [gettext](/man/gettext)(1)
