# TAGLINE

向已登录的用户发送消息

# TLDR

向特定终端上的用户**发送**消息

```write [username] [terminal_id]```

向 tty5 上的用户**发送**消息

```write [username] tty5```

向伪终端上的用户**发送**消息

```write [username] pts/5```

# SYNOPSIS

**write** _user_ [_ttyname_]

# DESCRIPTION

**write** 允许你与其他用户通信，方式是把你的终端上输入的内容逐行复制到对方的终端。运行 write 后，对方会收到一条提示，显示谁在发消息。然后你可以逐行输入内容，这些内容会出现在对方的终端上。

按 Ctrl+D（EOF）或 Ctrl+C 结束消息会话。可以使用 **who** 命令查找已登录用户的终端 ID。

# CAVEATS

接收方的终端必须可写（使用 **mesg y**）。如果用户登录了多个终端且未指定 ttyname，write 会选择空闲时间最短的终端。只能对同一系统上的用户生效。

# SEE ALSO

[mesg](/man/mesg)(1), [wall](/man/wall)(1), [talk](/man/talk)(1), [who](/man/who)(1)
