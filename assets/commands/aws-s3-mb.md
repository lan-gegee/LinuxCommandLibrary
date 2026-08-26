# TAGLINE

创建 S3 存储桶

# TLDR

在默认区域**创建新 S3 存储桶**

```aws s3 mb s3://[bucket-name]```

在指定区域**创建存储桶**

```aws s3 mb s3://[bucket-name] --region [us-west-1]```

# SYNOPSIS

**aws s3 mb** _S3Uri_ [_options_]

# DESCRIPTION

**aws s3 mb**（make bucket）创建新的 Amazon S3 存储桶。存储桶名称必须在所有 AWS 账户间全局唯一，并遵守 S3 命名规则。

默认情况下，存储桶创建在 AWS 配置中指定的区域。可使用 **--region** 选项在其他区域创建存储桶。

# PARAMETERS

**S3Uri**
> 要创建的存储桶的 S3 URI，格式为 s3://bucket-name

**--region** _value_
> 在指定的 AWS 区域创建存储桶（覆盖来自配置或环境的区域设置）

**--tags** _key_ _value_
> 为存储桶添加标签。可多次指定以设置多个标签。

# CAVEATS

存储桶名称必须在所有 AWS 账户和区域内全局唯一。名称必须为 3-63 个字符，只能包含小写字母、数字和连字符，且不能是 IP 地址格式。如果名称已被其他 AWS 账户占用，创建将失败。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws-s3](/man/aws-s3)(1), [aws-s3-rb](/man/aws-s3-rb)(1), [aws-s3-ls](/man/aws-s3-ls)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/s3/mb.html)```

<!-- verified: 2026-06-18 -->
