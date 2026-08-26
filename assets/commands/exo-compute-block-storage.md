# TAGLINE

Exoscale 持久块存储卷管理

# TLDR

**列出某可用区中的块存储卷**

```exo compute block-storage list --zone [ch-gva-2]```

**创建卷**

```exo compute block-storage create [name] --size [100] --zone [ch-gva-2]```

**显示卷详情**

```exo compute block-storage show [name]```

**将卷挂载到实例**

```exo compute block-storage attach [volume] [instance] --zone [ch-gva-2]```

**卸载卷**

```exo compute block-storage detach [volume] --zone [ch-gva-2]```

**删除卷**

```exo compute block-storage delete [name]```

# SYNOPSIS

**exo** **compute** **block-storage** _command_ [_options_]

# SUBCOMMANDS

**list**
> 列出块存储卷。

**create**
> 创建卷。

**show**
> 显示卷详情。

**attach**
> 挂载到实例。

**detach**
> 从实例卸载。

**update**
> 更新卷属性（重命名、调整大小、修改标签）。

**snapshot**
> 管理卷快照（创建、列出、查看、删除、更新）。

**delete**
> 删除卷。

# DESCRIPTION

**exo compute block-storage** 用于管理 Exoscale 块存储卷。卷提供可挂载到计算实例的持久化存储。

块存储卷在实例终止后依然存在，并且可以在实例之间移动。它们非常适合数据库、应用数据，以及任何需要独立于实例生命周期的持久化存储的工作负载。

卷可通过 **update** 子命令调整大小，并支持快照以用于备份和克隆。

# SEE ALSO

[exo-compute-instance](/man/exo-compute-instance)(1), [exo](/man/exo)(1)
