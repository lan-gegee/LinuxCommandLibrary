# TAGLINE

netExec，一款网络服务漏洞利用工具

# TLDR

**SMB 身份验证检查**

```nxc smb [target] -u [user] -p [password]```

**枚举共享**

```nxc smb [target] -u [user] -p [password] --shares```

**执行命令**

```nxc smb [target] -u [user] -p [password] -x "[command]"```

**扫描多台主机**

```nxc smb [targets.txt] -u [user] -p [password]```

**使用哈希进行身份验证**

```nxc smb [target] -u [user] -H [hash]```

# SYNOPSIS

**nxc** [_protocol_] [_target_] [_options_]

# PARAMETERS

_PROTOCOL_
> 协议模块（smb、ssh、ldap 等）。

_TARGET_
> 目标主机或文件。

**-u** _USER_
> 用户名。

**-p** _PASSWORD_
> 密码。

**-H** _HASH_
> 用于哈希传递的 NT 哈希。

**--shares**
> 枚举共享。

**-x** _COMMAND_
> 执行命令。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nxc**（NetExec）是一款网络服务漏洞利用工具，可帮助自动化评估大型网络的安全性。它是 CrackMapExec 的社区维护后继者，后者最初创建于 2015 年。

该工具支持多种协议，包括 SMB、SSH、LDAP、WinRM、MSSQL、RDP、FTP 等。它支持跨网络进行凭据测试、共享枚举、命令执行和 Active Directory 操作。身份验证结果以颜色标记：绿色表示成功，红色表示失败，品红色表示凭据有效但被拒绝。

# CAVEATS

仅限授权渗透测试使用的安全工具。需要 Python，通常通过 pipx 安装。CrackMapExec 的后继者。

# HISTORY

NetExec 作为 **CrackMapExec 的后继者**被创建，用于网络渗透测试；在原项目归档后开始由社区维护。

# SEE ALSO

[nmap](/man/nmap)(1), [crackmapexec](/man/crackmapexec)(1), [hydra](/man/hydra)(1), [impacket](/man/impacket)(1), [metasploit](/man/metasploit)(1)
