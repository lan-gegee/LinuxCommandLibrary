# TAGLINE

向运行中的 i3 窗口管理器发送命令

# TLDR

**切换工作区**

```i3-msg workspace [3]```

**移动窗口**

```i3-msg move left```

**执行命令**

```i3-msg exec [firefox]```

**重载配置**

```i3-msg reload```

**获取工作区**

```i3-msg -t get_workspaces```

**更改布局**

```i3-msg layout [tabbed]```

# SYNOPSIS

**i3-msg** [_options_] _command_

# PARAMETERS

_COMMAND_
> 要执行的 i3 命令。

**-t** _TYPE_
> 消息类型（command、get_workspaces）。

**-s** _SOCKET_
> 套接字路径。

**-q**
> 安静模式。

**--help**
> 显示帮助信息。

# DESCRIPTION

**i3-msg** 向运行中的 i3 窗口管理器发送命令。它提供对窗口、工作区和布局的可脚本化控制。

该工具可以执行任何 i3 命令并查询状态信息。它是脚本化和自动化不可或缺的工具。

# CAVEATS

需要 i3 正在运行。套接字必须可访问。命令必须符合有效的 i3 语法。

# HISTORY

i3-msg 是 **i3** 窗口管理器项目中负责 IPC 通信的部分。

# INSTALL

```apt: sudo apt install i3-wm```

```pacman: sudo pacman -S i3-wm```

```apk: sudo apk add i3wm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[i3](/man/i3)(1), [swaymsg](/man/swaymsg)(1), [i3lock](/man/i3lock)(1)
