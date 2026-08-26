# TAGLINE

管理 Azure 存储账户

# TLDR

**创建存储账户**

```az storage account create -n [account-name] -g [resource-group] -l [westus] --sku [Standard_LRS]```

**列出所有存储账户**

```az storage account list -o table```

**显示存储账户详情**

```az storage account show -n [account-name] -g [resource-group]```

**获取连接字符串**

```az storage account show-connection-string -n [account-name] -g [resource-group]```

**列出存储账户密钥**

```az storage account keys list -n [account-name] -g [resource-group]```

**生成账户级 SAS 令牌**

```az storage account generate-sas --account-name [account-name] --services [bfqt] --resource-types [sco] --permissions [racwdl] --expiry [2026-12-31T00:00Z]```

**检查名称可用性**

```az storage account check-name --name [proposed-name]```

**删除存储账户**

```az storage account delete -n [account-name] -g [resource-group] --yes```

# SYNOPSIS

**az storage account** _subcommand_ [_options_]

# DESCRIPTION

**az storage account** 管理 Azure 存储账户。存储账户为存储和访问 Azure 存储数据对象提供唯一命名空间，支持 Blob、文件、队列、表和磁盘。

不同的账户类型和 SKU 提供不同的性能层级、冗余选项和访问模式。StorageV2（常规用途 v2）账户支持所有存储服务和功能。

# SUBCOMMANDS

**账户生命周期**
> create, delete, list, show, update, check-name

**访问**
> keys list, keys renew, generate-sas, show-connection-string, revoke-delegation-keys

**网络安全**
> network-rule add, network-rule list, network-rule remove, private-endpoint-connection

**Blob 服务**
> blob-service-properties show, blob-service-properties update, blob-inventory-policy

**文件服务**
> file-service-properties show, file-service-properties update

**高级功能**
> management-policy create, encryption-scope create, failover, local-user

# PARAMETERS

**-n, --name** _value_
> 存储账户名（全局唯一，3-24 个字符，只能包含小写字母/数字）

**-g, --resource-group** _value_
> 资源组的名称

**-l, --location** _value_
> 存储账户所在的 Azure 区域

**--sku** _value_
> 存储 SKU。默认 **Standard_RAGRS**。取值包括 Standard_LRS、Standard_GRS、Standard_RAGRS、Standard_ZRS、Standard_GZRS、Standard_RAGZRS、Premium_LRS、Premium_ZRS。

**--kind** _value_
> 账户类型。默认 **StorageV2**。取值：StorageV2、Storage、BlobStorage、FileStorage、BlockBlobStorage。

**--access-tier** _value_
> Blob 数据的访问层：Hot、Cool、Cold、Premium。

**--https-only** _value_
> 要求请求使用 HTTPS。默认 **true**。

**--min-tls-version** _value_
> 允许的最低 TLS 版本：TLS1_0、TLS1_1、TLS1_2、TLS1_3。

**--allow-blob-public-access** _value_
> 允许匿名公开访问 Blob。新建账户默认 **false**。

**--hns**, **--enable-hierarchical-namespace** _value_
> 启用分层命名空间（Azure Data Lake Storage Gen2）。

# CAVEATS

存储账户名称必须在所有 Azure 客户之间全局唯一。更改冗余选项（例如从 GRS 改为 LRS）可能需要进行数据迁移。删除存储账户不可逆，会一并移除其中包含的所有数据。高级（Premium）账户具有不同的定价和性能特征。

# HISTORY

Azure 存储是最早的 Azure 服务之一，自平台 **2010** 年上线起即可使用。StorageV2 账户于 **2018** 年成为推荐的默认账户类型，它统一了此前相互独立的存储类型，并启用了访问层等新功能。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [azure-cli](/man/azure-cli)(1), [az-storage](/man/az-storage)(1), [az-storage-blob](/man/az-storage-blob)(1), [az-storage-container](/man/az-storage-container)(1), [azcopy](/man/azcopy)(1)

# RESOURCES

```[Documentation](https://learn.microsoft.com/en-us/cli/azure/storage/account)```

```[Homepage](https://learn.microsoft.com/en-us/cli/azure/)```

```[Source code](https://github.com/Azure/azure-cli)```

<!-- verified: 2026-06-19 -->
