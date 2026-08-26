# TAGLINE

面向 WinRM 的渗透测试 Shell

# TLDR

**连接目标**

```evil-winrm -i [target_ip] -u [username] -p [password]```

**使用哈希连接**

```evil-winrm -i [target_ip] -u [username] -H [NTLM_hash]```

**使用 SSL**

```evil-winrm -i [target_ip] -u [user] -p [pass] -S```

**上传文件**

```upload [local_file] [remote_path]```

**下载文件**

```download [remote_file] [local_path]```

从目录**加载 PowerShell** 脚本

```evil-winrm -i [ip] -u [user] -p [pass] -s [scripts/]```

使用 SSL 和自定义**端口**连接

```evil-winrm -i [target_ip] -u [user] -p [pass] -S -P [5986]```

**使用 Kerberos** 认证连接

```evil-winrm -i [target_ip] -u [user] -p [pass] -r [DOMAIN.LOCAL]```

**使用基于证书的**认证连接

```evil-winrm -i [target_ip] -c [cert.pem] -k [key.pem] -S```

# SYNOPSIS

**evil-winrm** [_options_]

# PARAMETERS

**-i** _IP_
> 目标 IP 地址。

**-u** _USER_
> 用户名。

**-p** _PASSWORD_
> 密码。

**-H** _HASH_
> 用于哈希传递攻击的 NTLM 哈希。

**-S**, **--ssl**
> 启用 SSL 加密连接。

**-c** _PATH_, **--pub-key** _PATH_
> 公钥证书的本地路径。

**-k** _PATH_, **--priv-key** _PATH_
> 私钥证书的本地路径。

**-s** _PATH_, **--scripts** _PATH_
> PowerShell 脚本的本地路径。

**-e** _PATH_, **--executables** _PATH_
> C# 可执行文件的本地路径。

**-P** _PORT_, **--port** _PORT_
> 远程主机端口（默认 5985）。

**-U** _URL_, **--url** _URL_
> 远程 URL 端点（默认 /wsman）。

**-r** _DOMAIN_, **--realm** _DOMAIN_
> Kerberos 认证的 realm/域。

**--spn** _PREFIX_
> Kerberos 认证的 SPN 前缀（默认 HTTP）。

**-l**, **--log**
> 记录 WinRM 会话日志。

**-n**, **--no-colors**
> 禁用彩色输出。

**-N**, **--no-rpath-completion**
> 禁用远程路径补全。

**-a** _USERAGENT_, **--user-agent** _USERAGENT_
> 指定连接使用的 user-agent（默认 Microsoft WinRM Client）。

**-V**, **--version**
> 显示版本。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**Evil-WinRM** 是一个针对 Windows 远程管理（WinRM）的渗透测试 Shell。它提供一个交互式 PowerShell 会话，并带有面向渗透测试活动的额外功能。

该工具支持哈希传递认证、Kerberos 认证、基于证书的认证、文件上传下载，以及加载自定义 PowerShell 脚本和 C# 可执行程序。它专为红队行动和授权的安全测试而设计。

Shell 内可用的内建命令包括用于传输文件的 **upload** 和 **download**、在内存中执行 C# 程序集的 **Invoke-Binary**，以及加载 DLL 的 **Dll-Loader**。**menu** 命令会列出所有可用的内建命令。

# CAVEATS

仅在获得明确授权时使用。目标上必须启用 WinRM（HTTP 使用端口 5985，HTTPS 使用端口 5986）。可能触发安全告警和终端检测。某些 PowerShell 脚本可能需要绕过 AMSI。Kerberos 认证需要正确配置 /etc/krb5.conf。

# HISTORY

Evil-WinRM 由 **Hackplayers** 面向安全研究社区创建，为渗透测试提供了一个功能丰富的新式 WinRM 工具替代方案。

# INSTALL

```nix: nix profile install nixpkgs#evil-winrm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[winrm](/man/winrm)(1), [impacket](/man/impacket)(1), [sshpass](/man/sshpass)(1)
