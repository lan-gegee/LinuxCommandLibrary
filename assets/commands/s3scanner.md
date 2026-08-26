# TAGLINE

扫描各云服务商中配置不当的 S3 存储桶

# TLDR

**扫描文件中的存储桶名称列表**

```s3scanner -bucket-file [names.txt]```

**扫描并枚举存储桶中的对象**

```s3scanner -bucket [my-bucket] -enumerate```

**扫描 GCP 存储桶**

```s3scanner -provider gcp -bucket [my-bucket]```

**以 JSON 格式输出扫描结果**

```s3scanner -bucket [my-bucket] -json```

# SYNOPSIS

**s3scanner** [_options_]

# PARAMETERS

**-bucket** _NAME_
> 要扫描的单个存储桶名称。

**-bucket-file** _FILE_
> 包含待扫描存储桶名称的文件。

**-enumerate**
> 列出可访问存储桶中发现的所有对象。

**-provider** _PROVIDER_
> 存储服务商：aws、gcp、digitalocean、dreamhost、linode 或 scaleway。

**-threads** _N_
> 并发扫描工作线程数。默认：4。

**-json**
> 以 JSON 格式输出结果。

# DESCRIPTION

**s3scanner** 检查对象存储桶的权限，以发现公开访问类的配置错误。它支持 AWS 和多种兼容 S3 的服务商，具备多线程扫描能力，可通过 PostgreSQL 持久化数据，并集成 RabbitMQ 以支持大规模部署。

# CAVEATS

对象枚举每个存储桶最多 5000 页。非 AWS 服务商仅支持匿名用户权限。仅限用于获得授权的安全测试。

# HISTORY

**s3scanner** 由 **Dan Salmon**（sa7mon）创建，使用 **Go** 编写。

# INSTALL

```brew: brew install s3scanner```

```nix: nix profile install nixpkgs#s3scanner```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aws](/man/aws)(1), [rclone](/man/rclone)(1), [trivy](/man/trivy)(1)
