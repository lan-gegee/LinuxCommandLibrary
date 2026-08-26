# TAGLINE

用于处理网络协议的 Python 类集合

# TLDR

**使用密码获取 TGT**

```impacket-getTGT [domain/user:password]```

**远程命令执行**

```impacket-psexec [domain/user:password@target]```

**WMI 执行**

```impacket-wmiexec [domain/user:password@target]```

**SMB 执行**

```impacket-smbexec [domain/user:password@target]```

**导出机密**

```impacket-secretsdump [domain/user:password@target]```

**AS-REP roasting**

```impacket-GetNPUsers [domain/] -usersfile [users.txt] -no-pass```

# SYNOPSIS

**impacket-**_tool_ [_options_] [_target_]

# DESCRIPTION

**Impacket** 是一组用于处理网络协议的 Python 类。它包含大量渗透测试工具，对 Windows 网络攻击和评估尤其有用。

该工具包实现了 Windows 环境中常用的 SMB、MSRPC、Kerberos、LDAP 等协议。

# COMMON TOOLS

```
psexec         Remote command execution via SMB
wmiexec        Remote execution via WMI
smbexec        Remote execution via SMB
secretsdump    Dump SAM/NTDS secrets
getTGT         Get Kerberos TGT
GetNPUsers     AS-REP roasting
GetUserSPNs   Kerberoasting
ntlmrelayx     NTLM relay attacks
```

# AUTHENTICATION FORMATS

```
domain/user:password
domain/user:LMhash:NThash
domain/user@target -k (Kerberos)
```

# CAVEATS

仅限用于经授权的测试。可能触发安全告警。需要 Python。部分工具需要对目标拥有本地管理员权限。Windows Defender 可能检出这些工具。

# HISTORY

Impacket 由 **SecureAuth** 创建（现为 Delinea 的一部分）。它在针对 Windows 网络的渗透测试和红队行动中被广泛使用。

# INSTALL

```pacman: sudo pacman -S impacket```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[crackmapexec](/man/crackmapexec)(1)
