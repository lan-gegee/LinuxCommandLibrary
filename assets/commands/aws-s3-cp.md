# TAGLINE

在 S3 存储桶与本地之间复制文件

# TLDR

将**本地文件复制到** S3 存储桶

```aws s3 cp [file.txt] s3://[bucket-name]/```

将 **S3 对象下载到**本地文件系统

```aws s3 cp s3://[bucket-name]/[file.txt] [./local-file.txt]```

在 S3 位置之间**复制对象**

```aws s3 cp s3://[source-bucket]/[file.txt] s3://[dest-bucket]/[file.txt]```

**递归复制**目录到 S3

```aws s3 cp [./local-dir] s3://[bucket-name]/[prefix/] --recursive```

以指定存储类别**复制**

```aws s3 cp [file.txt] s3://[bucket-name]/ --storage-class [STANDARD_IA]```

**复制时排除**某些文件

```aws s3 cp [./local-dir] s3://[bucket-name]/ --recursive --exclude "*.log"```

启用服务器端加密**上传**

```aws s3 cp [file.txt] s3://[bucket-name]/ --sse aws:kms --sse-kms-key-id [key-id]```

**预览复制操作**而不实际执行

```aws s3 cp [./local-dir] s3://[bucket-name]/ --recursive --dryrun```

# SYNOPSIS

**aws s3 cp** _source_ _destination_ [_options_]

# DESCRIPTION

**aws s3 cp** 在本地文件系统与 Amazon S3 之间或 S3 位置之间复制文件。源和目标可以是 LocalPath（本地文件/目录）或 S3Uri（s3://bucket-name/key）。

该命令支持单文件传输、递归目录复制以及与 S3 之间的流式数据传输。对大文件会自动进行分段上传（multipart upload），并可在复制过程中保留或修改对象元数据。

# PARAMETERS

**--recursive**
> 复制指定目录或 S3 前缀下的所有文件和对象

**--dryrun**
> 显示将要执行的操作但不实际执行

**--quiet**
> 在复制过程中抑制所有输出

**--include** _pattern_
> 包含匹配模式的文件（与 --exclude 配合使用）

**--exclude** _pattern_
> 从复制操作中排除匹配模式的文件

**--acl** _value_
> 设置访问控制列表：private、public-read、public-read-write、authenticated-read、bucket-owner-full-control

**--storage-class** _value_
> 指定存储类别：STANDARD、REDUCED_REDUNDANCY、STANDARD_IA、ONEZONE_IA、INTELLIGENT_TIERING、GLACIER、DEEP_ARCHIVE、GLACIER_IR

**--sse** _value_
> 启用服务器端加密：AES256 或 aws:kms

**--sse-kms-key-id** _value_
> 用于 AWS KMS 服务器端加密的 KMS 密钥 ID

**--metadata** _value_
> 与 S3 对象一起存储的自定义元数据（JSON 格式）

**--metadata-directive** _value_
> COPY 或 REPLACE：是复制源元数据还是替换它（S3 到 S3 的复制）

**--content-type** _value_
> 覆盖上传对象的 MIME 类型

**--expires** _value_
> 设置 Expires 头（如 2024-12-31T23:59:59Z）

**--no-overwrite**
> 防止覆盖目标处已有的文件

**--expected-size** _value_
> 预期的流大小（字节；超过 50GB 的流必须提供）

**--follow-symlinks** / **--no-follow-symlinks**
> 复制时跟随符号链接（默认：跟随）

# CAVEATS

递归复制目录时，应一致地使用末尾斜杠来控制前缀行为。**--include** 和 **--exclude** 的模式匹配与顺序有关。与 Glacier 存储类之间的复制需要特殊标志（**--force-glacier-transfer**）。从标准输入进行流式操作时，大于 50GB 的文件需要指定 **--expected-size**。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws-s3](/man/aws-s3)(1), [aws-s3-sync](/man/aws-s3-sync)(1), [aws-s3-mv](/man/aws-s3-mv)(1), [aws-s3api](/man/aws-s3api)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html)```

<!-- verified: 2026-06-18 -->
