# TAGLINE

用于收发互联网邮件的增强版 mail 命令

# TLDR

**发送邮件**（输入正文后按 Ctrl+D 结束）

```mailx -s "[Subject]" [recipient@example.com]```

**通过管道传入正文发送**

```echo "[message]" | mailx -s "[Subject]" [recipient@example.com]```

**从文件读取正文发送**

```mailx -s "[Subject]" [recipient@example.com] < [message.txt]```

**发送带附件的邮件**

```mailx -s "[Subject]" -a [file.pdf] [recipient@example.com]```

**发送带抄送和密送的邮件**

```mailx -s "[Subject]" -c [cc@example.com] -b [bcc@example.com] [recipient@example.com]```

**阅读邮件**

```mailx```

**从指定的邮箱文件阅读邮件**

```mailx -f [path/to/mbox]```

**使用 SMTP 服务器**

```mailx -S smtp=[smtp://mail.example.com] -s "[Subject]" [recipient@example.com]```

# SYNOPSIS

**mailx** [_options_] [_recipients_]

# PARAMETERS

_RECIPIENTS_
> 电子邮件地址。

**-s** _SUBJECT_
> 邮件主题。

**-a** _FILE_
> 附加文件。

**-c** _ADDR_
> 抄送收件人。

**-b** _ADDR_
> 密送收件人。

**-r** _ADDR_
> 设置发件人地址。

**-S** _VAR=VALUE_
> 设置内部变量（如 smtp、from、smtp-auth）。

**-t**
> 从邮件的 To/Cc/Bcc 头部读取收件人。

**-f** _FILE_
> 从邮箱文件读取。

**-N**
> 不读取系统级启动文件。

**-H**
> 打印邮件头摘要后退出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mailx** 是一个用于收发互联网邮件的增强版 mail 命令。它与 POSIX 兼容，并扩展了 MIME 支持、SMTP 连接、S/MIME、附件等功能，比基础 mail 命令特性更多。

它既能发送也能阅读电子邮件。不带参数调用时，它会读取用户邮箱；给定收件人时，则进入撰写模式。

# CAVEATS

存在多种实现（heirloom-mailx、s-nail、BSD mailx），功能集各不相同。SMTP 配置和附件语法在不同实现之间也有差异。在 heirloom-mailx/s-nail 中 **-a** 表示"附加文件"，而在 BSD mailx 中则表示"设置邮件头"。

# HISTORY

mailx 由最初的 **Unix mail** 命令经过 Berkeley Mail 演化而来。现代实现包括 **s-nail**（heirloom-mailx 的继任者），它增加了 MIME、SMTP、POP3 和 IMAP 支持。

# INSTALL

```zypper: sudo zypper install mailx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mail](/man/mail)(1), [mutt](/man/mutt)(1), [sendmail](/man/sendmail)(8)
