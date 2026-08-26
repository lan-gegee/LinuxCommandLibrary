# TAGLINE

设置 gcloud 持久配置属性

# TLDR

**设置默认项目**

```gcloud config set project [project-id]```

**设置默认大区**

```gcloud config set compute/region [us-central1]```

**设置默认区域**

```gcloud config set compute/zone [us-central1-a]```

**设置账号**

```gcloud config set account [email@example.com]```

**禁用使用情况报告**

```gcloud config set disable_usage_reporting true```

# SYNOPSIS

**gcloud config set** _property_ _value_

# PARAMETERS

_PROPERTY_
> 配置属性名称。

_VALUE_
> 要设置的值。

**project**
> 默认项目 ID。

**compute/region**
> 默认 Compute 大区。

**compute/zone**
> 默认 Compute 区域。

**account**
> 当前活动账号。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gcloud config set** 为 gcloud 配置属性赋值，建立适用于后续所有 gcloud 命令的默认值。这样就无需在每次执行时重复指定项目 ID、大区和区域等常见参数。

属性采用分层命名方案：有些作用于特定服务（如用于 Compute Engine 操作的 compute/region），另一些则全局生效（如 project）。该命令会校验属性名，但可能不会立即校验值的有效性——无效的值可能导致后续命令报错。

命令行标志始终优先于已配置的属性，因此可以临时覆盖而不改变存储的配置。属性保存在活动配置中，切换配置即改变生效的属性值。这套基于属性的机制是高效使用 gcloud 的关键，对跨多个区域或项目管理资源的用户尤为重要。

# CAVEATS

命令行选项会覆盖设置。无效的值可能在之后引发错误。设置按配置隔离。

# HISTORY

gcloud config set 是 **Google Cloud SDK** 配置系统的属性设置器，为 CLI 操作提供默认值能力。

# SEE ALSO

[gcloud-config](/man/gcloud-config)(1), [gcloud](/man/gcloud)(1)

# RESOURCES

```[Documentation](https://cloud.google.com/sdk/gcloud/reference/config/set)```

<!-- verified: 2026-07-15 -->
