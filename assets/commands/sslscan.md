# TAGLINE

测试 SSL/TLS 服务器配置与密码套件

# TLDR

**扫描服务器的 SSL/TLS 配置**

```sslscan [example.com]```

**扫描指定端口**

```sslscan [example.com:8443]```

**仅显示支持的密码套件**

```sslscan --no-ciphersuites [example.com]```

**显示证书详情**

```sslscan --show-certificate [example.com]```

**无彩色输出**

```sslscan --no-colour [example.com]```

**使用 STARTTLS**

```sslscan --starttls-smtp [mail.example.com:25]```

**XML 输出**

```sslscan --xml=[output.xml] [example.com]```

**检查所有协议版本**

```sslscan --tlsall [example.com]```

# SYNOPSIS

**sslscan** [_--show-certificate_] [_--starttls-protocol_] [_--xml file_] [_options_] _host_[:_port_]

# PARAMETERS

**--show-certificate**
> 显示证书详情。

**--no-ciphersuites**
> 跳过密码套件列表。

**--no-colour**
> 禁用彩色输出。

**--xml** _FILE_
> XML 输出。

**--starttls-smtp**
> 为 SMTP 使用 STARTTLS。

**--starttls-imap**
> 为 IMAP 使用 STARTTLS。

**--starttls-pop3**
> 为 POP3 使用 STARTTLS。

**--starttls-ftp**
> 为 FTP 使用 STARTTLS。

**--ssl2**, **--ssl3**, **--tls10**, **--tls11**, **--tls12**, **--tls13**
> 测试特定协议版本。

**--tlsall**
> 测试所有 TLS 版本。

**--no-fallback**
> 不进行版本回退。

**--sni** _HOST_
> SNI 主机名。

**--bugs**
> 启用 SSL 兼容性变通方案。

# DESCRIPTION

**sslscan** 用于测试 SSL/TLS 服务的配置问题。它能识别支持的密码套件、协议以及证书问题。

扫描结果显示启用了哪些 TLS 版本。旧式协议（SSLv2、SSLv3、TLS 1.0、TLS 1.1）是安全隐患。

密码套件测试会暴露弱算法。出口级（Export-grade）、NULL 和 RC4 密码会被标记出来。颜色编码可突出显示问题。

证书检查能发现过期、链和信任问题。它可以识别自签名、过期或配置错误的证书。

STARTTLS 支持使邮件服务器及其他将连接升级为 TLS 的服务也能被测试。

扫描结果有助于改进服务器配置。可将结果与安全标准和最佳实践进行对照。

# CAVEATS

需要对目标的网络访问权限。某些服务器会对扫描限速。结果取决于客户端能力。无法测试客户端证书。

# HISTORY

**sslscan** 最初由 **Ian Ventura-Whiting** 于 **2007 年**前后编写。后来由 **rbsec** fork 并积极维护，以支持现代 TLS 特性和协议。

# INSTALL

```apt: sudo apt install sslscan```

```dnf: sudo dnf install sslscan```

```pacman: sudo pacman -S sslscan```

```apk: sudo apk add sslscan```

```zypper: sudo zypper install sslscan```

```brew: brew install sslscan```

```nix: nix profile install nixpkgs#sslscan```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nmap](/man/nmap)(1), [openssl](/man/openssl)(1), [testssl](/man/testssl)(1), [sslyze](/man/sslyze)(1)
