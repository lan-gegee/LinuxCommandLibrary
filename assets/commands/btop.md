# TAGLINE

支持 GPU 的终端资源监视器

# TLDR

**启动**资源监视器

```btop```

以指定的**更新率**（毫秒）启动

```btop -u [500]```

以**进程过滤器**启动

```btop -f [process_name]```

以**预设**布局（0-9）启动

```btop -p [0]```

以 **TTY 模式**启动（16 色、ANSI 图形符号）

```btop -t```

# SYNOPSIS

**btop** [_options_]

# PARAMETERS

**-p**, **--preset** _0-9_
> 以预设布局启动

**-u**, **--update** _ms_
> 设置初始更新率（毫秒）

**-f**, **--filter** _filter_
> 设置初始进程过滤器

**-t**, **--tty**
> 强制使用 tty 模式

**-l**, **--low-color**
> 仅使用 256 色（不用真彩色）

**-c**, **--config** _file_
> 配置文件路径

**--force-utf**
> 即使未检测到 UTF-8 locale 也强制启动

**--themes-dir** _dir_
> 自定义主题目录的路径

**--no-tty**
> 强制禁用 tty 模式

**--default-config**
> 将默认配置打印到标准输出

**-d**, **--debug**
> 以调试模式启动并记录额外日志

**-V**, **--version**
> 显示版本

**-h**, **--help**
> 显示帮助

# DESCRIPTION

**btop++**（btop）是一个用 C++ 编写的资源监视器，通过精美的终端界面显示 CPU、内存、磁盘、网络和进程信息。它是 bashtop 和 bpytop 的继任者，性能更好且功能更多。

该工具提供全面的系统监控，支持 GPU 监控、鼠标交互和丰富的自定义选项。

# FEATURES

- 每个 CPU 核心的使用率及图表
- 内存与交换空间监控
- 磁盘 I/O 与使用情况
- 网络带宽
- 进程管理
- GPU 监控（NVIDIA、AMD）
- 支持鼠标
- 类 Vim 快捷键
- 可自定义主题
- 进程过滤与树状视图
- 电池监控

# KEYBINDINGS

- **q** - 退出
- **ESC/m** - 菜单
- **f** - 过滤进程
- **t** - 树状视图
- **k** - 杀死进程
- **+/-** - 调整更新间隔
- **方向键** - 导航
- **鼠标** - 点击交互

# INTERFACE BOXES

**CPU**
> 每个核心的使用率、温度和频率

**Memory**
> 内存、交换空间和缓存，附图表

**Disks**
> I/O 活动、空间使用情况

**Network**
> 按接口统计的带宽

**Processes**
> 详细的可排序列表

# CONFIGURATION

**~/.config/btop/btop.conf**
> 主配置文件，包含更新间隔、主题和布局等设置。

**~/.config/btop/themes/**
> 自定义颜色主题目录。

# CAVEATS

需要支持真彩色的现代终端。GPU 监控需要相应的驱动程序。资源占用比 top 等极简工具更高。部分功能与平台相关。

# HISTORY

**btop++** 由 **Jakob P. Liljenberg**（aristocratos）于 **2021 年**创建，是 bpytop 的 C++ 重写版本，性能显著提升并增加了更多功能。

# INSTALL

```apt: sudo apt install btop```

```dnf: sudo dnf install btop```

```pacman: sudo pacman -S btop```

```apk: sudo apk add btop```

```zypper: sudo zypper install btop```

```brew: brew install btop```

```nix: nix profile install nixpkgs#btop```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[htop](/man/htop)(1), [bpytop](/man/bpytop)(1), [top](/man/top)(1)
