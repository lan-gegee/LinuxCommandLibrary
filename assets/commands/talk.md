# TAGLINE

实时的终端文字交流工具

# TLDR

**与本机用户交谈**

```talk [username]```

**与特定终端上的用户交谈**

```talk [username] [tty3]```

**与远程主机上的用户交谈**

```talk [username]@[hostname]```

# SYNOPSIS

**talk** _user_ [_ttyname_]

**talk** _user@host_ [_ttyname_]

# PARAMETERS

_user_
> 要交谈对象的用户名。远程用户可写成 @hostname 的形式。

_ttyname_
> 当对方登录在多个终端时，指定要联系的特定终端。

# DESCRIPTION

**talk** 是一个可视化的交流程序，可以在两个用户的终端之间实时复制文本。屏幕被分成上下两半：上半部分显示你输入的内容，下半部分显示对方的文字。

目标用户会收到一条邀请交谈的消息，他们必须也对你运行 `talk` 来接受邀请。

# CAVEATS

双方用户都必须已登录。需要 talk 守护进程（talkd）正在运行。mesg 命令控制用户是否能接收 talk 请求。此工具基本已被即时通讯取代，属于过时技术。

# HISTORY

**talk** 于 **20 世纪 80 年代**起源于 BSD Unix，是最早的即时通讯形式之一。它曾是标准 Unix 网络工具的一部分，现在包含在 GNU inetutils 中。

# INSTALL

```dnf: sudo dnf install talk```

```zypper: sudo zypper install talk```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[write](/man/write)(1), [wall](/man/wall)(1), [mesg](/man/mesg)(1)
