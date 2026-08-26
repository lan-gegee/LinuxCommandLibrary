# TAGLINE

校验 SPF 电子邮件身份验证记录

# TLDR

**检查 SPF 记录**

```spfquery -ip [192.168.1.1] -sender [user@example.com]```

**查询域名**

```spfquery -ip [ip] -sender [email] -helo [mail.example.com]```

**调试模式**

```spfquery -debug -ip [ip] -sender [email]```

**显示版本**

```spfquery -version```

# SYNOPSIS

**spfquery** [_-ip addr_] [_-sender email_] [_-helo hostname_] [_options_]

# PARAMETERS

**-ip** _ADDR_
> 客户端 IP 地址。

**-sender** _EMAIL_
> 信封发件人。

**-helo** _HOST_
> HELO 主机名。

**-debug**
> 调试输出。

**-version**
> 显示版本。

**-rcpt-to** _EMAIL_
> 信封收件人地址（用于辅助 MX 检查）。

**-help**
> 显示帮助。

# DESCRIPTION

**spfquery** 通过检查给定 IP 地址是否有权代表某个域发送邮件来验证 Sender Policy Framework（SPF）记录。它会查询该域名的 DNS SPF 记录，并根据已发布的策略评估发信 IP。

该工具返回标准的 SPF 结果代码：pass、fail、softfail、neutral、none、temperror 或 permerror。邮件服务器管理员可用它调试 SPF 配置、验证 DNS 记录是否正确，以及排查由 SPF 校验失败引起的邮件投递问题。

作为 **libspf2** 库的一部分，spfquery 实现了完整的 SPF 规范，包括机制求值、宏展开以及 redirect/include 处理。

# CAVEATS

需要 DNS 连接才能解析 SPF 记录。被查询的域名必须存在 SPF 记录。结果代码需要正确解读才能用于策略执行。

# INSTALL

```apk: sudo apk add libspf2-tools```

```zypper: sudo zypper install libspf2-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dig](/man/dig)(1), [host](/man/host)(1), [nslookup](/man/nslookup)(1), [sendmail](/man/sendmail)(1), [postfix](/man/postfix)(1)
