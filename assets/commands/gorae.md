# TAGLINE

管理 PDF 和 EPUB 的 TUI 图书馆工具

# TLDR

**打开**图书馆浏览器

```gorae```

向图书馆中**添加**文件

```gorae add [/path/to/books]```

**搜索**图书馆

```gorae search [query]```

# SYNOPSIS

**gorae** [_options_] [_command_]

# PARAMETERS

**add** _PATH_
> 将文件或目录加入图书馆

**remove** _ID_
> 从图书馆移除条目

**search** _QUERY_
> 搜索图书馆

**list**
> 列出所有条目

**open** _ID_
> 用外部查看器打开书籍

**-c, --config** _FILE_
> 配置文件的路径

**-v, --version**
> 显示版本并退出

**-h, --help**
> 显示帮助并退出

# DESCRIPTION

**gorae** 是一个基于终端的 PDF 和 EPUB 文档图书馆管理器。它为浏览、搜索和管理电子书收藏提供了有条理的方式。

该工具可以从文档中提取元数据、（在支持的终端中）显示封面，并与外部查看器集成以便阅读。

# KEYBINDINGS

**↑/↓**
> 在条目之间导航

**/**
> 搜索

**Enter**
> 打开书籍

**i**
> 显示书籍信息

**d**
> 从图书馆删除

**q**
> 退出

# CAVEATS

阅读需要外部查看器。封面显示取决于终端的能力。部分文档的元数据提取可能失败。

# HISTORY

**gorae** 作为 GUI 电子书管理器的 TUI 替代方案而创建，提供完全由键盘驱动的图书库管理。

# SEE ALSO

[zathura](/man/zathura)(1), [pdftotext](/man/pdftotext)(1)
