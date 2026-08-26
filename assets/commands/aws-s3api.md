# TAGLINE

底层 S3 API 操作

# TLDR

**列出账户中的所有存储桶**

```aws s3api list-buckets```

从 S3 **获取对象**

```aws s3api get-object --bucket [bucket-name] --key [object-key] [output-file]```

向 S3 **上传对象**

```aws s3api put-object --bucket [bucket-name] --key [object-key] --body [file.txt]```

从 S3 **删除对象**

```aws s3api delete-object --bucket [bucket-name] --key [object-key]```

**列出**存储桶中的**对象**

```aws s3api list-objects-v2 --bucket [bucket-name]```

从 JSON 文件**附加存储桶策略**

```aws s3api put-bucket-policy --bucket [bucket-name] --policy file://[policy.json]```

**获取存储桶版本控制**状态

```aws s3api get-bucket-versioning --bucket [bucket-name]```

以指定配置**创建存储桶**

```aws s3api create-bucket --bucket [bucket-name] --create-bucket-configuration LocationConstraint=[us-west-2]```

# SYNOPSIS

**aws s3api** _subcommand_ [_options_]

# DESCRIPTION

**aws s3api** 提供对 Amazon S3 API 操作的底层访问。与高级 **aws s3** 命令不同，s3api 暴露完整的 S3 API，可对请求参数和响应处理进行细粒度控制。

当高级命令无法覆盖某些操作时，例如管理存储桶策略、配置生命周期规则、处理分段上传或操作对象版本，可使用 s3api 直接访问 API。

# SUBCOMMANDS

**Bucket Operations**
> create-bucket, delete-bucket, list-buckets, head-bucket, get-bucket-location

**Object Operations**
> put-object, get-object, delete-object, delete-objects, head-object, copy-object, restore-object, get-object-attributes

**Listing**
> list-objects-v2, list-objects, list-object-versions

**Bucket Configuration**
> put-bucket-policy, get-bucket-policy, delete-bucket-policy, put-bucket-acl, get-bucket-acl, put-bucket-cors, get-bucket-cors, put-public-access-block, get-public-access-block

**Versioning**
> put-bucket-versioning, get-bucket-versioning, list-object-versions

**Lifecycle**
> put-bucket-lifecycle-configuration, get-bucket-lifecycle-configuration, delete-bucket-lifecycle

**Encryption**
> put-bucket-encryption, get-bucket-encryption, delete-bucket-encryption

**Multipart Uploads**
> create-multipart-upload, upload-part, complete-multipart-upload, abort-multipart-upload, list-multipart-uploads

**Tagging**
> put-bucket-tagging, get-bucket-tagging, put-object-tagging, get-object-tagging

# CAVEATS

s3api 命令比高级 **aws s3** 命令需要更冗长的语法，但提供完整的 API 覆盖。在 us-east-1 之外创建存储桶时必须指定 **--create-bucket-configuration**。对象键区分大小写。上传大文件时建议使用分段上传操作。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws-s3](/man/aws-s3)(1), [aws-s3-cp](/man/aws-s3-cp)(1), [aws](/man/aws)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/s3api/index.html)```

<!-- verified: 2026-06-18 -->
