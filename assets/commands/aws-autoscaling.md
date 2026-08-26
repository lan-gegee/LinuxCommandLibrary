# TAGLINE

根据需求自动扩缩 EC2 实例组

# TLDR

用启动模板**创建 Auto Scaling 组**

```aws autoscaling create-auto-scaling-group --auto-scaling-group-name [my-asg] --launch-template LaunchTemplateId=[lt-12345] --min-size [1] --max-size [5] --vpc-zone-identifier "[subnet-abc,subnet-def]"```

**列出 Auto Scaling 组**

```aws autoscaling describe-auto-scaling-groups```

**更新组容量**

```aws autoscaling update-auto-scaling-group --auto-scaling-group-name [my-asg] --desired-capacity [3]```

**设置扩展策略**（目标跟踪）

```aws autoscaling put-scaling-policy --auto-scaling-group-name [my-asg] --policy-name [cpu-policy] --policy-type TargetTrackingScaling --target-tracking-configuration file://[config.json]```

**描述组内实例**

```aws autoscaling describe-auto-scaling-instances```

通过实例刷新**上线新的启动模板版本**

```aws autoscaling start-instance-refresh --auto-scaling-group-name [my-asg]```

**挂载负载均衡器**目标组

```aws autoscaling attach-load-balancer-target-groups --auto-scaling-group-name [my-asg] --target-group-arns [arn:aws:elasticloadbalancing:...]```

**删除一个 Auto Scaling 组**

```aws autoscaling delete-auto-scaling-group --auto-scaling-group-name [my-asg] --force-delete```

# SYNOPSIS

**aws autoscaling** _command_ [_options_]

# PARAMETERS

**create-auto-scaling-group**
> 创建新的 Auto Scaling 组

**describe-auto-scaling-groups**
> 列出 Auto Scaling 组及其配置

**update-auto-scaling-group**
> 修改组设置（容量、健康检查等）

**delete-auto-scaling-group**
> 删除一个 Auto Scaling 组

**put-scaling-policy**
> 创建或更新扩展策略

**describe-scaling-activities**
> 查看扩展活动历史

**start-instance-refresh**
> 替换实例以上线新的启动模板版本

**put-scheduled-update-group-action**
> 创建计划扩展操作

**set-desired-capacity**
> 设置期望的实例数量

**attach-load-balancer-target-groups**
> 将目标组挂载到该组

**create-launch-configuration**
> 创建启动配置（旧式做法）

**--auto-scaling-group-name** _name_
> Auto Scaling 组的名称

**--launch-template** _spec_
> 启动模板 ID 或名称及版本

**--min-size** _n_
> 最小实例数

**--max-size** _n_
> 最大实例数

**--desired-capacity** _n_
> 期望的实例数量

**--vpc-zone-identifier** _subnets_
> 以逗号分隔的子网 ID

**--health-check-type** _type_
> EC2 或 ELB 健康检查类型

**--health-check-grace-period** _seconds_
> 健康检查开始前的等待秒数

**--force-delete**
> 即使存在运行中的实例也强制删除

# DESCRIPTION

**aws autoscaling** 管理 Amazon EC2 Auto Scaling 组，根据需求或计划自动调整 EC2 实例的数量。这些组维持应用可用性，在需求高峰时自动扩容，并在需求回落时缩容以降低成本。

启动模板或启动配置定义实例设置（AMI、实例类型、安全组）。扩展策略根据 CPU 利用率或请求数等指标决定何时以及如何扩缩。

**目标跟踪扩展**维持特定的指标值（如 50% CPU）。**分步扩展**根据告警阈值分步调整容量。**计划扩展**在指定时间改变容量。

健康检查（EC2 或 ELB）检测不健康的实例以便自动替换。**health-check-grace-period** 可防止仍在初始化中的实例被过早终止。

# CAVEATS

建议使用启动模板而非旧式的启动配置。删除含有运行中实例的组需要 **--force-delete**。扩展活动有速率限制。实例可能需要一些时间才能变为健康状态，这会影响扩缩的响应速度。

# HISTORY

**Amazon EC2 Auto Scaling** 于 **2009 年 5 月**上线，是 AWS 最早的弹性计算容量服务之一。最初使用启动配置，AWS 于 **2017 年**推出了更灵活的启动模板。此后该服务不断扩展，支持了混合实例类型、预测式扩展以及加速扩容的暖池（warm pools）。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-ec2](/man/aws-ec2)(1), [aws-elbv2](/man/aws-elbv2)(1), [aws-cloudwatch](/man/aws-cloudwatch)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/autoscaling/)```

<!-- verified: 2026-06-17 -->
