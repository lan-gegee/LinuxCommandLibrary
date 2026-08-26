# TAGLINE

通过 LDAP 枚举 Active Directory 用户账户

# TLDR

**枚举所有域用户**及其详细信息

```impacket-getadusers -all '[domain]/[user]:[password]'```

指定域控制器 IP **查询用户**

```impacket-getadusers -all -dc-ip [192.168.1.100] '[domain]/[user]:[password]'```

使用 **NTLM 哈希**身份验证获取用户

```impacket-getadusers -all -hashes ':[nthash]' '[domain]/[user]'```

通过 **Kerberos** 身份验证枚举用户

```impacket-getadusers -all -k -no-pass '[domain]/[user]'```

以特定格式**输出用户信息**

```impacket-getadusers -all -dc-ip [192.168.1.100] '[domain]/[user]:[password]' 2>/dev/null```

# SYNOPSIS

**impacket-getadusers** [_-h_] [_-user USERNAME_] [_-all_] [_-dc-ip IP_] [_-dc-host HOSTNAME_] [_-hashes LMHASH:NTHASH_] [_-no-pass_] [_-k_] [_-aesKey KEY_] _target_

# PARAMETERS

**-all**
> 返回域中的所有用户

**-user** _USERNAME_
> 仅查询特定用户的信息

**-dc-ip** _IP_
> 域控制器的 IP 地址

**-dc-host** _HOSTNAME_
> 域控制器的主机名（用于 Kerberos）

**-hashes** _LMHASH:NTHASH_
> 使用 NTLM 哈希而非密码进行身份验证

**-no-pass**
> 不询问密码（与 -k 或 -hashes 搭配时有用）

**-k**
> 使用 ccache 文件中的 Kerberos 身份验证

**-aesKey** _KEY_
> 用于 Kerberos 身份验证的 AES 密钥

# DESCRIPTION

**impacket-getadusers** 通过 LDAP 查询 Active Directory 来枚举用户账户及其属性。它检索诸如用户名、上次登录时间、密码上次设置日期和账户状态标志等信息。

该工具在渗透测试侦察阶段很有用，可用于识别潜在目标、发现长期未改密码的账户或找出服务账户。输出包括 SAM 账户名、badPwdCount 及其他相关安全属性。

# CAVEATS

需要有效的域凭据。输出可能非常冗长；建议将 stderr 重定向到 /dev/null 以获得更整洁的输出。要查看已认证用户以外的结果，通常必须使用 -all 选项。

# HISTORY

属于 SecureAuth 开发的 **Impacket** 库。该工具利用针对 Active Directory 的 LDAP 查询，用 Python 实现微软的目录服务协议，以实现跨平台兼容。

# INSTALL

```pacman: sudo pacman -S impacket```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[impacket-addcomputer](/man/impacket-addcomputer)(1), [impacket-secretsdump](/man/impacket-secretsdump)(1), [ldapsearch](/man/ldapsearch)(1), [net](/man/net)(1)
