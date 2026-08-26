# TAGLINE

带图表的终端资源监视器

# TLDR

**启动**资源监视器

```bpytop```

以较低更新间隔（毫秒）**启动**

```bpytop --update [1000]```

**强制**使用对 TTY 友好的制表符边框模式

```bpytop --low-color```

**打开**应用内帮助

```bpytop --help```

# SYNOPSIS

**bpytop** [_options_]

# DESCRIPTION

**bpytop** 是一款用 Python 编写的资源监视器，以美观的终端界面显示 CPU、内存、磁盘、网络和进程信息。它是 bashtop 的 Python 重写版，性能更佳且功能更多。

该工具提供全面的系统监控，支持鼠标操作和可自定义的主题。

# FEATURES

- 每个 CPU 核心的使用率图表
- 内存与交换分区统计
- 磁盘 I/O 和空间占用
- 网络带宽监控
- 进程管理
- 鼠标支持
- 可自定义主题
- 配置菜单（ESC）
- 进程过滤和排序
- 进程树视图

# INTERFACE SECTIONS

**CPU**
> 每个核心的使用率图表、温度。

**Memory**
> RAM 和交换分区及图表。

**Disks**
> I/O 活动和空间占用。

**Network**
> 按接口统计的带宽。

**Processes**
> 详细的进程列表。

# KEYBINDINGS

- **ESC** - 配置菜单
- **q** - 退出
- **f** - 过滤进程
- **t** - 切换树视图
- **+/-** - 调整更新速度
- **Mouse** - 点击交互
- **Arrow keys** - 导航

# THEMES

内置主题：
- Default
- Default-light
- Gruvbox dark/light
- Nord
- Monokai

# CONFIGURATION

**~/.config/bpytop/bpytop.conf**
> 主配置文件，控制主题、更新间隔、进程排序和显示选项。

# CAVEATS

需要 Python 3.6+。CPU 占用高于原生工具。已被 btop++（C++ 重写版）取代。并非所有系统都能显示所有指标。GPU 监控功能有限。

# HISTORY

**bpytop** 由 Jakob P. Liljenberg（aristocratos）于 **2020 年**创建，是 bashtop 的 Python 重写版。同一作者后来在 **2021 年**开始开发 btop++（C++ 重写版，即 btop），它现在是积极开发的继任者；bpytop 基本不再更新。

# INSTALL

```pacman: sudo pacman -S bpytop```

```brew: brew install bpytop```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[btop](/man/btop)(1), [htop](/man/htop)(1), [bashtop](/man/bashtop)(1), [glances](/man/glances)(1), [top](/man/top)(1)

# RESOURCES

```[Source code](https://github.com/aristocratos/bpytop)```

```[Documentation](https://pypi.org/project/bpytop/)```

<!-- verified: 2026-06-19 -->
