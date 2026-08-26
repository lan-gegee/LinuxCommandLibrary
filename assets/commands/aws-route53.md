# TAGLINE

管理 DNS 托管区域和记录

# TLDR

**列出账户中的所有托管区域**

```aws route53 list-hosted-zones```

**获取**特定托管区域的**详细信息**

```aws route53 get-hosted-zone --id [/hostedzone/ZONE_ID]```

**列出**托管区域中的 **DNS 记录**

```aws route53 list-resource-record-sets --hosted-zone-id [ZONE_ID]```

为域名**创建新托管区域**

```aws route53 create-hosted-zone --name [example.com] --caller-reference [unique-string]```

**测试**特定记录的 **DNS 应答**

```aws route53 test-dns-answer --hosted-zone-id [ZONE_ID] --record-name [www.example.com] --record-type [A]```

**列出所有健康检查**

```aws route53 list-health-checks```

# SYNOPSIS

**aws route53** _subcommand_ [_options_]

# DESCRIPTION

**aws route53** 是 AWS CLI 中用于管理 Amazon Route 53 的接口。Route 53 是一项高可用、可扩展的域名系统（DNS）Web 服务。它提供用于域名注册、DNS 路由配置和资源健康检查的命令。

Route 53 将用户请求连接到 AWS 中运行的基础设施（如 EC2 实例、Elastic Load Balancer 或 S3 存储桶），也可以将用户路由到 AWS 之外的基础设施。该服务支持 DNS 故障转移、地理位置路由、基于延迟的路由和加权轮询路由。

# SUBCOMMANDS

**Hosted Zones**
> create-hosted-zone, delete-hosted-zone, get-hosted-zone, list-hosted-zones, list-hosted-zones-by-name, list-hosted-zones-by-vpc, update-hosted-zone-comment

**Resource Records**
> change-resource-record-sets, list-resource-record-sets, test-dns-answer

**Health Checks**
> create-health-check, delete-health-check, get-health-check, get-health-check-status, list-health-checks, update-health-check

**Traffic Policies**
> create-traffic-policy, delete-traffic-policy, get-traffic-policy, list-traffic-policies, create-traffic-policy-instance, update-traffic-policy-instance

**DNSSEC**
> enable-hosted-zone-dnssec, disable-hosted-zone-dnssec, get-dnssec, create-key-signing-key, delete-key-signing-key

**VPC Association**
> associate-vpc-with-hosted-zone, disassociate-vpc-from-hosted-zone, list-vpc-association-authorizations

**Query Logging**
> create-query-logging-config, delete-query-logging-config, get-query-logging-config, list-query-logging-configs

**CIDR Collections**（用于基于 IP 的路由）
> create-cidr-collection, delete-cidr-collection, change-cidr-collection, list-cidr-collections, list-cidr-blocks, list-cidr-locations

**Tagging / Misc**
> list-tags-for-resource, list-tags-for-resources, change-tags-for-resource, get-checker-ip-ranges, wait

# CAVEATS

通过 **change-resource-record-sets** 所做的 DNS 更改并非即时生效；传播最长可能需要 60 秒。可使用变更 ID 配合 **get-change** 检查传播状态。在某些命令中，托管区域 ID 必须带上 **/hostedzone/** 前缀。Route 53 有 API 速率限制，可能影响批量操作。

# HISTORY

Amazon Route 53 于 **2010 年 12 月**作为 AWS 基础设施服务的一部分推出。其名称源自 TCP/UDP 端口 53，即 DNS 服务器请求所使用的端口。AWS CLI 对 Route 53 的支持随 AWS CLI 工具一同推出，此后持续扩展，陆续支持了 DNSSEC（2020 年）、CIDR 集合和流量策略等功能。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-s3](/man/aws-s3)(1), [dig](/man/dig)(1), [nslookup](/man/nslookup)(1)
