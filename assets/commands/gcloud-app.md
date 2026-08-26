# TAGLINE

Google App Engine 管理命令

# TLDR

**部署应用**

```gcloud app deploy```

**浏览已部署的应用**

```gcloud app browse```

**查看日志**

```gcloud app logs tail```

**列出服务**

```gcloud app services list```

**描述应用**

```gcloud app describe```

在版本间**分配流量**

```gcloud app services set-traffic [service] --splits [v1=0.5,v2=0.5]```

**删除某个版本**

```gcloud app versions delete [version-id]```

# SYNOPSIS

**gcloud app** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 操作：deploy、browse、logs、services 等。

**deploy** [_YAML_]
> 部署应用。

**browse**
> 在浏览器中打开应用。

**logs tail**
> 流式跟踪应用日志。

**services list**
> 列出已部署的服务。

**versions list**
> 列出应用版本。

**describe**
> 显示应用信息。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gcloud app** 为 Google App Engine 应用提供全面的管理能力。App Engine 是 Google 最早的平台即服务（PaaS）产品，让开发者无需管理底层基础设施即可部署 Web 应用。

该命令组覆盖完整的应用生命周期，包括从 app.yaml 配置文件部署、版本管理以及多个版本间的流量路由。这使零停机部署和通过流量分割实现的灰度发布成为可能。

监控功能包括流式日志和查看应用状态。browse 命令可在浏览器中快速访问已部署的应用。gcloud app 与其他 GCP 服务集成，方便将 App Engine 应用连接到数据库、存储和其他云资源。

# CAVEATS

需要启用 App Engine。部署可能需要一些时间。费用按使用量计算。

# HISTORY

gcloud app 属于 **Google Cloud SDK**，用于管理 App Engine——Google 最早的无需管理基础设施即可运行 Web 应用的平台即服务产品。

# SEE ALSO

[gcloud](/man/gcloud)(1), [gcloud-compute](/man/gcloud-compute)(1)
