# TAGLINE

LocalStack 的 AWS CLI 包装器

# TLDR

在 LocalStack 上**列出 Kinesis 流**

```awslocal kinesis list-streams```

**与 aws 相同，但使用 LocalStack 端点**

```awslocal s3 ls```

**创建本地存储桶**

```awslocal s3 mb s3://[my-bucket]```

本地**调用 Lambda**

```awslocal lambda list-functions```

# SYNOPSIS

**awslocal** [*aws-cli-arguments*...]

# DESCRIPTION

**awslocal** 是 **aws** CLI 的一层薄包装，配合 [LocalStack](https://github.com/localstack/localstack) 使用。无需每次调用都传入 **--endpoint-url=http://localhost:4566**，直接通过 **awslocal** 运行相同的子命令即可。

使用 **pip install awscli-local** 安装（仅包装器），或使用 **pip install awscli-local[ver1]** 同时安装 AWS CLI v1。用法与 **aws** 一致；参见 **aws help**。

# PARAMETERS

所有参数都会转发给底层的 **aws** CLI（服务、子命令和选项）。没有独立的命令树。

# CONFIGURATION

环境变量：

**AWS_ENDPOINT_URL**

> 要使用的端点（优先于下述已弃用的变量）。

**LOCALSTACK_HOST**（已弃用）

> LocalStack 的 **hostname:port**（默认 **localhost:4566**）。

**USE_SSL**（已弃用）

> 连接时是否使用 SSL（默认 false）。

标准的 AWS 凭证与区域变量对 CLI 仍然生效；LocalStack 通常接受测试凭证。

# CAVEATS

AWS CLI v2 无法从 PyPI 自动安装；如果 v2 已存在于 PATH 中，**awslocal** 仍然可以工作，但存在已知缺口（例如某些 **cloudformation package** 的端点场景）。服务的覆盖范围和端口请以 LocalStack 文档为准。它不能替代针对真实 AWS 的生产级 **aws**。

# SEE ALSO

[aws](/man/aws)(1), [localstack](/man/localstack)(1)

# RESOURCES

```[Source code](https://github.com/localstack/awscli-local)```

```[Homepage](https://localstack.cloud)```

<!-- verified: 2026-07-19 -->
