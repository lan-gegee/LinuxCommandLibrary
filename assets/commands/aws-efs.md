# TAGLINE

管理 Amazon Elastic File System 资源

# TLDR

**列出所有文件系统**

```aws efs describe-file-systems```

**创建新的文件系统**

```aws efs create-file-system --creation-token [unique_token]```

**查看特定文件系统**

```aws efs describe-file-systems --file-system-id [fs-xxxxxxxx]```

**在子网中创建挂载目标**

```aws efs create-mount-target --file-system-id [fs-xxxxxxxx] --subnet-id [subnet-xxxxxxxx] --security-groups [sg-xxxxxxxx]```

**列出文件系统的挂载目标**

```aws efs describe-mount-targets --file-system-id [fs-xxxxxxxx]```

**删除文件系统**

```aws efs delete-file-system --file-system-id [fs-xxxxxxxx]```

**为不常访问存储添加生命周期策略**

```aws efs put-lifecycle-configuration --file-system-id [fs-xxxxxxxx] --lifecycle-policies TransitionToIA=AFTER_30_DAYS```

# SYNOPSIS

**aws efs** _subcommand_ [_options_]

# DESCRIPTION

**aws efs** 是 AWS CLI 的子命令，用于管理 Amazon Elastic File System——一项面向 EC2 实例和本地服务器的无服务器 NFS 文件系统。随着文件的增删，EFS 会自动伸缩。

文件系统通过挂载目标访问，挂载目标会在 VPC 子网中提供 IP 地址。多个 EC2 实例可以并发挂载同一个文件系统，因此 EFS 适合 Web 服务、内容管理和容器存储等共享工作负载。

EFS 支持两种存储类别：Standard 用于频繁访问的数据，Infrequent Access（IA）用于优化成本。生命周期策略会根据访问模式自动在两类存储之间移动文件。

# PARAMETERS

**describe-file-systems**
> 列出文件系统及其详情。

**create-file-system**
> 创建新的 EFS 文件系统。

**delete-file-system**
> 删除文件系统（必须为空）。

**describe-mount-targets**
> 列出文件系统的挂载目标。

**create-mount-target**
> 在子网中创建挂载目标。

**delete-mount-target**
> 删除挂载目标。

**put-lifecycle-configuration**
> 设置存储类别转换的生命周期策略。

**describe-lifecycle-configuration**
> 查看当前的生命周期策略。

**--file-system-id** _id_
> 文件系统标识符（fs-xxxxxxxx）。

**--creation-token** _token_
> 用于创建文件系统的幂等令牌。

**--subnet-id** _id_
> 挂载目标所在的子网。

**--security-groups** _ids_
> 挂载目标使用的安全组。

**--performance-mode** _mode_
> generalPurpose 或 maxIO。

**--throughput-mode** _mode_
> bursting、provisioned 或 elastic。

# CAVEATS

删除文件系统前需先删除其所有挂载目标。为实现高可用性，每个可用区应有一个挂载目标。安全组必须放行 NFS 流量（端口 2049）。性能模式在创建后无法更改。跨区域访问需要 VPC 对等连接或 Transit Gateway。

# HISTORY

Amazon EFS 在 **AWS re:Invent 2015** 上发布，并于 **2016 年 6 月** 正式可用，是 AWS 首个托管 NFS 服务。用于成本优化的 **Infrequent Access** 存储类别于 **2019 年** 加入。面向单可用区工作负载、成本更低的 **EFS One Zone** 存储类别于 **2021 年** 推出。弹性吞吐量模式于 **2022 年** 引入。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [mount](/man/mount)(8)
