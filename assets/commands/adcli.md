# TAGLINE

Active Directory 域客户端工具

# TLDR

**加入**域

```sudo adcli join [domain.com]```

使用**指定凭据**加入

```sudo adcli join -U [administrator] [domain.com]```

**查看**域信息

```adcli info [domain.com]```

**测试**与域控制器的连接

```adcli testjoin```

# SYNOPSIS

**adcli** _command_ [_options_] [_domain_]

# DESCRIPTION

**adcli** 是一个命令行工具，用于对 Active Directory 域执行操作。它可以将 Linux 机器加入 AD 域、管理计算机账户、查询域信息，并且无需依赖 Samba。

该工具使用标准的 Kerberos 和 LDAP 协议与域控制器通信，因此非常轻量，适合自动化部署场景。

# PARAMETERS

**join**
> 将本地机器加入域

**preset-computer**
> 在域中预创建计算机账户

**reset-computer**
> 重置计算机账户密码

**delete-computer**
> 从域中删除计算机账户

**update**
> 更新机器账户属性

**testjoin**
> 测试机器是否已加入域

**info**
> 显示发现的有关某个域或域控制器的信息

**-U** _user_, **--login-user** _user_
> 创建计算机账户时用于身份验证的用户账户

**-D** _domain_, **--domain** _domain_
> 要连接的域

**-R** _realm_, **--domain-realm** _realm_
> 域的 Kerberos realm（当其与域名不同时指定）

**-S** _server_, **--domain-server** _server_
> 连接到指定的域控制器

**-O** _ou_, **--domain-ou** _ou_
> 计算机账户所在组织单元（OU）的可分辨名称

**-N** _name_, **--computer-name** _name_
> 计算机账户的短名称（sAMAccountName）

**-H** _fqdn_, **--host-fqdn** _fqdn_
> 覆盖本地机器的完全限定域名

**--stdin-password**
> 从标准输入读取密码而不是交互式提示

**-v**, **--verbose**
> 输出详细的调试级进度信息

# CAVEATS

需要在 AD 中具备创建计算机账户的相应权限。防火墙规则必须放行 LDAP（389）和 Kerberos（88）流量。要实现完整的 AD 集成，可结合 SSSD 进行用户认证。**adcli** 通常由 **realm**（realmd）间接调用，由后者调用它来执行实际的加域操作。

# HISTORY

**adcli** 由 Red Hat 的 Stef Walter 开发，首次发布于 **2012** 年前后。它的诞生是为 AD 加域提供一个轻量级的 Samba 替代方案，适用于现代 Linux 企业部署。

# INSTALL

```apt: sudo apt install adcli```

```dnf: sudo dnf install adcli```

```aur: yay -S adcli```

```zypper: sudo zypper install adcli```

```nix: nix profile install nixpkgs#adcli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[kinit](/man/kinit)(1), [net](/man/net)(8)

# RESOURCES

```[Source code](https://gitlab.freedesktop.org/realmd/adcli)```

```[Documentation](https://www.freedesktop.org/software/realmd/adcli/adcli.html)```

<!-- verified: 2026-06-11 -->
