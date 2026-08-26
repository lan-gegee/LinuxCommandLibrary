# TAGLINE

通过 Impacket 在 Active Directory 中添加或删除计算机账户

# TLDR

使用默认凭据向域**添加计算机账户**

```impacket-addcomputer -computer-name '[NEWPC$]' -computer-pass '[Password123]' '[domain]/[user]:[password]'```

指定域控制器 IP **添加计算机账户**

```impacket-addcomputer -computer-name '[NEWPC$]' -dc-ip [192.168.1.100] '[domain]/[user]:[password]'```

使用 LDAPS（安全连接）**添加计算机**

```impacket-addcomputer -computer-name '[NEWPC$]' -use-ldaps '[domain]/[user]:[password]'```

使用带票据的 Kerberos 身份验证**添加计算机**

```impacket-addcomputer -computer-name '[NEWPC$]' -k -no-pass '[domain]/[user]'```

使用 LDAPS 方法**添加计算机**

```impacket-addcomputer -computer-name '[NEWPC$]' -method LDAPS '[domain]/[user]:[password]'```

从域中**删除计算机账户**

```impacket-addcomputer -computer-name '[TARGETPC$]' -delete '[domain]/[user]:[password]'```

# SYNOPSIS

**impacket-addcomputer** [_-h_] [_-computer-name NAME_] [_-computer-pass PASSWORD_] [_-no-add_] [_-delete_] [_-method {SAMR,LDAPS}_] [_-port {139,445,636}_] [_-baseDN DC=x,DC=y_] [_-computer-group GROUP_] [_-domain-netbios NETBIOSNAME_] [_-dc-ip IP_] [_-dc-host HOSTNAME_] [_-use-ldaps_] [_-hashes LMHASH:NTHASH_] [_-no-pass_] [_-k_] [_-aesKey KEY_] _target_

# PARAMETERS

**-computer-name** _NAME_
> 要添加的计算机账户名（应以 $ 结尾）

**-computer-pass** _PASSWORD_
> 新计算机账户的密码

**-delete**
> 删除指定的计算机账户而不是添加

**-no-add**
> 不添加计算机，仅设置其密码（要求账户已存在）

**-dc-ip** _IP_
> 域控制器的 IP 地址

**-dc-host** _HOSTNAME_
> 域控制器的主机名

**-use-ldaps**
> 使用 LDAPS 代替 LDAP

**-hashes** _LMHASH:NTHASH_
> 使用 NTLM 哈希而非密码进行身份验证

**-no-pass**
> 不询问密码（与 -k 搭配时有用）

**-k**
> 使用 ccache 文件中的 Kerberos 身份验证

**-aesKey** _KEY_
> 用于 Kerberos 身份验证的 AES 密钥

**-method** _{SAMR,LDAPS}_
> 添加计算机账户的方法（默认：SAMR）

**-port** _{139,445,636}_
> 目标端口（SAMR 默认为 445，LDAPS 为 636）

**-baseDN** _DN_
> LDAP 基准专有名称（省略时从域名推导）

**-computer-group** _GROUP_
> 要将计算机加入的组的 LDAP 路径（例如 CN=Computers,DC=test,DC=local）

**-domain-netbios** _NETBIOSNAME_
> 域的 NetBIOS 名称（当域控制器上有多个域时必需）

**-ts**
> 在输出中添加时间戳

**-debug**
> 启用调试输出

# DESCRIPTION

**impacket-addcomputer** 是 Impacket 库中的一个工具，用于在 Active Directory 域中添加或删除计算机账户。默认情况下，域用户最多可以添加 10 个计算机账户（由 ms-DS-MachineAccountQuota 属性控制），因此该工具在渗透测试场景中很有用。

该工具通过 LDAP 或 SAMR 协议与域控制器通信来创建机器账户。创建的计算机账户随后可用于多种攻击技术，包括基于资源的约束委派攻击。

# CAVEATS

需要具有创建计算机账户权限的有效域凭据。在加固环境中，ms-DS-MachineAccountQuota 默认值可能被设为 0。计算机名应遵循 NetBIOS 命名规范，通常以美元符号（$）结尾。

# HISTORY

Impacket 由 **SecureAuth**（前身为 Core Security）创建，是一组用于处理网络协议的 Python 类。addcomputer 脚本的加入是为了支持 Active Directory 渗透测试工作流，尤其是在 **2018-2019 年**前后基于资源的约束委派攻击研究兴起之后。

# INSTALL

```pacman: sudo pacman -S impacket```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[impacket-getadusers](/man/impacket-getadusers)(1), [impacket-secretsdump](/man/impacket-secretsdump)(1), [impacket-psexec](/man/impacket-psexec)(1), [ldapsearch](/man/ldapsearch)(1), [net](/man/net)(1)
