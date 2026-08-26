# TAGLINE

用离开消息锁定终端

# TLDR

**锁定终端**并设置离开消息

```away [message]```

锁定终端并**启用邮件检查**

```away -c message```

锁定终端并**禁用邮件检查**

```away -C message```

以秒为单位设置**后台任务间隔**

```away -t seconds message```

锁定终端并**持续检查邮件**，直到所有邮箱都收到邮件

```away -p message```

# SYNOPSIS

**away** [_options_] _message_

# DESCRIPTION

**away** 会锁定终端，并向看到屏幕的人显示一条离开消息。它可以选择性地监视新邮件，并管理后台任务的执行时机。

终端会保持锁定状态，直到用户完成认证。离开消息对可能接触该终端的其他用户可见。

# PARAMETERS

**-c**, **--mail**
> 启用邮件检查

**-C**, **--nomail**
> 禁用邮件检查

**-f**, **--rcfile**=_FILE_
> 指定替代 ~/.awayrc 的配置文件

**-F**, **--norcfile**
> 忽略用户配置文件

**-m**, **--message**
> 将命令行剩余部分视为消息

**-t**, **--time**=_SECONDS_
> 设置 away 在执行后台任务前休眠的秒数

**-T**, **--notime**
> 忽略时间间隔选项，使用默认值

**-p**, **--persist**
> 只要还有至少一个邮箱未收到新邮件，就继续检查邮件

**-P**, **--nopersist**
> 一旦发现任何邮箱有新邮件即停止检查

**-h**, **--help**
> 显示帮助信息

**-v**, **--version**
> 显示版本信息

# CAVEATS

锁定机制依赖系统认证。邮件检查要求正确配置邮件 spool 目录。任何能物理接触到终端的人都能看到离开消息。

# INSTALL

```apt: sudo apt install away```

```aur: yay -S away```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[vlock](/man/vlock)(1), [screen](/man/screen)(1)
