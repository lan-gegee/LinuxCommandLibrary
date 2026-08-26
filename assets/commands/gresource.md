# TAGLINE

GNOME GResource 资源包检查器

# TLDR

**列出文件中的资源**

```gresource list [file.gresource]```

**提取资源**

```gresource extract [file.gresource] [/path/to/resource]```

**显示资源段**

```gresource sections [file.gresource]```

**获取资源详情**

```gresource details [file.gresource] [/path/to/resource]```

# SYNOPSIS

**gresource** _command_ [_options_] _file_ [_path_]

# PARAMETERS

_COMMAND_
> 要执行的操作（list、extract、sections、details）。

_FILE_
> GResource 文件或内嵌资源的 ELF 二进制文件。

_PATH_
> 资源包内的资源路径。

**--section** _NAME_
> 指定资源段。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gresource** 用于检查和提取 GResource 资源包中的资源。GResource 是 GNOME 的资源打包系统，可将图标、UI 定义和数据等文件嵌入可执行文件。

该工具可以列出所有资源、提取单个文件并显示详细信息。它既适用于独立的 .gresource 文件，也适用于内嵌了资源的 ELF 二进制文件。

# CAVEATS

专用于 GNOME/GLib 应用程序。资源路径区分大小写。属于 glib 软件包的一部分。

# HISTORY

gresource 作为 **GLib** 的一部分由 **GNOME** 项目开发，用于提供资源检查和提取能力。

# INSTALL

```apt: sudo apt install libglib2.0-bin```

```apk: sudo apk add glib-dev```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[glib-compile-resources](/man/glib-compile-resources)(1)
