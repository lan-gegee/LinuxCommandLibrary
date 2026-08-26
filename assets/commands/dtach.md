# TAGLINE

极简的可分离终端会话管理器

# TLDR

**创建新会话**

```dtach -c [/tmp/session.sock] [command]```

**连接到已有会话**

```dtach -a [/tmp/session.sock]```

**创建会话但不连接**

```dtach -n [/tmp/session.sock] [command]```

**连接会话，不存在则创建**

```dtach -A [/tmp/session.sock] [command]```

**设置自定义分离键**

```dtach -c [/tmp/session.sock] -e '^a' [command]```

**创建不设分离键的会话**

```dtach -c [/tmp/session.sock] -E [command]```

# SYNOPSIS

**dtach** [_options_] _socket_ [_command_ [_args_]]

# DESCRIPTION

**dtach** 提供类似 screen 或 tmux 的可分离终端会话，但只专注于分离/连接这一项功能。它会创建一个 Unix 套接字用于会话通信。

这种极简的设计使 dtach 在只需要会话分离功能时比其他工具更轻量，没有窗口管理或其他附加特性。

# PARAMETERS

**-c** _socket_
> 创建新会话并连接。

**-n** _socket_
> 创建新会话但不连接。

**-a** _socket_
> 连接到已有会话。

**-A** _socket_
> 连接会话，不存在则创建。

**-r** _method_
> 重绘方法（none、ctrl_l、winch）。

**-e** _char_
> 设置分离字符。

**-E**
> 禁用分离字符。

**-z**
> 禁用挂起键处理。

# CAVEATS

没有窗口管理。没有回滚缓冲区。会话结束后套接字文件仍会保留。默认同一时间只允许一个客户端。没有内置的会话列表功能。

# HISTORY

**dtach** 由 **Ned T. Crigler** 于 **2001 年**创建，作为 GNU Screen 的极简替代品。它源于对会话分离功能的需求，同时避免了 screen 的复杂性。当需要与其他终端复用器配合使用或只需简单的会话持久化时，该工具非常实用。

# INSTALL

```apt: sudo apt install dtach```

```dnf: sudo dnf install dtach```

```apk: sudo apk add dtach```

```zypper: sudo zypper install dtach```

```brew: brew install dtach```

```nix: nix profile install nixpkgs#dtach```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[screen](/man/screen)(1), [tmux](/man/tmux)(1), [abduco](/man/abduco)(1), [nohup](/man/nohup)(1)
