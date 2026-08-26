# TAGLINE

为 BloodHound 分析收集 Active Directory 数据

# TLDR

**收集所有 Active Directory 数据**

```bloodhound-python -d [domain.local] -u [username] -p [password] -ns [dc_ip] -c all```

**收集特定数据**（逗号分隔的方法）

```bloodhound-python -d [domain.local] -u [username] -p [password] -c [Group,LocalAdmin,Session]```

**使用 NTLM 哈希**进行身份验证

```bloodhound-python -d [domain.local] -u [username] --hashes [LM:NT] -ns [dc_ip] -c all```

**输出到 zip 文件**

```bloodhound-python -d [domain.local] -u [username] -p [password] -c all --zip```

**使用 Kerberos 身份验证**

```bloodhound-python -d [domain.local] -u [username] -p [password] -k -c all```

**指定 DNS 服务器**

```bloodhound-python -d [domain.local] -u [username] -p [password] -ns [dns_server] -c all```

**针对 BloodHound CE 收集**（使用 CE 版采集器）

```bloodhound-ce-python -d [domain.local] -u [username] -p [password] -ns [dc_ip] -c all --zip```

# SYNOPSIS

**bloodhound-python** [_options_]

# DESCRIPTION

**bloodhound-python** 是 BloodHound（一款 Active Directory 安全分析工具）的 Python 采集器。它收集 AD 对象（用户、计算机、组）及其关系的信息，输出 JSON 文件以导入 BloodHound 图数据库。

该工具利用图论识别 Active Directory 环境中难以人工发现的攻击路径，帮助攻击者和防御者理解域安全态势。

# PARAMETERS

**-d, --domain** _domain_
> 目标 Active Directory 域

**-u, --username** _user_
> 用于身份验证的用户名

**-p, --password** _pass_
> 用于身份验证的密码

**--hashes** _LMHASH:NTHASH_
> 用于哈希传递（pass-the-hash）身份验证的 NTLM 哈希。LM 部分可以留空

**--auth-method** _auto|ntlm|kerberos_
> 使用的身份验证方法（默认：auto）

**-aesKey** _hexkey_
> 用于 Kerberos 身份验证的 AES 密钥（128 或 256 位）

**-no-pass**
> 不提示输入密码（配合 -k 和 ccache 使用；单独使用则为空会话）

**-ns, --nameserver** _ip_
> 要查询的 DNS 服务器，通常是目标域中的域控制器

**-dc** _host_
> 覆盖要查询的域控制器主机名（默认：通过 DNS 检测）

**-gc** _host_
> 覆盖要查询的全局编录（Global Catalog）主机名

**-c, --collectionmethod** _method_
> 逗号分隔的收集方法：Default、Group、LocalAdmin、RDP、DCOM、PSRemote、Session、LoggedOn、Trusts、ACL、Container、ObjectProps、DCOnly、All

**-k, --kerberos**
> 使用 Kerberos 身份验证。从 ccache 文件获取凭证（KRB5CCNAME 环境变量）

**--zip**
> 将 JSON 输出压缩为单个 zip 文件

**-o, --outputdir** _dir_
> JSON 文件的输出目录

**-w** _workers_
> 计算机枚举工作线程数（默认：10）

**--dns-tcp**
> DNS 查询使用 TCP 而非 UDP

**--use-ldaps**
> 连接时使用基于 TLS 的 LDAP（端口 636）

**-v**
> 启用详细输出

# CAVEATS

需要有效的域凭证。某些收集方法（如 Session 和 LoggedOn）需要目标主机上的本地管理员权限。**bloodhound-python** 命令（旧版采集器）面向 BloodHound 4.2 和 4.3，而单独的 **bloodhound-ce-python** 命令产出适用于 BloodHound Community Edition 的数据。不要混用旧版与 CE 版采集器的输出。请负责任地使用，仅在你获得授权的系统上进行测试。

# HISTORY

BloodHound 由 **SpecterOps** 的 **@_wald0**、**@CptJesus** 和 **@harmj0y** 创建，于 **2016 年**发布。Python 采集器（bloodhound-python）由 **Dirk-jan Mollema** 开发，作为 C# SharpHound 采集器的跨平台替代方案。

# INSTALL

```nix: nix profile install nixpkgs#bloodhound```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ldapsearch](/man/ldapsearch)(1), [impacket](/man/impacket)(1), [netexec](/man/netexec)(1), [crackmapexec](/man/crackmapexec)(1)

# RESOURCES

```[Source code](https://github.com/dirkjanm/BloodHound.py)```

```[Homepage](https://bloodhound.specterops.io/)```

<!-- verified: 2026-06-19 -->
