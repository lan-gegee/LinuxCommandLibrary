# TAGLINE

同步目录与 S3 前缀

# TLDR

将**本地目录同步到** S3 存储桶

```aws s3 sync [./local-dir] s3://[bucket-name]/```

将 **S3 存储桶下载到**本地目录

```aws s3 sync s3://[bucket-name]/ [./local-dir]```

在**两个 S3 存储桶之间同步**

```aws s3 sync s3://[source-bucket] s3://[dest-bucket]```

**同步并删除**源中不存在的文件

```aws s3 sync [./local-dir] s3://[bucket-name]/ --delete```

**同步时排除**某些文件类型

```aws s3 sync [./local-dir] s3://[bucket-name]/ --exclude "*.log"```

**预览同步操作**而不实际执行

```aws s3 sync [./local-dir] s3://[bucket-name]/ --dryrun```

**只同步新文件**而不覆盖

```aws s3 sync [./local-dir] s3://[bucket-name]/ --no-overwrite```

# SYNOPSIS

**aws s3 sync** _source_ _destination_ [_options_]

# DESCRIPTION

**aws s3 sync** 通过递归地将新增和已更新的文件从源复制到目标来同步目录与 S3 前缀。它只传输新增或有变化的文件，因此非常适合增量备份和部署。

默认情况下，sync 通过比较文件大小和最后修改时间来判断哪些文件需要更新。只有当目标文件夹中包含文件时才会创建该文件夹。

# PARAMETERS

**--delete**
> 删除目标中不存在于源中的文件

**--dryrun**
> 显示将要执行的操作但不实际执行

**--quiet**
> 抑制除错误之外的所有输出

**--no-overwrite**
> 只传输目标中不存在的文件

**--size-only**
> 仅凭文件大小判断是否需要同步（忽略时间戳）

**--exact-timestamps**
> 从 S3 同步到本地时精确匹配时间戳

**--include** _pattern_
> 包含匹配模式的文件

**--exclude** _pattern_
> 从同步中排除匹配模式的文件

**--acl** _value_
> 设置访问控制列表：private、public-read 等

**--storage-class** _value_
> 指定存储类别：STANDARD、STANDARD_IA、GLACIER 等

**--source-region** _value_
> 源存储桶所在区域（跨区域 S3 到 S3 同步时必需）

# CAVEATS

**--delete** 选项会删除目标中不存在于源里的文件；请谨慎使用。**--include** 与 **--exclude** 的模式匹配与顺序有关。同步到本地时，除非目录中包含文件，否则不会创建目录。sync 不会保留符号链接。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws-s3](/man/aws-s3)(1), [aws-s3-cp](/man/aws-s3-cp)(1), [rsync](/man/rsync)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/s3/sync.html)```

<!-- verified: 2026-06-18 -->
