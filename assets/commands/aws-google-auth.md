# TAGLINE

通过 Google Workspace SSO 获取 AWS 凭据

# TLDR

**使用 Google SSO 认证并获取 AWS 凭据**

```aws-google-auth```

**使用指定配置文件认证**

```aws-google-auth -p [profile-name]```

**显式指定 Google IDP 和 SP ID 进行认证**

```aws-google-auth -I [google-idp-id] -S [google-sp-id] -u [user@domain.com]```

**认证并担任特定角色**

```aws-google-auth -R [arn:aws:iam::account:role/role-name]```

**以秒为单位设置凭据有效期**

```aws-google-auth -d [3600]```

**通过环境变量认证**

```GOOGLE_USERNAME=[user@domain.com] GOOGLE_IDP_ID=[abc123] GOOGLE_SP_ID=[xyz789] aws-google-auth```

# SYNOPSIS

**aws-google-auth** [**-h**] [**-u** _username_] [**-I** _idp-id_] [**-S** _sp-id_] [**-R** _role-arn_] [**-d** _duration_] [**-p** _profile_]

# DESCRIPTION

**aws-google-auth** 是一款命令行工具，它以 Google Workspace（前身为 G Suite）作为联合 SAML 身份提供方，获取 AWS 临时（STS）凭据，实现从 Google 账户到 AWS 的单点登录（SSO）。

该工具向 Google 完成认证后获取 SAML 断言，并将其兑换为 AWS 临时凭据存入 AWS 凭据文件。它支持包括 TOTP 和 U2F 安全密钥在内的 MFA。

# PARAMETERS

**-u, --username**
> Google 账户电子邮件地址

**-I, --idp-id**
> Google 身份提供方 ID

**-S, --sp-id**
> AWS 所用的 Google 服务提供方 ID

**-R, --role-arn**
> 要担任的 AWS IAM 角色 ARN

**-d, --duration**
> 凭据有效期，单位为秒（默认：3600）

**-p, --profile**
> 用于存储凭据的 AWS 配置文件名称

**-a, --ask-role**
> 即使只有一个可用角色也提示进行选择

**--no-cache**
> 禁用对 IDP 和 SP ID 的缓存

# CONFIGURATION

**~/.aws/credentials**
> 存储认证后获得的临时 AWS 凭据。

**~/.aws/config**
> AWS 配置文件的配置，包括区域和输出格式。可在此处设置配置文件专属的 google_config.google_idp_id 和 google_config.google_sp_id。

# CAVEATS

需要先在 Google Workspace 与 AWS IAM 之间完成 SAML SSO 配置。由于 USB 设备访问受限，U2F 安全密钥无法在 Docker 容器中使用。Google IDP 和 SP ID 必须从 Google Admin 控制台的 SAML Apps 设置中获取。

# HISTORY

由 **Cevo Australia** 创建的开源工具，用于衔接 Google Workspace 认证与 AWS。最初发布于 **2017 年** 前后，旨在满足基于 Google 的 SSO 登录 AWS 账户的需求。可通过 PyPI 和 Docker Hub 获取。

# INSTALL

```brew: brew install aws-google-auth```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-sts](/man/aws-sts)(1)
