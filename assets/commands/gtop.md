# TAGLINE

用 Node 编写的终端图形化活动监视器

# TLDR

**启动 gtop**

```gtop```

# SYNOPSIS

**gtop**

# KEYBOARD COMMANDS

**q**
> 退出。

**p**
> 按 PID 排序。

**c**
> 按 CPU 排序。

**m**
> 按内存排序。

# DESCRIPTION

**gtop** 是一款用 Node.js 编写的终端图形化活动监视器。它以可视化图形展示 CPU、内存、网络、磁盘和进程信息。

界面通过多个面板展示系统指标：按核心显示 CPU 占用的条形图、内存与交换分区使用情况、网络吞吐量图表、磁盘占用条形图以及进程列表。

CPU 面板将每个核心的占用率显示为带百分比的横向条形。内存面板用进度条显示已用/总量。网络面板显示发送/接收速率。

进程列表按资源占用显示排名靠前的进程。可以按 CPU（**c**）、内存（**m**）或 PID（**p**）排序。列表实时更新。

gtop 启发了多个用其他语言编写的类似工具（gotop、btm），后者提供了更多功能和更好的性能。

# CAVEATS

需要 Node.js 运行时。相比原生替代方案 CPU 占用更高。配置选项有限。不支持自定义布局或主题。

# HISTORY

gtop 由 **Can Güney Aksakalli**（aksakalli）创建，首次发布于 **2017 年**。它使用基于 blessed-contrib 的 Node.js 编写，普及了图形化终端监视器的风格。其视觉设计启发了众多后继者，包括 gotop（Go）、bashtop/bpytop（Python）和 bottom（Rust）。凭借简单易用和 npm 安装便捷，gtop 至今仍然流行。

# INSTALL

```pacman: sudo pacman -S gtop```

```brew: brew install gtop```

```nix: nix profile install nixpkgs#gtop```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[htop](/man/htop)(1), [gotop](/man/gotop)(1), [btm](/man/btm)(1), [top](/man/top)(1)

# RESOURCES

```[Source code](https://github.com/aksakalli/gtop)```

<!-- verified: 2026-07-17 -->
