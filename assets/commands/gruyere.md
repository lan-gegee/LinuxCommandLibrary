# TAGLINE

查看并终止监听端口的进程

# TLDR

**显示所有**监听端口的进程

```gruyere```

显示**完整命令详情**而不是应用名称

```gruyere --details```

**按指定端口过滤**

```gruyere --port [8000]```

**按当前用户过滤**

```gruyere --user```

# SYNOPSIS

**gruyere** [**--details**] [**--port** _PORT_] [**--user**]

# DESCRIPTION

**gruyere** 是一个小巧且美观的 TUI 程序，用于查看和终止监听网络端口的进程。相比手动使用 **lsof** 或 **ss** 查找占用端口的进程，它提供了更简洁的替代方案，以易读的终端界面呈现信息，并支持直接终止进程。

该工具以格式化的视图显示进程名、PID 和端口号，便于在开发过程中识别和处理端口冲突。

# CAVEATS

需要相应权限才能查看和终止进程。终止系统进程可能需要 root 权限。只显示拥有活动监听套接字的进程。

# HISTORY

**gruyere** 由 **Savannah Ostrowski** 创建，是一款面向经常需要识别并释放被占用端口的开发者的轻量级工具。它用 **Rust** 编写，名字取自以其孔洞闻名的瑞士奶酪，是对网络端口的一种俏皮呼应。

# INSTALL

```brew: brew install gruyere```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lsof](/man/lsof)(1), [ss](/man/ss)(8), [fuser](/man/fuser)(1), [netstat](/man/netstat)(8)
