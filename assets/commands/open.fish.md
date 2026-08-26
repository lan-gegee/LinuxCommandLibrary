# TAGLINE

使用默认应用程序打开文件的 Fish shell 函数

# TLDR

**使用默认应用程序打开文件**

```open [file]```

**在默认浏览器中打开 URL**

```open [https://example.com]```

**在文件管理器中打开目录**

```open [directory]```

**打开当前目录**

```open .```

**打开多个文件**

```open [file1] [file2] [file3]```

# SYNOPSIS

**open** [_file_...]

# PARAMETERS

_FILE_
> 要打开的一个或多个文件、目录或 URL。

# DESCRIPTION

**open** 是 Fish shell 自带的内置函数，无论主机操作系统为何，都会使用用户的默认应用程序打开文件、目录和 URL。它定义在 Fish 安装目录的 **share/fish/functions/open.fish** 中。

在 macOS 和 Haiku 上，该函数会委托给原生的 **open** 二进制程序。在其他类 Unix 系统上，它会分派给 **xdg-open**、**gnome-open** 或 **kde-open**（取决于哪一个存在）。在缺少这些辅助程序的系统上，该函数会打印错误，说明没有可用的打开方式。

由于它是作为 Fish 函数实现的，因此只存在于交互式 Fish 会话中，用 **sh**、**bash** 或 **zsh** 运行的脚本无法使用它。

# CAVEATS

仅在 Fish shell 内部定义；不是 **$PATH** 上的可执行文件。在 Linux 上的行为取决于已安装的桌面辅助程序——在没有 **xdg-open** 的精简服务器上，该函数会失败。在 macOS 上，Fish 优先使用系统的 **open(1)**，并绕过任何名为 **open** 的用户自定义函数。

# HISTORY

**open** 函数自 Fish 早期版本起就随 Fish 一同发布，作为 macOS 的 **open(1)** 和 Linux 的 **xdg-open** 的可移植替代品。它随 Fish 本身一起更新。

# SEE ALSO

[open](/man/open)(1), [xdg-open](/man/xdg-open)(1), [fish](/man/fish)(1)
