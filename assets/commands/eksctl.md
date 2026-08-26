# TAGLINE

AWS EKS 集群管理 CLI

# TLDR

**创建 EKS 集群**

```eksctl create cluster --name [cluster_name]```

**使用节点**配置创建

```eksctl create cluster --name [name] --nodes [3] --node-type [t3.medium]```

**列出集群**

```eksctl get clusters```

**删除集群**

```eksctl delete cluster --name [cluster_name]```

**创建节点组**

```eksctl create nodegroup --cluster [name] --name [ng-name]```

**伸缩节点组**

```eksctl scale nodegroup --cluster [name] --name [ng-name] --nodes [5]```

**更新 kubeconfig**

```eksctl utils write-kubeconfig --cluster [name]```

**从配置文件创建集群**

```eksctl create cluster -f [cluster.yaml]```

**升级控制平面**到新的 Kubernetes 版本

```eksctl upgrade cluster --name [name] --version [1.31] --approve```

# SYNOPSIS

**eksctl** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 操作：create、get、delete、scale、upgrade 等。

**create cluster** **--name** _NAME_
> 创建新的 EKS 集群。

**--nodes** _N_
> 工作节点数量。

**--node-type** _TYPE_
> 节点使用的 EC2 实例类型。

**--region** _REGION_
> AWS 区域。

**-f**, **--config-file** _FILE_
> 声明式 YAML 集群配置；大多数标志都有对应的字段。

**--dry-run**
> 打印 eksctl 将要应用的配置文件而不实际创建任何内容。

**delete cluster** **--name** _NAME_
> 删除集群。

**get clusters**
> 列出集群。

**--help**
> 显示帮助信息。

# DESCRIPTION

**eksctl** 是 Amazon EKS（Elastic Kubernetes Service）的官方 CLI。它简化了 EKS 集群及其关联资源的创建、管理和删除。

该工具负责处理复杂的 AWS 基础设施设置，包括 VPC、子网、安全组和 IAM 角色。集群可以通过 YAML 配置以声明式方式定义。

eksctl 支持托管节点组、Fargate 配置文件和集群升级等高级特性。

# CAVEATS

需要 AWS 凭证。集群创建需要时间。会产生 AWS 费用。某些操作需要特定的 IAM 权限。

# HISTORY

eksctl 由 **Weaveworks** 与 AWS 合作创建，于 **2018 年**发布以简化 EKS 集群管理。后来成为 EKS 的官方 CLI 工具。Weaveworks 于 2024 年停业后，该项目迁移到社区运营的 **eksctl-io** 组织并持续维护。

# INSTALL

```pacman: sudo pacman -S eksctl```

```zypper: sudo zypper install eksctl```

```brew: brew install eksctl```

```nix: nix profile install nixpkgs#eksctl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [aws](/man/aws)(1), [helm](/man/helm)(1)

# RESOURCES

```[Source code](https://github.com/eksctl-io/eksctl)```

```[Homepage](https://eksctl.io/)```

<!-- verified: 2026-07-14 -->
