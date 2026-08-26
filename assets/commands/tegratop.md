# TAGLINE

面向 NVIDIA Jetson 开发板的 TUI 监控工具

# TLDR

**启动 Jetson 监控面板**

```tegratop```

# SYNOPSIS

**tegratop**

# DESCRIPTION

**tegratop** 是一个类似 top 的 TUI 工具，用于监控 NVIDIA Jetson 开发板。它在单页界面上显示 GPU 利用率、CPU 各核心、内存使用、风扇转速、功耗、磁盘空间、引擎状态和网络流量。

# CAVEATS

需要 NVIDIA Jetson 开发板。访问全部传感器可能需要提升权限。

# HISTORY

**tegratop** 由 **Badr**（pythops）创建，使用 **Rust** 编写。

# INSTALL

```aur: yay -S tegratop```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nvtop](/man/nvtop)(1), [htop](/man/htop)(1)
