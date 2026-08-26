# TAGLINE

通过邮件传输代理发送邮件

# TLDR

**从命令行发送邮件**

```echo "Message body" | sendmail [recipient@example.com]```

**发送带主题的邮件**（使用邮件头部）

```printf "Subject: Test\n\nMessage body" | sendmail [recipient@example.com]```

**从文件发送邮件**

```sendmail [recipient@example.com] < [message.txt]```

**处理邮件队列**

```sendmail -q```

**显示邮件队列**

```sendmail -bp```

**在不实际发送的情况下测试配置**

```sendmail -bv [recipient@example.com]```

# SYNOPSIS

**sendmail** [**-flags**] [_address_...]

# PARAMETERS

**-t**
> 从消息头部读取收件人（To:、Cc:、Bcc:）

**-f** _address_
> 设置信封发件人地址

**-F** _name_
> 设置发件人的全名

**-i**
> 忽略单独成行的点号

**-q**
> 处理队列中保存的消息

**-bp**
> 打印邮件队列摘要

**-bv**
> 校验地址而不实际发送

**-bd**
> 以守护进程方式运行

**-bs**
> 在 stdin/stdout 上使用 SMTP 协议

**-v**
> 详细模式

**-O** _option_=_value_
> 设置邮件服务器选项

# DESCRIPTION

**sendmail** 是传统的 Unix 邮件传输代理（MTA）接口。虽然原始的 sendmail 程序较为复杂，但大多数 Linux 系统使用提供相同命令行接口的兼容替代品（Postfix、Exim）。

该命令从标准输入接收消息并将其投递给指定的收件人。输入中可以包含头部；如果使用了 **-t**，则从 To/Cc/Bcc 头部读取收件人，而不是从命令行参数读取。

对于简单的邮件发送，消息格式包括可选的头部、一个空行以及正文。Subject:、From:、To: 等头部都是标准格式。

邮件队列保存等待投递的消息。使用 **-q** 触发队列处理，使用 **-bp**（或 **mailq**）查看队列状态。

# MESSAGE FORMAT

```
From: sender@example.com
To: recipient@example.com
Subject: Test Email

This is the message body.
```

# CONFIGURATION

**/etc/mail/sendmail.cf**
> sendmail 主配置文件（或 Postfix/Exim 兼容层的等价文件）。

**/etc/aliases**
> 邮件别名数据库，将本地地址映射到收件人或程序。

**/var/spool/mqueue/**
> 保存等待投递消息的邮件队列目录。

# CAVEATS

现代系统通常使用提供 sendmail 兼容接口的 Postfix 或 Exim。实际的 MTA 可能与传统 sendmail 不同。

许多系统需要正确配置后 sendmail 才能投递外部邮件。未配置 MTA 时，邮件可能仅在本地可用。

在缺乏适当身份验证及 SPF、DKIM 和 DMARC 配置的情况下，避免用 sendmail 发送批量邮件或进行自动化发送，以免被判定为垃圾邮件。

# HISTORY

Sendmail 由 UC Berkeley 的 **Eric Allman** 编写，首个版本于 **1983** 年发布。它曾是占主导地位的 Unix MTA，并确立了标准的命令行接口，Postfix 和 Exim 等替代品为保持兼容而沿袭了这一接口。

# INSTALL

```apt: sudo apt install dma```

```dnf: sudo dnf install postfix```

```pacman: sudo pacman -S postfix```

```apk: sudo apk add postfix```

```zypper: sudo zypper install postfix```

```nix: nix profile install nixpkgs#dma```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mail](/man/mail)(1), [postfix](/man/postfix)(1), [mailq](/man/mailq)(1), [newaliases](/man/newaliases)(1)
