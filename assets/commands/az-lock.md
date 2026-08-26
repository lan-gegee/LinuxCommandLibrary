# TAGLINE

管理 Azure 资源锁

# TLDR

在资源组上**创建只读锁**

```az lock create --name [MyLock] --resource-group [MyResourceGroup] --lock-type ReadOnly```

创建删除锁以防止意外删除

```az lock create --name [MyLock] --resource-group [MyResourceGroup] --lock-type CanNotDelete```

**列出资源组中的所有锁**

```az lock list --resource-group [MyResourceGroup]```

**显示**某个锁的**详情**

```az lock show --name [MyLock] --resource-group [MyResourceGroup]```

**删除锁**

```az lock delete --name [MyLock] --resource-group [MyResourceGroup]```

对特定资源**创建锁**

```az lock create --name [MyLock] --resource-group [MyResourceGroup] --resource-name [MyResource] --resource-type [Microsoft.Storage/storageAccounts] --lock-type CanNotDelete```

# SYNOPSIS

**az** **lock** _subcommand_ [_options_]

# SUBCOMMANDS

**create**
> 创建锁。

**delete**
> 删除锁。

**list**
> 列出锁。

**show**
> 显示某个锁的详情。

**update**
> 更新锁。

# PARAMETERS

**--name** **-n**
> 锁的名称。

**--lock-type** **-t**
> 锁的类型：CanNotDelete 或 ReadOnly。

**--resource-group** **-g**
> 资源组的名称。

**--resource-name** **--resource**
> 被锁定资源的名称。

**--resource-type**
> 被锁定资源的类型（例如 Microsoft.Network/subnets）。

**--namespace**
> 提供程序命名空间（例如 Microsoft.Provider）。

**--parent**
> 嵌套资源的父路径（例如 resA/myA/resB/myB）。

**--notes**
> 关于该锁的备注。

**--ids**
> 一个或多个资源 ID。用于 delete/show/update，代替 --name。

# DESCRIPTION

**az lock** 管理 Azure 资源锁。锁可以防止关键资源被意外删除或修改。有两种锁类型：**CanNotDelete** 允许读取和修改操作但禁止删除，而 **ReadOnly** 只允许读取操作。

锁可以应用于订阅、资源组或单个资源级别。子资源会继承父资源上的锁。

# CAVEATS

需要 Azure CLI 和相应的 RBAC 权限（Owner 或 User Access Administrator）。锁不会限制 Azure 平台自身执行的操作。资源组上的 ReadOnly 锁会影响其中的所有资源。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [az-tag](/man/az-tag)(1), [az-provider](/man/az-provider)(1)
