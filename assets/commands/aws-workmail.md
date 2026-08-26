# TAGLINE

管理企业邮件与日历的组织和用户。

# TLDR

**列出所有组织**

```aws workmail list-organizations```

**描述组织**

```aws workmail describe-organization --organization-id [m-1234567890abcdef0]```

**列出**组织中的**用户**

```aws workmail list-users --organization-id [m-1234567890abcdef0]```

**创建用户**

```aws workmail create-user --organization-id [m-1234567890abcdef0] --name [username] --display-name "[Display Name]" --password [password]```

**重置用户密码**

```aws workmail reset-password --organization-id [m-1234567890abcdef0] --user-id [user-id] --password [new-password]```

**列出**组织中的**组**

```aws workmail list-groups --organization-id [m-1234567890abcdef0]```

**列出邮件域**

```aws workmail list-mail-domains --organization-id [m-1234567890abcdef0]```

# SYNOPSIS

**aws workmail** _subcommand_ [_options_]

# DESCRIPTION

**aws workmail** 是 AWS CLI 中用于管理 Amazon WorkMail 的接口。WorkMail 是一项安全的托管企业邮件与日历服务，支持现有的桌面和移动邮件客户端，包括 Microsoft Outlook、iOS 和 Android 应用。

该 CLI 提供对 WorkMail 组织、用户、组、资源（会议室、设备）、邮件域以及移动设备访问策略的管理能力。

# SUBCOMMANDS

**Organization Management**
> create-organization, delete-organization, describe-organization, list-organizations

**User Management**
> create-user, delete-user, describe-user, list-users, update-user, reset-password, register-to-work-mail, deregister-from-work-mail

**Group Management**
> create-group, delete-group, describe-group, list-groups, associate-member-to-group, disassociate-member-from-group, list-group-members

**Resource Management**
> create-resource, delete-resource, describe-resource, list-resources, update-resource

**Mail Domains**
> register-mail-domain, deregister-mail-domain, get-mail-domain, list-mail-domains

**Aliases**
> create-alias, delete-alias, list-aliases, update-primary-email-address

**Access Control**
> create-access-control-rule, delete-access-control-rule, put-access-control-rule, list-access-control-rules

**Mailbox Management**
> put-mailbox-permissions, delete-mailbox-permissions, get-mailbox-details, start-mailbox-export-job

# CAVEATS

大多数操作都需要组织 ID，其格式为 **m-** 后接字母数字字符。用户和资源必须先注册到 WorkMail，邮件操作才能生效。邮箱导出任务是异步的，需要提供 S3 存储桶作为输出位置。

# HISTORY

Amazon WorkMail 于 **2015 年 1 月**上线，是一项面向企业的托管邮件与日历服务。它被设计为 Microsoft Exchange 和 Google Workspace 的替代方案，具备加密、合规和目录集成等企业级特性。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-ses](/man/aws-ses)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/workmail/index.html)```

<!-- verified: 2026-06-18 -->
