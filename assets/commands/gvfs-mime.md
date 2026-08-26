# TAGLINE

管理 GNOME 中的 MIME 类型关联

# TLDR

**显示默认处理程序**

```gvfs-mime --query [text/plain]```

**设置默认处理程序**

```gvfs-mime --set [text/html] [firefox.desktop]```

**查询图像处理程序**

```gvfs-mime --query [image/jpeg]```

# SYNOPSIS

**gvfs-mime** [_options_] _mimetype_ [_handler_]

# PARAMETERS

_MIMETYPE_
> 要查询或设置的 MIME 类型。

_HANDLER_
> 处理程序对应的 desktop 文件。

**--query**
> 查询默认处理程序。

**--set**
> 设置默认处理程序。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gvfs-mime** 管理 GNOME 中的 MIME 类型关联。它查询并设置打开不同文件类型的默认应用程序。

该工具会修改用户的 MIME 数据库，将应用程序与内容类型相关联。更改会影响 GNOME 中文件的打开方式。

# CAVEATS

属于 gvfs-bin 命令行工具集，在 gvfs 1.31（2016 年）中被弃用，并在 gvfs 1.38（2018 年）中被完全移除，由统一的 **gio** 命令（`gio mime`）取代。现代发行版不再附带 gvfs-mime。GNOME 专属；使用 .desktop 文件 ID 作为处理程序。

# HISTORY

**gvfs-mime** 是 GVFS 原始 gvfs-bin 实用工具的一部分，于 **2008 年**（GNOME 2.22）随 GVFS 一同为 GNOME 引入。此后被 **gio mime** 取代。

# SEE ALSO

[gio](/man/gio)(1), [xdg-mime](/man/xdg-mime)(1), [update-mime-database](/man/update-mime-database)(1)

# RESOURCES

```[Source code](https://gitlab.gnome.org/GNOME/gvfs)```

```[Homepage](https://wiki.gnome.org/Projects/gvfs)```

<!-- verified: 2026-07-17 -->
