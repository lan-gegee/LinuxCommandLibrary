# TAGLINE

用于开发和测试的本地 Azure Storage 模拟器。

# TLDR

**启动** Azurite（所有服务）

```azurite```

仅启动 **blob 服务**

```azurite-blob```

在**自定义端口**上启动

```azurite --blobPort [10000] --queuePort [10001] --tablePort [10002]```

使用**自定义位置**

```azurite --location [/path/to/data]```

**静默**模式

```azurite --silent```

# SYNOPSIS

**azurite** [_options_]

# DESCRIPTION

**azurite** 是一个开源的服务器模拟器，兼容 Azure Storage API。它为 Azure Blob、队列和表存储提供本地开发和测试环境，无需 Azure 账户。

该工具由微软官方维护，取代了已弃用的 Azure Storage Emulator。

# PARAMETERS

**--blobPort** _port_
> Blob 服务端口（默认：10000）

**--queuePort** _port_
> 队列服务端口（默认：10001）

**--tablePort** _port_
> 表服务端口（默认：10002）

**--location**, **-l** _path_
> 数据存储位置

**--silent**, **-s**
> 静默模式（不输出日志）

**--debug** _path_
> 调试日志文件路径

**--loose**
> 宽松模式（放宽校验）

**--cert** _path_
> HTTPS 证书路径

**--key** _path_
> HTTPS 密钥路径

**--oauth** _level_
> OAuth 身份验证级别（例如 basic）

**--blobHost** _addr_
> Blob 服务监听地址（默认：127.0.0.1）

**--queueHost** _addr_
> 队列服务监听地址（默认：127.0.0.1）

**--tableHost** _addr_
> 表服务监听地址（默认：127.0.0.1）

**--inMemoryPersistence**
> 所有数据仅保存在内存中（退出后即丢失）

**--disableProductStyleUrl**
> 强制从 URI 路径而不是主机名解析账户名

# SERVICES

**azurite**
> 所有服务（Blob、队列、表）

**azurite-blob**
> 仅 Blob 服务

**azurite-queue**
> 仅队列服务

**azurite-table**
> 仅表服务

# CONNECTION STRINGS

默认的开发用连接字符串：
```
DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;QueueEndpoint=http://127.0.0.1:10001/devstoreaccount1;TableEndpoint=http://127.0.0.1:10002/devstoreaccount1;
```

# CAVEATS

并非所有 Azure Storage 功能都受支持。某些 API 行为与生产环境不同。除非使用 --inMemoryPersistence，否则数据会在多次运行之间保留。请勿用于生产环境。通过 npm 安装需要 Node.js。

# HISTORY

**Azurite** 由 Xiao Ning Guo 创建，并于 **2019** 年被微软采用，作为仅限 Windows 的 Azure Storage Emulator 的官方替代品，提供跨平台支持。

# INSTALL

```brew: brew install azurite```

```nix: nix profile install nixpkgs#azurite```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az-storage](/man/az-storage)(1), [docker](/man/docker)(1), [node](/man/node)(1), [npm](/man/npm)(1)
