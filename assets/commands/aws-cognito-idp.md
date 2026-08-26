# TAGLINE

管理用于认证和用户目录的用户池。

# TLDR

**创建新的用户池**

```aws cognito-idp create-user-pool --pool-name [my-pool]```

**在用户池中创建用户**

```aws cognito-idp admin-create-user --user-pool-id [pool-id] --username [user@example.com]```

**自助注册用户**（客户端注册）

```aws cognito-idp sign-up --client-id [client-id] --username [user@example.com] --password [Password123!]```

**列出用户池中的所有用户**

```aws cognito-idp list-users --user-pool-id [pool-id]```

**认证用户**（客户端方式，无需管理员凭据）

```aws cognito-idp initiate-auth --client-id [client-id] --auth-flow USER_PASSWORD_AUTH --auth-parameters USERNAME=[username],PASSWORD=[password]```

**以管理员身份在服务器端认证用户**

```aws cognito-idp admin-initiate-auth --user-pool-id [pool-id] --client-id [client-id] --auth-flow ADMIN_USER_PASSWORD_AUTH --auth-parameters USERNAME=[username],PASSWORD=[password]```

**为应用创建用户池客户端**

```aws cognito-idp create-user-pool-client --user-pool-id [pool-id] --client-name [my-app]```

**永久设置用户的密码**

```aws cognito-idp admin-set-user-password --user-pool-id [pool-id] --username [user@example.com] --password [NewPassword123!] --permanent```

**将用户加入组**

```aws cognito-idp admin-add-user-to-group --user-pool-id [pool-id] --username [user@example.com] --group-name [admins]```

# SYNOPSIS

**aws cognito-idp** _command_ [_options_]

# DESCRIPTION

**aws cognito-idp** 是 Amazon Cognito 用户池的 AWS CLI 接口。Cognito 用户池是一项面向 Web 和移动应用认证的用户目录服务，负责用户注册、认证、账户恢复，并可与 Google、Facebook 及基于 SAML 的系统等外部身份提供方集成。

Cognito 用户池提供多因素认证、密码策略、电子邮件/短信验证和 OAuth 2.0 令牌签发等功能，既可用于服务器端管理，也可用于客户端用户流程。

# COMMANDS

**create-user-pool**
> 创建新的用户池

**admin-create-user**
> 以管理员身份创建用户

**sign-up**
> 从客户端注册用户（自助注册）

**admin-delete-user**
> 从用户池中删除用户

**list-users**
> 列出用户池中的用户

**initiate-auth**
> 启动客户端认证（USER_PASSWORD_AUTH、USER_SRP_AUTH、REFRESH_TOKEN_AUTH、CUSTOM_AUTH）

**admin-initiate-auth**
> 启动服务器端认证（ADMIN_USER_PASSWORD_AUTH）

**admin-respond-to-auth-challenge**
> 响应认证质询（MFA、新密码）

**admin-set-user-password**
> 设置或重置用户的密码

**create-group**
> 创建用户组

**admin-add-user-to-group**
> 将用户添加到组

**create-user-pool-client**
> 创建用于认证的应用客户端

# CAVEATS

部分设置（如用户名属性）在用户池创建后无法更改。Cognito 签发的令牌中，访问令牌最长有效期为 24 小时。自定义认证 Lambda 会增加登录流程的延迟。基于短信的 MFA 会产生额外的 SNS 费用。

# HISTORY

Amazon Cognito 用户池于 **2016 年 7 月** 作为托管用户目录推出，构建于 **2014 年** 推出的 Cognito Identity（联合身份）之上。自适应认证等高级安全功能于 **2017 年** 加入，WebAuthn/passkey 支持于 **2023 年** 引入。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-cognito-identity](/man/aws-cognito-identity)(1), [aws-iam](/man/aws-iam)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/cognito-idp/index.html)```

<!-- verified: 2026-06-18 -->
