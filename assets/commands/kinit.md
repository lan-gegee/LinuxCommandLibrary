# TAGLINE

从密钥分发中心获取 Kerberos 票据

# TLDR

**获取 Kerberos 票据**

```kinit [username]```

**为特定主体获取票据**

```kinit [username@REALM]```

**指定 keytab 文件**

```kinit -k -t [keytab.file] [principal]```

**获取可转发票据**

```kinit -f [username]```

**设置票据有效期**

```kinit -l [1h] [username]```

**续订现有票据**

```kinit -R```

# SYNOPSIS

**kinit** [_options_] [_principal_]

# DESCRIPTION

**kinit** 从密钥分发中心（KDC）获取 Kerberos 票据。票据授予票据（TGT）让你无需反复输入密码即可向受 Kerberos 保护的服务进行身份验证。

该工具在企业环境中进行 Kerberos 认证时必不可少，可用于访问 NFS、SSH 和 Active Directory 等服务。

# PARAMETERS

**-k**
> 使用 keytab 文件。

**-t** _keytab_
> keytab 文件路径。

**-l** _lifetime_
> 票据有效期。

**-r** _lifetime_
> 可续订期限。

**-f**
> 获取可转发票据。

**-F**
> 获取不可转发票据。

**-p**
> 获取可代理票据。

**-R**
> 续订现有票据。

**-c** _cache_
> 凭据缓存。

**-S** _service_
> 服务主体。

# CAVEATS

需要能访问 KDC。票据会过期，需要续订。keytab 需妥善保护。要求时钟同步。

# HISTORY

**kinit** 是 **MIT Kerberos** 和 **Heimdal** 实现的组成部分。Kerberos 于 **20 世纪 80 年代**在 **MIT** 作为 Athena 计划的一部分开发，得名于希腊神话中守护冥界的三头犬。

# INSTALL

```apk: sudo apk add heimdal```

```zypper: sudo zypper install kinit```

```brew: brew install heimdal```

```nix: nix profile install nixpkgs#heimdal```

<!-- packages: 2026-07-22 -->

# SEE ALSO
