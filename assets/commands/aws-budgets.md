# TAGLINE

管理成本预算和支出告警。

# TLDR

**创建月度成本预算**

```aws budgets create-budget --account-id [123456789012] --budget file://[budget.json]```

**创建带通知的预算**

```aws budgets create-budget --account-id [123456789012] --budget file://[budget.json] --notifications-with-subscribers file://[notifications.json]```

**列出账户的所有预算**

```aws budgets describe-budgets --account-id [123456789012] --max-results [100]```

**获取**特定预算的**详情**

```aws budgets describe-budget --account-id [123456789012] --budget-name "[MyBudget]"```

**更新预算**上限

```aws budgets update-budget --account-id [123456789012] --new-budget file://[updated-budget.json]```

**删除预算**

```aws budgets delete-budget --account-id [123456789012] --budget-name "[MyBudget]"```

**列出**特定预算的**预算操作**

```aws budgets describe-budget-actions-for-budget --account-id [123456789012] --budget-name "[MyBudget]"```

# SYNOPSIS

**aws budgets** _command_ [_options_]

# PARAMETERS

**create-budget**
> 创建新预算，可选配通知

**describe-budgets**
> 列出账户的所有预算

**describe-budget**
> 获取特定预算的详情

**update-budget**
> 修改现有预算

**delete-budget**
> 移除一个预算

**create-budget-action**
> 创建超出阈值时执行的自动化操作

**describe-budget-actions-for-budget**
> 列出与某个预算关联的操作

**create-notification**
> 为现有预算添加通知

**--account-id** _id_
> AWS 账户 ID（12 位数字）

**--budget** _json_
> 预算规格（内联 JSON 或 file://path）

**--budget-name** _name_
> 预算名称

**--notifications-with-subscribers** _json_
> 通知阈值以及订阅者的邮箱/SNS 主题

**--new-budget** _json_
> 更新后的预算规格

**--max-results** _integer_
> 返回结果的最大数量（用于列表操作）

# BUDGET JSON STRUCTURE

```json
{
  "BudgetName": "Monthly-EC2-Budget",
  "BudgetLimit": {"Amount": "100", "Unit": "USD"},
  "TimeUnit": "MONTHLY",
  "BudgetType": "COST"
}
```

预算类型包括 **COST**、**USAGE**、**RI_UTILIZATION**、**RI_COVERAGE**、**SAVINGS_PLANS_UTILIZATION** 和 **SAVINGS_PLANS_COVERAGE**。

# DESCRIPTION

**aws budgets** 管理 AWS Budgets，用于成本控制和监控。预算会对照设定的限额跟踪支出或使用量，并在接近或超过阈值时发送告警。

可以创建预算来监控整体账户成本、特定服务、关联账户或带标签的资源。当支出达到预算限额的指定百分比时，通知会通过电子邮件或 SNS 向订阅者发出告警。

**预算操作**可自动化对预算告警的响应，例如在超过阈值时应用限制性的 IAM 策略或停止 EC2 实例。

时间单位包括 DAILY、MONTHLY、QUARTERLY 和 ANNUALLY。如果未指定开始日期，预算将从所选周期的起始点开始。

# CAVEATS

成本数据存在最长 24 小时的处理延迟。预算限额是软性限制：只会触发告警，除非配置了预算操作，否则不会自动停止支出。免费额度包含每个账户 2 个启用操作的预算；额外的预算会产生费用。CLI 命令中必须显式指定账户 ID。

# HISTORY

**AWS Budgets** 于 **2017 年 1 月**作为 AWS 成本管理工具的一部分推出，由更早的 Billing Alerts 功能演化而来。用于自动化响应的预算操作于 **2020 年**加入，使成本控制措施不再局限于通知。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-ce](/man/aws-ce)(1), [aws-sns](/man/aws-sns)(1), [aws-organizations](/man/aws-organizations)(1)
