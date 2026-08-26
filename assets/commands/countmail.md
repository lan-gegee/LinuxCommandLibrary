# TAGLINE

统计邮箱中的邮件数量

# TLDR

**统计默认邮箱**中的邮件数

```countmail```

**统计指定**邮箱文件中的邮件数

```countmail [/var/mail/user]```

**统计 Maildir 中的邮件数**

```countmail [~/Maildir]```

仅**显示未读邮件数量**

```countmail --unread```

**显示多个**邮箱的统计结果

```countmail [mailbox1] [mailbox2]```

以**机器可读的格式**输出

```countmail --quiet [mailbox]```

# SYNOPSIS

**countmail** [_options_] [_mailbox_...]

# PARAMETERS

_MAILBOX_
> 要统计的邮箱文件或 Maildir 的路径。省略时使用默认邮箱。

**--unread**
> 只统计未读邮件。

**--read**
> 只统计已读邮件。

**--quiet**
> 只输出数字，不带标签。

**--mbox**
> 将路径视为 mbox 格式。

**--maildir**
> 将路径视为 Maildir 格式。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**countmail** 是一个用于统计邮箱中邮件数量的简单实用工具。它同时支持传统的 mbox 格式文件和 Maildir 目录，并在可能时自动检测格式。

该工具适用于需要在状态栏、脚本和通知中显示未读邮件数量的场景。它可以处理多个邮箱，并输出便于其他程序解析的结果。

countmail 高效读取邮箱头部而不加载完整邮件内容，即使面对大邮箱也能快速完成。它能根据标准邮件标志区分已读和未读邮件。

# CAVEATS

对于不常见的配置，邮箱格式自动检测可能失败；必要时请显式使用 **--mbox** 或 **--maildir** 标志。该工具不执行文件锁定，因此当邮箱正被并发修改时，统计结果可能略有偏差。

# HISTORY

countmail 延续了简单 Unix 邮件工具的传统。存在多种实现来提供这一基础功能，有的作为大型邮件处理工具集的一部分，有的则是用于桌面集成的独立脚本。

# SEE ALSO

[mail](/man/mail)(1), [from](/man/from)(1), [mutt](/man/mutt)(1), [fetchmail](/man/fetchmail)(1), [procmail](/man/procmail)(1)
