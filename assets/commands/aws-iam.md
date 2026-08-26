# TAGLINE

管理 AWS 资源的身份、访问和权限。

# TLDR

**创建新的 IAM 用户**

```aws iam create-user --user-name [my-user]```

**为用户创建访问密钥**

```aws iam create-access-key --user-name [my-user]```

**为用户附加策略**

```aws iam attach-user-policy --user-name [my-user] --policy-arn [arn:aws:iam::aws:policy/ReadOnlyAccess]```

**创建带信任策略的角色**

```aws iam create-role --role-name [my-role] --assume-role-policy-document file://[trust-policy.json]```

**列出账户中的所有用户**

```aws iam list-users```

**创建组并添加用户**

```aws iam create-group --group-name [developers] && aws iam add-user-to-group --user-name [my-user] --group-name [developers]```

**生成凭据报告**

```aws iam generate-credential-report && aws iam get-credential-report --output text --query Content | base64 -d```

# SYNOPSIS

**aws iam** _command_ [_options_]

# DESCRIPTION

**aws iam** 是 AWS Identity and Access Management（IAM）的 AWS CLI 接口。IAM 是控制 AWS 资源访问的服务，支持创建用户、组、角色和策略来管理认证与授权。

IAM 是全局性服务（不区分区域），通过 JSON 策略提供细粒度的访问控制。它支持与 SAML 2.0 和 OIDC 提供方进行身份联合，并支持多因素认证以增强安全性。

# COMMANDS

**create-user**
> 创建新的 IAM 用户

**delete-user**
> 删除用户

**create-access-key**
> 生成访问密钥凭据

**create-role**
> 创建用于服务或跨账户访问的角色

**attach-user-policy**
> 向用户附加托管策略

**attach-role-policy**
> 向角色附加托管策略

**create-policy**
> 创建自定义托管策略

**create-group**
> 创建用户组

**add-user-to-group**
> 将用户添加到组

**list-users**
> 列出所有 IAM 用户

**get-user**
> 获取用户详情

**simulate-principal-policy**
> 测试策略权限

# CAVEATS

策略更改可能需要数秒才能传播生效。切勿将根账户用于日常操作。访问密钥应定期轮换。每个账户的 IAM 用户数量上限为 5000。内联策略比托管策略更难审计。

# HISTORY

AWS IAM 于 **2010 年 5 月** 作为 AWS 的访问控制系统推出。角色于 **2012 年** 引入，用于跨账户和服务访问。策略条件多年来大幅扩展；用于集中化访问管理的 IAM Identity Center（前身为 SSO）于 **2017 年** 加入。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-sts](/man/aws-sts)(1), [aws-organizations](/man/aws-organizations)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/iam/index.html)```

<!-- verified: 2026-06-18 -->
