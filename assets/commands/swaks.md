# TAGLINE

SMTP 测试的瑞士军刀

# TLDR

向服务器发送**测试邮件**

```swaks -t [user@example.com] -s [mail.example.com]```

使用 **SMTP 认证**发送

```swaks -t [user@example.com] -s [mail.example.com] -a LOGIN -au [username] -ap [password]```

发送带**自定义主题和正文**的邮件

```swaks -t [user@example.com] --header "Subject: [Test]" --body "[Hello World]"```

发送带**附件**的邮件

```swaks -t [user@example.com] --attach [path/to/file]```

使用 **STARTTLS** 加密发送

```swaks -t [user@example.com] -s [mail.example.com] --tls```

使用**隐式 TLS** 发送（端口 465 上的 SMTPS）

```swaks -t [user@example.com] -s [mail.example.com] --tls-on-connect -p 465```

通过 **UNIX 套接字**以 LMTP 协议测试

```swaks -t [user@example.com] --socket [/var/lda.sock] --protocol LMTP```

设置自定义的 **EHLO/HELO** 问候语

```swaks -t [user@example.com] -s [mail.example.com] --helo [myhost.example.com]```

# SYNOPSIS

**swaks** [_OPTIONS_]

# PARAMETERS

**-t**, **--to** _address_
> 收件人邮箱地址。可多次指定。

**-f**, **--from** _address_
> 发件人邮箱地址。

**-s**, **--server** _host_
> SMTP 服务器主机名或 IP。

**-p**, **--port** _port_
> SMTP 端口（默认：25；使用 --tls-on-connect 时为 465）。

**-h**, **--helo** _string_
> 用作 HELO/EHLO 问候语的字符串。

**-a**, **--auth** _type_
> 认证类型（PLAIN、LOGIN、CRAM-MD5、DIGEST-MD5、NTLM）。

**-au**, **--auth-user** _user_
> 认证用户名。

**-ap**, **--auth-password** _pass_
> 认证密码。

**--auth-optional**
> 尝试认证，但不可用时继续执行。

**-d**, **--data** _data_
> 将参数用作消息的整个 DATA 部分。

**--body** _text_
> 消息正文内容或文件路径。

**--header** _header_
> 为消息添加头部（如 "Subject: Test"）。

**-ah**, **--add-header** _header_
> 追加额外的头部而不替换默认值。

**--attach** _file_
> 为消息附加文件。可多次使用。

**--tls**
> 连接后要求 STARTTLS 加密。

**--tls-on-connect**
> 从连接一开始就使用隐式 TLS（SMTPS）。

**--tls-verify**
> 校验服务器的 TLS 证书。

**--tls-cert** _file_
> 客户端 TLS 证书文件。

**--tls-key** _file_
> 客户端 TLS 私钥文件。

**--socket** _path_
> 通过 UNIX 域套接字连接。

**--protocol** _proto_
> 使用的协议：SMTP、ESMTP（默认）、LMTP。

**-n**, **--suppress-data**
> 不在输出中显示 DATA 部分。

**-q**, **--quit-after** _stage_
> 在指定阶段后退出（CONNECT、EHLO、AUTH、MAIL、RCPT）。

**--timeout** _seconds_
> 连接和读写超时时间。

**-4**
> 强制使用 IPv4 连接。

**-6**
> 强制使用 IPv6 连接。

**--dump**
> 显示所有解析后的选项并退出。

# DESCRIPTION

**swaks**（Swiss Army Knife SMTP）是一款功能丰富、可脚本化的 SMTP 测试工具，用于诊断邮件服务器配置、测试认证和验证邮件投递。它支持基于多种传输方式的 SMTP、ESMTP 和 LMTP 协议，包括 TCP 套接字、UNIX 套接字和 TLS 连接。

该工具对于测试垃圾邮件过滤器（使用 GTUBE）、病毒扫描器（使用 EICAR）、认证机制和 TLS 配置极为有用。它提供详细的交互日志，展示 SMTP 会话的每一步。

# CAVEATS

需要 Perl。命令行中的密码会在进程列表中可见；敏感数据请使用 **--auth-password-optional** 或配置文件。某些认证方法需要额外的 Perl 模块。测试邮件可能触发垃圾邮件过滤器。

# HISTORY

**swaks** 由 **John Jetmore** 创建，自 **2000 年代初**以来一直活跃维护。它已成为邮件服务器管理员的标准工具，可在大多数 Linux 发行版仓库中获取。该工具用 Perl 编写，以 GPLv2 许可证发布。

# INSTALL

```dnf: sudo dnf install swaks```

```pacman: sudo pacman -S swaks```

```zypper: sudo zypper install swaks```

```brew: brew install swaks```

```nix: nix profile install nixpkgs#swaks```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sendmail](/man/sendmail)(8), [postfix](/man/postfix)(1), [openssl](/man/openssl)(1), [curl](/man/curl)(1)
