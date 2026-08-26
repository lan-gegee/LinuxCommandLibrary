# TAGLINE

通过指标、警报和控制面板监控资源。

# TLDR

**向 CloudWatch 写入自定义指标数据**

```aws cloudwatch put-metric-data --namespace [MyApp] --metric-name [RequestCount] --value [1] --unit Count```

**获取 EC2 实例 CPU 的指标统计数据**

```aws cloudwatch get-metric-statistics --namespace AWS/EC2 --metric-name CPUUtilization --dimensions Name=InstanceId,Value=[i-1234567890abcdef0] --start-time [2024-01-01T00:00:00Z] --end-time [2024-01-02T00:00:00Z] --period 3600 --statistics Average```

**为高 CPU 使用率创建警报**

```aws cloudwatch put-metric-alarm --alarm-name [high-cpu] --metric-name CPUUtilization --namespace AWS/EC2 --statistic Average --period 300 --threshold 80 --comparison-operator GreaterThanThreshold --evaluation-periods 2 --alarm-actions [arn:aws:sns:us-east-1:123456789012:my-topic] --dimensions Name=InstanceId,Value=[i-1234567890abcdef0]```

**列出账户中的所有警报**

```aws cloudwatch describe-alarms```

**列出某命名空间下的可用指标**

```aws cloudwatch list-metrics --namespace [AWS/EC2]```

**删除指定的警报**

```aws cloudwatch delete-alarms --alarm-names [high-cpu] [low-disk]```

**禁用警报的操作**

```aws cloudwatch disable-alarm-actions --alarm-names [high-cpu]```

**启用警报的操作**

```aws cloudwatch enable-alarm-actions --alarm-names [high-cpu]```

# SYNOPSIS

**aws cloudwatch** _command_ [_options_]

# DESCRIPTION

**aws cloudwatch** 是 Amazon CloudWatch 的 AWS CLI 接口。CloudWatch 是一项面向 AWS 资源和应用程序的监控与可观测性服务，可收集指标、日志和事件，让你掌握资源利用率、应用性能和运行健康状况。

CloudWatch 支持设置警报，在指标越过阈值时触发通知或自动化操作。它既支持 AWS 服务内置指标，也支持自定义应用指标。

# COMMANDS

**put-metric-data**
> 发布自定义指标数据点

**get-metric-data**
> 通过查询检索指标值

**get-metric-statistics**
> 获取特定指标的统计数据

**list-metrics**
> 按命名空间列出可用指标

**put-metric-alarm**
> 创建或更新指标警报

**describe-alarms**
> 列出已配置的警报及其状态

**set-alarm-state**
> 手动设置警报状态以便测试

**put-dashboard**
> 创建或更新 CloudWatch 控制面板

**delete-alarms**
> 删除一个或多个警报

**enable-alarm-actions**
> 为指定警报启用操作

**disable-alarm-actions**
> 为指定警报禁用操作

**describe-alarms-for-metric**
> 列出与特定指标关联的警报

**list-tags-for-resource**
> 列出 CloudWatch 资源的标签

**put-anomaly-detector**
> 为指标创建异常检测模型

# CAVEATS

超过 15 个月的指标数据会被自动删除。高分辨率指标（1 秒粒度）会产生额外费用。自定义指标按每月每个指标计费。服务中断期间，警报评估可能出现延迟。

# HISTORY

Amazon CloudWatch 于 **2009 年 5 月** 随 EC2 监控一同推出。自定义指标于 **2011 年** 加入，控制面板于 **2015 年** 加入，异常检测于 **2019 年** 加入。该服务已发展为所有 AWS 服务的核心监控中枢，现已与 CloudWatch Logs 和 EventBridge 集成。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-logs](/man/aws-logs)(1), [aws-events](/man/aws-events)(1), [aws-ec2](/man/aws-ec2)(1), [aws-sns](/man/aws-sns)(1)
