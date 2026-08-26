# TAGLINE

请求 Kerberos 服务票据并保存为 ccache

# TLDR

为特定 SPN **请求服务票据**

```impacket-getst -spn '[cifs/target.domain.com]' '[domain]/[user]:[password]'```

使用 NTLM 哈希**请求服务票据**

```impacket-getst -spn '[cifs/target.domain.com]' -hashes ':[nthash]' '[domain]/[user]'```

通过 S4U2Self 和 S4U2Proxy **模拟用户**（委派攻击）

```impacket-getst -spn '[cifs/target.domain.com]' -impersonate '[administrator]' '[domain]/[user]:[password]'```

使用 ccache 中的 Kerberos 身份验证**请求服务票据**

```impacket-getst -spn '[cifs/target.domain.com]' -k -no-pass '[domain]/[user]'```

使用 AES 密钥**请求服务票据**

```impacket-getst -spn '[cifs/target.domain.com]' -aesKey '[aes256key]' '[domain]/[user]'```

**请求 User-to-User 票据**

```impacket-getst -u2u -spn '[cifs/target.domain.com]' '[domain]/[user]:[password]'```

# SYNOPSIS

**impacket-getst** [_-spn SPN_] [_-impersonate USER_] [_-altservice SPN_] [_-additional-ticket FILE_] [_-hashes LMHASH:NTHASH_] [_-aesKey KEY_] [_-k_] [_-no-pass_] [_-dc-ip IP_] _identity_

# PARAMETERS

**-spn** _SPN_
> 目标服务的服务主体名称（service/server）。

**-altservice** _SPN_
> 在生成的票据中设置新的 sname/SPN。

**-impersonate** _USER_
> 要通过 S4U2Self 模拟的目标用户名。需要委派权限。

**-additional-ticket** _FILE_
> 在 S4U2Proxy 请求中包含一张可转发的服务票据，用于 RBCD + KCD。

**-dmsa**
> 使用 Delegated Managed Service Accounts。

**-u2u**
> 请求 User-to-User 票据。

**-self**
> 仅执行 S4U2Self，跳过 S4U2Proxy。

**-force-forwardable**
> 强制将 S4U2Self 服务票据设为可转发。

**-renew**
> 续订用于身份验证的 TGT。

**-ts**
> 为每条日志输出添加时间戳。

**-debug**
> 开启 DEBUG 输出。

**-hashes** _LMHASH:NTHASH_
> 使用 NTLM 哈希而非密码进行身份验证。

**-no-pass**
> 不询问密码（与 -k 搭配时有用）。

**-k**
> 使用 ccache 文件（KRB5CCNAME）中的 Kerberos 身份验证。

**-aesKey** _KEY_
> 用于 Kerberos 身份验证的 AES 密钥（128 或 256 位）。

**-dc-ip** _IP_
> 域控制器的 IP 地址。

# DESCRIPTION

**impacket-getst** 从 Active Directory 域控制器请求 Kerberos 服务票据（ST），并将其保存为 ccache 文件。它支持标准票据请求、用于用户模拟的 S4U2Self/S4U2Proxy 委派攻击，以及 User-to-User 身份验证。

该工具常用于渗透测试中的 Kerberos 委派滥用（约束委派、基于资源的约束委派）：拥有委派权限的攻击者可以模拟任意用户访问目标服务。生成的 ccache 文件可通过 **KRB5CCNAME** 环境变量供其他工具使用。

# CAVEATS

需要有效的 TGT 或凭据。通过 S4U2Self/S4U2Proxy 进行模拟要求身份账户在 Active Directory 中配置了委派权限。客户端与 KDC 的时间同步误差必须在 5 分钟以内。**-force-forwardable** 选项利用了 CVE-2020-17049（Bronze Bit），在已修补的域控制器上可能无效。

# HISTORY

属于 **SecureAuth**（现为 **Fortra**）的 **Impacket** 库。S4U 扩展（S4U2Self 和 S4U2Proxy）最初由微软为约束委派场景设计。安全研究人员发现这些机制可被滥用于权限提升，使 getST 成为基于 Kerberos 的攻击链中的关键工具。

# INSTALL

```pacman: sudo pacman -S impacket```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[impacket-gettgt](/man/impacket-gettgt)(1), [impacket-getuserspns](/man/impacket-getuserspns)(1), [impacket-secretsdump](/man/impacket-secretsdump)(1)
