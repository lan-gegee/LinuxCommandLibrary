# TAGLINE

TLS/SSL 连接测试与调试客户端

# TLDR

**连接到 TLS 服务器**

```gnutls-cli [example.com]```

**在指定端口连接**

```gnutls-cli -p [443] [example.com]```

**显示证书链**

```gnutls-cli --print-cert [example.com]```

**用特定协议测试**

```gnutls-cli --priority="NORMAL:-VERS-TLS-ALL:+VERS-TLS1.3" [example.com]```

**以 STARTTLS 方式启动**

```gnutls-cli --starttls-proto=[smtp] [mail.example.com]:587```

**仅验证证书**

```gnutls-cli --tofu [example.com] < /dev/null```

# SYNOPSIS

**gnutls-cli** [_options_] _hostname_

# PARAMETERS

**-p**, **--port** _port_
> 要连接的端口。

**-s**, **--starttls**
> 先建立明文会话，在收到 EOF 或 SIGALRM 时切换到 TLS（通用 STARTTLS）。

**--print-cert**
> 打印服务器证书。

**--starttls-proto** _proto_
> 使用 STARTTLS（smtp、pop3、imap、ftp、xmpp、ldap）。

**--priority** _string_
> 用于密码套件选择的优先级字符串。

**-V**, **--verbose**
> 详细输出。

**--tofu**
> 首次使用即信任（TOFU）。

**--insecure**
> 不验证证书。

**-x**, **--x509cafile** _file_
> CA 证书文件。

**--benchmark-ciphers**
> 对密码套件性能进行基准测试。

**--list**
> 列出支持的算法。

**-d**, **--debug** _LEVEL_
> 设置调试详细级别。

# DESCRIPTION

**gnutls-cli** 是一个用于测试和调试安全连接的 TLS/SSL 客户端。它可以连接服务器、显示证书信息，并允许测试各种 TLS 配置。

该工具有助于诊断证书问题、协议支持和密码套件协商。它还可以作为交互式协议的简单安全客户端使用。

# CAVEATS

证书验证需要正确的 CA 配置。优先级字符串语法复杂。某些服务器对测试客户端的表现可能不同。

# HISTORY

**gnutls-cli** 是 **GnuTLS** 的一部分，后者由 **Nikos Mavrogiannopoulos** 等人自 **2000** 年起开发。GnuTLS 在 LGPL 许可证下提供了 OpenSSL 的替代方案，而 gnutls-cli 则是其诊断和测试工具。

# INSTALL

```apt: sudo apt install gnutls-bin```

```dnf: sudo dnf install gnutls-utils```

```apk: sudo apk add gnutls-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openssl](/man/openssl)(1), [curl](/man/curl)(1), [certtool](/man/certtool)(1), [nmap](/man/nmap)(1)

# RESOURCES

```[Source code](https://gitlab.com/gnutls/gnutls)```

```[Homepage](https://www.gnutls.org/)```

<!-- verified: 2026-07-17 -->
