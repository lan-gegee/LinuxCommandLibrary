# TAGLINE

列出 Cloud Logging 中可用的日志

# TLDR

**列出日志**

```gcloud logging logs list```

**限制数量列出日志**

```gcloud logging logs list --limit [10]```

**在指定项目中列出日志**

```gcloud logging logs list --project [project_id]```

**以 JSON 格式列出日志**

```gcloud logging logs list --format json```

# SYNOPSIS

**gcloud** **logging** **logs** **list** [_options_]

# PARAMETERS

**--limit** _num_
> 最大结果数。

**--project** _id_
> 项目 ID。

**--format** _format_
> 输出格式。

# DESCRIPTION

**gcloud logging logs list** 显示 Google Cloud 项目的 Cloud Logging 服务中所有可用的日志流。每个日志名称代表一个独立的日志条目流，通常对应特定的服务、应用程序或资源。

当日志服务写入条目时会自动创建日志。常见的日志名称包括来自 Compute Engine 实例、App Engine 应用程序、Kubernetes 集群以及其他 GCP 服务的日志。用户应用程序也可以写入自定义日志。

在使用其他日志命令读取内容之前，该命令可用于发现有哪些日志可用。其输出有助于确定查询或跟踪特定应用程序或服务日志时应使用的正确日志名称。

# SEE ALSO

