# TAGLINE

管理 Simple Notification Service 主题和订阅。

# TLDR

**创建新 SNS 主题**

```aws sns create-topic --name [topic-name]```

**列出所有主题**

```aws sns list-topics```

向主题**发布消息**

```aws sns publish --topic-arn [arn:aws:sns:region:account:topic-name] --message "[Hello World]"```

将**邮箱端点订阅到**主题

```aws sns subscribe --topic-arn [arn:aws:sns:region:account:topic-name] --protocol email --notification-endpoint [user@example.com]```

将 **Lambda 函数订阅到**主题

```aws sns subscribe --topic-arn [arn:aws:sns:region:account:topic-name] --protocol lambda --notification-endpoint [arn:aws:lambda:region:account:function:name]```

**取消订阅**主题

```aws sns unsubscribe --subscription-arn [arn:aws:sns:region:account:topic-name:subscription-id]```

**列出**主题的**订阅**

```aws sns list-subscriptions-by-topic --topic-arn [arn:aws:sns:region:account:topic-name]```

**删除主题**

```aws sns delete-topic --topic-arn [arn:aws:sns:region:account:topic-name]```

# SYNOPSIS

**aws sns** _subcommand_ [_options_]

# DESCRIPTION

**aws sns** 是 AWS CLI 中用于管理 Amazon Simple Notification Service（SNS）的接口。SNS 是一项全托管的消息传递服务，支持应用程序间（A2A）和应用程序对人（A2P）的通信。

SNS 支持发布/订阅消息模式：发布者向主题发送消息，订阅者通过 HTTP/HTTPS、电子邮件、SMS、SQS、Lambda 和移动推送通知等协议接收通知。

# SUBCOMMANDS

**Topic Management**
> create-topic, delete-topic, list-topics, get-topic-attributes, set-topic-attributes

**Publishing**
> publish, publish-batch

**Subscriptions**
> subscribe, unsubscribe, list-subscriptions, list-subscriptions-by-topic, confirm-subscription, get-subscription-attributes, set-subscription-attributes

**Mobile Push**
> create-platform-application, create-platform-endpoint, delete-platform-application, delete-endpoint, list-platform-applications, list-endpoints-by-platform-application

**SMS**
> set-sms-attributes, get-sms-attributes, check-if-phone-number-is-opted-out, opt-in-phone-number, list-phone-numbers-opted-out

**Permissions**
> add-permission, remove-permission, tag-resource, untag-resource, list-tags-for-resource

# CAVEATS

邮件订阅需要收件人确认后才能接收消息。SMS 消息有区域限制，可能需要提高消费限额。标准主题的消息大小上限为 256KB。FIFO 主题需要兼容的 SQS FIFO 队列订阅者。

# HISTORY

Amazon SNS 于 **2010 年 4 月**上线，最初是一项推送通知服务。它已从简单的发布/订阅消息模式发展为支持移动推送通知、SMS，以及消息过滤、死信队列和 FIFO 主题等高级特性。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-sqs](/man/aws-sqs)(1), [aws-ses](/man/aws-ses)(1)
