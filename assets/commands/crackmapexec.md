# TAGLINE

针对 Windows/AD 网络的后期渗透利用工具

# TLDR

**枚举 SMB 共享**

```crackmapexec smb [192.168.1.0/24] -u [user] -p [password] --shares```

**在主机上验证凭据**

```crackmapexec smb [hosts.txt] -u [user] -p [password]```

**执行命令**

```crackmapexec smb [target] -u [user] -p [password] -x "[whoami]"```

**转储 SAM 哈希**

```crackmapexec smb [target] -u [admin] -p [password] --sam```

**哈希传递攻击**

```crackmapexec smb [target] -u [user] -H [ntlm_hash]```

**枚举用户**

```crackmapexec smb [target] -u [user] -p [password] --users```

# SYNOPSIS

**crackmapexec** _protocol_ _target_ [_options_]

# DESCRIPTION

**crackmapexec**（CME）是一款面向 Windows/Active Directory 环境渗透测试的后期渗透利用工具。它可以自动完成常见任务，例如跨多台主机进行凭据验证、共享枚举和命令执行。

该工具支持 SMB、WinRM、LDAP、MSSQL 和 SSH 协议。专为经授权的安全评估和红队行动而设计。

# PARAMETERS

**-u** _user_
> 用于身份验证的用户名。

**-p** _password_
> 用于身份验证的密码。

**-H** _hash_
> 用于哈希传递的 NTLM 哈希。

**-d** _domain_
> 域名称。

**-x** _command_
> 执行命令。

**-X** _command_
> 执行 PowerShell 命令。

**--shares**
> 枚举 SMB 共享。

**--users**
> 枚举域用户。

**--sam**
> 转储 SAM 数据库。

**--lsa**
> 转储 LSA 机密。

**--local-auth**
> 使用本地身份验证。

**-M** _module_
> 运行指定模块。

# CAVEATS

仅限经授权的渗透测试。可能触发安全告警。需要有效的凭据或哈希。部分功能需要管理员权限。网络策略可能会阻止访问。

**已弃用**：上游项目已停止发布更新；名为 **NetExec**（`nxc`）的社区分支是仍在积极维护的后继者，可直接替代。

# HISTORY

**crackmapexec** 由 **byt3bl33d3r**（Marcello Salvati）于 **2015 年**前后创建。它源于对一款统一的 Windows 网络渗透测试工具的需求。该项目在安全社区中被广泛使用，并持续得到积极维护。

# SEE ALSO

[impacket](/man/impacket)(1), [nmap](/man/nmap)(1), [enum4linux](/man/enum4linux)(1)
