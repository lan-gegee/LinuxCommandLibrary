# TAGLINE

在多个 Qt 安装之间切换

# TLDR

**列出**可用的 Qt 版本

```qtchooser --list-versions```

打印**环境**信息

```qtchooser --print-env```

使用特定 Qt 版本**运行工具**

```qtchooser --run-tool=[qmake] --qt=[5]```

**安装**Qt 版本条目

```qtchooser --install [version_name] [path/to/qmake]```

显示**帮助**

```qtchooser --help```

# SYNOPSIS

**qtchooser** [**--list-versions**] [**--print-env**] [**--run-tool** _tool_ **--qt** _version_] [**--install** _name_ _path_]

# PARAMETERS

**--list-versions**
> 列出可用的 Qt 版本

**--print-env**
> 打印 Qt 环境变量

**--run-tool _tool_**
> 运行指定的 Qt 工具

**--qt _version_**
> 选择要使用的 Qt 版本

**--install _name_ _path_**
> 注册一个 Qt 安装

**-qt=**_version_
> **--qt** 的短形式，包装器二进制文件可直接接受（如 `qmake -qt=5`）。

**-run-tool=**_tool_
> **--run-tool** 的短形式。

**-list-versions**, **-print-env**
> 对应长选项的单横线别名。

# DESCRIPTION

**qtchooser** 管理系统上的多个 Qt 安装。它允许开发者在不同的 Qt 版本（Qt4、Qt5、Qt6）之间切换以构建应用程序。

该工具包装 Qt 开发二进制文件（qmake、moc、uic 等），并根据配置文件或命令行选项将它们定向到所选的 Qt 安装。

# CONFIGURATION

**/usr/share/qtchooser/**
> 系统级的 Qt 版本配置文件，每个文件为一种 Qt 安装指定 bin 和 lib 路径。

**~/.config/qtchooser/**
> 用户级的 Qt 版本配置文件，可覆盖系统默认值。

**QT_SELECT**
> 选择默认 Qt 版本的环境变量（如 qt5、qt6）。

# CAVEATS

并非所有发行版都使用 qtchooser；Debian/Ubuntu 仍在使用，但 Fedora 和 Arch 已弃用该包装器，改用带版本后缀的二进制名（`qmake-qt5`、`qmake6`）。Qt 6 的安装通常不会自行注册——你可能需要用 **--install** 手动注册。

# HISTORY

**qtchooser** 的诞生是为了处理 Linux 系统上 Qt4 向 Qt5 的过渡，让两个版本得以共存，同时保持与构建系统的兼容性。

# INSTALL

```apt: sudo apt install qtchooser```

```dnf: sudo dnf install qtchooser```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qmake](/man/qmake)(1), [moc](/man/moc)(1), [qt-select](/man/qt-select)(1)
