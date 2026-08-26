# TAGLINE

通过 AWS 发送和管理电子邮件

# TLDR

**发送带主题和正文的电子邮件**

```aws ses send-email --from [sender@example.com] --to [recipient@example.com] --subject "[Subject]" --text "[Body text]"```

**验证电子邮箱身份**

```aws ses verify-email-identity --email-address [email@example.com]```

**列出已验证的身份**

```aws ses list-identities```

**获取发送配额**和限制

```aws ses get-send-quota```

**获取发送统计信息**

```aws ses get-send-statistics```

**创建邮件模板**

```aws ses create-template --template file://[template.json]```

**发送模板化邮件**

```aws ses send-templated-email --source [sender@example.com] --destination ToAddresses=[recipient@example.com] --template [template-name] --template-data '{"name":"value"}'```

# SYNOPSIS

**aws ses** _subcommand_ [_options_]

# DESCRIPTION

**aws ses** 是 AWS CLI 中用于管理 Amazon Simple Email Service（SES）的接口。SES 是一项基于云的邮件发送服务，适用于事务性邮件、营销消息和高流量邮件通信。

SES 提供邮件发送能力，并具备送达率跟踪、退信与投诉处理、邮件模板以及用于管理发送行为的配置集等功能。

# SUBCOMMANDS

**Email Sending**
> send-email, send-raw-email, send-templated-email, send-bulk-templated-email, send-bounce, send-custom-verification-email

**Identity Verification**
> verify-email-identity, verify-domain-identity, verify-domain-dkim, delete-identity, list-identities, get-identity-verification-attributes

**Templates**
> create-template, get-template, update-template, delete-template, list-templates, test-render-template

**Configuration Sets**
> create-configuration-set, describe-configuration-set, delete-configuration-set, list-configuration-sets

**Receipt Rules**
> create-receipt-rule, describe-receipt-rule, update-receipt-rule, delete-receipt-rule, list-receipt-rule-sets

**Statistics**
> get-send-quota, get-send-statistics, get-account-sending-enabled

# CAVEATS

新的 SES 账户以沙盒模式启动，只能发送给已验证的邮箱地址。需申请生产访问权限才能向任意地址发送。邮箱身份（地址或域名）在发送前必须完成验证。SES 按每发送 1000 封邮件计费，另加数据传输费。

# HISTORY

Amazon SES 于 **2011 年 1 月**上线，是 AWS 的邮件发送服务，为开发者提供了大规模发送邮件的经济方式。该服务后来逐步增加了接收功能、模板和高级送达率特性。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [sendmail](/man/sendmail)(1), [mail](/man/mail)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/ses/index.html)```

<!-- verified: 2026-06-18 -->
