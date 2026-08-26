# TAGLINE

管理简化版的虚拟服务器、数据库和存储。

# TLDR

**创建新实例**（虚拟专用服务器）

```aws lightsail create-instances --instance-names [my-instance] --availability-zone [us-east-1a] --blueprint-id [amazon_linux_2] --bundle-id [nano_2_0]```

**列出所有实例**

```aws lightsail get-instances```

**获取实例状态和公网 IP**

```aws lightsail get-instance --instance-name [my-instance]```

**停止实例**

```aws lightsail stop-instance --instance-name [my-instance]```

**为实例创建快照**

```aws lightsail create-instance-snapshot --instance-name [my-instance] --instance-snapshot-name [my-snapshot]```

**在实例上开放端口**

```aws lightsail open-instance-public-ports --instance-name [my-instance] --port-info fromPort=[80],toPort=[80],protocol=[tcp]```

**分配静态 IP 并附加到实例**

```aws lightsail allocate-static-ip --static-ip-name [my-ip] && aws lightsail attach-static-ip --static-ip-name [my-ip] --instance-name [my-instance]```

**创建托管数据库**

```aws lightsail create-relational-database --relational-database-name [my-db] --availability-zone [us-east-1a] --relational-database-blueprint-id [mysql_8_0] --relational-database-bundle-id [micro_2_0] --master-database-name [mydb] --master-username [admin]```

# SYNOPSIS

**aws lightsail** _command_ [_options_]

# DESCRIPTION

**aws lightsail** 是 Amazon Lightsail 的 AWS CLI 接口。Lightsail 是一个面向开发者的简化云平台，以可预测的价格提供虚拟服务器、存储、数据库和网络，并为常见应用提供预配置蓝图。

Lightsail 提供实例、容器、托管数据库、对象存储、负载均衡器、CDN 分发和 DNS 管理。它面向不需要 EC2 及其他 AWS 服务全部灵活性的较简单工作负载。

# COMMANDS

**create-instances**
> 启动新的虚拟专用服务器

**get-instances**
> 列出所有实例

**get-instance**
> 获取特定实例的详情

**start-instance**
> 启动已停止的实例

**stop-instance**
> 停止运行中的实例

**reboot-instance**
> 重启实例

**create-instance-snapshot**
> 创建备份快照

**allocate-static-ip**
> 预留静态 IP 地址

**create-relational-database**
> 创建托管数据库

**create-bucket**
> 创建对象存储桶

**create-load-balancer**
> 创建负载均衡器

**open-instance-public-ports**
> 在实例上开放防火墙端口

**delete-instance**
> 删除实例

**get-bundles**
> 列出可用的实例套餐（bundle）

**get-blueprints**
> 列出可用的操作系统/应用蓝图

# CAVEATS

Lightsail 实例无法直接转换为 EC2 实例。资源限制比标准 AWS 服务更严格。与其他 AWS 服务建立 VPC 对等连接需要额外设置。快照仅能存储在同一区域内。

# HISTORY

Amazon Lightsail 于 **2016 年 11 月** 作为简化的 AWS 入门平台推出。容器服务于 **2020 年** 加入。该服务在保持简单定价模式的同时，已扩展至托管数据库、对象存储、CDN 分发和域名管理。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-ec2](/man/aws-ec2)(1)
