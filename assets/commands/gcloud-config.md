# TAGLINE

gcloud CLI 配置管理

# TLDR

**设置默认项目**

```gcloud config set project [project-id]```

**设置默认的 Compute Engine 大区和区域**

```gcloud config set compute/region [us-central1] && gcloud config set compute/zone [us-central1-a]```

**获取某个属性的值**

```gcloud config get-value [project]```

**取消某个属性**

```gcloud config unset [compute/zone]```

**列出活动配置中的所有属性**

```gcloud config list```

**创建新的命名配置**

```gcloud config configurations create [name]```

**激活命名配置**

```gcloud config configurations activate [name]```

**列出所有配置**

```gcloud config configurations list```

# SYNOPSIS

**gcloud config** _command_ [_options_]

# PARAMETERS

**set** _SECTION/PROPERTY_ _VALUE_
> 将配置属性设置为给定值。

**get-value** _SECTION/PROPERTY_
> 打印某个属性的值。

**unset** _SECTION/PROPERTY_
> 从活动配置中移除某个属性。

**list**
> 列出活动配置中的所有属性。

**configurations create** _NAME_
> 创建新的命名配置。

**configurations activate** _NAME_
> 切换到命名配置。

**configurations delete** _NAME_
> 删除命名配置。不能删除当前活动的配置。

**configurations describe** _NAME_
> 显示命名配置的详细信息。

**configurations list**
> 列出所有可用配置。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gcloud config** 管理 gcloud 命令行工具的持久配置属性。通过此命令设置的属性将成为所有 gcloud 命令使用的默认值，除非被命令行标志显式覆盖。

常见属性包括默认项目、Compute Engine 大区与区域以及活动账号。这些默认值免去了在每条命令中重复输入常用值的麻烦，显著简化日常工作的命令长度。

命名配置让你能管理多套相互独立的属性集，方便在不同项目、账号或环境之间切换。每个配置都是一组完整的属性值，一条命令即可激活。对于跨多个 GCP 项目或组织工作的开发者而言，这一点至关重要，可避免在错误的项目上下文中误执行命令。

# CAVEATS

单条命令的选项优先于配置。配置仅对当前用户有效。某些属性要求有效值。活动配置无法删除。

# HISTORY

gcloud config 属于 **Google Cloud SDK** 配置系统，为 CLI 提供持久设置管理。

# SEE ALSO

[gcloud](/man/gcloud)(1), [gcloud-auth](/man/gcloud-auth)(1), [gcloud-init](/man/gcloud-init)(1), [gcloud-components](/man/gcloud-components)(1)
