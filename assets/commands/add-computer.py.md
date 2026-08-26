# TAGLINE

向 Active Directory 域添加计算机账户

# TLDR

**向 Active Directory 添加**计算机账户

```add-computer.py [domain]/[user]:[password] -computer-name [hostname]```

以**指定属性**添加

```add-computer.py [domain]/[user]:[password] -computer-name [hostname] -computer-pass [password]```

使用 **Kerberos** 身份验证

```add-computer.py -k [domain]/[user] -computer-name [hostname]```

# SYNOPSIS

**add-computer.py** [_-dc-ip ip_] _domain_/_user_:_password_ -computer-name _name_ [_options_]

# DESCRIPTION

**add-computer.py** 是一个 Impacket 工具，用于向 Active Directory 域添加计算机账户。它利用了 AD 的默认配置——允许已认证用户最多向域添加 10 个计算机账户。

在渗透测试中，它常被用于基于资源的约束委派攻击，因为掌控一台计算机账户能在 AD 环境内提供额外的攻击面。

# PARAMETERS

**-dc-ip** _ip_
> 域控制器的 IP 地址

**-computer-name** _name_
> 新计算机账户的名称

**-computer-pass** _password_
> 计算机账户的密码（未指定时自动生成）

**-method** _method_
> 添加计算机所用的方法：SAMR 或 LDAPS（默认 SAMR）。

**-dc-host** _hostname_
> 域控制器主机名（FQDN）。若省略，则从 domain 参数推导。

**-baseDN** _dn_
> LDAP 中的可分辨名称基址。若省略，则从域名推导。

**-domain-netbios** _name_
> 当林中包含多个域时使用的域 NetBIOS 名称。

**-no-add**
> 仅修改现有计算机账户的密码，不新增账户。

**-k**
> 使用 Kerberos 身份验证（需要 KRB5CCNAME ccache）。

**-no-pass**
> 不提示输入密码（与 -k 配合使用）。

**-hashes** _LMHASH:NTHASH_
> 使用 NTLM 哈希进行哈希传递（pass-the-hash）认证。

**-aesKey** _key_
> 用于 Kerberos 密钥传递（pass-the-key）认证的 AES128 或 AES256 十六进制密钥。

**-debug**
> 启用详细调试输出。

# CAVEATS

此工具仅可用于经授权的渗透测试。默认情况下，AD 允许用户创建至多 10 个计算机账户（ms-DS-MachineAccountQuota）。管理员可以修改这一限额。

# HISTORY

**add-computer.py** 是 Impacket 库的一部分，由 SecureAuth（前身为 Core Security）开发。Impacket 作为一组面向网络协议的 Python 类集合，自 **2000** 年代初起持续活跃开发。

# SEE ALSO

[impacket](/man/impacket)(1), [adcli](/man/adcli)(8), [addcomputer.py](/man/addcomputer.py)(1)
