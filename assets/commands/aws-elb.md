# TAGLINE

管理 Classic Load Balancer

# TLDR

**列出所有 Classic Load Balancer**

```aws elb describe-load-balancers```

**查看特定负载均衡器**

```aws elb describe-load-balancers --load-balancer-names [lb_name]```

**检查已注册实例的健康状况**

```aws elb describe-instance-health --load-balancer-name [lb_name]```

**将实例注册到负载均衡器**

```aws elb register-instances-with-load-balancer --load-balancer-name [lb_name] --instances [i-xxxxxxxx]```

**将实例从负载均衡器注销**

```aws elb deregister-instances-from-load-balancer --load-balancer-name [lb_name] --instances [i-xxxxxxxx]```

**创建 Classic Load Balancer**

```aws elb create-load-balancer --load-balancer-name [lb_name] --listeners Protocol=HTTP,LoadBalancerPort=80,InstanceProtocol=HTTP,InstancePort=80 --subnets [subnet-id] --security-groups [sg-id]```

**删除负载均衡器**

```aws elb delete-load-balancer --load-balancer-name [lb_name]```

# SYNOPSIS

**aws elb** _subcommand_ [_options_]

# DESCRIPTION

**aws elb** 是 AWS CLI 的子命令，用于管理 Classic Load Balancer（CLB），即最早的 Elastic Load Balancing 服务。经典负载均衡器将传入流量分发到一个或多个可用区内的多台 EC2 实例。

CLB 同时工作在第 4 层（TCP）和第 7 层（HTTP/HTTPS），根据应用层或网络层信息路由流量。它会对已注册的实例执行健康检查，只将流量路由到健康的目标。

经典负载均衡器支持会话保持（sticky session）、SSL 卸载，并可与 Auto Scaling 组集成，实现实例的动态管理。

# PARAMETERS

**describe-load-balancers**
> 列出负载均衡器及其配置。

**create-load-balancer**
> 创建新的 Classic Load Balancer。

**delete-load-balancer**
> 删除负载均衡器。

**describe-instance-health**
> 检查已注册实例的健康状态。

**register-instances-with-load-balancer**
> 将实例添加到负载均衡器。

**deregister-instances-from-load-balancer**
> 将实例从负载均衡器移除。

**configure-health-check**
> 设置健康检查参数。

**create-load-balancer-listeners**
> 添加监听器配置。

**delete-load-balancer-listeners**
> 移除监听器。

**set-load-balancer-listener-ssl-certificate**
> 更新 HTTPS 监听器的 SSL 证书。

**describe-load-balancer-attributes**
> 检索连接排空（connection draining）、访问日志设置等属性。

**modify-load-balancer-attributes**
> 修改连接排空和空闲超时等属性。

**describe-load-balancer-policies**
> 列出与负载均衡器关联的策略。

**create-load-balancer-policy**
> 为负载均衡器创建新策略。

**delete-load-balancer-policy**
> 从负载均衡器删除策略。

**create-app-cookie-stickiness-policy**
> 启用由应用程序控制的会话保持。

**create-lb-cookie-stickiness-policy**
> 启用由负载均衡器控制的会话保持。

**attach-load-balancer-to-subnets**
> 为负载均衡器添加子网（仅限 VPC）。

**detach-load-balancer-from-subnets**
> 从负载均衡器移除子网。

**enable-availability-zones-for-load-balancer**
> 为负载均衡器添加可用区（EC2-Classic）。

**disable-availability-zones-for-load-balancer**
> 从负载均衡器移除可用区。

**apply-security-groups-to-load-balancer**
> 将安全组关联到 VPC 负载均衡器。

**add-tags**
> 在负载均衡器上添加或覆盖标签。

**remove-tags**
> 从负载均衡器移除标签。

**describe-tags**
> 列出一个或多个负载均衡器上的标签。

**describe-account-limits**
> 显示账户的 ELB 服务限制。

**wait**
> 等待负载均衡器达到指定状态。

**--load-balancer-name** _name_
> 负载均衡器名称。

**--load-balancer-names** _names_
> 负载均衡器名称列表。

**--instances** _ids_
> EC2 实例 ID。

**--listeners** _config_
> 监听器的协议和端口映射。

**--subnets** _ids_
> 负载均衡器所在的 VPC 子网。

**--security-groups** _ids_
> 要分配的安全组。

# CAVEATS

经典负载均衡器属于上一代服务。AWS 建议 HTTP/HTTPS 工作负载改用 Application Load Balancer（ALB），TCP/UDP 工作负载改用 Network Load Balancer（NLB）。CLB 原生不支持基于路径的路由、基于主机的路由或 WebSocket。CLB 不再添加新功能。

# HISTORY

Elastic Load Balancing 于 **2009 年** 推出，是 AWS 最早的服务之一。在 **2016 年 8 月** Application Load Balancer 问世之前，Classic Load Balancer 一直是唯一的负载均衡器类型。Network Load Balancer 于 **2017 年** 推出。经典负载均衡器目前仍受支持，但已被视为遗留产品，AWS 鼓励用户迁移到更新的类型。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-elbv2](/man/aws-elbv2)(1), [aws-ec2](/man/aws-ec2)(1), [aws-autoscaling](/man/aws-autoscaling)(1)
