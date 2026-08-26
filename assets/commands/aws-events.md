# TAGLINE

管理 Amazon EventBridge 规则和事件路由

# TLDR

**列出默认事件总线中的所有规则**

```aws events list-rules```

**查看特定规则**

```aws events describe-rule --name [rule_name]```

**列出规则的目标**

```aws events list-targets-by-rule --rule [rule_name]```

**创建每小时运行的计划规则**

```aws events put-rule --name [rule_name] --schedule-expression "rate(1 hour)"```

**创建事件模式规则以匹配特定事件**

```aws events put-rule --name [rule_name] --event-pattern '{"source":["aws.ec2"],"detail-type":["EC2 Instance State-change Notification"]}'```

**为规则添加 Lambda 目标**

```aws events put-targets --rule [rule_name] --targets Id=1,Arn=[arn:aws:lambda:region:account:function:name]```

**禁用规则**

```aws events disable-rule --name [rule_name]```

**删除规则**（需先移除目标）

```aws events delete-rule --name [rule_name]```

# SYNOPSIS

**aws events** _subcommand_ [_options_]

# DESCRIPTION

**aws events** 是 AWS CLI 的子命令，用于管理 Amazon EventBridge（前身为 CloudWatch Events）——一项无服务器事件总线服务。它在 AWS 服务、SaaS 应用和你自己的应用程序之间路由事件。

规则按模式匹配传入的事件，并将其路由到 Lambda 函数、Step Functions、SNS 主题、SQS 队列等目标。规则还可以使用 cron 或 rate 表达式按计划触发。

事件总线充当路由器：默认总线接收 AWS 服务的事件，自定义总线可接收来自你自己应用的事件。合作伙伴事件源则对接 SaaS 提供商。

# PARAMETERS

**list-rules**
> 列出事件总线上的规则。

**describe-rule**
> 获取特定规则的详细信息。

**put-rule**
> 创建或更新规则。

**delete-rule**
> 删除规则。

**enable-rule**
> 启用已禁用的规则。

**disable-rule**
> 停用规则但不删除。

**list-targets-by-rule**
> 列出规则关联的目标。

**put-targets**
> 为规则添加目标。

**remove-targets**
> 从规则中移除目标。

**list-event-buses**
> 列出账户中的事件总线。

**put-events**
> 向事件总线发送自定义事件。

**--name** _rule-name_
> 规则名称。

**--schedule-expression** _expression_
> 计划规则的 cron 或 rate 表达式。

**--event-pattern** _json_
> 用于匹配事件的 JSON 模式。

**--targets** _targets_
> 目标规格（Id、Arn、Input 等）。

**--event-bus-name** _name_
> 事件总线名称（未指定时使用默认值）。

# CAVEATS

删除规则前必须先移除所有目标。计划表达式使用 UTC 时区。事件模式默认精确匹配取值；可使用 prefix 或 anything-but 提高灵活性。每条规则最多 5 个目标（可通过配额申请提升）。规则最长可能需要一分钟才能生效。

# HISTORY

**CloudWatch Events** 于 **2016 年 1 月** 推出，是 AWS 首个事件驱动的集成服务。在 **AWS re:Invent 2019** 上更名为 **Amazon EventBridge**，能力随之扩展，包括自定义事件总线和第三方 SaaS 集成。架构注册表（schema registry）与发现功能随后加入，帮助开发者理解事件结构。该服务至今仍是 AWS 上无服务器和事件驱动架构的核心。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-lambda](/man/aws-lambda)(1), [aws-sns](/man/aws-sns)(1), [aws-sqs](/man/aws-sqs)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/events/index.html)```

<!-- verified: 2026-06-18 -->
