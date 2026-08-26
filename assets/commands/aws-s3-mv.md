# TAGLINE

在 S3 存储桶之间及与本地之间移动文件

# TLDR

将**本地文件移动到** S3

```aws s3 mv [file.txt] s3://[bucket-name]/```

将 **S3 对象移动到**另一个 S3 位置

```aws s3 mv s3://[bucket-name]/[file.txt] s3://[bucket-name]/[new-path/file.txt]```

**下载并删除** S3 对象

```aws s3 mv s3://[bucket-name]/[file.txt] [./local-file.txt]```

**递归移动**目录到 S3

```aws s3 mv [./local-dir] s3://[bucket-name]/[prefix/] --recursive```

**移动时排除**某些文件

```aws s3 mv [./local-dir] s3://[bucket-name]/ --recursive --exclude "*.log"```

**预览移动操作**而不实际执行

```aws s3 mv [./local-dir] s3://[bucket-name]/ --recursive --dryrun```

# SYNOPSIS

**aws s3 mv** _source_ _destination_ [_options_]

# DESCRIPTION

**aws s3 mv** 在本地文件系统与 Amazon S3 之间或 S3 位置之间移动文件。该命令先将源复制到目标，然后删除源对象或文件。

源和目标可以是 LocalPath 或 S3Uri（s3://bucket-name/key）。对于 S3 到 S3 的移动，命令会先执行服务器端复制，再删除源。

# PARAMETERS

**--recursive**
> 移动指定目录或 S3 前缀下的所有文件和对象

**--dryrun**
> 显示将要执行的操作但不实际执行

**--quiet**
> 在移动过程中抑制输出

**--include** _pattern_
> 包含匹配模式的文件（与 --exclude 配合使用）

**--exclude** _pattern_
> 从移动操作中排除匹配模式的文件

**--acl** _value_
> 设置访问控制列表：private、public-read、public-read-write、authenticated-read

**--storage-class** _value_
> 指定存储类别：STANDARD、REDUCED_REDUNDANCY、STANDARD_IA、ONEZONE_IA、INTELLIGENT_TIERING、GLACIER、DEEP_ARCHIVE、GLACIER_IR

**--sse** _value_
> 启用服务器端加密：AES256 或 aws:kms

**--sse-kms-key-id** _value_
> 用于服务器端加密的客户托管 AWS KMS 密钥 ID

**--content-type** _value_
> 对象的显式内容类型（覆盖 MIME 类型猜测）

**--metadata** _map_
> 要附加到对象的键值元数据对

**--cache-control** _value_
> 指定请求/响应链路上的缓存行为

**--no-overwrite**
> 防止覆盖目标处已有的文件

**--only-show-errors**
> 输出中仅显示错误和警告

**--no-progress**
> 不显示文件传输进度

**--follow-symlinks** | **--no-follow-symlinks**
> 上传时是否跟随符号链接（默认：跟随）

**--no-guess-mime-type**
> 不尝试猜测上传文件的 MIME 类型

**--validate-same-s3-paths**
> 校验源和目标解析到不同的位置（安全检查）

# CAVEATS

使用接入点 ARN 或别名时，确保源和目标解析到不同的存储桶，以防误删自身。建议使用 **--validate-same-s3-paths** 以保安全。源只有在复制成功后才会被删除；如果复制失败，源保持原样。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws-s3](/man/aws-s3)(1), [aws-s3-cp](/man/aws-s3-cp)(1), [aws-s3-rm](/man/aws-s3-rm)(1), [mv](/man/mv)(1)
