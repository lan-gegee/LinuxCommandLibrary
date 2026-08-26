# TAGLINE

带实时图表的系统观测工具

# TLDR

**启动主监控界面**

```sot```

**带端口检测的交互式进程查看器**

```sot ps```

**运行磁盘性能基准测试**

```sot bench```

# SYNOPSIS

**sot** [_command_] [_options_]

# DESCRIPTION

**sot** 是一款受 **top** 启发的跨平台系统监控工具，提供 CPU、内存、磁盘 I/O 和网络活动的实时监控及实时图表。它包含带端口检测的交互式进程查看器、磁盘基准测试（顺序吞吐量、随机 IOPS、延迟）、带 ASCII 徽标的系统信息显示，以及系统清理工具。

# HISTORY

**sot** 由 **Kumar Anirudha**（anistark）创建，使用 **Python** 编写。

# INSTALL

```aur: yay -S sot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[top](/man/top)(1), [htop](/man/htop)(1), [glances](/man/glances)(1)
