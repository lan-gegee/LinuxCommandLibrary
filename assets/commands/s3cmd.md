# TAGLINE

Amazon S3 管理命令行工具

# TLDR

**配置 s3cmd**（交互式设置）

```s3cmd --configure```

**列出所有存储桶**

```s3cmd ls```

**列出存储桶的内容**

```s3cmd ls s3://[bucket_name]```

**创建存储桶**

```s3cmd mb s3://[bucket_name]```

**上传文件**

```s3cmd put [file] s3://[bucket_name]/```

**下载文件**

```s3cmd get s3://[bucket_name]/[file]```

**将本地目录同步到 S3**

```s3cmd sync [local_dir]/ s3://[bucket_name]/[path]/```

**删除文件**

```s3cmd del s3://[bucket_name]/[file]```

**删除存储桶**（必须为空）

```s3cmd rb s3://[bucket_name]```

# SYNOPSIS

**s3cmd** [_options_] _command_ [_parameters_]

# PARAMETERS

**ls** [_s3://bucket_]
> 列出存储桶或对象

**mb** _s3://bucket_
> 创建存储桶

**rb** _s3://bucket_
> 删除存储桶

**put** _file_ _s3://bucket/path_
> 上传文件

**get** _s3://bucket/path_ [_local_]
> 下载文件

**del**, **rm** _s3://bucket/path_
> 删除对象

**sync** _source_ _dest_
> 同步目录（本地到 S3 或 S3 到本地）

**cp** _src_ _dst_
> 复制对象

**mv** _src_ _dst_
> 移动对象

**info** _s3://bucket/object_
> 获取存储桶或对象的信息

**du** [_s3://bucket_]
> 查看磁盘用量

**la**
> 列出所有存储桶中的全部对象

**setacl** _s3://bucket/object_
> 修改访问控制列表

**signurl** _s3://bucket/object_ _expiry_
> 生成限时签名的 URL

**restore** _s3://bucket/object_
> 从 Glacier 存储恢复文件

**--configure**
> 交互式配置

**--recursive**, **-r**
> 递归操作

**--delete-removed**
> 同步时删除源中已不存在的文件

**--dry-run**, **-n**
> 显示将要执行的操作而不实际执行

**--acl-public**
> 将上传的文件设为公开

**--acl-private**
> 将上传的文件设为私有

**--exclude** _pattern_
> 排除匹配模式的文件

**--include** _pattern_
> 包含匹配模式的文件

**--storage-class** _CLASS_
> 设置存储类别（STANDARD、GLACIER、DEEP_ARCHIVE 等）

**--server-side-encryption**
> 使用 S3 托管的服务器端加密

**--skip-existing**
> 跳过目标位置已存在的文件

**--verbose**, **-v**
> 启用详细输出

**--limit-rate** _RATE_
> 限制上传/下载速度

**--config** _FILE_
> 使用指定的配置文件替代 ~/.s3cfg

# DESCRIPTION

**s3cmd** 是一款用于管理 Amazon S3 及兼容 S3 的存储服务的命令行工具。它为云端对象存储中的文件上传、下载和管理提供了熟悉的操作界面。

配置存储在 **~/.s3cfg** 中，包含访问密钥、加密设置和默认选项。运行 **--configure** 可进行交互式设置。

**sync** 命令在备份场景中尤为强大：它把目录镜像到 S3，并且只传输发生变化的文件。配合 **--delete-removed** 可以创建完全一致的镜像。

S3cmd 支持服务器端加密和大文件的多部分上传，还可用于 MinIO、DigitalOcean Spaces、Wasabi 等兼容 S3 的服务。

# CAVEATS

~/.s3cfg 中的 AWS 凭据应限制权限（600）。切勿把凭据提交到版本控制系统。

同步操作默认按大小和修改时间进行比较。使用 **--check-md5** 可进行校验和验证，但会降低速度。

大文件上传会自动使用多部分上传。对于超大文件，可增大 **--multipart-chunk-size-mb**。

存储桶名称必须在所有 AWS 账户间全局唯一，并遵循 DNS 命名规范。

# INSTALL

```dnf: sudo dnf install s3cmd```

```pacman: sudo pacman -S s3cmd```

```apk: sudo apk add s3cmd```

```zypper: sudo zypper install s3cmd```

```brew: brew install s3cmd```

```nix: nix profile install nixpkgs#s3cmd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aws](/man/aws)(1), [rclone](/man/rclone)(1), [gsutil](/man/gsutil)(1), [mc](/man/mc)(1)
