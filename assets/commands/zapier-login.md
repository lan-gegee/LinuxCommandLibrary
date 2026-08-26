# TAGLINE

向 Zapier 平台进行身份验证

# TLDR

交互式**登录 Zapier**

```zapier login```

使用 SSO **登录**（适用于 Google、Facebook 或 Microsoft 账户）

```zapier login --sso```

# SYNOPSIS

**zapier** **login** [_options_]

# PARAMETERS

**--sso**
> 使用 SSO 身份验证。如果你通过单点登录（Google、Facebook 或 Microsoft）登录 Zapier 且没有 Zapier 密码，则必须使用此选项。它会提示你输入从 Zapier 开发者账户生成的部署密钥（deploy key）。

# DESCRIPTION

**zapier login** 向 Zapier 平台进行身份验证，并将凭据存储在 **~/.zapierrc** 中。它会打开浏览器完成认证。使用其他 Zapier CLI 命令前必须先登录。

作为交互式登录的替代方案，可以设置 **ZAPIER_DEPLOY_KEY** 环境变量来在无需用户输入的情况下运行特权命令。

注意：自 v18.0.0 起，CLI 二进制已从 **zapier** 更名为 **zapier-platform**。旧的 **zapier** 命令仍可使用，但已弃用。

# SEE ALSO

[zapier](/man/zapier)(1), [zapier-test](/man/zapier-test)(1), [zapier-push](/man/zapier-push)(1), [zapier-validate](/man/zapier-validate)(1)
