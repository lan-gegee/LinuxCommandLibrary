# TAGLINE

管理 Azure 容器注册表

# TLDR

**创建容器注册表**

```az acr create -n [registry-name] -g [resource-group] --sku [Standard]```

**登录**到注册表

```az acr login -n [registry-name]```

**列出订阅中的所有注册表**

```az acr list -o table```

**构建并推送镜像**

```az acr build -t [image:tag] -r [registry-name] [./source-directory]```

从另一个注册表**导入镜像**

```az acr import -n [registry-name] --source [source-registry.azurecr.io/repo:tag]```

**列出注册表中的仓库**

```az acr repository list -n [registry-name] -o table```

**显示注册表详情**

```az acr show -n [registry-name]```

**检查注册表健康状况**

```az acr check-health -n [registry-name]```

# SYNOPSIS

**az acr** _subcommand_ [_options_]

# DESCRIPTION

**az acr** 管理 Azure 容器注册表（ACR），一种用于存储和管理容器镜像的私有 Docker 注册表服务。ACR 与 Azure Kubernetes Service、App Service 及其他 Azure 服务集成。

该命令组支持注册表创建、镜像管理、身份验证、异地复制、通过 ACR Tasks 进行自动构建，以及制品流式传输和供应链安全等高级功能。

# SUBCOMMANDS

**Registry Management**
> create, delete, update, show, list, show-usage, show-endpoints, check-name, check-health

**Authentication**
> login, credential show, credential renew, token create, token delete

**Image Operations**
> build, run, import, repository list, repository show, repository show-tags, repository delete, manifest list, manifest delete

**Tasks**
> task create, task run, task list, task show, task update, task logs

**Replication**
> replication create, replication delete, replication list, replication show

**Advanced**
> webhook create, webhook list, private-endpoint-connection, network-rule add, scope-map create, config retention update

# PARAMETERS

**-n, --name** _value_
> 容器注册表的名称

**-g, --resource-group** _value_
> 资源组的名称

**--sku** _value_
> 注册表 SKU：Basic、Standard 或 Premium

**--admin-enabled** _{true,false}_
> 启用管理员用户（用户名和密码登录）。默认禁用。

**-t, --image** _value_
> 镜像名称和标签（name:tag 格式）

**-r, --registry** _value_
> 构建操作使用的注册表名称

# CAVEATS

注册表名称必须全局唯一，长度为 5-50 个字符。异地复制和专用终结点需要 **Premium** SKU。ACR Tasks 按计算时间计费。登录令牌会在一段时间后过期；使用 **az acr login** 刷新。

# HISTORY

Azure 容器注册表于 **2017** 年作为托管的 Docker 注册表服务推出。此后它扩展到支持 Helm chart、OCI 制品，并与 Microsoft Defender for Cloud 集成了安全扫描。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [az-aks](/man/az-aks)(1), [docker](/man/docker)(1)

# RESOURCES

```[Source code](https://github.com/Azure/azure-cli)```

```[Documentation](https://learn.microsoft.com/en-us/cli/azure/acr)```

<!-- verified: 2026-06-18 -->
