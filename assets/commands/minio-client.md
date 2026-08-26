# TAGLINE

管理 MinIO 和 S3 存储

# TLDR

**设置别名**

```mc alias set [myminio] [https://minio.example.com] [access_key] [secret_key]```

**列出存储桶**

```mc ls [myminio]```

**复制文件**

```mc cp [file.txt] [myminio/bucket/]```

**镜像目录**

```mc mirror [local/] [myminio/bucket/]```

**删除文件**

```mc rm [myminio/bucket/file.txt]```

**创建存储桶**

```mc mb [myminio/newbucket]```

# SYNOPSIS

**mc** _command_ [_options_] [_args_]

# PARAMETERS

_COMMAND_
> MinIO 客户端命令。

**alias**
> 管理服务器别名。

**ls**
> 列出对象。

**cp**
> 复制对象。

**mirror**
> 同步目录。

**rm**
> 删除对象。

**--help**
> 显示帮助信息。

# DESCRIPTION

**minio-client**（mc）管理 MinIO 和 S3 存储。它为对象存储提供文件操作。

该工具可用于 MinIO 服务器和 AWS S3。支持多种云服务提供商。

# CAVEATS

先配置别名。兼容 S3。与 Midnight Commander 的 mc 不同。

# HISTORY

MinIO Client 由 **MinIO** 创建，用于管理跨云提供商的对象存储。

# INSTALL

```apt: sudo apt install minio-client```

```pacman: sudo pacman -S minio-client```

```zypper: sudo zypper install minio-client```

```nix: nix profile install nixpkgs#minio-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[minio-server](/man/minio-server)(1), [aws](/man/aws)(1), [s3cmd](/man/s3cmd)(1)
