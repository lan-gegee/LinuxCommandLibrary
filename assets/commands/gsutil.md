# TAGLINE

Google Cloud Storage 命令行工具

# TLDR

**列出存储桶**

```gsutil ls```

**列出存储桶内容**

```gsutil ls gs://[bucket-name]```

**复制文件到存储桶**

```gsutil cp [file.txt] gs://[bucket]/```

**复制存储桶到本地**

```gsutil cp gs://[bucket]/[file] [./]```

**同步目录到存储桶**

```gsutil rsync -r [local_dir] gs://[bucket]/[path]```

**将对象设为公开**

```gsutil acl ch -u AllUsers:R gs://[bucket]/[file]```

**删除对象**

```gsutil rm gs://[bucket]/[file]```

# SYNOPSIS

**gsutil** [_options_] _command_ [_args_]

# DESCRIPTION

**gsutil** 是一款与 Google Cloud Storage（GCS）交互的命令行工具。它提供的命令可以创建和删除存储桶、上传和下载对象、将本地目录与远程存储桶路径同步，以及管理访问控制列表（ACL）和存储桶策略。对象通过 `gs://bucket/path` URI 方案引用。

对于大规模操作，`-m` 标志可以并行多线程执行 `cp`、`mv`、`rm` 和 `rsync` 等命令，在处理大量文件或大型数据集时显著提升吞吐量。传输默认支持断点续传——中断的上传和下载可以重试而不必从头开始。gsutil 还支持对象版本控制、生命周期管理和跨存储桶复制等服务端特性，并通过 Google Cloud SDK 的凭据体系进行身份验证。

# PARAMETERS

**ls**
> 列出存储桶或对象。

**cp**
> 复制文件/对象。

**mv**
> 移动文件/对象。

**rm**
> 删除对象。

**rsync**
> 同步目录。

**mb**
> 创建存储桶。

**rb**
> 删除存储桶。

**acl**
> 管理访问控制。

**-m**
> 并行操作。

**-r**
> 递归操作。

**-n**
> 试运行（不做更改）。

# CAVEATS

**gsutil 已属于旧版工具**：Google 现在推荐更新的 **gcloud storage** 命令（Google Cloud CLI 的一部分），它们速度更快，并支持 gsutil 缺少的功能，如软删除和托管文件夹。gsutil 仍随 Cloud CLI 一同发布且照常可用，但只做最低限度的维护。

需要 Google Cloud 身份验证。大规模传输可能产生费用。ACL 更改需要谨慎考虑。并行操作会占用更多资源。

# HISTORY

**gsutil** 由 **Google** 开发，是 Google Cloud SDK 的一部分。它从早期的 Cloud Storage 访问工具演变为 Cloud Storage 操作的标准 CLI，最初支持 Python 2，后来支持 Python 3。

# SEE ALSO

[gcloud](/man/gcloud)(1), [aws](/man/aws)(1), [azcopy](/man/azcopy)(1), [rclone](/man/rclone)(1)

# RESOURCES

```[Source code](https://github.com/GoogleCloudPlatform/gsutil)```

```[Documentation](https://cloud.google.com/storage/docs/gsutil)```

<!-- verified: 2026-07-17 -->
