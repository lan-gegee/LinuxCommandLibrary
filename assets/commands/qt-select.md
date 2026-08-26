# TAGLINE

在 Qt 安装版本之间切换

# TLDR

**显示当前 Qt 版本**

```qtchooser -print-env```

**列出可用版本**

```qtchooser -l```

**选择 Qt 版本**

```export QT_SELECT=[qt5]```

**使用特定 Qt 运行工具**

```qtchooser -run-tool=[qmake] -qt=[5]```

# SYNOPSIS

**qtchooser** [_options_]

# PARAMETERS

**-l**, **--list-versions**
> 列出可用的 Qt 版本。

**-print-env**
> 打印环境设置。

**-run-tool=**_tool_
> 运行指定工具。

**-qt=**_version_
> 选择 Qt 版本。

# DESCRIPTION

**qtchooser**（即 qt-select）允许在多个 Qt 安装之间切换。它管理默认使用哪个 Qt 版本的工具（qmake、moc 等）。

# EXAMPLES

```bash
# List available
qtchooser -l

# Show current
qtchooser -print-env

# Use Qt 5
export QT_SELECT=qt5
qmake --version

# Use Qt 6
export QT_SELECT=qt6
qmake --version

# Run specific qmake
qtchooser -run-tool=qmake -qt=5 --version
```

# CONFIGURATION

**/usr/share/qtchooser/**
> 系统级的 Qt 版本配置文件，每个文件为一种 Qt 安装指定 bin 和 lib 路径。

**~/.config/qtchooser/**
> 用户级的 Qt 版本配置文件，可覆盖系统默认值。

**QT_SELECT**
> 选择默认 Qt 版本的环境变量（如 qt5、qt6）。

**QTCHOOSER_NO_GLOBAL_DIR**
> 设为 1 时忽略系统级配置目录的环境变量。

# CAVEATS

并非所有发行版都可用。可能与手动安装的 Qt 冲突。如需持久选择，请使用环境变量。

# HISTORY

qtchooser 的诞生是为了在使用发行版软件包的 Linux 系统上管理多个 Qt 安装。

# SEE ALSO

[qmake](/man/qmake)(1), [update-alternatives](/man/update-alternatives)(1), [qt](/man/qt)(1)
