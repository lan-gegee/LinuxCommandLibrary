# TAGLINE

用于测试和调试连接的 TLS/SSL 客户端

# TLDR

**连接到 HTTPS 服务器**

```openssl s_client -connect [example.com]:443```

**使用 SNI 连接**

```openssl s_client -connect [example.com]:443 -servername [example.com]```

**显示证书链**

```openssl s_client -connect [example.com]:443 -showcerts```

**以 STARTTLS 连接 SMTP**

```openssl s_client -connect [mail.example.com]:587 -starttls smtp```

**验证证书**

```openssl s_client -connect [example.com]:443 -verify_return_error```

**测试特定协议**

```openssl s_client -connect [example.com]:443 -tls1_3```

# SYNOPSIS

**openssl s_client** [_options_] -connect _host:port_

# PARAMETERS

**-connect** _host:port_
> 要连接的服务器。

**-servername** _name_
> SNI 主机名。

**-showcerts**
> 显示证书链。

**-starttls** _proto_
> STARTTLS 协议。

**-verify** _depth_
> 验证深度。

**-CAfile** _file_
> CA 证书。

**-tls1_2**, **-tls1_3**
> 指定 TLS 版本。

**-cipher** _list_
> 密码套件列表。

# DESCRIPTION

**openssl s_client** 是一个用于测试和调试连接的 TLS/SSL 客户端。它建立 SSL/TLS 连接并显示证书和连接信息。

连接建立后，你可以输入协议命令（HTTP、SMTP 等）。

# EXAMPLE

```bash
# Test HTTPS
openssl s_client -connect example.com:443 <<< "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n"
```

# CAVEATS

默认进入交互模式；脚本中请使用 `<<<` 或 EOF。缺少 CAfile 时证书验证可能失败。

# HISTORY

s_client 自 OpenSSL 早期版本起就是其组成部分，是 SSL/TLS 测试与调试的必备工具。

# INSTALL

```apt: sudo apt install openssl```

```dnf: sudo dnf install openssl```

```pacman: sudo pacman -S openssl```

```apk: sudo apk add openssl```

```zypper: sudo zypper install openssl```

```brew: brew install openssl```

```nix: nix profile install nixpkgs#openssl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openssl-verify](/man/openssl-verify)(1), [curl](/man/curl)(1)
