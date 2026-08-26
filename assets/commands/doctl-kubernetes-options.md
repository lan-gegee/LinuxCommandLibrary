# TAGLINE

枚举可用的 Kubernetes 配置取值

# TLDR

**列出 Kubernetes 版本**

```doctl kubernetes options versions```

**列出可用区域**

```doctl kubernetes options regions```

**列出节点规格**

```doctl kubernetes options sizes```

**以指定输出格式列出版本**

```doctl kubernetes options versions --format [slug]```

# SYNOPSIS

**doctl kubernetes options** _command_

# PARAMETERS

_COMMAND_
> 选项类型：versions、regions、sizes。

**versions**
> 列出可用的 Kubernetes 版本。

**regions**
> 列出支持 Kubernetes 的区域。

**sizes**
> 列出可用于节点池的机器规格。

**--format** _columns_
> 以逗号分隔的输出列列表。

**--no-header**
> 返回不带表头的原始数据。

**--help**
> 显示帮助信息。

# DESCRIPTION

**doctl kubernetes options** 枚举可与 DigitalOcean Kubernetes（DOKS）集群命令配合使用的有效取值。它帮助用户确定创建和修改集群时的有效值，例如受支持的 Kubernetes 版本、DOKS 可用的区域以及适合工作节点的机器规格。

使用这些选项可以确保集群配置有效，并有助于了解各区域的可用资源。

# CAVEATS

选项可能随 DigitalOcean 更新产品而变化。并非所有区域都提供所有规格。Kubernetes 版本有支持生命周期。

# HISTORY

doctl kubernetes options 是 **2018 年** DigitalOcean 推出托管 Kubernetes 服务（DOKS）时加入 **doctl** 的 Kubernetes 管理命令的一部分。

# SEE ALSO

[doctl](/man/doctl)(1), [kubectl](/man/kubectl)(1), [doctl-kubernetes-cluster](/man/doctl-kubernetes-cluster)(1)
