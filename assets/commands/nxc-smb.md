# TAGLINE

执行 SMB 协议操作以进行安全测试

# TLDR

**对整个子网喷洒凭据**

```nxc smb [192.168.1.0/24] -u [user] -p [password]```

**枚举共享及访问级别**

```nxc smb [target] -u [user] -p [password] --shares```

**通过 SAMR 枚举域用户**

```nxc smb [target] -u [user] -p [password] --users```

**对本地 SAM 进行身份验证**（而非域）

```nxc smb [target] -u [user] -p [password] --local-auth```

**执行 cmd.exe 命令**

```nxc smb [target] -u [admin] -p [password] -x [whoami]```

**执行 PowerShell 命令**

```nxc smb [target] -u [admin] -p [password] -X "[Get-Process]"```

**哈希传递**（NTLM）

```nxc smb [target] -u [user] -H [NTLM_hash]```

**转储 SAM 哈希**

```nxc smb [target] -u [admin] -p [password] --sam```

**运行 NetExec 模块**

```nxc smb [target] -u [admin] -p [password] -M [spider_plus]```

# SYNOPSIS

**nxc smb** _target_ [_options_]

# PARAMETERS

**-u** _USER_
> 用户名或用户名文件（加 **@** 前缀表示从文件读取）。

**-p** _PASS_
> 密码或密码文件。

**-H** _HASH_
> NTLM 哈希（LM:NT 或仅 NT）。

**-d**, **--domain** _DOMAIN_
> 对给定域进行身份验证。

**--local-auth**
> 本地身份验证（使用本机的 SAM，跳过域查找）。

**-x** _CMD_
> 通过 **cmd.exe** 执行 _CMD_。

**-X** _CMD_
> 通过 **PowerShell** 执行 _CMD_。

**--exec-method** _METHOD_
> 远程执行技术：**wmiexec**、**atexec** 或 **smbexec**。

**--shares**
> 枚举 SMB 共享以及当前用户对各共享的权限。

**--users**
> 通过 SAMR 枚举域用户。

**--groups**
> 枚举本地组或域组。

**--sessions**
> 列出目标上活动的 SMB 会话。

**--loggedon-users**
> 列出当前登录到目标的用户。

**--pass-pol**
> 获取生效的密码策略。

**--sam**
> 转储本地 SAM 哈希数据库（需要管理员权限）。

**--lsa**
> 转储缓存的 LSA 秘密。

**-M**, **--module** _NAME_
> 运行 NetExec 模块（完整列表见 **nxc smb -L**）。

# DESCRIPTION

**nxc smb** 执行用于安全测试的 SMB 协议操作。它是 **NetExec**（社区维护的 **CrackMapExec** 后继者）的一部分。它可以枚举共享、用户、会话、组和密码策略；跨整个子网验证凭据；还能通过 WMI、计划任务或命名管道远程执行命令。

# CAVEATS

仅限授权的安全评估用途。使用前需获得适当授权。

# SEE ALSO

[nxc](/man/nxc)(1), [smbclient](/man/smbclient)(1)
