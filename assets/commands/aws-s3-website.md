# TAGLINE

配置 S3 存储桶的静态网站托管

# TLDR

将**存储桶配置为静态网站**

```aws s3 website s3://[bucket-name]/ --index-document [index.html] --error-document [error.html]```

**只设置索引文档**

```aws s3 website s3://[bucket-name]/ --index-document [index.html]```

# SYNOPSIS

**aws s3 website** _S3Uri_ [_--index-document value_] [_--error-document value_] [_options_]

# DESCRIPTION

**aws s3 website** 将 S3 存储桶配置为托管静态网站。配置完成后，存储桶内容可通过 S3 网站端点 URL 访问。

当访问者请求网站根路径或任何目录路径时，会返回索引文档。发生 4XX 错误（如 404 Not Found）时则显示错误文档。

# PARAMETERS

**S3Uri**
> 要配置的 S3 存储桶 URI（s3://bucket-name/）

**--index-document** _value_
> 附加到目录请求末尾的后缀（如 index.html）；不能为空或包含斜杠

**--error-document** _value_
> 发生 4XX 类错误时显示的对象键名

# CAVEATS

此命令只配置网站托管；还必须单独配置存储桶策略和对象权限才能允许公开访问。网站端点 URL 与标准 S3 端点不同（如 **http://bucket-name.s3-website-region.amazonaws.com**）。网站端点不支持 HTTPS；需要 HTTPS 时请使用 CloudFront。公开网站托管必须禁用 Block Public Access 设置。

# HISTORY

S3 静态网站托管于 **2011 年 2 月**推出，使存储桶可以直接提供静态内容。**aws s3 website** CLI 命令简化了此前需要通过 **s3api put-bucket-website** 进行多次 API 调用的配置过程。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws-s3](/man/aws-s3)(1), [aws-s3api](/man/aws-s3api)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/s3/website.html)```

<!-- verified: 2026-06-18 -->
