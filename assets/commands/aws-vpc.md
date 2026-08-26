# TAGLINE

管理 Virtual Private Cloud 网络、子网和网关。

# TLDR

**列出所有 VPC**

```aws ec2 describe-vpcs```

**创建 VPC**

```aws ec2 create-vpc --cidr-block [10.0.0.0/16]```

**列出子网**

```aws ec2 describe-subnets --filters Name=vpc-id,Values=[vpc-xxxxxxxx]```

**创建子网**

```aws ec2 create-subnet --vpc-id [vpc-xxxxxxxx] --cidr-block [10.0.1.0/24] --availability-zone [us-east-1a]```

**创建互联网网关**

```aws ec2 create-internet-gateway```

将**互联网网关附加到** VPC

```aws ec2 attach-internet-gateway --vpc-id [vpc-xxxxxxxx] --internet-gateway-id [igw-xxxxxxxx]```

**列出路由表**

```aws ec2 describe-route-tables --filters Name=vpc-id,Values=[vpc-xxxxxxxx]```

向互联网网关**添加路由**

```aws ec2 create-route --route-table-id [rtb-xxxxxxxx] --destination-cidr-block 0.0.0.0/0 --gateway-id [igw-xxxxxxxx]```

# SYNOPSIS

**aws ec2** _vpc-subcommand_ [_options_]

# DESCRIPTION

**aws-vpc** 指 AWS CLI 的 ec2 命名空间中的 VPC（Virtual Private Cloud）命令。VPC 在 AWS 中提供隔离的虚拟网络，你可以完全掌控 IP 编址、子网、路由和安全来启动资源。

关键组件包括 **VPC**（网络容器）、**子网**（可用区中的 IP 地址范围）、**路由表**（流量路由规则）、**互联网网关**（公网访问）、**NAT 网关**（为私有子网提供仅出站的互联网访问）和**安全组**（实例防火墙）。

VPC Peering 以私有方式连接 VPC。Transit Gateway 可大规模连接多个 VPC 和本地网络。VPC Endpoints 无需经过互联网即可私有访问 AWS 服务。

# PARAMETERS

**describe-vpcs**
> 列出 VPC 及其详情。

**create-vpc**
> 创建新 VPC。

**delete-vpc**
> 删除 VPC（必须为空）。

**describe-subnets**
> 列出子网。

**create-subnet**
> 在 VPC 中创建子网。

**delete-subnet**
> 删除子网。

**describe-internet-gateways**
> 列出互联网网关。

**create-internet-gateway**
> 创建互联网网关。

**attach-internet-gateway**
> 将网关附加到 VPC。

**describe-route-tables**
> 列出路由表。

**create-route**
> 向路由表添加路由。

**describe-nat-gateways**
> 列出 NAT 网关。

**create-nat-gateway**
> 创建 NAT 网关。

**--vpc-id** _id_
> VPC 标识符。

**--cidr-block** _cidr_
> CIDR 表示法的 IP 地址范围。

**--subnet-id** _id_
> 子网标识符。

**--availability-zone** _az_
> 子网所在的可用区。

**--filters** _filters_
> 按属性过滤结果。

# CAVEATS

VPC 的 CIDR 块不能与已建立对等连接的 VPC 重叠。每个子网只存在于一个可用区中。公有子网需要有指向互联网网关的路由并启用公网 IP。NAT 网关会产生按小时和数据量的费用。默认 VPC 与自定义 VPC 的行为不同。安全组规则是有状态的；网络 ACL 是无状态的。

# HISTORY

**Amazon VPC** 于 **2009 年 8 月**上线，是 AWS 的基础网络服务之一，让客户可以定义隔离的网络。最初 EC2 运行在共享网络（EC2-Classic）中，但自 **2013 年**起 VPC 成为新账户的默认选择。**VPC Peering** 于 **2014 年**加入。作为托管服务的 **NAT Gateway** 于 **2015 年**推出。**Transit Gateway** 在 **re:Invent 2018** 上发布，用于中心辐射型架构。EC2-Classic 于 **2022 年**全面退役。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-ec2](/man/aws-ec2)(1), [ip](/man/ip)(1)
