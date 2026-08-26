# TAGLINE

灵活的邮件传输代理

# TLDR

**启动邮件队列处理**

```exim -q```

**发送测试消息**

```echo "Test" | exim [user@example.com]```

**显示邮件队列**

```exim -bp```

**显示队列数量**

```exim -bpc```

**强制投递消息**

```exim -M [message_id]```

**从队列中删除消息**

```exim -Mrm [message_id]```

**测试地址路由**

```exim -bt [user@example.com]```

**检查配置**

```exim -bV```

# SYNOPSIS

**exim** [_options_] [_addresses_...]

# PARAMETERS

**-q** [_time_]
> 运行队列，可选周期性重复执行。

**-bp**
> 列出队列中的消息。

**-bpc**
> 统计队列中的消息数。

**-bt** _address_
> 测试地址路由。

**-bV**
> 显示版本和配置。

**-M** _id_
> 强制投递消息。

**-Mrm** _id_
> 从队列中删除消息。

**-Mvh** _id_
> 查看消息头。

**-Mvb** _id_
> 查看消息正文。

**-d**
> 启用调试模式。

**-C** _file_
> 使用备用配置。

# DESCRIPTION

**exim** 是一个邮件传输代理（MTA），负责在 Unix 系统上发送、接收和路由电子邮件。它以灵活的配置和强大的过滤能力著称。

该工具支持 ACL、内容扫描、TLS 加密以及多种认证机制。它可以同时充当收信和发信邮件服务器。

# CONFIGURATION

**/etc/exim4/exim4.conf**
> 主配置文件，控制路由、ACL、认证和传输设置。

**/etc/exim4/passwd**
> SMTP 客户端的认证凭据。

# CAVEATS

配置语法复杂。需要细致的安全设置。端口 25 常被 ISP 封锁。生产环境中必须监控日志。

# HISTORY

**Exim** 由 **剑桥大学**的 **Philip Hazel** 自 **1995 年**起编写。名字代表 "EXperimental Internet Mailer"。它成为 Debian 的默认 MTA，并在 Unix 服务器上广泛使用。

# INSTALL

```apt: sudo apt install exim4-daemon-heavy```

```dnf: sudo dnf install exim```

```pacman: sudo pacman -S exim```

```apk: sudo apk add exim```

```zypper: sudo zypper install exim```

```brew: brew install exim```

```nix: nix profile install nixpkgs#exim```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sendmail](/man/sendmail)(1), [postfix](/man/postfix)(1), [mailq](/man/mailq)(1), [mutt](/man/mutt)(1)

# RESOURCES

```[Source code](https://github.com/Exim/exim)```

```[Homepage](https://www.exim.org/)```

<!-- verified: 2026-07-15 -->
