# TAGLINE

管理 Amazon Elastic Kubernetes Service 集群

# TLDR

**创建新的 EKS 集群**

```aws eks create-cluster --name [my-cluster] --role-arn [arn:aws:iam::account:role/eks-role] --resources-vpc-config subnetIds=[subnet-1],[subnet-2],securityGroupIds=[sg-123]```

**列出账户中的所有 EKS 集群**

```aws eks list-clusters```

**查看集群及其状态**

```aws eks describe-cluster --name [my-cluster]```

**更新 kubeconfig 以便用 kubectl 访问集群**

```aws eks update-kubeconfig --name [my-cluster]```

**创建托管节点组**

```aws eks create-nodegroup --cluster-name [my-cluster] --nodegroup-name [my-nodes] --node-role [arn:aws:iam::account:role/node-role] --subnets [subnet-1] [subnet-2] --instance-types [t3.medium]```

**列出集群上已安装的附加组件**

```aws eks list-addons --cluster-name [my-cluster]```

**删除集群**

```aws eks delete-cluster --name [my-cluster]```

# SYNOPSIS

**aws eks** _command_ [_options_]

# DESCRIPTION

**aws eks** 是 Amazon Elastic Kubernetes Service（EKS）的 AWS CLI 接口。EKS 是一项托管 Kubernetes 服务，其控制平面横跨多个 AWS 可用区运行，并自动检测和替换不健康的控制平面节点。

EKS 与 AWS 的网络（VPC）、安全（IAM）、负载均衡（ELB）和存储（EBS/EFS）服务深度集成。它支持托管节点组、自管理节点，以及用于无服务器容器的 AWS Fargate。

# COMMANDS

**create-cluster**
> 创建新的 EKS 集群

**delete-cluster**
> 删除 EKS 集群

**describe-cluster**
> 获取集群详情和状态

**list-clusters**
> 列出账户中的所有集群

**update-kubeconfig**
> 配置 kubectl 以访问集群

**create-nodegroup**
> 创建托管节点组

**delete-nodegroup**
> 删除节点组

**list-nodegroups**
> 列出集群中的节点组

**create-addon**
> 安装集群附加组件

**create-fargate-profile**
> 为无服务器 Pod 创建 Fargate 配置文件

**update-cluster-version**
> 升级 Kubernetes 版本

# CAVEATS

创建集群需要 10-15 分钟。控制平面和节点组必须分别且按顺序升级。服务账户的 IAM 角色（IRSA）需要先配置 OIDC 提供方。同一个节点组内不能混用多种实例类型。

# HISTORY

Amazon EKS 于 **2018 年 6 月** 作为托管 Kubernetes 服务推出。Fargate 支持于 **2019 年 12 月** 加入，托管节点组则在同年早些时候推出。面向本地部署的 EKS Anywhere 于 **2021 年** 推出，Pod Identity 于 **2023 年** 简化了 IAM 访问。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [kubectl](/man/kubectl)(1), [aws-ecr](/man/aws-ecr)(1), [eksctl](/man/eksctl)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/eks/index.html)```

<!-- verified: 2026-06-18 -->
