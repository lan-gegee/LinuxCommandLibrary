# TAGLINE

请求临时安全凭证并验证身份。

# TLDR

**获取**当前调用者的**身份**

```aws sts get-caller-identity```

**担任 IAM 角色**

```aws sts assume-role --role-arn [arn:aws:iam::account:role/role-name] --role-session-name [session-name]```

**获取临时会话凭证**

```aws sts get-session-token --duration-seconds [3600]```

配合 MFA **担任角色**

```aws sts assume-role --role-arn [arn:aws:iam::account:role/role-name] --role-session-name [session-name] --serial-number [arn:aws:iam::account:mfa/device] --token-code [123456]```

从访问密钥**获取账户 ID**

```aws sts get-access-key-info --access-key-id [AKIAIOSFODNN7EXAMPLE]```

**解码授权错误消息**

```aws sts decode-authorization-message --encoded-message [encoded-message]```

# SYNOPSIS

**aws sts** _subcommand_ [_options_]

# DESCRIPTION

**aws sts** 是 AWS CLI 中用于管理 AWS Security Token Service（STS）的接口。STS 可为 IAM 用户或联合身份用户请求临时的、权限受限的凭证。

STS 对于跨账户访问、身份联合以及实施最小权限安全至关重要。临时凭证包括访问密钥、秘密密钥和会话令牌，过期时间可配置。

# SUBCOMMANDS

**Identity**
> get-caller-identity, get-access-key-info

**Role Assumption**
> assume-role, assume-role-with-saml, assume-role-with-web-identity, assume-root

**Temporary Credentials**
> get-session-token, get-federation-token

**Federation**
> get-web-identity-token, get-delegated-access-token

**Troubleshooting**
> decode-authorization-message

# PARAMETERS

**--role-arn** _value_
> 要担任的角色的 ARN

**--role-session-name** _value_
> 担任角色会话的标识符

**--duration-seconds** _value_
> 临时凭证的有效时长（900-43200 秒）

**--serial-number** _value_
> 用于 MFA 保护操作的 MFA 设备 ARN

**--token-code** _value_
> MFA 设备提供的验证码

**--external-id** _value_
> 跨账户访问的唯一标识符

# CAVEATS

担任角色的临时凭证最长有效期为 12 小时（默认 1 小时）。受 MFA 保护的角色担任需要同时提供 **--serial-number** 和 **--token-code**。链式角色担任（从已担任的角色再担任另一角色）最长有效期只有 1 小时。

# HISTORY

自 IAM 于 **2011 年 5 月**推出起，AWS STS 即已可用，为 AWS 服务提供临时安全凭证。它此后扩展出 Web 身份联合、SAML 2.0 以及多种角色担任场景的支持。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-iam](/man/aws-iam)(1), [aws-sso](/man/aws-sso)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/sts/index.html)```

<!-- verified: 2026-06-18 -->
