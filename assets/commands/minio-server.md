# TAGLINE

运行 MinIO 对象存储

# TLDR

**启动服务器**

```minio server [/data]```

**以指定控制台端口启动**

```minio server --console-address ":[9001]" [/data]```

**分布式模式**

```minio server [http://server{1...4}/data]```

**设置凭据**

```MINIO_ROOT_USER=[admin] MINIO_ROOT_PASSWORD=[password] minio server [/data]```

**指定地址**

```minio server --address ":[9000]" [/data]```

# SYNOPSIS

**minio server** [_options_] _path_

# PARAMETERS

_PATH_
> 数据目录或端点。

**--address** _ADDR_
> 服务器地址。

**--console-address** _ADDR_
> 控制台地址。

**--certs-dir** _DIR_
> TLS 证书目录。

**--help**
> 显示帮助信息。

# DESCRIPTION

**minio server** 运行 MinIO 对象存储。MinIO 是兼容 S3 的存储服务器。

该工具提供高性能对象存储。支持纠删码和分布式模式。

# CAVEATS

需要持久化存储。请设置安全的凭据。大型部署内存消耗较高。

# HISTORY

MinIO 的创建目标是提供 Kubernetes 原生的、高性能的 **S3 兼容**对象存储。

# SEE ALSO

[minio-client](/man/minio-client)(1), [mc](/man/mc)(1), [aws](/man/aws)(1)
