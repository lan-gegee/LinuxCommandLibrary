# TAGLINE

管理 Linode NodeBalancer（节点负载均衡器）

# TLDR

**列出负载均衡器**

```linode-cli nodebalancers list```

**创建负载均衡器**

```linode-cli nodebalancers create --region [us-east] --label [my-balancer]```

**查看负载均衡器**

```linode-cli nodebalancers view [nodebalancer_id]```

**列出配置**

```linode-cli nodebalancers configs-list [nodebalancer_id]```

**删除负载均衡器**

```linode-cli nodebalancers delete [nodebalancer_id]```

**添加节点**

```linode-cli nodebalancers node-create [nodebalancer_id] [config_id] --address [192.168.1.1:80]```

# SYNOPSIS

**linode-cli nodebalancers** _subcommand_ [_options_]

# PARAMETERS

_SUBCOMMAND_
> NodeBalancer 操作。

**list**
> 列出所有 NodeBalancer。

**create**
> 创建 NodeBalancer。

**view** _ID_
> 查看 NodeBalancer 详情。

**configs-list** _ID_
> 列出配置。

**delete** _ID_
> 删除 NodeBalancer。

**--region** _REGION_
> 数据中心所在区域。

**--label** _NAME_
> NodeBalancer 名称。

**--help**
> 显示帮助信息。

# DESCRIPTION

**linode-cli nodebalancers** 管理 Linode NodeBalancer。NodeBalancer 可在多个实例之间分发流量。

该工具为高可用场景配置负载均衡、健康检查和 SSL 终止。

# CAVEATS

需要身份验证。按小时计费。需要配置后端节点。

# HISTORY

linode-cli nodebalancers 是 **Linode CLI** 的一部分，用于管理 NodeBalancer 负载均衡服务。

# SEE ALSO

[linode-cli](/man/linode-cli)(1), [linode-cli-linodes](/man/linode-cli-linodes)(1)
