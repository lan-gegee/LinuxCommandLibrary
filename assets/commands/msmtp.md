# TAGLINE

用于从命令行发送电子邮件的轻量级 SMTP 客户端

# TLDR

**发送邮件**

```echo "[message]" | msmtp [recipient@example.com]```

**发送带主题的邮件**

```echo -e "Subject: [Hello]\n\n[Body]" | msmtp [recipient@example.com]```

**从特定账户发送**

```msmtp -a [account_name] [recipient@example.com]```

**测试配置**

```msmtp --serverinfo```

**检查账户配置**

```msmtp --configure [account_name]```

**将文件作为消息发送**

```msmtp [recipient@example.com] < [message.txt]```

**打印配置**

```msmtp -P```

# SYNOPSIS

**msmtp** [_-a account_] [_--serverinfo_] [_options_] [_recipients_]

# PARAMETERS

**-a** _ACCOUNT_, **--account** _ACCOUNT_
> 使用指定的账户。

**-f** _ADDRESS_, **--from** _ADDRESS_
> 设置 From 地址。

**-C** _FILE_, **--file** _FILE_
> 使用指定的配置文件。

**--serverinfo**
> 打印服务器信息。

**-P**, **--pretend**
> 只打印配置，不实际发送。

**--configure** _ACCOUNT_
> 显示账户配置。

**-d**, **--debug**
> 调试模式。

**-t**, **--read-recipients**
> 从消息中读取收件人。

**-X** _FILE_, **--logfile** _FILE_
> 记录日志到文件。

**--tls**
> 使用 TLS 加密。

**--tls-starttls**
> 使用 STARTTLS。

**--host** _HOST_
> SMTP 服务器主机。

**--port** _PORT_
> SMTP 服务器端口。

**--user** _USER_
> 身份验证用户名。

**--passwordeval** _CMD_
> 从命令获取密码。

# DESCRIPTION

**msmtp** 是一个用于从命令行发送电子邮件的轻量级 SMTP 客户端。它可作为 sendmail 的替代品，让脚本和应用程序通过外部 SMTP 服务器发送邮件。

~/.msmtprc 中的配置定义了各个账户的服务器设置、身份验证和 TLS 选项。可以为不同的邮件服务器或身份配置多个账户。

密码处理支持多种方式：明文（不推荐）、通过 passwordeval 运行命令（例如密码管理器），或集成系统钥匙串。

支持通过 STARTTLS 或直接 TLS 连接使用 TLS。证书验证可配置为使用系统 CA 证书或指定文件。

作为 sendmail 替代品，msmtp 可以符号链接到 /usr/sbin/sendmail，从而成为系统的默认邮件传输程序。许多应用程序都通过 sendmail 发送外发邮件。

与 mutt、git 及其他工具的集成非常简单——它们只需知道 sendmail 路径，或直接使用 msmtp 即可。

# CAVEATS

需要能够访问 SMTP 服务器。需要考虑密码的存储方式。某些服务商要求使用应用专用密码。可能出现 TLS 证书问题。队列/离线发送需要 msmtpd 或 msmtp-queue。

# HISTORY

**msmtp** 由 **Martin Lambers** 于约 **2000 年**开始编写，作为一个简单的 sendmail 替代品。它专注于轻量和可配置性，支持带身份验证和 TLS 的现代 SMTP。该项目至今仍在积极维护。

# INSTALL

```apt: sudo apt install msmtp```

```dnf: sudo dnf install msmtp```

```pacman: sudo pacman -S msmtp```

```apk: sudo apk add msmtp```

```zypper: sudo zypper install msmtp```

```brew: brew install msmtp```

```nix: nix profile install nixpkgs#msmtp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sendmail](/man/sendmail)(1), [mutt](/man/mutt)(1), [mailx](/man/mailx)(1)
