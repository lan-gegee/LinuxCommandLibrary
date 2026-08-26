# TAGLINE

分析云成本与用量数据。

# TLDR

**获取上个月的成本与用量数据**，按服务分组

```aws ce get-cost-and-usage --time-period Start=[YYYY-MM-DD],End=[YYYY-MM-DD] --granularity MONTHLY --metrics "BlendedCost" --group-by Type=DIMENSION,Key=SERVICE```

**获取下个月的成本预测**

```aws ce get-cost-forecast --time-period Start=[YYYY-MM-DD],End=[YYYY-MM-DD] --metric BLENDED_COST --granularity MONTHLY```

**列出最近 30 天检测到的所有成本异常**

```aws ce get-anomalies --date-interval StartDate=[YYYY-MM-DD],EndDate=[YYYY-MM-DD]```

**获取本月的预留实例使用率**

```aws ce get-reservation-utilization --time-period Start=[YYYY-MM-DD],End=[YYYY-MM-DD]```

**按服务获取节省计划的覆盖情况**

```aws ce get-savings-plans-coverage --time-period Start=[YYYY-MM-DD],End=[YYYY-MM-DD] --group-by Type=DIMENSION,Key=SERVICE```

**获取 EC2 实例的容量调整建议**

```aws ce get-rightsizing-recommendation --service AmazonEC2```

# SYNOPSIS

**aws ce** _command_ [_options_]

# DESCRIPTION

**aws ce** 是 AWS Cost Explorer 的 AWS CLI 接口，支持以编程方式访问成本与用量数据。它既能查询聚合数据（如月度总成本），也能查询细粒度指标（如特定服务的每日操作量）。

Cost Explorer 提供对支出模式的洞察、预测、异常检测，以及针对预留实例和节省计划的建议。所有请求都经由 **us-east-1** 区域端点。

# COMMANDS

**get-cost-and-usage**
> 检索带过滤和分组的成本与用量指标

**get-cost-forecast**
> 根据历史数据生成成本预测

**get-anomalies**
> 列出检测到的支出异常

**get-reservation-utilization**
> 检查预留实例的使用率

**get-savings-plans-coverage**
> 分析节省计划在各服务上的覆盖情况

**get-rightsizing-recommendation**
> 获取 EC2 实例的容量调整建议

**get-dimension-values**
> 列出某个过滤维度的可用值（例如 SERVICE）

**get-usage-forecast**
> 预测未来周期的用量

**create-anomaly-monitor**
> 设置自动异常检测监控

**create-anomaly-subscription**
> 订阅某个异常监控器的告警

**create-cost-category-definition**
> 定义自定义的成本归类规则

# CAVEATS

Cost Explorer API 的使用超出免费额度会产生费用。数据通常有 24-48 小时的延迟。历史数据仅保留最近 13 个月。无论资源部署在何处，都必须使用 **us-east-1** 端点。

# HISTORY

AWS Cost Explorer 于 **2017 年**作为 AWS 控制台中的可视化工具推出。Cost Explorer API 于 **2018 年**引入，以支持编程访问。异常检测于 **2020 年**加入，承诺购买分析功能在 **2023-2024** 年间持续扩展。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-budgets](/man/aws-budgets)(1), [aws-pricing](/man/aws-pricing)(1), [aws-cur](/man/aws-cur)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/ce/)```

<!-- verified: 2026-06-17 -->
