# TAGLINE

在 Red Hat 系发行版上配置系统认证

# TLDR

显示**当前**配置

```authconfig --test```

更改**密码**算法

```authconfig --update --passalgo=sha512```

启用 **LDAP** 认证

```authconfig --update --enableldapauth```

禁用 **LDAP** 认证

```authconfig --update --disableldapauth```

启用 **NIS**

```authconfig --update --enablenis```

启用 **Kerberos**

```authconfig --update --enablekrb5```

启用 **Winbind**（Active Directory）

```authconfig --update --enablewinbindauth```

启用 **SSSD** 进行身份查询和认证

```authconfig --update --enablesssd --enablesssdauth```

首次登录时**创建家目录**

```authconfig --update --enablemkhomedir```

保存一份**命名的配置文件备份**

```authconfig --savebackup=[name]```

# SYNOPSIS

**authconfig** [_OPTIONS_]

# DESCRIPTION

**authconfig** 用于在 Red Hat 系 Linux 发行版上配置系统认证资源。它管理 PAM 栈配置、nsswitch.conf 设置以及相关认证文件，用于启用或禁用 LDAP、NIS、Kerberos、Winbind 和本地认证等机制。

该工具通过修改系统文件，将集中式身份提供方与本地认证栈集成。先用 **--test** 查看当前配置，再用 **--update** 应用更改。

# PARAMETERS

**--test**
> 显示当前配置但不做更改

**--update**
> 应用配置变更

**--passalgo** _algorithm_
> 设置密码哈希算法（sha256、sha512）

**--probe**
> 通过 DNS 探测网络默认值并打印出来，不修改任何内容

**--enableldap**
> 使用 LDAP 查询用户信息（修改 nsswitch.conf）

**--enableldapauth**
> 使用 LDAP 进行认证（修改 PAM 栈）

**--disableldapauth**
> 禁用 LDAP 认证

**--enablesssd**
> 使用 SSSD 查询用户信息

**--enablesssdauth**
> 使用 SSSD 进行认证

**--enablenis**
> 启用网络信息服务（NIS）

**--enablekrb5**
> 启用 Kerberos 5 认证

**--enablewinbindauth**
> 启用 Winbind（Active Directory）认证

**--enablelocauthorize**
> 启用本地授权

**--enablemkhomedir**
> 首次登录时自动创建用户家目录

**--enableshadow**
> 启用影子密码文件

**--savebackup** _name_
> 为 authconfig 修改的文件保存一份命名备份

**--restorebackup** _name_
> 恢复之前保存的命名备份

**--restorelastbackup**
> 恢复上次更改前自动生成的备份

# CONFIGURATION

**/etc/sysconfig/authconfig**
> 以键值对形式存储当前的 authconfig 设置。

**/etc/pam.d/**
> PAM 配置目录，authconfig 会修改它以启用认证模块。

**/etc/nsswitch.conf**
> 名称服务切换配置，会随身份来源的变化而更新。

# CAVEATS

此工具仅适用于 Red Hat 系发行版（RHEL、CentOS、Fedora）。自 RHEL 8 和 Fedora 28 起，它已被 **authselect** 取代，并从 Fedora 35 开始彻底移除。在这些系统上请改用 **authselect**。更改需要 root 权限，且必须运行 **--update** 才能持久生效。

# HISTORY

**authconfig** 多年来一直是 Red Hat Enterprise Linux 及相关发行版的标准认证配置工具。它后来被 **authselect** 取代，后者使用预定义的配置档（profile）来管理 PAM 栈和 nsswitch.conf。等效命令参见 authselect-migration(7) 手册页。

# INSTALL

```aur: yay -S authconfig```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[authselect](/man/authselect)(8), [pam](/man/pam)(8)
