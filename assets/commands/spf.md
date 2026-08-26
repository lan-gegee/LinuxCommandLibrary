# TAGLINE

现代终端文件管理器

# TLDR

在当前目录**打开文件管理器**

```spf```

**打开指定目录**

```spf [/path/to/directory]```

**打开并选中某个文件**

```spf [/path/to/file.txt]```

**打印配置文件路径**

```spf path-list```

**使用自定义配置文件**

```spf -c [/path/to/config.toml]```

**显示版本信息**

```spf --version```

**显示帮助**

```spf --help```

# SYNOPSIS

**spf** [_options_] [_path_...]

# PARAMETERS

**-c**, **--config-file** _path_
> 使用自定义配置文件而非默认配置

**--version**
> 显示版本信息

**--help**
> 显示帮助消息

**path-list**, **pl**
> 打印所有配置文件的路径

# DESCRIPTION

**spf**（Superfile）是一款注重美观与易用性的现代终端文件管理器。它提供多面板界面以高效地浏览和操作文件，支持类似 vim 的键盘驱动工作流。

界面以图标（需要 Nerd Font）和元数据预览展示文件列表，并支持多面板同时操作不同目录。操作包括复制、移动、重命名、删除文件，以及创建新文件和目录。

导航默认采用 vim 风格按键：**h/j/k/l** 移动光标，**y** 复制，**p** 粘贴，**d** 删除，**enter** 打开。按 **>** 打开命令提示符，执行 SPF 特有命令，例如用 **split** 打开更多面板。

配置文件控制快捷键、主题和行为。配置存储在 Linux 和 macOS 的 **~/.config/superfile/** 目录中。主题和边框样式均可完全自定义。

# CONFIGURATION

**~/.config/superfile/config.toml**
> 主配置文件，控制键绑定、默认排序方式、显示选项和面板行为。

**~/.config/superfile/theme.toml**
> 主题配置，定义颜色、边框样式和图标设置。

**~/.config/superfile/hotkeys.toml**
> 导航和文件操作的自定义键绑定覆盖项。

# CAVEATS

Superfile 需要 **Nerd Font** 才能正确显示文件和目录图标。Windows 支持尚不完整。默认键绑定可能与现有的终端快捷键冲突；针对 vim/nvim 用户提供了专用的 vim 配置。

# HISTORY

**Superfile** 由 **yorukot** 创建，于 **2024 年**首次发布。它使用 **Go** 语言和 **Bubble Tea** 终端 UI 框架编写，定位为 ranger、mc 和 nnn 等传统文件管理器的现代、美观替代品。

# SEE ALSO

[ranger](/man/ranger)(1), [mc](/man/mc)(1), [nnn](/man/nnn)(1), [lf](/man/lf)(1), [vifm](/man/vifm)(1)
