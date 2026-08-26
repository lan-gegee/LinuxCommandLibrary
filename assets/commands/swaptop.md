# TAGLINE

面向终端的实时交换空间使用监控器

# TLDR

**启动交换空间监控器**

```swaptop```

以提升的权限运行以获得完整可见性

```sudo -E swaptop```

# SYNOPSIS

**swaptop**

# DESCRIPTION

**swaptop** 是一款 TUI 工具，用于监控 Linux 和 Windows 上的交换内存使用情况。它显示每个进程的交换空间占用、聚合的软件使用视图以及动态图表。它支持多种配色主题和单位切换。

# HISTORY

**swaptop** 由 **luis-ota** 创建，使用 **Rust** 编写。

# INSTALL

```pacman: sudo pacman -S swaptop```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[btop](/man/btop)(1), [htop](/man/htop)(1), [free](/man/free)(1)
