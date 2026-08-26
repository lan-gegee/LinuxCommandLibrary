# TAGLINE

快速的 TLS 证书与密码套件探测

# TLDR

**检查 TLS**

```tlsx -u [example.com]```

**显示证书**

```tlsx -u [example.com] -san -cn```

**多主机**

```tlsx -l [hosts.txt]```

**JSON 输出**

```tlsx -u [example.com] -json```

**检查特定端口**

```tlsx -u [example.com:8443]```

**显示密码套件**

```tlsx -u [example.com] -cipher```

# SYNOPSIS

**tlsx** [_-u host_] [_-l file_] [_-json_] [_options_]

# PARAMETERS

**-u** _HOST_
> 目标主机。

**-l** _FILE_
> 主机列表文件。

**-san**
> 显示主题备用名称。

**-cn**
> 显示公用名称。

**-cipher**
> 显示密码套件。

**-json**
> JSON 输出。

# DESCRIPTION

**tlsx** 是一个快速的 TLS 探测工具，它连接主机并检查其 TLS 配置、证书和支持的密码套件。它可以提取证书详情，包括主题名称、主题备用名称（SAN）、到期日期和颁发者信息。

该工具支持从文件列表并行扫描多个主机，因此适合大规模 TLS 侦察。输出可以格式化为 JSON，便于与其他安全工具集成。它是安全评估中常用的 ProjectDiscovery 工具集的一部分。

# CAVEATS

需要网络访问。某些主机可能会拦截。基于 Go 的工具。

# HISTORY

**tlsx** 由 **ProjectDiscovery** 创建，用于快速 TLS 探测和证书分析。

# INSTALL

```brew: brew install tlsx```

```nix: nix profile install nixpkgs#tlsx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openssl](/man/openssl)(1), [testssl](/man/testssl)(1), [sslyze](/man/sslyze)(1)
