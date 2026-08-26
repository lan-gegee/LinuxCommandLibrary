# TAGLINE

发送和阅读电子邮件

# TLDR

**发送邮件**

```mail -s "[Subject]" [recipient@example.com]```

**发送带正文的邮件**

```echo "[message]" | mail -s "[Subject]" [recipient@example.com]```

**发送文件内容**

```mail -s "[Subject]" [recipient@example.com] < [message.txt]```

**发送带附件的邮件**

```mail -s "[Subject]" -A [file.pdf] [recipient@example.com]```

**阅读邮件**

```mail```

**检查指定邮箱**

```mail -f [/var/mail/user]```

# SYNOPSIS

**mail** [_options_] [_recipients_]

# PARAMETERS

_RECIPIENTS_
> 电子邮件地址。

**-s** _SUBJECT_
> 邮件主题。

**-A** _FILE_
> 附加文件。

**-c** _ADDR_
> 抄送（CC）收件人。

**-b** _ADDR_
> 密送（BCC）收件人。

**-f** _FILE_
> 从邮箱读取。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mail** 用于发送和阅读电子邮件。它是一个基础的命令行邮件用户代理。

该工具可在脚本中快速发送邮件，并从本地邮箱读取邮件。

# CAVEATS

需要配置好 MTA。存在多种实现。可能需要安装 mailutils 软件包。

# HISTORY

mail 的历史可以追溯到早期的 **Unix** 系统，为用户和脚本提供基础的电子邮件功能。

# INSTALL

```apk: sudo apk add mailx```

```zypper: sudo zypper install mailx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mailx](/man/mailx)(1), [sendmail](/man/sendmail)(8), [mutt](/man/mutt)(1)
