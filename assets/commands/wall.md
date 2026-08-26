# TAGLINE

向所有已登录用户发送消息

# TLDR

**向所有已登录用户发送消息**

```wall [message]```

**向特定组发送消息**

```wall -g [group_name] [message]```

**将文件内容发送给所有已登录用户**

```wall [file]```

**带写入超时时间发送消息**

```wall -t [seconds] [message]```

**不带横幅发送消息**

```wall -n [message]```

# SYNOPSIS

**wall** [_options_] [_message_ | _file_]

# PARAMETERS

**-g**, **--group** _group_
> 只发送给指定组的成员。

**-n**, **--nobanner**
> 不显示通常位于每条消息之前的横幅（包含发送者和时间戳）。

**-t**, **--timeout** _seconds_
> 写入每个终端的超时时间，以秒为单位。默认为 300 秒。

# DESCRIPTION

**wall**（write all）在所有当前已登录用户的终端上显示一条消息、某个文件的内容或其标准输入。系统管理员通常用它进行全系统公告，例如即将关机的通知。

消息前面有一条横幅，显示发送者和时间戳。超过 79 个字符的行会被换行，较短的行会用空白填充至 79 个字符。对于已用 **mesg**(1) 拒绝消息的用户，只有超级用户才能在其终端上写入。

# CAVEATS

用户可以用 **mesg n** 屏蔽 wall 消息。只有 root 才能绕过这一限制。某些会话（例如显示管理器）的 utmp ut_type 数据以 ':' 开头，将不会收到消息。运行图形桌面环境且未打开终端的用户看不到消息。

# HISTORY

**wall** 命令自 Unix 早期版本就已存在，Linux 系统上包含在 **util-linux** 软件包中。

# INSTALL

```apt: sudo apt install bsdutils```

```apk: sudo apk add util-linux-misc```

```nix: nix profile install nixpkgs#wall```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[write](/man/write)(1), [mesg](/man/mesg)(1), [talk](/man/talk)(1), [shutdown](/man/shutdown)(8)
