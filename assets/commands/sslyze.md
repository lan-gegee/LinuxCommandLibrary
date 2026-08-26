# TAGLINE

快速而强大的 SSL/TLS 服务器扫描工具

# TLDR

**扫描服务器**的 SSL/TLS 配置

```sslyze [www.example.com]```

**扫描多台服务器**

```sslyze [www.example.com] [www.google.com]```

**测试特定的 SSL/TLS 版本**

```sslyze --sslv2 --sslv3 --tlsv1 --tlsv1_1 --tlsv1_2 --tlsv1_3 [server]```

**测试 Heartbleed 漏洞**

```sslyze --heartbleed [server]```

**测试所有漏洞**

```sslyze --heartbleed --robot --openssl_ccs --compression [server]```

**对照 Mozilla TLS 配置检查**

```sslyze --mozilla_config=[intermediate] [server]```

**为邮件服务器使用 STARTTLS**

```sslyze --starttls [smtp] [mail.example.com]```

**输出到 JSON**

```sslyze --json_out=[results.json] [server]```

# SYNOPSIS

**sslyze** [_options_] _target_ [_target_...]

# PARAMETERS

**--sslv2**, **--sslv3**
> 测试是否支持 SSL 2.0 或 SSL 3.0。

**--tlsv1**, **--tlsv1_1**, **--tlsv1_2**, **--tlsv1_3**
> 测试特定 TLS 版本的支持情况。

**--certinfo**
> 获取并分析服务器证书。

**--heartbleed**
> 测试 OpenSSL Heartbleed 漏洞。

**--robot**
> 测试 ROBOT 漏洞。

**--openssl_ccs**
> 测试 OpenSSL CCS 注入漏洞（CVE-2014-0224）。

**--compression**
> 测试 TLS 压缩支持（CRIME 攻击向量）。

**--reneg**
> 测试不安全的 TLS 重协商。

**--fallback**
> 测试 TLS_FALLBACK_SCSV 降级防护。

**--early_data**
> 测试 TLS 1.3 early data 支持。

**--starttls** _protocol_
> 使用 STARTTLS 握手。协议：auto、smtp、xmpp、pop3、imap、ftp、ldap、rdp、postgres。

**--sni** _hostname_
> 用于 TLS 1.0+ 的服务器名称指示（SNI）主机名。

**--mozilla_config** _level_
> 检查合规性：**old**、**intermediate** 或 **modern**。

**--json_out** _file_
> 将结果输出到 JSON 文件。

**--targets_in** _file_
> 从文件读取目标（每行一个）。

**--quiet**
> 抑制除错误外的输出。

# DESCRIPTION

**SSLyze** 是一款快速的 SSL/TLS 扫描工具，用于分析服务器配置以发现安全弱点。它测试协议支持、密码套件、证书有效性，以及 Heartbleed、ROBOT、CRIME 等已知漏洞。

该工具直接连接服务器并执行真实的协议握手来验证配置。它支持对升级到 TLS 的协议（SMTP、IMAP 等）使用 STARTTLS，并支持虚拟主机的服务器名称指示（SNI）。

SSLyze 可以对照 Mozilla 推荐的 TLS 设置检查配置，并对不符合要求的服务器返回非零退出码。这使其适合集成到 CI/CD 流水线中。

# CAVEATS

扫描不属于你的服务器可能被视为未经授权的测试。某些扫描可能触发受监控系统上的安全警报。该工具需要与目标服务器的网络连通性。漏洞测试只是某一时间点的评估；服务器变更后应重新测试。

# HISTORY

**SSLyze** 由 Alban Diquet（nabla-c0d3）创建并以开源形式发布。它已成为 TLS 安全评估的标准工具，被用于扫描数十万台服务器。该项目得到积极维护，支持新的 TLS 特性和漏洞检测。它以 GNU Affero 通用公共许可证（AGPL）分发。

# INSTALL

```aur: yay -S sslyze```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[testssl](/man/testssl)(1), [nmap](/man/nmap)(1), [openssl](/man/openssl)(1), [sslscan](/man/sslscan)(1)
