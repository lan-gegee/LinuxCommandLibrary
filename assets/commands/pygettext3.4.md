# TAGLINE

Python 3.4 可翻译字符串提取工具

# TLDR

**提取可翻译字符串**

```pygettext3.4 [file.py]```

**输出到指定文件**

```pygettext3.4 -o [messages.pot] [file.py]```

**从目录中提取**

```pygettext3.4 -d [domain] [*.py]```

# SYNOPSIS

**pygettext3.4** [_options_] [_files_]

# PARAMETERS

_FILES_
> 要从中提取的 Python 文件。

**-o** _FILE_
> 输出文件。

**-d** _DOMAIN_
> 文本域。

**-k** _KEYWORD_
> 额外关键字。

# DESCRIPTION

**pygettext3.4** 是 pygettext 的 Python 3.4 版本，用于从 Python 源文件中提取可翻译字符串并生成 POT（Portable Object Template）文件以供国际化使用。它会扫描被 **_()**、**gettext()** 及类似标记函数包裹的字符串。

这个版本专属的二进制文件面向 Python 3.4 代码。当前开发请使用最新的 **pygettext** 或功能更丰富的 **xgettext** 与 **Babel** 替代方案。

# CAVEATS

Python 3.4 专属版本。请使用最新的 pygettext3。

# HISTORY

pygettext3.4 是 **Python 3.4** 的字符串提取工具。

# SEE ALSO

[pygettext](/man/pygettext)(1), [xgettext](/man/xgettext)(1), [gettext](/man/gettext)(1)
