# TAGLINE

快速的多线程 S3 命令行工具

# TLDR

**列出**存储桶的前缀

```s4cmd ls s3://[bucket]/prefix]```

**上传**文件

```s4cmd put [file] s3://[bucket]/key]```

**下载**指定键

```s4cmd get s3://[bucket]/key] [file]```

**递归的 sync** 风格复制

```s4cmd dsync [local_dir] s3://[bucket]/prefix]```

# SYNOPSIS

**s4cmd** *command* [*options*] [*args*]

# DESCRIPTION

**s4cmd** 是一款面向 Amazon S3 的多线程客户端，主打大批量传输的速度。它提供 **ls**、**put**、**get**、**del**、**dsync** 等操作，并支持兼容 S3 的端点。通过 **pip install s4cmd** 安装。使用标准 AWS 凭据链（**AWS_ACCESS_KEY_ID**、profile 等）。

# PARAMETERS

**ls** *s3://bucket/prefix*

> 列出对象。

**put** *local* *s3://...*

> 上传。

**get** *s3://...* *local*

> 下载。

**del** *s3://...*

> 删除键。

**dsync** *src* *dst*

> 本地与 S3 之间的目录式同步（视版本而定，也可用于 S3 到 S3）。

线程数与端点相关选项见：**s4cmd --help**。

# CAVEATS

请确认与你现有的 AWS CLI 凭据配置兼容。并行删除/上传可能产生费用并触发限流。语义与 **aws s3** 并不完全相同——生产迁移前务必先测试。

# INSTALL

```brew: brew install s4cmd```

```nix: nix profile install nixpkgs#s4cmd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aws](/man/aws)(1), [s3cmd](/man/s3cmd)(1), [rclone](/man/rclone)(1)

# RESOURCES

```[Source code](https://github.com/bloomreach/s4cmd)```

<!-- verified: 2026-07-19 -->
