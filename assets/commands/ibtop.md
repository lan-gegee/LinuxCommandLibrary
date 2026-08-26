# TAGLINE

InfiniBand 网络的实时 TUI 监控工具

# TLDR

**启动 ibtop** 监控 InfiniBand 端口

```ibtop```

# SYNOPSIS

**ibtop** [_options_]

# DESCRIPTION

**ibtop** 是一款基于终端的 **InfiniBand** 高速互连实时监控工具，类似于面向网络 fabric 监控的 htop。它持续更新并显示实时的端口统计信息，包括吞吐量、包速率和错误。界面基于 **Ratatui** 构建，提供现代化的 TUI 体验。

# CAVEATS

仅在配备 InfiniBand 硬件的系统上才有用。读取 InfiniBand 端口计数器需要相应的权限。

# HISTORY

**ibtop** 由 **JannikSt** 创建，用 **Rust** 编写。

# SEE ALSO

[htop](/man/htop)(1)
