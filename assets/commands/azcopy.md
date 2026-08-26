# TAGLINE

面向 Azure Storage 的高性能数据传输工具

# TLDR

**将本地文件复制到** Azure Blob Storage

```azcopy copy [path/to/file] "https://[account].blob.core.windows.net/[container]/[blob]?[SAS_token]"```

**将 Blob 下载到**本地文件系统

```azcopy copy "https://[account].blob.core.windows.net/[container]/[blob]?[SAS_token]" [path/to/destination]```

**将本地目录同步到**容器

```azcopy sync [path/to/directory] "https://[account].blob.core.windows.net/[container]?[SAS_token]"```

**在存储账户之间复制**

```azcopy copy "https://[source].blob.core.windows.net/[container]?[SAS]" "https://[dest].blob.core.windows.net/[container]?[SAS]" --recursive```

**按模式匹配复制**

```azcopy copy "https://[account].blob.core.windows.net/[container]/*.txt?[SAS]" [path/to/destination]```

**列出容器中的 Blob**

```azcopy list "https://[account].blob.core.windows.net/[container]?[SAS_token]"```

**使用 Azure AD 登录**

```azcopy login```

**显示传输作业**

```azcopy jobs list```

**针对容器做吞吐量基准测试**

```azcopy bench "https://[account].blob.core.windows.net/[container]?[SAS_token]"```

# SYNOPSIS

**azcopy** _command_ [_options_]

# DESCRIPTION

**AzCopy** 是一个命令行实用工具，用于与 Azure Blob Storage、Azure Files 和 Azure Data Lake Storage 之间进行高性能数据传输。它利用并行连接和自动重试逻辑实现可靠的传输。

AzCopy 支持在本地文件系统与 Azure 存储之间、不同 Azure 存储账户之间以及 AWS S3 与 Azure 之间复制数据。身份验证可使用 SAS 令牌、Azure AD 或服务主体。

sync 命令提供单向同步，只复制新增或有修改的文件。复制操作可以保留元数据和访问层，并能处理递归的目录结构。

# PARAMETERS

**copy**
> 在位置之间复制文件或 Blob。

**sync**
> 将源同步到目标。

**list**
> 列出 Blob 或文件。

**login**
> 使用 Azure AD 进行身份验证。

**logout**
> 清除缓存的凭据。

**jobs list**
> 显示传输作业。

**jobs show**
> 获取特定作业的详情。

**jobs resume**
> 恢复失败的传输。

**remove**
> 删除 Blob 或文件。

**bench**
> 对存储目标运行吞吐量基准测试。

**make**
> 创建容器或文件共享。

**--recursive**
> 包含子目录（默认 false）。

**--include-pattern** _pattern_
> 只包含匹配分号分隔模式列表的文件。

**--exclude-pattern** _pattern_
> 排除匹配分号分隔模式列表的文件。

**--overwrite** _mode_
> true、false、prompt 或 ifSourceNewer（默认 true）。

**--put-md5**
> 为每个上传的 Blob 计算并存储 MD5 哈希（默认 false）。

**--check-md5** _mode_
> 下载时校验 MD5：NoCheck、LogOnly、FailIfDifferent 或 FailIfDifferentOrMissing（默认 FailIfDifferent）。

**--from-to** _value_
> 强制指定传输方向，例如 LocalBlob 或 BlobLocal。

**--as-subdir**
> 将源目录作为子目录放到目标位置（默认 true）。

**--preserve-permissions**
> 保留 ACL 和权限（SMB 或 POSIX）。

**--block-size-mb** _size_
> 上传和下载使用的块大小，单位 MiB（默认 0，自动）。

**--cap-mbps** _rate_
> 以兆比特每秒为单位限制传输速率（默认 0，不限制）。

**--dry-run**
> 显示将要传输的内容但不实际执行。

**--log-level** _level_
> 日志详细程度：DEBUG、INFO、WARNING、ERROR 或 NONE（默认 INFO）。

# CAVEATS

SAS 令牌必须具备适当的权限（读取、写入、列出、删除）。URL 必须加引号，以防止 shell 解释特殊字符。同步是单向的，且默认不删除目标端的文件。大文件会自动分块传输。性能取决于网络带宽和存储账户的限制。

# HISTORY

**AzCopy v10** 于 **2018** 年发布，是对早期版本的完全重写，从 .NET 迁移到 Go 以获得跨平台支持，取代了仅限 Windows 的 AzCopy v8。该工具陆续增加了 Azure AD 身份验证、S3 到 Azure 迁移、bench 基准测试命令以及与 Azure 存储生命周期的集成等功能。它仍是批量 Azure 存储操作的推荐工具。

# INSTALL

```pacman: sudo pacman -S azcopy```

```brew: brew install azcopy```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [az-storage](/man/az-storage)(1), [rsync](/man/rsync)(1), [rclone](/man/rclone)(1)

# RESOURCES

```[Source code](https://github.com/Azure/azure-storage-azcopy)```

```[Documentation](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10)```

<!-- verified: 2026-06-19 -->
