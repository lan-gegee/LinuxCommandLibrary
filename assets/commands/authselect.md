# TAGLINE

通过配置档（profile）配置系统认证来源

# TLDR

**列出可用的配置档**

```authselect list```

**显示当前配置**

```authselect current```

**选择 SSSD 配置档**用于 LDAP/FreeIPA 认证

```sudo authselect select sssd --force```

**选择 SSSD 配置档**并启用指纹认证

```sudo authselect select sssd with-fingerprint --force```

**选择 Winbind 配置档**用于 Active Directory

```sudo authselect select winbind --force```

在当前配置档上**启用一个特性**

```sudo authselect enable-feature with-mkhomedir```

**备份当前配置**

```sudo authselect backup [backup-name]```

**从备份恢复**

```sudo authselect backup-restore [backup-name]```

# SYNOPSIS

**authselect** _command_ [_options_]

# PARAMETERS

**list**
> 列出可用的配置档

**show** _profile_
> 显示某个配置档的信息

**current**
> 显示当前选定的配置档和已启用的特性

**select** _profile_ [_features_]
> 激活一个配置档，可选附加特性

**enable-feature** _feature_
> 在当前配置档上启用某特性

**disable-feature** _feature_
> 在当前配置档上禁用某特性

**backup** [_name_]
> 备份当前的系统配置

**backup-restore** _name_
> 从备份恢复配置

**backup-list**
> 列出可用的备份

**opt-out**
> 取消 authselect 对配置的管理

**--force**
> 覆盖已有的非 authselect 配置

**-b**, **--backup**
> 在更改前创建备份

**-q**, **--quiet**
> 不输出提示消息

# PROFILES

**sssd**
> 系统安全服务守护进程（SSSD），用于 LDAP、FreeIPA、Active Directory

**winbind**
> Samba Winbind，用于直接集成 Active Directory

**nis**
> 旧式网络信息服务（NIS）兼容

**minimal**
> 仅本地用户和组（系统文件）

# COMMON FEATURES

**with-mkhomedir**
> 首次登录时自动创建家目录

**with-fingerprint**
> 启用指纹认证

**with-smartcard**
> 启用智能卡认证

**with-faillock**
> 启用多次失败后的账户锁定

**with-sudo**
> 启用 SSSD 作为 sudo 规则来源

# DESCRIPTION

**authselect** 通过预定义的配置档管理 PAM 栈和 nsswitch.conf 文件，从而配置系统认证来源。自 Fedora 28 和 RHEL 8 起，它取代了 **authconfig**。

配置档定义用户如何通过认证以及从何处获取身份信息。**sssd** 配置档在使用 LDAP、FreeIPA 或 Active Directory 的企业环境中最常见。**winbind** 配置档提供了集成 Active Directory 的另一种方式。

Authselect 只配置 PAM 和 nsswitch，不配置底层的守护进程（SSSD、Winbind）。请使用 **realm join** 或 **ipa-client-install** 之类工具来加入域，它们会自动完成 authselect 配置。

自定义配置档可通过复制并修改 **/etc/authselect/custom/** 中已有的配置档来创建。

# CONFIGURATION

**/etc/authselect/authselect.conf**
> 记录当前激活的配置档及已启用的特性。

**/etc/authselect/custom/**
> 存放用户自建配置档的目录。可将现有配置档复制到此目录再修改。

# CAVEATS

从手工配置的系统切换时必须使用 **--force**。不要改动由 **ipa-client-install** 或 **realm join** 配置好的 authselect 配置档。在 authselect 之外对 nsswitch.conf 或 PAM 文件所做的修改会在切换配置档时被覆盖。

# HISTORY

**authselect** 由 Red Hat 开发，于 **Fedora 28**（2018 年）作为 authconfig 的替代品推出。其设计目标是使用预定义配置档而非零散的选项开关，从而提供更简单、更易维护的认证配置方式。到 **Fedora 35** 时，authconfig 已被彻底移除，authselect 成为标准工具。

# INSTALL

```apt: sudo apt install authselect```

```dnf: sudo dnf install authselect```

```aur: yay -S authselect```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[pam](/man/pam)(8)
