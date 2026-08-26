# TAGLINE

面向 Windows/Active Directory 环境的网络安全工具

# TLDR

**枚举 SMB 共享**

```netexec smb [192.168.1.0/24] -u [user] -p [password] --shares```

**验证凭据**

```netexec smb [target] -u [user] -p [password]```

**执行命令**

```netexec smb [target] -u [admin] -p [password] -x "[whoami]"```

**哈希传递攻击**

```netexec smb [target] -u [user] -H [hash]```

**枚举用户**

```netexec smb [target] -u [user] -p [password] --users```

**喷洒密码**

```netexec smb [target] -u [users.txt] -p [password]```

**WinRM 访问**

```netexec winrm [target] -u [user] -p [password]```

**LDAP 枚举**

```netexec ldap [target] -u [user] -p [password] --users```

# SYNOPSIS

**netexec** _protocol_ _target_ [_-u user_] [_-p pass_] [_-H hash_] [_options_]

# PARAMETERS

**smb**
> SMB 协议。

**winrm**
> WinRM 协议。

**ldap**
> LDAP 协议。

**ssh**
> SSH 协议。

**mssql**
> MSSQL 协议。

**ftp**
> FTP 协议。

**rdp**
> RDP 协议。

**wmi**
> WMI 协议。

**vnc**
> VNC 协议。

**nfs**
> NFS 协议。

**-u** _USER_
> 用户名或文件。

**-p** _PASS_
> 密码或文件。

**-H** _HASH_
> NTLM 哈希。

**-d** _DOMAIN_
> 域名。

**-x** _CMD_
> 执行命令。

**-X** _PS_CMD_
> 执行 PowerShell。

**--shares**
> 枚举共享。

**--users**
> 枚举用户。

**--groups**
> 枚举组。

**--local-auth**
> 使用本地身份验证。

**--sam**
> 转储 SAM 数据库。

**--lsa**
> 转储 LSA 机密。

**-t** _THREADS_
> 并发线程数量（默认：100）。

**--timeout** _SECONDS_
> 连接的最大超时时间（秒）。

**--jitter** _INTERVAL_
> 连接之间的随机延迟。

**--verbose**
> 启用详细输出。

**--debug**
> 启用调试级别的信息输出。

# DESCRIPTION

**netexec**（前身为 CrackMapExec）是一款面向 Windows/Active Directory 环境的网络安全工具。它可以在网络中测试凭据、枚举资源并执行命令。

支持多种协议：SMB、WinRM、LDAP、SSH、MSSQL、FTP、RDP、WMI、VNC 和 NFS。每种协议都有特定的枚举和利用模块。

凭据测试用于在多个目标上验证用户名和密码。哈希传递（Pass-the-hash）直接使用 NTLM 哈希。密码喷洒则用一个密码尝试多个账户。

共享枚举可以揭示可访问的网络共享。用户和组的枚举可绘制出 Active Directory 结构。这些功能为安全评估提供侦察信息。

命令执行需要相应的权限。结果会跨所有目标收集以便分析。

该工具专为授权的渗透测试和安全评估设计。

# CAVEATS

仅在获得授权的情况下使用。可能触发安全告警。某些功能需要管理员权限。大规模扫描可能导致账户锁定。

# HISTORY

**NetExec** 是 **CrackMapExec**（CME）的后继者，由 **byt3bl33d3r** 于 **2015 年**前后创建。在 CrackMapExec 开发放缓后，NetExec 于 **2023 年**分叉该项目以继续维护和开发。

# INSTALL

```nix: nix profile install nixpkgs#netexec```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[smbclient](/man/smbclient)(1), [rpcclient](/man/rpcclient)(1), [ldapsearch](/man/ldapsearch)(1), [nmap](/man/nmap)(1)
