# TAGLINE

显示手册页

# TLDR

**查看 man page**

```man [command]```

**查看特定章节**

```man [5 passwd]```

**搜索描述**

```man -k [keyword]```

**显示所有章节**

```man -a [command]```

**显示文件路径**

```man -w [command]```

**经 PostScript 导出为 PDF**

```man -t [command] | ps2pdf - [output.pdf]```

# SYNOPSIS

**man** [_options_] [_section_] _page_

# PARAMETERS

_PAGE_
> 手册页名称。

_SECTION_
> 章节号（1-9）。

**-k** _KEYWORD_
> 按关键字搜索。

**-a**
> 显示所有匹配的手册页。

**-w**
> 显示文件位置。

**-f** _NAME_
> 显示简短描述（等同于 whatis）。

**-K** _STRING_
> 在所有 man page 中搜索某个字符串。

**-t**
> 使用 groff 将 man page 格式化为 PostScript，用于打印或转换为 PDF。

**--help**
> 显示帮助信息。

# DESCRIPTION

**man** 用于显示手册页。Man page 记录命令、系统调用和配置等内容。

该工具是 Unix 的主要文档系统。不同章节组织着不同类型的文档。

# CAVEATS

章节划分因系统而异。有些命令没有 man page。GNU 文档请使用 info。

# HISTORY

man 最早可追溯到贝尔实验室的第一套 **Unix** 系统，至今仍是标准的文档格式。

# INSTALL

```apt: sudo apt install man-db```

```dnf: sudo dnf install man-db```

```pacman: sudo pacman -S man-db```

```apk: sudo apk add mandoc```

```zypper: sudo zypper install mandoc```

```brew: brew install man-db```

```nix: nix profile install nixpkgs#man-db```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[info](/man/info)(1), [apropos](/man/apropos)(1), [whatis](/man/whatis)(1), [mandb](/man/mandb)(8), [manpath](/man/manpath)(1), [less](/man/less)(1)
