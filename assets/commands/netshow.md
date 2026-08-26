# TAGLINE

可感知进程的交互式网络连接监控器

# TLDR

**启动网络监控器**

```netshow```

**以提升的权限运行**，获取完整的进程信息

```sudo netshow```

**通过 uvx 安装并运行**

```uvx netshow```

# SYNOPSIS

**netshow**

# DESCRIPTION

**netshow** 是一个轻量级的交互式 TUI 工具，用于监控活动的 TCP 连接及其关联进程，并以人类友好的服务名称显示（如 "Docker"、"VS Code"、"Plex"）。它提供实时连接计数、可选接口的带宽监控，以及支持实时过滤的正则表达式搜索。

以 root 身份运行时，它通过 psutil 获取完整保真的进程信息；以普通用户身份运行时则退回使用 lsof。选中某个连接即可查看进程详情，包括路径、PID、资源占用和打开的文件。界面支持键盘导航、列排序以及可配置的刷新间隔。

# CAVEATS

获取完整进程信息需要 root 权限。无特权运行时只能显示有限的信息。

# HISTORY

**netshow** 由 **Taylor Wilsdon** 创建，使用 **Python** 编写。可以通过 **uvx**、**pip** 安装，或用 **uv** 从源码构建。

# INSTALL

```brew: brew install netshow```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ss](/man/ss)(8), [netstat](/man/netstat)(8), [lsof](/man/lsof)(8), [iftop](/man/iftop)(8), [nethogs](/man/nethogs)(8)
