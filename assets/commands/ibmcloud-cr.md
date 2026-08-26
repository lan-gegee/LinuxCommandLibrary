# TAGLINE

管理 IBM Cloud Container Registry

# TLDR

**登录镜像仓库**

```ibmcloud cr login```

**列出镜像**

```ibmcloud cr image-list```

**创建命名空间**

```ibmcloud cr namespace-add [namespace]```

**构建镜像**

```ibmcloud cr build -t [registry/namespace/image:tag] [.]```

**移除镜像**

```ibmcloud cr image-rm [image]```

**列出命名空间**

```ibmcloud cr namespace-list```

# SYNOPSIS

**ibmcloud cr** _command_ [_options_]

# PARAMETERS

_COMMAND_
> Container Registry 命令。

**login**
> 将本地 Docker 守护进程登录到 IBM Cloud 镜像仓库。

**image-list**
> 列出你账户/命名空间中的镜像。

**image-rm** _IMAGE_
> 从镜像仓库中移除一个或多个镜像。

**image-tag** _SRC_ _DST_
> 为现有镜像添加新标签。

**namespace-add** _NAME_
> 创建命名空间。

**namespace-list**
> 列出目标账户中的命名空间。

**namespace-rm** _NAME_
> 删除命名空间（必须为空）。

**build** _CONTEXT_
> 使用 IBM Cloud 的远程构建器构建容器镜像并推送结果。

**va** _IMAGE_
> 显示镜像的漏洞顾问（Vulnerability Advisor）结果。

**quota**
> 显示账户的存储和拉取流量配额。

**region-set** _REGION_
> 切换镜像仓库区域（例如 _us-south_、_eu-de_、_jp-tok_）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ibmcloud cr** 管理 IBM Cloud Container Registry。它提供私有 Docker 镜像存储和漏洞扫描功能。

该工具管理命名空间、镜像和仓库身份验证。它与 IBM Cloud Kubernetes Service 集成。

# CAVEATS

需要安装 Registry 插件。受命名空间配额限制。提供漏洞扫描功能。

# HISTORY

ibmcloud cr 是 **IBM Cloud** CLI 的 Container Registry 插件。

# SEE ALSO

[ibmcloud](/man/ibmcloud)(1), [docker](/man/docker)(1), [ibmcloud-ks](/man/ibmcloud-ks)(1)
