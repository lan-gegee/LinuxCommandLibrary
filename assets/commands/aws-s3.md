# TAGLINE

高级 S3 文件管理命令

# TLDR

**列出账户中的所有存储桶**

```aws s3 ls```

**列出**存储桶中的**对象**

```aws s3 ls s3://[bucket-name]/```

将**本地文件复制到** S3

```aws s3 cp [file.txt] s3://[bucket-name]/```

从 S3 **下载文件**

```aws s3 cp s3://[bucket-name]/[file.txt] [./local-file.txt]```

将**本地目录同步到** S3 存储桶

```aws s3 sync [./local-dir] s3://[bucket-name]/[prefix/]```

将**文件移动到** S3（先上传后删除源文件）

```aws s3 mv [file.txt] s3://[bucket-name]/```

**生成限时下载 URL**

```aws s3 presign s3://[bucket-name]/[file.txt] --expires-in [3600]```

**创建新存储桶**

```aws s3 mb s3://[bucket-name]```

**移除空存储桶**

```aws s3 rb s3://[bucket-name]```

从 S3 **删除对象**

```aws s3 rm s3://[bucket-name]/[file.txt]```

# SYNOPSIS

**aws s3** _command_ [_arguments_] [_options_]

# DESCRIPTION

**aws s3** 提供用于管理 Amazon S3 存储桶和对象的高级命令。它为复制、同步和列出文件等常见 S3 操作提供简化接口，屏蔽了底层 S3 API 的复杂性。

该命令使用两类路径参数：**LocalPath**（本地文件的绝对或相对路径）和 **S3Uri**（形如 **s3://bucket-name/key** 的 S3 资源路径）。大多数命令接受源作为第一个参数，可选的目标作为第二个参数。

若需要完全控制请求参数的底层 S3 API 访问，请改用 **aws s3api**。

# SUBCOMMANDS

**cp**
> 在本地文件系统与 S3 之间或 S3 位置之间复制文件

**ls**
> 列出 S3 存储桶或存储桶/前缀中的对象

**mb**
> 创建新的 S3 存储桶

**mv**
> 在本地文件系统与 S3 之间或 S3 位置之间移动文件

**presign**
> 生成预签名 URL，用于限时访问 S3 对象

**rb**
> 移除（删除）S3 存储桶

**rm**
> 移除（删除）S3 对象

**sync**
> 同步目录与 S3 前缀（上传新增/已更改的文件）

**website**
> 配置 S3 存储桶的网站托管设置

# PARAMETERS

**--recursive**
> 以递归方式对目录或 S3 前缀下的所有文件应用命令

**--exclude** _pattern_
> 从操作中排除匹配模式的文件

**--include** _pattern_
> 包含匹配模式的文件（与 --exclude 配合使用）

**--dryrun**
> 显示将要执行的操作但不实际执行

**--acl** _value_
> 设置访问控制列表（private、public-read 等）

**--storage-class** _value_
> 指定存储类别（STANDARD、REDUCED_REDUNDANCY、GLACIER 等）

**--sse** _value_
> 启用服务器端加密（AES256 或 aws:kms）

**--delete**
> 配合 sync 使用时，删除目标中不再存在于源里的文件

# CAVEATS

**sync** 命令默认只复制新增或有修改的文件；使用 **--delete** 可移除目标中不存在于源里的文件。**--exclude** 和 **--include** 的模式匹配与顺序有关；过滤器按指定顺序依次应用。**rb** 命令在存储桶非空时会失败，除非使用 **--force**。

# HISTORY

Amazon S3（Simple Storage Service）于 **2006 年 3 月**上线，是 AWS 最早的服务之一。**aws s3** 高级 CLI 命令随 AWS CLI v1 于 **2013 年**推出，用于简化此前需要通过 **s3api** 多次 API 调用才能完成的常见操作。sync 命令和分段上传支持在后续版本中不断增强。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-s3api](/man/aws-s3api)(1), [aws-s3-cp](/man/aws-s3-cp)(1), [aws-s3-sync](/man/aws-s3-sync)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/s3/index.html)```

<!-- verified: 2026-06-18 -->
