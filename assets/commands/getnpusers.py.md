# TAGLINE

用于域用户枚举的 AS-REP roasting 工具

# TLDR

**查询域中禁用 Kerberos 预身份验证的用户**（使用凭据）

```GetNPUsers.py [DOMAIN]/[username]:[password] -request -format hashcat -outputfile [hashes.txt]```

**检查来自文件的用户列表**（无需凭据）

```GetNPUsers.py [DOMAIN]/ -usersfile [users.txt] -format hashcat -outputfile [hashes.txt] -dc-ip [DC_IP]```

为特定用户**请求 TGT**（无需密码）

```GetNPUsers.py [DOMAIN]/[username] -no-pass -dc-ip [DC_IP]```

**使用 pass-the-hash** 认证

```GetNPUsers.py [DOMAIN]/[username] -hashes [LMhash]:[NThash] -request```

以 **John 格式输出**哈希以便破解

```GetNPUsers.py [DOMAIN]/[username]:[password] -request -format john```

# SYNOPSIS

**GetNPUsers.py** [_DOMAIN_]/[_USER_]:[_PASSWORD_] [_OPTIONS_]

**GetNPUsers.py** [_DOMAIN_]/ **-usersfile** _FILE_ [_OPTIONS_]

# PARAMETERS

**-request**
> 为发现的存在预身份验证已禁用的用户请求 TGT。

**-format** _FORMAT_
> 哈希的输出格式：hashcat 或 john。

**-outputfile** _FILE_
> 将 AS-REP 哈希写入指定文件。

**-usersfile** _FILE_
> 包含待检查用户名列表的文件。

**-dc-ip** _IP_
> 域控制器的 IP 地址。

**-no-pass**
> 使用空密码或不提供密码。

**-hashes** _LMHASH_:_NTHASH_
> 使用 NTLM 哈希进行 pass-the-hash 认证。

**-k**
> 使用 ccache 中的 Kerberos 认证（需设置 KRB5CCNAME）。

**-debug**
> 启用调试输出。

# DESCRIPTION

**GetNPUsers.py** 是一个 Impacket 工具，用于识别 Active Directory 中禁用了 Kerberos 预身份验证的用户并获取其 AS-REP（Authentication Service Response）加密数据。这些数据可以离线破解以恢复用户密码，这种攻击称为 **AS-REP Roasting**。

当用户被禁用预身份验证时，任何人都可以在不了解其密码的情况下代其请求 TGT。域控制器会返回用该用户密码哈希加密的数据，可以离线暴力破解。

该工具可以通过 LDAP 查询所有域用户（需要凭据），或从文件检查特定的用户名（如果已知用户名则不需要凭据）。

# CAVEATS

本工具仅限授权的安全测试、CTF 竞赛和防御性安全研究使用。未经授权对你不拥有或无权测试的系统使用属于违法行为。获取到的哈希需要用 hashcat（-m 18200）或 John the Ripper 之类的工具进行破解。

# HISTORY

GetNPUsers.py 是 **Impacket** 的一部分。Impacket 是一组用于处理网络协议的 Python 类库，由 SecureAuth（现为 Fortra）创建，广泛用于渗透测试和安全研究。在对 Kerberos 预身份验证弱点进行研究之后，AS-REP Roasting 成为一种广为人知的攻击技术。

# SEE ALSO

[hashcat](/man/hashcat)(1), [john](/man/john)(1)
