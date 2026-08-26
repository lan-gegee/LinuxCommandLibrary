# TAGLINE

管理 Azure 表存储中的实体

# TLDR

**向表中插入实体**

```az storage entity insert --table-name [MyTable] --entity PartitionKey=[pk] RowKey=[rk] Property=[value] --account-name [mystorageaccount]```

**插入并处理冲突**（fail、merge 或 replace）

```az storage entity insert --table-name [MyTable] --entity PartitionKey=[pk] RowKey=[rk] Property=[value] --if-exists [merge] --connection-string [$CS]```

**从表中查询实体**

```az storage entity query --table-name [MyTable] --account-name [mystorageaccount]```

**使用 OData 筛选器查询**

```az storage entity query --table-name [MyTable] --filter "PartitionKey eq 'pk'" --account-name [mystorageaccount]```

**显示特定实体**

```az storage entity show --table-name [MyTable] --partition-key [pk] --row-key [rk] --account-name [mystorageaccount]```

**合并实体属性**

```az storage entity merge --table-name [MyTable] --entity PartitionKey=[pk] RowKey=[rk] Property=[newvalue] --account-name [mystorageaccount]```

**替换实体**

```az storage entity replace --table-name [MyTable] --entity PartitionKey=[pk] RowKey=[rk] Property=[newvalue] --account-name [mystorageaccount]```

**删除实体**

```az storage entity delete --table-name [MyTable] --partition-key [pk] --row-key [rk] --account-name [mystorageaccount]```

# SYNOPSIS

**az** **storage** **entity** _subcommand_ [_options_]

# SUBCOMMANDS

**insert**
> 向表中插入实体。

**delete**
> 从表中删除实体。

**merge**
> 通过合并属性来更新实体。

**replace**
> 通过整体替换来更新实体。

**query**
> 列出匹配查询条件的实体。

**show**
> 从表中获取单个实体。

# PARAMETERS

**-t**, **--table-name** _NAME_
> 表的名称。

**-e**, **--entity** _KEY=VAL ..._
> 以空格分隔的 `key=value` 对。必须包含 `PartitionKey` 和 `RowKey`。可追加 `key@odata.type=<EdmType>` 来显式指定 Edm 类型（Edm.String、Edm.Int32、Edm.Int64、Edm.Double、Edm.Boolean、Edm.DateTime、Edm.Guid、Edm.Binary）。

**--partition-key** _PK_
> 实体的分区键。

**--row-key** _RK_
> 实体的行键。

**--filter** _EXPR_
> 用于 `query` 的 OData 筛选表达式。

**--select** _PROPS_
> 要返回的属性列表，以空格分隔。

**--num-results** _N_
> 每个服务请求返回的实体数量。

**--marker** _NEXTPK=... NEXTRK=..._
> 分页查询的续接标记。

**--if-exists** _BEHAVIOR_
> 实体已存在时的处理方式：`fail`（默认）、`merge` 或 `replace`（仅限 insert）。

**--if-match** _ETAG_
> 仅当实体的 ETag 匹配时才执行操作。默认 `*`。

**--account-name** _NAME_
> 存储账户名。环境变量：`AZURE_STORAGE_ACCOUNT`。

**--account-key** _KEY_
> 存储账户密钥。环境变量：`AZURE_STORAGE_KEY`。

**--connection-string** _CS_
> 存储账户连接字符串。环境变量：`AZURE_STORAGE_CONNECTION_STRING`。

**--sas-token** _TOKEN_
> 共享访问签名令牌。环境变量：`AZURE_STORAGE_SAS_TOKEN`。

**--auth-mode** _MODE_
> 身份验证模式：`key`（旧式）或 `login`（Azure AD）。

**--table-endpoint** _URL_
> 自定义服务端点，适用于 Cosmos DB Table API。

# DESCRIPTION

**az storage entity** 管理 Azure 表存储中的实体。表存储是一种面向结构化数据的 NoSQL 键值存储。实体是存储在表中的条目，类似于数据库中的行，由 `PartitionKey` 和 `RowKey` 唯一标识。

该命令既适用于 Azure 存储账户，也适用于 Azure Cosmos DB Table API（通过 `--table-endpoint`）。

# CAVEATS

需要 Azure CLI 和有效的存储凭据。属性类型仅限于 Edm 类型系统。每次请求最多返回 1000 个实体；分页请使用 `--marker`。PartitionKey 和 RowKey 各自最长可达 64KB。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az-storage-table](/man/az-storage-table)(1), [az-storage-queue](/man/az-storage-queue)(1), [az](/man/az)(1)
