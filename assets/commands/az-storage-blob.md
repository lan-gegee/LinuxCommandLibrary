# TAGLINE

管理 Azure Blob 存储对象

# TLDR

**将文件上传到 Blob 存储**

```az storage blob upload -f [/path/to/file] -c [container-name] -n [blob-name] --account-name [account]```

**将 Blob 下载到本地文件系统**

```az storage blob download -f [/path/to/file] -c [container-name] -n [blob-name] --account-name [account]```

**列出容器中的 Blob**

```az storage blob list -c [container-name] --account-name [account] -o table```

**删除 Blob**

```az storage blob delete -c [container-name] -n [blob-name] --account-name [account]```

**从目录上传多个文件**

```az storage blob upload-batch -d [container-name] -s [/path/to/directory] --account-name [account]```

**按模式下载多个 Blob**

```az storage blob download-batch -d [./local-dir] -s [container-name] --pattern "*.txt" --account-name [account]```

**为 Blob 生成 SAS 令牌**

```az storage blob generate-sas -c [container-name] -n [blob-name] --permissions [r] --expiry [2024-12-31T00:00Z] --account-name [account]```

**设置 Blob 访问层**

```az storage blob set-tier -c [container-name] -n [blob-name] --tier [Cool] --account-name [account]```

# SYNOPSIS

**az storage blob** _subcommand_ [_options_]

# DESCRIPTION

**az storage blob** 管理 Azure Blob Storage 中面向非结构化数据的对象存储。Blob 可以存储任何类型的文本或二进制数据，包括文档、媒体文件和应用程序数据。

该命令组支持上传、下载、复制，以及管理 Blob 的属性、元数据、访问层和安全设置。

# SUBCOMMANDS

**传输操作**
> upload, upload-batch, download, download-batch, copy start, copy cancel

**Blob 管理**
> list, delete, delete-batch, exists, show, snapshot, restore

**属性与元数据**
> metadata show, metadata update, update, set-tier, tag list, tag set

**安全**
> generate-sas, lease acquire, lease break, lease release, lease renew

**查询**
> query（对 Blob 数据执行 SQL 查询）

# PARAMETERS

**-c, --container-name** _value_
> Blob 容器的名称

**-n, --name** _value_
> Blob 的名称

**-f, --file** _value_
> 用于上传/下载的本地文件路径

**--account-name** _value_
> 存储账户名

**--account-key** _value_
> 存储账户密钥

**--sas-token** _value_
> 共享访问签名（SAS）令牌

**--tier** _value_
> 访问层：Hot、Cool、Cold、Archive

**--pattern** _value_
> 批量操作使用的 glob 模式

**--overwrite**
> 上传时覆盖现有 Blob（默认：false）

**--auth-mode** _value_
> 身份验证模式：login（Azure AD）或 key

**-o**, **--output** _value_
> 输出格式：json、table、tsv、yaml、jsonc、none

# CAVEATS

需要通过 **--account-key**、**--sas-token**、**--connection-string** 或 **--auth-mode login** 进行身份验证。Archive 层的 Blob 必须先解除冻结（rehydrate）才能访问。批量操作遵循模式匹配，但默认不会递归遍历虚拟目录。删除操作只是将 Blob 标记为待删除；软删除策略可能允许恢复。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az-storage](/man/az-storage)(1), [az-storage-container](/man/az-storage-container)(1), [az-storage-account](/man/az-storage-account)(1)
