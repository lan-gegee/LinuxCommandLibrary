# TAGLINE

删除 S3 存储桶

# TLDR

**删除空的 S3 存储桶**

```aws s3 rb s3://[bucket-name]```

**强制删除存储桶**及其所有未版本化的对象

```aws s3 rb s3://[bucket-name] --force```

**删除特定区域中的存储桶**

```aws s3 rb s3://[bucket-name] --region [us-east-1]```

# SYNOPSIS

**aws s3 rb** _S3Uri_ [_--force_] [_options_]

# DESCRIPTION

**aws s3 rb**（remove bucket）删除 S3 存储桶。默认情况下，存储桶必须完全清空对象后才能删除。

使用 **--force** 选项可在删除存储桶本身之前自动删除桶中所有未版本化的对象。这是一个无法撤销的破坏性操作。

# PARAMETERS

**S3Uri**
> 要删除的存储桶的 S3 URI（s3://bucket-name）

**--force**
> 在删除存储桶本身之前删除桶中所有对象

# CAVEATS

**--force** 选项只删除未版本化的对象。如果存储桶中包含已版本化的对象或删除标记，即使加上 **--force** 删除也会失败。对于启用了版本控制的存储桶，请先使用 **aws s3api delete-object** 配合 **--version-id** 移除所有对象版本，或配置生命周期策略使版本过期。删除存储桶是永久性的，其名称将变为可被他人使用。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws-s3](/man/aws-s3)(1), [aws-s3-mb](/man/aws-s3-mb)(1), [aws-s3-rm](/man/aws-s3-rm)(1), [aws-s3-ls](/man/aws-s3-ls)(1)
