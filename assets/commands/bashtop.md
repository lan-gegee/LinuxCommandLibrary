# TAGLINE

用 bash 编写的终端资源监视器（已弃用）

# TLDR

> **bashtop** 已弃用且不再维护。请改用 **btop**（其 C++ 继任者）。

**启动**资源监视器

```bashtop```

# SYNOPSIS

**bashtop**

# DESCRIPTION

**bashtop** 是一款用 bash 编写的资源监视器，在终端 UI 中展示 CPU、内存、磁盘、网络和进程信息。它提供美观且支持鼠标操作的系统监控界面。

该工具在保持纯 bash 脚本的同时提供了游戏般的视觉效果和交互性。它从未实现命令行参数解析，因此只能以 **bashtop** 直接启动，并通过应用内菜单进行配置。

**bashtop** 已不再积极开发。它先被重写为 Python 版 **bpytop**，随后又重写为 C++ 版 **btop**——后者是在所有平台上推荐的替代品。

# FEATURES

- CPU 占用及各核心细分
- 内存与交换分区占用
- 磁盘 I/O 统计
- 网络带宽
- 可过滤的进程列表
- 鼠标支持
- 可自定义主题
- 配置菜单

# INTERFACE

显示区域：
- **CPU** - 各核心占用图表
- **Memory** - RAM 与交换分区占用
- **Disks** - I/O 与空间占用
- **Network** - 按接口统计的带宽
- **Processes** - 可排序进程列表

# KEYBINDINGS

- **q** - 退出
- **m** - 配置菜单
- **f** - 过滤进程
- **p/n** - 进程排序
- **Arrow keys** - 导航
- **Mouse** - 点击交互

# CONFIGURATION

**~/.config/bashtop/bashtop.cfg**
> 用户配置文件。控制主题、刷新间隔、进程排序和显示选项。

# CAVEATS

纯 bash 编写，性能受此限制。需要 bash 4.4 或更新版本。监控本身的开销相对偏高。**不再维护**：已被 **bpytop**（Python）取代，之后又被 **btop**（C++）取代。

# HISTORY

**bashtop** 由 aristocratos (Jakob Palme) 于 **2020** 年创建，是一款完全用 bash 编写的系统监视器，后来重写为 **bpytop**，再后来是 **btop**。

# INSTALL

```pacman: sudo pacman -S bashtop```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[btop](/man/btop)(1), [bpytop](/man/bpytop)(1), [htop](/man/htop)(1), [top](/man/top)(1), [glances](/man/glances)(1)

# RESOURCES

```[Source code](https://github.com/aristocratos/bashtop)```

<!-- verified: 2026-06-19 -->
