# TAGLINE

对 IBM Cloud 进行身份验证

# TLDR

**交互式登录**

```ibmcloud login```

**使用 SSO 登录**

```ibmcloud login --sso```

**使用 API 密钥登录**

```ibmcloud login --apikey [API_KEY]```

**登录到指定区域**

```ibmcloud login -r [us-south]```

**使用用户名和密码登录**

```ibmcloud login -u [user@example.com] -p [password]```

**登录到指定 API 端点**

```ibmcloud login -a [https://cloud.ibm.com]```

**从文件读取 API 密钥登录**

```ibmcloud login --apikey @[keyfile]```

# SYNOPSIS

**ibmcloud** **login** [_options_]

# PARAMETERS

**-u** _user_
> 用户名（邮箱）。

**-p** _password_
> 密码。

**--sso**
> 使用单点登录（联合 ID）。

**--apikey** _key_
> 用于身份验证的 API 密钥。

**-a** _endpoint_
> API 端点 URL。

**-r** _region_
> 目标区域。

**-c** _account_
> 目标账户 ID。

**-o** _org_
> 目标组织。

**-s** _space_
> 目标空间。

# DESCRIPTION

**ibmcloud login** 对 IBM Cloud 进行身份验证。支持交互式登录、联合 ID 的 SSO 以及 API 密钥认证。登录后，使用 **ibmcloud target** 设置账户、区域或资源组上下文。自动化场景可使用环境变量 IC_API_KEY、IC_API_ENDPOINT 和 IC_REGION。

# SEE ALSO

[ibmcloud](/man/ibmcloud)(1), [ibmcloud-target](/man/ibmcloud-target)(1), [ibmcloud-api](/man/ibmcloud-api)(1)
