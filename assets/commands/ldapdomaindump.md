# TAGLINE

通过 LDAP 提取 Active Directory 信息，包括用户信息

# TLDR

使用**凭据**导出域信息

```ldapdomaindump -u domain\username -p password [hostname]```

导出时进行**主机名解析**

```ldapdomaindump -r -u domain\username -p password [hostname]```

使用**自定义 DNS 服务器**导出

```ldapdomaindump -r -n [dns_ip] -u domain\username -p password [hostname]```

导出到**特定目录**且不生成 JSON

```ldapdomaindump --no-json -o [path/to/dir] -u domain\username -p password [hostname]```

# SYNOPSIS

**ldapdomaindump** [_options_] **-u** _domain_\\_user_ **-p** _password_ _hostname_

# DESCRIPTION

**ldapdomaindump** 通过 LDAP 提取 Active Directory 信息，包括用户、计算机、组、操作系统和组成员关系。输出以 HTML、JSON 和可 grep 的格式生成，便于分析。

# PARAMETERS

**-u, --user DOMAIN\USER**
> 用于 LDAP 认证的域用户名

**-p, --password PASSWORD**
> 用于认证的密码或 NTLM 哈希

**-r, --resolve**
> 通过 DNS 解析计算机主机名

**-n, --dns-server IP**
> 用于主机名解析的 DNS 服务器

**-o, --outdir PATH**
> 导出文件的输出目录

**--no-json**
> 跳过生成 JSON 输出

**--no-html**
> 跳过生成 HTML 输出

**--no-grep**
> 跳过生成可 grep 的输出

# CAVEATS

需要有效的域凭据。仅用于经授权的安全评估和渗透测试。

# INSTALL

```nix: nix profile install nixpkgs#ldapdomaindump```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ldapsearch](/man/ldapsearch)(1), [bloodhound](/man/bloodhound)(1)
