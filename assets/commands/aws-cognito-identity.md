# TAGLINE

管理用于访问 AWS 资源的联合身份池。

# TLDR

**列出当前区域的身份池**

```aws cognito-identity list-identity-pools --max-results [20]```

**创建新的身份池**

```aws cognito-identity create-identity-pool --identity-pool-name [pool_name] --allow-unauthenticated-identities```

**按 ID 查看身份池详情**

```aws cognito-identity describe-identity-pool --identity-pool-id [region:pool-id]```

**为未认证访问获取身份 ID**

```aws cognito-identity get-id --identity-pool-id [region:pool-id]```

**为身份获取临时 AWS 凭据**

```aws cognito-identity get-credentials-for-identity --identity-id [region:identity-id]```

**删除身份池**

```aws cognito-identity delete-identity-pool --identity-pool-id [region:pool-id]```

**将登录提供方关联到现有身份**

```aws cognito-identity get-id --identity-pool-id [region:pool-id] --logins [provider]=[token]```

# SYNOPSIS

**aws cognito-identity** _subcommand_ [_options_]

# DESCRIPTION

**aws cognito-identity** 是 AWS CLI 的子命令，用于管理 Amazon Cognito 身份池（联合身份）。它为通过 Amazon、Facebook、Google、SAML 或 Cognito 用户池等身份提供方认证的用户颁发临时 AWS 凭据。

身份池将用户身份映射到 IAM 角色，使移动应用和 Web 应用能够安全地访问 AWS 服务。每个身份池可同时支持已认证和未认证（访客）访问，并赋予不同的 IAM 权限。

该服务签发唯一的身份 ID，并通过 STS 服务发放临时 AWS 凭据，从而实现细粒度的访问控制，无需在应用程序中嵌入长期凭据。

# PARAMETERS

**list-identity-pools**
> 列出账户的所有身份池。

**create-identity-pool**
> 按指定设置创建新的身份池。

**describe-identity-pool**
> 获取身份池的详细信息。

**update-identity-pool**
> 修改身份池配置。

**delete-identity-pool**
> 删除身份池。

**delete-identities**
> 删除之前合并或关联的身份。

**describe-identity**
> 获取特定身份的详细信息，包括其外部 ID。

**get-id**
> 获取或创建用户的身份 ID。

**get-credentials-for-identity**
> 为身份获取临时 AWS 凭据。

**get-identity-pool-roles**
> 获取为身份池配置的角色。

**set-identity-pool-roles**
> 设置身份池的角色。

**get-open-id-token**
> 为身份获取 OpenID 令牌。

**get-open-id-token-for-developer-identity**
> 为开发者认证的身份获取令牌。

**list-identities**
> 列出特定身份池中的身份。

**lookup-developer-identity**
> 检索与开发者身份关联的身份 ID。

**tag-resource**
> 为身份池分配标签。

**untag-resource**
> 移除身份池上的标签。

**--identity-pool-id** _id_
> 身份池 ID（格式：region:uuid）。

**--identity-pool-name** _name_
> 身份池的名称。

**--allow-unauthenticated-identities**
> 启用无需认证的访客访问。

**--no-allow-unauthenticated-identities**
> 禁用访客访问。

**--logins** _map_
> 用于认证的提供方名称到令牌的映射。

**--max-results** _number_
> 返回结果的最大数量。

# CAVEATS

身份池 ID 带有区域前缀（例如 us-east-1:xxxxxxxx）。凭据默认 1 小时后过期。需要为已认证和未认证访问分别配置 IAM 角色。不要把 Cognito 身份池与 Cognito 用户池混淆，后者直接处理用户注册和登录。

# HISTORY

Amazon Cognito Identity 在 **AWS re:Invent 2014** 上发布，并于 **2014 年 7 月** 作为移动服务套件的一部分推出，旨在简化移动应用程序对 AWS 资源的安全访问。该服务后续陆续支持了更多身份提供方、SAML 联合以及面向开发者认证身份的增强流程。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-cognito-idp](/man/aws-cognito-idp)(1), [aws-sts](/man/aws-sts)(1), [aws-iam](/man/aws-iam)(1)
