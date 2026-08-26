# TAGLINE

Backblaze B2 云存储官方命令行工具

# TLDR

**授权账户**

```b2 account authorize [applicationKeyId] [applicationKey]```

**上传文件到存储桶**

```b2 file upload [bucketName] [localFile] [remoteName]```

**从存储桶下载文件**

```b2 file download [b2://bucketName/fileName] [localPath]```

**列出存储桶中的文件**

```b2 ls [bucketName]```

**创建新存储桶**

```b2 bucket create [bucketName] [allPrivate]```

**将本地目录同步到 B2**

```b2 sync [localDir] b2://[bucketName]/[prefix]```

# SYNOPSIS

**b2** _command_ [_options_]

# PARAMETERS

**account authorize** _keyID_ _key_
> 使用应用密钥向 B2 授权。

**file upload** _bucket_ _local_ _remote_
> 将文件上传到存储桶。

**file download** _uri_ _local_
> 从 B2 下载文件。

**ls** _bucket_
> 列出存储桶中的文件。

**bucket create** _name_ _type_
> 创建存储桶（allPrivate 或 allPublic）。

**bucket delete** _name_
> 删除存储桶。

**sync** _source_ _destination_
> 在本地与 B2 之间或不同 B2 存储桶之间同步文件。

**file hide** _bucket_ _file_
> 隐藏文件（软删除）。

# DESCRIPTION

**b2-tools**（调用名为 **b2**）是 Backblaze B2 Cloud Storage 的官方命令行工具。它面向 B2 兼容 S3 的对象存储，提供文件上传、下载、同步以及存储桶管理等操作。

sync 命令可以高效地将本地目录镜像到 B2，只上传发生变化的文件。B2 提供价格实惠的云存储，并通过 Cloudflare 带宽联盟提供免费的外网流出流量。

# CAVEATS

使用前必须先使用应用密钥完成授权。大文件上传会自动分块。sync 命令通过 SHA1 哈希进行比较，因此首次同步大型目录可能较慢。B2 原生 URI 使用 `b2://` 前缀。

# HISTORY

**b2-tools** 是 **Backblaze** 为其 B2 Cloud Storage 服务开发的官方 CLI。该项目已在 GitHub 上开源，可通过 pip 以 `b2` 名称安装。

# INSTALL

```brew: brew install b2-tools```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[b2](/man/b2)(1), [rclone](/man/rclone)(1), [duplicity](/man/duplicity)(1)
