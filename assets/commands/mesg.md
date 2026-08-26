# TAGLINE

控制其他用户能否通过 write 向你的终端发送消息

# TLDR

检查**当前状态**

```mesg```

**禁止**消息

```mesg n```

**允许**消息

```mesg y```

启用**详细**模式

```mesg --verbose```

# SYNOPSIS

**mesg** [**y** | **n**]

# DESCRIPTION

**mesg** 控制其他用户能否通过 write 命令向你的终端发送消息。不带参数时，它显示当前设置。

# PARAMETERS

**y**
> 允许来自其他用户的消息

**n**
> 禁止来自其他用户的消息

**-v, --verbose**
> 若未在终端中执行则打印警告

# OUTPUT

不带参数时显示：
**is y**: 允许消息
**is n**: 禁止消息

# CAVEATS

仅影响当前终端。设置不会跨会话保持。某些终端可能默认拒绝消息。

# INSTALL

```apk: sudo apk add util-linux-misc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[write](/man/write)(1), [talk](/man/talk)(1), [wall](/man/wall)(1)
