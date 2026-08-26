# TAGLINE

MinIO 客户端

# TLDR

**列出存储桶**

```mc ls [alias]```

**创建存储桶**

```mc mb [alias/bucket]```

**复制文件**

```mc cp [file] [alias/bucket/]```

**设置别名**

```mc alias set [name] [url] [access_key] [secret_key]```

**镜像目录**

```mc mirror [dir/] [alias/bucket/]```

**显示对象信息**

```mc stat [alias/bucket/object]```

# SYNOPSIS

**mc** _command_ [_options_] [_args_]

# PARAMETERS

_COMMAND_
> MinIO 操作。

**ls**
> 列出存储桶/对象。

**mb**
> 创建存储桶。

**cp**
> 复制对象。

**alias**
> 管理别名。

**mirror**
> 同步目录。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mc** 是 MinIO 客户端。它为 MinIO 及 S3 兼容服务提供云存储操作。

该工具管理存储桶、对象和策略。支持 AWS S3、GCS 和 MinIO 服务器。

# CAVEATS

需要先配置别名。兼容 S3。注意与 Midnight Commander 区分。

# HISTORY

mc（MinIO 客户端）由 **MinIO** 创建，用于管理跨云提供商的对象存储。

# SEE ALSO

[minio-server](/man/minio-server)(1), [aws](/man/aws)(1), [s3cmd](/man/s3cmd)(1)
