# TAGLINE

通过 IAM Identity Center 进行联合身份认证。

# TLDR

**登录** AWS SSO

```aws sso login --profile [profile-name]```

**退出** AWS SSO

```aws sso logout```

**列出用户可用的 AWS 账户**

```aws sso list-accounts --access-token [token]```

**列出账户中可用的角色**

```aws sso list-account-roles --account-id [account-id] --access-token [token]```

**获取角色的临时凭证**

```aws sso get-role-credentials --account-id [account-id] --role-name [role-name] --access-token [token]```

以交互方式**配置 SSO profile**

```aws configure sso```

# SYNOPSIS

**aws sso** _subcommand_ [_options_]

# DESCRIPTION

**aws sso** 是 AWS CLI 中用于管理 AWS IAM Identity Center（旧称 AWS Single Sign-On）的接口，可通过集中式身份源对 AWS 账户和应用程序进行联合访问。

SSO 命令让用户只需认证一次，即可访问多个 AWS 账户和应用程序，无需为每个账户单独管理凭证。

# SUBCOMMANDS

**login**
> 通过浏览器发起 SSO 登录以获取访问令牌

**logout**
> 终止当前 SSO 会话并使缓存的凭证失效

**list-accounts**
> 列出已认证用户可用的 AWS 账户

**list-account-roles**
> 列出特定 AWS 账户中可用的 IAM 角色

**get-role-credentials**
> 获取用于担任角色的临时 AWS 凭证

# CONFIGURATION

**~/.aws/config**
> SSO profile 设置，包括 sso_start_url、sso_region、sso_account_id 和 sso_role_name。

# CAVEATS

SSO 登录需要浏览器参与授权流程。访问令牌会缓存在本地且有效期有限（通常为 8-12 小时）。使用 **aws sso login** 前必须先在 AWS 配置文件中配置 SSO profile。尽管服务已更名为 IAM Identity Center，API 命名空间为保持向后兼容仍保留 "sso" 名称。

# HISTORY

AWS Single Sign-On 于 **2017 年 12 月**上线，用于简化跨 AWS 账户的访问管理。它于 **2022 年 7 月**更名为 **AWS IAM Identity Center**，以更好地体现其与 IAM 的集成及扩展后的能力。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-sts](/man/aws-sts)(1), [aws-iam](/man/aws-iam)(1)
