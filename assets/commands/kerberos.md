# TAGLINE

网络身份验证协议

# TLDR

**获取票据**

```kinit [principal]```

**列出票据**

```klist```

**销毁票据**

```kdestroy```

**修改密码**

```kpasswd```

**获取可转发票据**

```kinit -f [principal]```

**续订票据**

```kinit -R```

# SYNOPSIS

Kerberos commands: **kinit**, **klist**, **kdestroy**, **kpasswd**

# PARAMETERS

**kinit** _PRINCIPAL_
> 获取 Kerberos 票据。

**klist**
> 列出缓存的票据。

**kdestroy**
> 销毁票据。

**kpasswd**
> 修改 Kerberos 密码。

**-f**
> 获取可转发票据。

**-R**
> 续订已有票据。

**-l** _LIFETIME_
> 票据有效期。

# DESCRIPTION

**Kerberos** 是一个网络身份验证协议。客户端出示凭据后会从密钥分发中心（KDC）获得有时限的票据授予票据（TGT），然后用 TGT 换取服务票据以访问各个网络服务。所有身份验证交换都是加密的，并且在初始 **kinit** 之后用户密码不再经过网络传输。

面向用户的 CLI 由四个小命令构成：**kinit**（请求 TGT）、**klist**（检查凭据缓存）、**kdestroy**（清除缓存的票据）和 **kpasswd**（修改 KDC 保存的密码）。服务票据由支持 Kerberos 的应用（SSH、NFSv4、经 SPNEGO 的 HTTP、LDAP、SMB）透明地获取。

# CONFIGURATION

**/etc/krb5.conf**
> 客户端配置：realm、KDC 地址、默认 principal、可转发标志、加密类型。

**/etc/krb5.keytab**（或 **$KRB5_KTNAME**）
> 服务端 keytab，包含守护进程 principal 的长期密钥。

**$KRB5CCNAME**
> 凭据缓存的路径或后端（如 **FILE:/tmp/krb5cc_$UID**、**KEYRING:persistent:$UID**、**KCM:**）。

# CAVEATS

客户端、KDC 和目标服务的时钟必须一致，偏差不能超过几分钟（默认偏斜：5 分钟）。DNS 正向和反向记录必须与 principal 名称匹配；反向 DNS 故障是 `KRB_AP_ERR_BAD_INTEGRITY` 和 `Server not found in Kerberos database` 错误最常见的原因。

# HISTORY

Kerberos 于 20 世纪 80 年代末在 **MIT** 作为 Project Athena 的一部分开发。**Kerberos v5**（RFC 4120）是现行标准；v4 已过时并被现代 Linux 发行版移除。目前广泛使用的两个可互操作实现是 **MIT Kerberos** 和 **Heimdal**。

# SEE ALSO

[kinit](/man/kinit)(1), [smbclient](/man/smbclient)(1), [ldapsearch](/man/ldapsearch)(1)
