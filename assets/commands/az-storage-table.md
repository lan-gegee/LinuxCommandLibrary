# TAGLINE

管理 Azure 表存储中的表

# TLDR

**创建表**

```az storage table create --name [mytable] --account-name [mystorageaccount]```

**列出所有表**

```az storage table list --account-name [mystorageaccount]```

**删除表**

```az storage table delete --name [mytable] --account-name [mystorageaccount]```

**检查表是否存在**

```az storage table exists --name [mytable] --account-name [mystorageaccount]```

**为表生成 SAS 令牌**

```az storage table generate-sas --name [mytable] --permissions [raud] --expiry [2026-12-31T00:00Z] --account-name [mystorageaccount]```

**列出表的存储访问策略**

```az storage table policy list --table-name [mytable] --account-name [mystorageaccount]```

# SYNOPSIS

**az** **storage** **table** _subcommand_ [_options_]

# SUBCOMMANDS

**create**
> 创建表。

**delete**
> 删除表。

**list**
> 列出存储账户中的表。

**exists**
> 检查表是否存在。

**generate-sas**
> 为表生成共享访问签名。

**policy create / delete / list / show / update**
> 管理表的存储访问策略。

**stats**
> 获取表服务的复制统计信息（需要 RA-GRS）。

# PARAMETERS

**--name** **-n**
> 表的名称。

**--account-name**
> 存储账户名。

**--account-key**
> 存储账户密钥。环境变量：AZURE_STORAGE_KEY。

**--auth-mode** _value_
> 身份验证模式：key（旧式账户密钥）或 login（Azure AD 凭据）。

**--permissions**
> generate-sas 使用的 SAS 权限：(r)ead/query、(a)dd、(u)pdate、(d)elete。可组合使用，例如 raud。

**--start-pk** / **--end-pk** / **--start-rk** / **--end-rk**
> 将表 SAS 限制在指定的分区键和行键范围内。

# DESCRIPTION

**az storage table** 管理 Azure 表存储中的表。表存储是一种 NoSQL 键值存储，适合存放结构化的非关系数据。表中包含实体（行），实体带有属性（列）。

请使用 **az storage entity** 命令管理表内的数据。

# CAVEATS

需要 Azure CLI 和有效的存储凭据。表名必须遵循 Azure 命名约定。表无法重命名，只能删除后重建。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [azure-cli](/man/azure-cli)(1), [az-storage](/man/az-storage)(1), [az-storage-entity](/man/az-storage-entity)(1), [az-storage-queue](/man/az-storage-queue)(1), [az-storage-account](/man/az-storage-account)(1)

# RESOURCES

```[Documentation](https://learn.microsoft.com/en-us/cli/azure/storage/table)```

```[Homepage](https://learn.microsoft.com/en-us/cli/azure/)```

```[Source code](https://github.com/Azure/azure-cli)```

<!-- verified: 2026-06-19 -->
