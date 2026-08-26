# TAGLINE

openDNSSEC 密钥管理组件

# TLDR

**初始化数据库**

```ods-enforcer-db-setup```

**添加区域**

```ods-enforcer zone add --zone [example.com]```

**列出区域**

```ods-enforcer zone list```

**查看密钥状态**

```ods-enforcer key list --zone [example.com]```

**强制密钥轮换**

```ods-enforcer key rollover --zone [example.com]```

**导出 DS 记录**

```ods-enforcer key ds --zone [example.com]```

# SYNOPSIS

**ods-enforcer** _command_ [_options_]

# PARAMETERS

**zone add**
> 将区域纳入管理。

**zone delete**
> 移除区域。

**zone list**
> 列出受管理的区域。

**key list**
> 显示密钥。

**key rollover**
> 发起密钥轮换。

**key ds**
> 导出 DS 记录。

**policy list**
> 列出签名策略。

# DESCRIPTION

**ods-enforcer** 是 OpenDNSSEC 的密钥管理组件。它根据配置的策略（KASP）管理 DNSSEC 密钥，处理密钥的生成、发布和轮换。

enforcer 与 signer 协同工作，维护 DNSSEC 签名。

# KASP POLICIES

```
Key Algorithm
Key Lifetime
Signature Validity
Rollover Timing
```

# KEY STATES

```
generate → publish → ready → active → retire → dead
```

# CAVEATS

需要 KASP 配置。必须先完成数据库初始化。与 ods-signer 配合使用。

# HISTORY

OpenDNSSEC enforcer 依据 **IETF** RFC 中的 DNSSEC 最佳实践实现自动化密钥管理。

# SEE ALSO

[ods-control](/man/ods-control)(8)
