# TAGLINE

Exoscale S3 兼容对象存储管理

# TLDR

**列出存储桶**

```exo storage list```

**创建存储桶**

```exo storage mb --zone [ch-gva-2] sos://[bucket-name]```

**上传文件**

```exo storage upload [file] sos://[bucket]/[path]```

**下载文件**

```exo storage download sos://[bucket]/[file] [local_path]```

**列出存储桶内容**

```exo storage list sos://[bucket]```

**删除对象**

```exo storage delete sos://[bucket]/[file]```

# SYNOPSIS

**exo** **storage** _command_ [_options_]

# SUBCOMMANDS

**list**
> 列出存储桶或对象。

**mb**
> 创建（make）存储桶。

**rb**
> 删除（remove）存储桶。

**upload**
> 上传文件到存储桶。

**download**
> 从存储桶下载文件。

**delete**
> 删除对象。

**show**
> 显示存储桶或对象的详情。

**presign**
> 为对象生成预签名 URL。

**setacl**
> 设置存储桶/对象的 ACL 权限。

**cors**
> 管理 CORS 配置（add、delete）。

**headers**
> 管理自定义 HTTP 头（add、delete）。

**metadata**
> 管理对象元数据（add、delete）。

**bucket**
> 管理存储桶设置（object-ownership、replication、versioning）。

**purge**
> 清空存储桶中的所有对象。

# DESCRIPTION

**exo storage** 用于管理 Exoscale Simple Object Storage（SOS），一种 S3 兼容的对象存储服务。可通过 HTTP 访问存取文件。

SOS 提供可扩展的对象存储，适用于备份、静态资源、媒体文件和数据湖。由于兼容 S3，它可以与 s3cmd、rclone 和 AWS SDK 等标准工具配合使用。

该工具支持存储桶管理、文件上传/下载、用于临时访问的预签名 URL，以及面向 Web 应用的 CORS 配置。

# INSTALL

```dnf: sudo dnf install exo```

```pacman: sudo pacman -S exo```

```apk: sudo apk add exoscale```

```nix: nix profile install nixpkgs#exo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[exo](/man/exo)(1), [aws-s3](/man/aws-s3)(1)
