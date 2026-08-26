# TAGLINE

用于 Active Directory 枚举的 NetExec LDAP 模块

# TLDR

**通过 LDAP 身份验证**

```nxc ldap [target] -u [user] -p [password]```

**使用 NTLM 哈希进行身份验证**

```nxc ldap [target] -u [user] -H [hash]```

**枚举用户**

```nxc ldap [target] -u [user] -p [password] --users```

**枚举组**

```nxc ldap [target] -u [user] -p [password] --groups```

**Kerberoasting 攻击**

```nxc ldap [target] -u [user] -p [password] --kerberoasting [output.txt]```

**AS-REP roasting 攻击**

```nxc ldap [target] -u [user] -p [password] --asreproast [output.txt]```

**运行自定义 LDAP 查询**

```nxc ldap [target] -u [user] -p [password] --query "([sAMAccountName=*])" --base-dn "[DC=domain,DC=com]"```

**收集 BloodHound 数据**

```nxc ldap [target] -u [user] -p [password] --bloodhound -c All --dns-server [dc_ip]```

# SYNOPSIS

**nxc** **ldap** _target_ [_options_]

# PARAMETERS

_TARGET_
> 域控制器的 IP 或主机名。

**-u** _USER_
> 用于身份验证的用户名。

**-p** _PASSWORD_
> 用于身份验证的密码。

**-H** _HASH_
> 用于哈希传递（pass-the-hash）身份验证的 NTLM 哈希。

**-k**
> 使用 Kerberos 身份验证。

**--use-kcache**
> 使用 Kerberos 凭据缓存。

**-d** _DOMAIN_
> 要进行身份验证的域。

**--port** _PORT_
> LDAP 端口（默认：389）。

**--users**
> 枚举域用户。

**--active-users**
> 枚举活跃（未禁用）的域用户。

**--groups**
> 枚举域组。

**--computers**
> 枚举域计算机。

**--dc-list**
> 列出域控制器。

**--get-sid**
> 获取域 SID。

**--pass-pol**
> 获取密码策略。

**--gmsa**
> 枚举组托管服务账户。

**--kerberoasting** _FILE_
> 执行 Kerberoasting 并将哈希保存到文件。

**--asreproast** _FILE_
> 执行 AS-REP roasting 并将哈希保存到文件。

**--trusted-for-delegation**
> 查找被信任用于委派的账户。

**--password-not-required**
> 查找不要求密码的账户。

**--admin-count**
> 查找 adminCount=1 的账户。

**--bloodhound**
> 为 BloodHound 收集数据。

**--query** _FILTER_
> 自定义 LDAP 查询过滤器。

**--base-dn** _DN_
> LDAP 查询的 Base DN。

**-M** _MODULE_
> 运行特定的 LDAP 模块。

**--continue-on-success**
> 认证成功后继续尝试（密码喷洒）。

# DESCRIPTION

**nxc ldap** 是 NetExec（前身为 CrackMapExec）的 LDAP 协议模块。它通过 LDAP 协议对域控制器执行 Active Directory 枚举和攻击。

该模块支持通过密码、NTLM 哈希和 Kerberos 票据进行身份验证。它可以枚举用户、组、计算机、策略和委派设置，还可以执行 Kerberoasting 和 AS-REP roasting 攻击。

# CAVEATS

安全/渗透测试工具。仅限授权使用。大多数操作需要有效凭据或哈希。部分功能需要特定的 AD 权限级别。

# HISTORY

NetExec（nxc）是 **CrackMapExec**（cme）的后继者，在原项目归档后由社区维护。LDAP 模块通过 LDAP 协议提供 Active Directory 枚举功能。

# SEE ALSO

[nxc](/man/nxc)(1), [nxc-smb](/man/nxc-smb)(1), [nxc-winrm](/man/nxc-winrm)(1), [ldapsearch](/man/ldapsearch)(1), [bloodhound](/man/bloodhound)(1)
