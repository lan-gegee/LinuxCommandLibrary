# TAGLINE

跨平台的图形化系统与进程监视器

# TLDR

**启动**系统监视器

```btm```

以**摄氏度**温度单位**启动**

```btm -C```

以**基本模式****启动**（无图表）

```btm -b```

**设置更新频率**（毫秒）

```btm -r [500]```

**只显示特定组件**（CPU、内存、网络）

```btm --default_widget_type [cpu]```

**启用**进程分组模式

```btm -g```

使用自定义配置文件**启动**

```btm -C [path/to/config.toml]```

# SYNOPSIS

**btm** [_options_]

# PARAMETERS

**-b**, **--basic**
> 使用无图表的基本模式。

**-C**, **--celsius**
> 温度使用摄氏度。

**-F**, **--fahrenheit**
> 温度使用华氏度。

**-g**, **--group**
> 将同名进程分组显示。

**-r** _MS_, **--rate** _MS_
> 设置刷新频率（毫秒）（默认：1000）。

**-t**, **--tree**
> 以树形结构显示进程。

**--default_widget_type** _TYPE_
> 设置启动时默认聚焦的组件。

**-C** _FILE_, **--config** _FILE_
> 使用自定义配置文件。

**--color** _SCHEME_
> 使用配色方案（default、gruvbox、nord 等）。

**--mem_as_value**
> 以数值而非百分比显示内存占用。

**--battery**
> 显示电池组件。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本。

# DESCRIPTION

**bottom**（二进制名为 **btm**）是一款跨平台的终端图形化系统监视器。它通过交互式图表实时显示 CPU 使用率、内存消耗、磁盘 I/O、网络流量、温度以及正在运行的进程等信息。

该界面支持鼠标和键盘导航、进程搜索和过滤、向进程发送信号，以及多种布局配置。它既提供图表模式，也提供更简单的纯文本基本模式，适用于 Unicode 支持有限的环境。

bottom 使用 **Rust** 编写，定位为 top 和 htop 等工具的现代替代品，注重视觉呈现，并支持 Linux、macOS 和 Windows 跨平台。

# CONFIGURATION

配置存储在 **~/.config/bottom/bottom.toml** 中。选项包括自定义配色主题、组件布局、默认行为、温度单位以及磁盘/网络过滤器。所有命令行标志都可以在配置文件中设为默认值。

# CAVEATS

二进制名称是 **btm**，而不是 **bottom**。某些功能（如温度传感器和电池监控）可能并非在所有平台上都可用。过高的刷新频率会增加 CPU 占用。

# HISTORY

**bottom** 由 **Clement Tsang** 创建，于 **2019 年**首次发布。它使用 **Rust** 编写，受 gtop 和 gotop 等工具启发，旨在提供一个美观且高度可定制的传统系统监视器替代品。

# INSTALL

```pacman: sudo pacman -S bottom```

```zypper: sudo zypper install bottom```

```brew: brew install bottom```

```nix: nix profile install nixpkgs#bottom```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[htop](/man/htop)(1), [top](/man/top)(1), [btop](/man/btop)(1), [glances](/man/glances)(1)
