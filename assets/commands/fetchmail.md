# TAGLINE

从远程服务器收取邮件

# TLDR

从服务器**收取邮件**

```fetchmail```

**从指定服务器收取**

```fetchmail [mail.example.com]```

**在服务器上保留邮件**

```fetchmail -k```

只检查是否有新邮件

```fetchmail -c```

详细输出

```fetchmail -v```

以守护进程方式运行

```fetchmail -d [300]```

使用指定配置文件

```fetchmail -f [~/.fetchmailrc]```

# SYNOPSIS

**fetchmail** [_options_] [_servers_...]

# DESCRIPTION

**fetchmail** 从远程服务器收取邮件并转发到本地邮件系统。它支持 POP3、IMAP、ETRN 和 ODMR 协议，并可使用 SSL/TLS 加密。

该工具通过 ~/.fetchmailrc 或命令行选项进行配置。它可以作为守护进程运行，定期检查新邮件，并与本地 MTA 集成。

# PARAMETERS

**-c**, **--check**
> 只检查是否有邮件，不收取。

**-k**, **--keep**
> 在服务器上保留邮件。

**-a**, **--all**
> 收取所有邮件（包括已读）。

**-d** _seconds_
> 以守护进程模式按轮询间隔运行。

**-f** _file_
> 使用备用配置文件。

**-u** _user_
> 远程用户名。

**-p** _proto_, **--proto** _proto_
> 协议（auto、pop3、imap、etrn、odmr）。

**--ssl**
> 使用隐式 SSL/TLS（直接通过加密通道连接）。

**--sslproto** _value_
> SSL/TLS 协议版本和 STARTTLS 控制。推荐：tls1.2+。

**-v**, **--verbose**
> 详细输出。

**-s**, **--silent**
> 抑制进度消息。

**-q**, **--quit**
> 终止正在运行的守护进程。

**-l** _maxbytes_, **--limit** _maxbytes_
> 跳过超过 maxbytes 的邮件。

**-r** _folder_, **--folder** _folder_
> 从非默认邮件文件夹收取（仅限 IMAP）。

**--idle**
> 使用 IMAP IDLE 对新邮件进行推送通知。

# CONFIGURATION

**~/.fetchmailrc**
> 主配置文件，包含服务器设置、认证和投递选项。

# CAVEATS

配置文件中的密码需要妥善保护。建议启用 SSL 验证。大邮箱可能较慢。本地 MTA 必须接受转发的邮件。

# HISTORY

**fetchmail** 最初由 **Carl Harris** 于 **1993 年**编写，名为 popclient。**Eric S. Raymond** 于 **1996 年**接手开发，将其更名为 fetchmail 并添加了 IMAP 支持。它成为从远程服务器拉取邮件的标准工具。

# INSTALL

```apt: sudo apt install fetchmail```

```dnf: sudo dnf install fetchmail```

```pacman: sudo pacman -S fetchmail```

```apk: sudo apk add fetchmail```

```zypper: sudo zypper install fetchmail```

```brew: brew install fetchmail```

```nix: nix profile install nixpkgs#fetchmail```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[procmail](/man/procmail)(1), [mutt](/man/mutt)(1), [sendmail](/man/sendmail)(1), [mail](/man/mail)(1)
