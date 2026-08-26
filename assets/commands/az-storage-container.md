# TAGLINE

管理 Azure Blob 存储容器

# TLDR

**创建容器**

```az storage container create -n [container-name] --account-name [account]```

**创建时允许公开 Blob 访问**

```az storage container create -n [container-name] --public-access blob --account-name [account]```

**列出所有容器**

```az storage container list --account-name [account] -o table```

**检查容器是否存在**

```az storage container exists -n [container-name] --account-name [account]```

**显示容器属性**

```az storage container show -n [container-name] --account-name [account]```

**为容器生成 SAS 令牌**

```az storage container generate-sas -n [container-name] --permissions [acdlrw] --expiry [2026-12-31T00:00Z] --account-name [account]```

**删除容器**

```az storage container delete -n [container-name] --account-name [account]```

**恢复软删除的容器**

```az storage container restore -n [container-name] --deleted-version [version] --account-name [account]```

# SYNOPSIS

**az storage container** _subcommand_ [_options_]

# DESCRIPTION

**az storage container** 管理 Azure 存储账户中的 Blob 存储容器。容器用于对 Blob 分组，类似文件系统中的目录。

容器可以有不同的访问级别：private（私有，默认）、blob（可匿名读取 Blob）或 container（可匿名读取容器及其中的 Blob）。所有 Blob 都必须位于某个容器中。

# SUBCOMMANDS

**容器生命周期**
> create, delete, list, exists, show, restore

**访问控制**
> set-permission, show-permission, generate-sas

**元数据**
> metadata show, metadata update

**租约**
> lease acquire, lease break, lease release, lease renew, lease change

**策略**
> policy create, policy delete, policy list, policy show, policy update

**合规**
> immutability-policy create, immutability-policy lock, immutability-policy extend, immutability-policy show, immutability-policy delete, legal-hold set, legal-hold clear, legal-hold show

# PARAMETERS

**-n, --name** _value_
> 容器的名称

**--account-name** _value_
> 存储账户名

**--account-key** _value_
> 存储账户密钥

**--public-access** _value_
> 公开访问级别：blob、container、off。默认 off（私有）。

**--auth-mode** _value_
> 身份验证模式：key（旧式账户密钥）或 login（你的 Azure AD 凭据）。

**--fail-on-exist**
> 若容器已存在则抛出异常。

**--permissions** _value_
> SAS 权限：(a)dd、(c)reate、(d)elete、(l)ist、(r)ead、(w)rite

**--expiry** _value_
> SAS 令牌的到期日期时间（UTC）

# CAVEATS

容器名称必须为 3-63 个字符，只能包含小写字母、数字和连字符。删除容器会删除其中包含的所有 Blob。软删除策略允许在保留期内进行恢复。出于合规目的，不可变性策略和法定保留会阻止删除。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [azure-cli](/man/azure-cli)(1), [az-storage](/man/az-storage)(1), [az-storage-blob](/man/az-storage-blob)(1), [az-storage-account](/man/az-storage-account)(1), [azcopy](/man/azcopy)(1)

# RESOURCES

```[Documentation](https://learn.microsoft.com/en-us/cli/azure/storage/container)```

```[Homepage](https://learn.microsoft.com/en-us/cli/azure/)```

```[Source code](https://github.com/Azure/azure-cli)```

<!-- verified: 2026-06-19 -->
