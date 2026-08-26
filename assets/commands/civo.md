# TAGLINE

面向 Kubernetes 与基础设施的 Civo 云平台 CLI

# TLDR

**创建 Kubernetes 集群**

```civo kubernetes create [cluster-name]```

**带选项创建集群**

```civo kubernetes create [cluster-name] --nodes [3] --size [g4s.kube.medium]```

**列出集群**

```civo kubernetes list```

**显示集群详情**

```civo kubernetes show [cluster-name]```

**保存 kubeconfig**

```civo kubernetes config [cluster-name] --save```

**删除集群**

```civo kubernetes delete [cluster-name]```

**创建实例**

```civo instance create [name]```

**列出区域**

```civo region list```

# SYNOPSIS

**civo** [_options_] _command_ [_subcommand_] [_arguments_]

# DESCRIPTION

**civo** 是 Civo 云平台的 CLI，可通过 Civo API 管理 Kubernetes 集群、实例、网络及其他云资源。

# COMMANDS

**kubernetes**
> 管理 Kubernetes 集群

**instance**
> 管理计算实例

**network**
> 管理网络

**firewall**
> 管理防火墙

**volume**
> 管理块存储

**loadbalancer**
> 管理负载均衡器

**database**
> 管理数据库

**objectstore**
> 管理对象存储

**region**
> 管理区域

**apikey**
> 管理 API 密钥

# KUBERNETES OPTIONS

**-n**, **--nodes** _count_
> 节点数量（默认：3）

**-s**, **--size** _size_
> 节点规格（默认：g4s.kube.medium）

**-v**, **--version** _version_
> K3s 版本

**--switch**
> 将 kubectl 上下文切换到新集群

**-c**, **--create-firewall**
> 创建所有端口均开放的防火墙

# GLOBAL OPTIONS

**-o**, **--output** _format_
> 输出格式：json、human、custom

**--region** _name_
> 目标区域

**-y**, **--yes**
> 自动确认提示

**--config** _file_
> 配置文件路径

# CONFIGURATION

**~/.civo.json**
> 存储 API 密钥、默认区域和 CLI 偏好设置。

# CAVEATS

需要已配置的 Civo API 密钥。保存时 kubeconfig 会合并到 ~/.kube/config。开源 CLI 可在 GitHub 获取。

# INSTALL

```nix: nix profile install nixpkgs#civo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [terraform](/man/terraform)(1)

# RESOURCES

```[Source code](https://github.com/civo/cli)```

```[Documentation](https://www.civo.com/docs/overview/civo-cli)```

<!-- verified: 2026-06-22 -->
