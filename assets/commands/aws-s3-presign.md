# TAGLINE

生成用于临时访问 S3 对象的预签名 URL

# TLDR

**生成预签名 URL**，默认 1 小时后过期

```aws s3 presign s3://[bucket-name]/[file.txt]```

**生成有效期**为 1 周（最大值）的**预签名 URL**

```aws s3 presign s3://[bucket-name]/[file.txt] --expires-in 604800```

**生成有效期**为 5 分钟的**预签名 URL**

```aws s3 presign s3://[bucket-name]/[file.txt] --expires-in 300```

为特定区域**生成预签名 URL**

```aws s3 presign s3://[bucket-name]/[file.txt] --region [us-west-2]```

# SYNOPSIS

**aws s3 presign** _S3Uri_ [_--expires-in value_] [_options_]

# DESCRIPTION

**aws s3 presign** 为 Amazon S3 对象生成预签名 URL。任何持有该预签名 URL 的人都可以通过 HTTP GET 请求获取 S3 对象，而无需 AWS 凭证。

预签名 URL 适用于临时共享私有 S3 对象、在应用程序中嵌入下载链接或提供限时文件访问。所有预签名 URL 均使用 Signature Version 4（SigV4）认证。

# PARAMETERS

**S3Uri**
> 要为其生成预签名 URL 的对象的 S3 URI（s3://bucket-name/key）

**--expires-in** _value_
> 预签名 URL 过期前的秒数（默认：3600，最大：604800）

**--region** _value_
> 存储桶所在的 AWS 区域（SigV4 必需；覆盖配置/环境设置）。

**--profile** _name_
> 使用凭证文件中的指定命名配置。

**--endpoint-url** _url_
> 覆盖默认端点 URL（对 S3 兼容服务很有用）。

# CAVEATS

最长过期时间为 604800 秒（7 天）。由于所有预签名 URL 都使用 SigV4 认证，必须显式配置区域。**aws s3 presign** 生成的预签名 URL 只授予只读（GET）访问权限；上传需要配合 SigV4 查询参数使用 **aws s3api** 或 SDK 辅助工具。URL 的有效期受签署它所用的凭证限制；如果使用临时凭证（STS），URL 的有效期不能超过这些凭证本身。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws-s3](/man/aws-s3)(1), [aws-s3-cp](/man/aws-s3-cp)(1), [aws-s3api](/man/aws-s3api)(1)
