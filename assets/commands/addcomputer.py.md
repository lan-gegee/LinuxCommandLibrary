# TAGLINE

在 Active Directory 中创建机器账户

# TLDR

**向 Active Directory 添加**计算机

```addcomputer.py [domain]/[user]:[password] -computer-name [hostname]```

指定**域控制器** IP

```addcomputer.py [domain]/[user]:[password] -dc-ip [192.168.1.1] -computer-name [hostname]```

使用**哈希传递**（pass-the-hash）认证

```addcomputer.py [domain]/[user] -hashes :[NTHASH] -computer-name [hostname]```

用 LDAP 方法以**指定密码**添加计算机

```addcomputer.py [domain]/[user]:[password] -computer-name [hostname] -computer-pass [password] -method LDAPS```

# SYNOPSIS

**addcomputer.py** _domain_/_user_:_password_ -computer-name _name_ [_options_]

# DESCRIPTION

**addcomputer.py**（也称为 add-computer.py）是一个 Impacket 脚本，用于在 Active Directory 中创建机器账户。它利用了 AD 的默认权限——允许任何已认证用户向域添加计算机账户。

在渗透测试中，这一能力可用于搭建基于资源的约束委派攻击，或在域内获取更多立足点。

# PARAMETERS

**-dc-ip** _ip_
> 域控制器的 IP 地址

**-computer-name** _name_
> 要创建的计算机账户的名称

**-computer-pass** _password_
> 计算机账户的密码

**-method** _SAMR|LDAPS_
> 添加计算机所用的协议（默认：SAMR）

**-hashes** _LMHASH:NTHASH_
> 使用 NT 哈希进行身份验证

**-k**, **--kerberos**
> 使用 Kerberos 身份验证

**-no-pass**
> 不提示输入密码

**-dc-host** _hostname_
> 域控制器的主机名

# CAVEATS

仅可用于经授权的安全测试。默认值为 10 的 ms-DS-MachineAccountQuota 可由管理员修改或设为 0。以这种方式创建的计算机账户对域管理员可见。

# HISTORY

该工具属于 SecureAuth 维护的 Impacket 套件。**2018** 年之后，随着基于资源的约束委派攻击被更广泛地理解，它在安全测试领域声名鹊起。

# INSTALL

```apk: sudo apk add py3-impacket```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[add-computer.py](/man/add-computer.py)(1), [impacket-getnpusers](/man/impacket-getnpusers)(1)
