# TAGLINE

用默认应用程序打开文件和 URI

# TLDR

**用默认应用打开文件**

```gvfs-open [file.pdf]```

**打开 URL**

```gvfs-open [https://example.com]```

**打开远程文件**

```gvfs-open smb://server/share/document.docx```

**在文件管理器中打开目录**

```gvfs-open [directory]```

# SYNOPSIS

**gvfs-open** [_OPTION..._] [_FILE..._]

# PARAMETERS

_FILE_
> 要打开的文件、目录或 URI。

**-h**, **--help**
> 显示帮助信息。

**--version**
> 显示版本号并退出。

# DESCRIPTION

**gvfs-open** 使用注册为处理该类型文件的默认应用程序来打开文件。它从 shared-mime-info 数据库获取 MIME 类型信息，默认处理程序则按用户存储在 `$XDG_DATA_HOME/applications/mimeapps.list` 中。

该工具可处理本地文件、远程 URI 和 URL。当检测到正在运行的 GNOME 会话时，`xdg-open` 实际上在内部调用 `gvfs-open`。

# CAVEATS

已被弃用，建议改用 gio open。GNOME 专属。需要正确的 MIME 关联。

# HISTORY

gvfs-open 是 GNOME 的 **GVFS** 的一部分开发而成，如今已在很大程度上被 **gio** 和 **xdg-open** 命令取代。

# SEE ALSO

[gio](/man/gio)(1), [xdg-open](/man/xdg-open)(1), [open](/man/open)(1)
