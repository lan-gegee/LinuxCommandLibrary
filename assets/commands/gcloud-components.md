# TAGLINE

Google Cloud SDK 组件管理器

# TLDR

**列出可用组件**

```gcloud components list```

**安装组件**

```gcloud components install [kubectl]```

**更新所有组件**

```gcloud components update```

**移除组件**

```gcloud components remove [component-id]```

**安装多个组件**

```gcloud components install [kubectl] [gke-gcloud-auth-plugin]```

# SYNOPSIS

**gcloud components** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 操作：list、install、update、remove、reinstall、repositories、copy-bundled-python。

**list**
> 显示可用与已安装组件及其大小和当前版本。

**install** _COMPONENT_...
> 安装一个或多个组件（及其依赖）。

**update**
> 将所有已安装组件更新到最新的可用版本。可用 **--version** 固定到特定 SDK 版本。

**remove** _COMPONENT_...
> 卸载一个或多个组件。

**reinstall**
> 重装 SDK：移除所有组件并全部恢复到最新版本。

**repositories**
> 管理额外的组件仓库（添加、列出、移除），用于受测者预览版发布。

**copy-bundled-python**
> 将自带的 Python 解释器复制到用户指定的位置。

**--quiet**, **-q**
> 禁用交互式提示。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gcloud components** 管理 Google Cloud SDK 的模块化组件系统。SDK 采用"核心 + 组件"架构，最小化的基础安装可按需扩展更多工具。

常见的可选组件包括管理 Kubernetes 的 kubectl、操作 Cloud Storage 的 gsutil、与 BigQuery 交互的 bq，以及各语言专用的 App Engine 运行时。这种模块化方式保持了初始 SDK 安装的精简，同时允许针对特定工作流进行扩展。

update 命令让所有已安装组件保持最新功能和缺陷修复。组件管理在本地跟踪，因此不同机器可以根据各自的使用场景拥有不同的组件集合。某些组件之间存在依赖关系，系统会在安装时自动处理。

# CAVEATS

更新可能改变行为。部分组件存在依赖关系。可能需要管理员权限。

# SEE ALSO

[gcloud](/man/gcloud)(1), [gcloud-help](/man/gcloud-help)(1)
