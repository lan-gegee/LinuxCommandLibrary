# TAGLINE

按 MIME 类型打开文件

# TLDR

**用默认应用打开文件**

```mimeopen [file.pdf]```

**询问使用哪个应用**（不更改默认设置）

```mimeopen --ask [file.pdf]```

**为文件的 MIME 类型设置默认应用**

```mimeopen -d [file.pdf]```

**不询问直接打开**，使用默认或第一个已知的处理程序

```mimeopen --no-ask [file.pdf]```

**仅按文件内容判断 MIME 类型**（忽略扩展名）

```mimeopen -M [file]```

**启用调试输出**，显示 mimetype 判定过程

```mimeopen -D [file]```

# SYNOPSIS

**mimeopen** [_options_] [**-**] _files_

# PARAMETERS

**-a**, **--ask**
> 提示从已知的处理程序中选择一个应用。不更改默认应用。

**-d**, **--ask-default**
> 让用户为给定文件选择新的默认程序。

**-n**, **--no-ask**
> 不询问用户使用哪个程序。选择默认程序或第一个已知能处理该文件 mimetype 的程序。不设置默认应用。

**-M**, **--magic-only**
> 不检查扩展名、glob 或 inode 类型，只查看文件内容。

**--database** _mimedir:mimedir:..._
> 强制程序在这些目录中查找共享的 mime-info 数据库。

**-D**, **--debug**
> 打印关于 mimetype 判定方式的调试信息。

**-h**, **--help**
> 显示帮助信息。

**-u**, **--usage**
> 显示用法信息。

**-v**, **--version**
> 打印程序版本。

# DESCRIPTION

**mimeopen** 尝试确定文件的 mimetype，并用默认的桌面应用打开它。如果没有配置默认应用，会在终端显示菜单让用户选择。

该工具是 **File::MimeInfo** Perl 模块（perl-file-mimeinfo 软件包）的一部分。它会读取并遵循 `~/.config/mimeapps.list` 中配置的 XDG MIME 关联以及系统默认设置。

# CAVEATS

属于 perl-file-mimeinfo。遵循 freedesktop.org 标准，使用共享 MIME info 数据库。桌面集成情况因环境而异。

# SEE ALSO

[xdg-open](/man/xdg-open)(1), [mimetype](/man/mimetype)(1), [file](/man/file)(1)
