# TAGLINE

收集并分析 SSL/TLS 证书信息

# TLDR

**检查主机的 SSL 证书**

```ssl_checker -H [github.com:443]```

**以 JSON 格式输出证书信息**

```ssl_checker -H [example.com] -j```

**分析主机的安全漏洞**

```ssl_checker -H [example.com] -a```

# SYNOPSIS

**ssl_checker** [**-H** _host_ [_host_...]] [**-f** _file_] [_options_]

# PARAMETERS

**-H** _HOST_
> 要检查的主机，格式为 host:port，可指定多个。

**-f** _FILE_
> 包含待检查主机名的文件。

**-j**
> 以 JSON 格式输出结果。

**-a**
> 分析主机的安全漏洞。

**-c**
> 以 CSV 格式输出结果。

**-S**
> 仅输出摘要。

**-x**
> 将结果导出为 HTML 文件。

**-J**
> 按主机分别导出 JSON。

**-v**
> 启用详细输出以便排查问题。

**-t** _TIMEOUT_
> 连接超时时间（秒）。

**-s** _HOST:PORT_
> 使用 SOCKS 代理进行连接。

# DESCRIPTION

**ssl-checker** 是一个从主机收集 SSL/TLS 信息的 Python 脚本。它可以检查证书过期日期、颁发者详情和密码套件。它支持安全漏洞分析、SOCKS 代理连接，并能以 JSON、CSV 或 HTML 格式导出结果。

# HISTORY

**ssl-checker** 由 **narbehaj** 创建，使用 **Python** 编写。

# INSTALL

```aur: yay -S ssl-checker```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openssl](/man/openssl)(1), [testssl](/man/testssl)(1)
