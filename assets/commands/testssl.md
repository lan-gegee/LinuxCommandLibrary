# TAGLINE

测试 TLS/SSL 服务器配置

# TLDR

**测试服务器**

```testssl [example.com]```

**测试指定端口**

```testssl [example.com:8443]```

**快速测试**

```testssl --fast [example.com]```

**显示所有密码套件**

```testssl -E [example.com]```

**仅检查漏洞**

```testssl -U [example.com]```

**HTML 输出**

```testssl --html [example.com]```

**JSON 输出**

```testssl --jsonfile [output.json] [example.com]```

**安静模式**

```testssl --quiet [example.com]```

# SYNOPSIS

**testssl** [_-E_] [_-U_] [_--fast_] [_--html_] [_--jsonfile file_] [_options_] _target_

# PARAMETERS

**-E**, **--each-cipher**
> 测试每个密码套件。

**-e**, **--cipher-per-proto**
> 按协议列出密码套件。

**-U**, **--vulnerable**
> 漏洞检查。

**-S**, **--server-defaults**
> 服务器默认设置。

**-P**, **--protocols**
> 协议支持情况。

**-H**, **--headers**
> HTTP 头部。

**--fast**
> 快速检查。

**--html**
> HTML 输出。

**--jsonfile** _FILE_
> JSON 输出。

**--csvfile** _FILE_
> CSV 输出。

**--quiet**
> 极简输出。

**--color** _N_
> 颜色模式（0-3）。

**--connect-timeout** _SEC_
> 连接超时。

**--openssl** _PATH_
> 自定义 OpenSSL 路径。

# DESCRIPTION

**testssl** 检查服务器上的 TLS/SSL 加密。它能识别漏洞、弱密码套件和配置问题。

协议测试显示启用了哪些 TLS 版本。旧协议（SSLv3、TLS 1.0、TLS 1.1）存在安全风险。

漏洞扫描检查 BEAST、POODLE、Heartbleed、ROBOT 及其他已知攻击。

密码套件分析可发现弱加密。导出级密码套件、NULL 加密和 RC4 都会被标记出来。

证书检查显示有效期、证书链和信任问题。它能识别即将过期、自签名或配置错误的证书。

该工具是一个依赖 OpenSSL 的 bash 脚本。它可以在任何类 Unix 系统上直接使用，无需安装。

# CAVEATS

彻底的扫描需要时间。某些检查可能触发 IDS。部分测试结果取决于 OpenSSL 版本。并非所有漏洞都能远程检测到。

# HISTORY

**testssl.sh** 由 **Dirk Wetter** 从 **2012** 年前后开始开发。它无需复杂的部署即可提供全面的 TLS 测试，已成为安全评估的标准工具。

# INSTALL

```dnf: sudo dnf install testssl```

```brew: brew install testssl```

```nix: nix profile install nixpkgs#testssl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sslscan](/man/sslscan)(1), [nmap](/man/nmap)(1), [openssl](/man/openssl)(1), [sslyze](/man/sslyze)(1)
