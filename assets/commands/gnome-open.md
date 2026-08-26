# TAGLINE

用关联的 GNOME 应用程序打开文件（已弃用）

# TLDR

**用默认应用打开文件**

```gnome-open [file.pdf]```

**打开 URL**

```gnome-open [https://example.com]```

**打开目录**

```gnome-open [/path/to/directory]```

# SYNOPSIS

**gnome-open** _location_

# PARAMETERS

_LOCATION_
> 要打开的文件、URL 或目录。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gnome-open** 用关联的应用程序打开文件、URL 和目录。它使用 GNOME 的 MIME 类型处理机制来确定合适的应用程序。

该命令已被弃用，推荐改用 xdg-open 或 gio open，它们提供跨桌面的功能。此命令仅为向后兼容而保留。

# CAVEATS

已弃用；请改用 xdg-open。这是 GNOME 特有的命令。在其他桌面上可能无法工作。

# HISTORY

gnome-open 曾是 **GNOME** 实用工具的一部分，后来为了跨桌面兼容性被 **xdg-open** 取代。

# SEE ALSO

[xdg-open](/man/xdg-open)(1), [gio](/man/gio)(1), [open](/man/open)(1)

# RESOURCES

```[Source code](https://gitlab.gnome.org/GNOME/gvfs)```

```[Homepage](https://wiki.gnome.org/Projects/gvfs)```

<!-- verified: 2026-07-17 -->
