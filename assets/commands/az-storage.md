# TAGLINE

管理 Azure 云存储资源

# TLDR

**将本地文件复制到 Blob 存储**

```az storage copy -s [/path/to/file.txt] -d https://[account].blob.core.windows.net/[container]/[blob]```

**将 Blob 下载到本地文件系统**

```az storage copy -s https://[account].blob.core.windows.net/[container]/[blob] -d [/path/to/file.txt]```

**递归上传目录**

```az storage copy -s [/path/to/dir] -d https://[account].blob.core.windows.net/[container]/[path/] --recursive```

**在存储账户之间复制**

```az storage copy -s https://[src].blob.core.windows.net/[container]/[blob] -d https://[dest].blob.core.windows.net/[container]/[blob]```

**删除 Blob**

```az storage remove -c [container-name] -n [blob-name] --account-name [account]```

**递归删除目录**

```az storage remove -c [container-name] -n [path/to/directory] --recursive --account-name [account]```

**从 AWS S3 复制到 Azure Blob**

```az storage copy -s https://s3.amazonaws.com/[bucket]/[object] -d https://[account].blob.core.windows.net/[container]/[blob]```

# SYNOPSIS

**az storage** _subcommand_ [_options_]

# DESCRIPTION

**az storage** 管理 Azure 云存储资源，包括存储账户、Blob 容器、文件共享、队列和表。它提供用于上传、下载、复制以及管理已存数据的命令。

Azure 存储提供多种存储类型：Blob 存储用于非结构化数据，文件存储用于 SMB 文件共享，队列存储用于消息传递，表存储用于 NoSQL 数据。

# SUBCOMMANDS

**账户管理**
> account create, account delete, account list, account show, account keys list

**Blob 存储**
> blob upload, blob download, blob delete, blob list, blob copy

**容器**
> container create, container delete, container list, container lease

**文件共享**
> share create, share delete, share list, file upload, file download

**复制操作**
> copy, remove

**Data Lake Gen2**
> fs create, fs file upload, fs directory create

**队列与表**
> queue create, queue list, message put, table create, entity insert

# PARAMETERS

**--account-name** _value_
> 存储账户名

**--account-key** _value_
> 存储账户访问密钥

**--connection-string** _value_
> 存储账户连接字符串

**-c, --container** _value_
> Blob 容器名称

**-s, --source** _value_
> 源路径（本地路径或 URL）

**-d, --destination** _value_
> 目标路径（本地路径或 URL）

**--recursive**
> 递归处理子目录。

**--auth-mode** _value_
> 身份验证模式：**key**（使用账户密钥）或 **login**（使用 Azure AD 凭据）。

**--sas-token** _value_
> 用于对请求进行身份验证的共享访问签名令牌。

# CAVEATS

命令支持多种身份验证方式：账户密钥、SAS 令牌、Azure AD 登录或连接字符串。**copy** 和 **remove** 命令底层使用 AzCopy，支持 S3 到 Azure 以及 Google Cloud Storage 到 Azure 的传输。通配符模式的匹配行为与 shell 的 glob 展开不同；请使用 **--include-pattern** 和 **--exclude-pattern** 进行筛选。部分子命令需要先安装 **storage-preview** 扩展。

# HISTORY

**az storage** 是 **Azure CLI**（微软的跨平台命令行工具，最早于 **2014** 年发布，原名 **xplat-cli**）的一部分。以 Python 重写的现代 `az` 接口于 **2017** 年推出。**az storage copy** 和 **az storage remove** 命令集成了 **AzCopy v10**，用更快速、可断点续传的传输引擎取代了旧的上传/下载流程。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [az-storage-account](/man/az-storage-account)(1), [az-storage-blob](/man/az-storage-blob)(1), [azcopy](/man/azcopy)(1)
