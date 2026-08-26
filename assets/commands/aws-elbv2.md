# TAGLINE

管理 Application 和 Network Load Balancer

# TLDR

**列出所有 Application 和 Network Load Balancer**

```aws elbv2 describe-load-balancers```

**查看目标组**

```aws elbv2 describe-target-groups```

**检查目标组中目标的健康状况**

```aws elbv2 describe-target-health --target-group-arn [arn:aws:elasticloadbalancing:region:account:targetgroup/name/id]```

**将目标注册到目标组**

```aws elbv2 register-targets --target-group-arn [target_group_arn] --targets Id=[i-xxxxxxxx],Port=[80]```

**将目标从目标组注销**

```aws elbv2 deregister-targets --target-group-arn [target_group_arn] --targets Id=[i-xxxxxxxx]```

**创建 Application Load Balancer**

```aws elbv2 create-load-balancer --name [lb_name] --type application --subnets [subnet-1] [subnet-2] --security-groups [sg-xxxxxxxx]```

**列出负载均衡器的监听器**

```aws elbv2 describe-listeners --load-balancer-arn [load_balancer_arn]```

**删除负载均衡器**

```aws elbv2 delete-load-balancer --load-balancer-arn [load_balancer_arn]```

# SYNOPSIS

**aws elbv2** _subcommand_ [_options_]

# DESCRIPTION

**aws elbv2** 是 AWS CLI 的子命令，用于管理 Application Load Balancer（ALB）和 Network Load Balancer（NLB），即第二代 Elastic Load Balancing 服务。

**Application Load Balancer** 工作在第 7 层，支持基于 URL 路径、主机名、HTTP 标头和查询字符串的高级路由。它可与 WAF 集成、支持 WebSocket，并能路由到 Lambda 函数。

**Network Load Balancer** 工作在第 4 层，延迟极低，每秒可处理数百万请求。它会保留客户端 IP 地址，并支持静态 IP 和 PrivateLink。

两种类型都使用目标组将请求路由到已注册的目标，例如 EC2 实例、容器、IP 地址或 Lambda 函数。

# PARAMETERS

**describe-load-balancers**
> 列出负载均衡器及其详情。

**create-load-balancer**
> 创建新的 ALB 或 NLB。

**delete-load-balancer**
> 删除负载均衡器。

**describe-target-groups**
> 列出目标组。

**create-target-group**
> 创建新的目标组。

**delete-target-group**
> 删除目标组。

**describe-target-health**
> 检查目标组中目标的健康状况。

**register-targets**
> 将目标添加到目标组。

**deregister-targets**
> 从目标组移除目标。

**describe-listeners**
> 列出负载均衡器上的监听器。

**create-listener**
> 为负载均衡器添加监听器。

**describe-rules**
> 列出监听器的路由规则。

**--load-balancer-arn** _arn_
> 负载均衡器的 ARN。

**--target-group-arn** _arn_
> 目标组的 ARN。

**--type** _type_
> 负载均衡器类型：application、network 或 gateway。

**--targets** _targets_
> 目标规格（Id、Port、AvailabilityZone）。

**--subnets** _ids_
> 负载均衡器所在的子网。

# CAVEATS

目标组绑定特定的负载均衡器类型，不能在 ALB 与 NLB 之间共享。删除负载均衡器不会删除其关联的目标组。ALB 要求至少有两个位于不同可用区的子网。跨可用区（cross-zone）负载均衡的行为在 ALB（始终启用）和 NLB（可配置）之间有所不同。

# HISTORY

**Application Load Balancer** 于 **2016 年 8 月** 推出，是 AWS 具备基于内容路由能力的第 7 层负载均衡器。**Network Load Balancer** 于 **2017 年 9 月** 推出，面向高性能的第 4 层工作负载。**Gateway Load Balancer** 于 **2020 年 11 月** 加入，用于第三方虚拟设备。此后陆续增加了加权目标组、Lambda 目标和 gRPC 支持等特性。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-elb](/man/aws-elb)(1), [aws-ec2](/man/aws-ec2)(1)
