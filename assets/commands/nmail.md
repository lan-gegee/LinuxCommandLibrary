# TAGLINE

适用于 Linux 和 macOS 的终端电子邮件客户端

# TLDR

**启动电子邮件客户端**

```nmail```

**设置 Gmail 账户**

```nmail -s gmail```

**设置 Outlook 账户**

```nmail -s outlook```

# SYNOPSIS

**nmail** [_options_]

# PARAMETERS

**-s** _SERVICE_
> 为特定服务运行设置向导（gmail、outlook）。

# DESCRIPTION

**nmail** 是一款面向 Linux 和 macOS 的基于控制台的电子邮件客户端，用户界面类似 Alpine/Pine。它支持 IMAP 和 SMTP、多账户、邮件会话线程、搜索和过滤、查看 HTML 邮件（转换为文本或在外部浏览器中打开）、用 Markdown 撰写 HTML 邮件、草稿、离线撰写以及附件处理。

为 Gmail 和 Outlook/Hotmail 提供了设置向导。可以使用 vim 或 emacs 等外部文本编辑器来撰写邮件。

# CAVEATS

启用双因素认证后，Gmail 需要使用应用专用密码。

# HISTORY

**nmail** 由 **d99kris** 创建，使用 **C++** 编写。

# INSTALL

```apk: sudo apk add nmail```

```brew: brew install nmail```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mutt](/man/mutt)(1), [alpine](/man/alpine)(1), [meli](/man/meli)(1)
