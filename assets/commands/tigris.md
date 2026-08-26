# TAGLINE

Tigris S3 兼容对象存储的命令行客户端

# TLDR

**认证** CLI 并登录你的 Tigris 账户

```tigris login```

**显示**当前登录的用户和活动账户

```tigris whoami```

**创建**新存储桶

```tigris bucket mk [bucket_name]```

**列出**账户中的所有存储桶

```tigris ls```

**列出**存储桶内的对象

```tigris ls t3://[bucket_name]/```

将本地文件**复制**到存储桶

```tigris cp [path/to/file] t3://[bucket_name]/[key]```

**递归复制**目录到存储桶

```tigris cp -r [path/to/dir] t3://[bucket_name]/[prefix]/```

**下载**对象到本地路径

```tigris cp t3://[bucket_name]/[key] [path/to/file]```

**删除**对象或递归删除某个前缀

```tigris rm -r t3://[bucket_name]/[prefix]/```

# SYNOPSIS

**tigris** _domain_ _operation_ [_argument_] [**--flags**]
**t3** _domain_ _operation_ [_argument_] [**--flags**]

# PARAMETERS

**login**
> 打开基于浏览器的认证流程，让 CLI 登录 Tigris（Fly 托管的桶则登录 Fly.io）。

**logout**
> 移除缓存的凭据。

**whoami**
> 打印当前活动的用户和账户。

**configure**
> 以交互方式配置 profile、端点和访问密钥，供非交互场景使用。

**bucket mk** _name_ [**--region** _region_] [**--public**]
> 创建新存储桶。桶名共享 Tigris 的全局命名空间。

**bucket ls**
> 列出当前账户拥有的存储桶。

**bucket rm** _name_
> 删除空存储桶。

**ls** [_t3-uri_]
> 不带参数时列出所有存储桶，给定 **t3://** URI 时列出桶 / 前缀下的键。

**cp** [**-r**] [**--acl** _acl_] [**--content-type** _type_] _src_ _dst_
> 在本地路径与 **t3://** URI 之间复制数据。任一侧都可以是本地或远程，因此支持本地到远程、远程到本地以及远程到远程的复制。

**rm** [**-r**] _t3-uri_
> 删除单个对象，或用 **-r** 递归删除某个前缀。

**touch** _t3-uri_
> 在给定键处创建零字节对象。

**presign** _t3-uri_ [**--expires** _duration_] [**--method** _GET\|PUT_]
> 生成预签名 URL，无需凭据即可分享单个对象。

**--profile** _name_
> 使用配置文件中的命名 profile。

**--endpoint** _url_
> 覆盖 Tigris 端点（默认为 **fly.storage.tigris.dev**）。

**--output** _format_
> _table_、_json_ 或 _yaml_ 输出。

**-v**, **--verbose**
> 详细日志。

**--help**
> 显示任意命令的帮助。

# DESCRIPTION

**tigris** 是 **Tigris**（一项全球分布式、S3 兼容的对象存储服务）的官方命令行客户端。该 CLI 有意采用模仿 **ls**、**cp**、**rm** 和 **touch** 的 **UNIX 风格**接口，并用 **t3://_bucket_/_key_** 形式的 URI 标识远程对象。

CLI 按域分组命令——**bucket**、**object**、**iam**、**config**——每个域都暴露一小组可预期的操作。由于 Tigris 与 S3 兼容，**tigris** 能做的一切也可以通过 **AWS CLI** 实现，只需把 **--endpoint-url** 指向 Tigris 端点；专用 CLI 主要改善的是易用性、登录流程以及桶生命周期管理。

当存储桶通过 **Fly.io** 创建时（使用 **fly storage create**），相同的凭据和端点可与 **tigris** 无缝配合，且提供了简短别名 **t3**，方便写出更精炼的单行命令。

# CONFIGURATION

凭据和 profile 保存在 _~/.config/tigris/config.toml_：

```
[default]
access_key_id = "tid_..."
secret_access_key = "tsec_..."
endpoint = "https://fly.storage.tigris.dev"
region = "auto"
```

环境变量优先于配置文件：

```
TIGRIS_ACCESS_KEY_ID
TIGRIS_SECRET_ACCESS_KEY
TIGRIS_ENDPOINT_URL
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_ENDPOINT_URL_S3
```

标准的 **AWS_*** 变量同样被识别，因此现有的 S3 工具无需改动代码即可指向 Tigris。**tigris configure** 会以交互方式写入同一份文件。

# CAVEATS

**tigris** CLI 与历史上同名的任何 **TigrisData** 数据库 CLI 都不是同一个东西；现代客户端针对的是运行在 Fly.io 基础设施上的 **Tigris Object Storage** 产品。桶名是**全局唯一**的，与 S3 类似。预签名 URL 受桶 ACL 约束，因此要限时公开分享某个对象，正确做法是对私有桶使用预签名 URL。

# HISTORY

**Tigris** 作为 **Fly.io** 应用的存储层推出，由 **Tigris Data** 运营。专用 CLI 的推出是为了给日常桶操作提供一个比 AWS CLI 更专注的替代方案，其中 **t3** 简写和 **t3://** URI 方案借鉴了 **s3cmd** 和 **rclone** 的使用体验。

# SEE ALSO

[aws](/man/aws)(1), [s3cmd](/man/s3cmd)(1), [rclone](/man/rclone)(1), [flyctl](/man/flyctl)(1), [mc](/man/mc)(1)
