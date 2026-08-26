# TAGLINE

设置或显示目标账户、区域、资源组和 Cloud Foundry 组织/空间

# TLDR

**显示当前目标**

```ibmcloud target```

**设置目标区域**

```ibmcloud target -r [us-south]```

**设置目标资源组**

```ibmcloud target -g [resource-group]```

**设置 Cloud Foundry 组织和空间**

```ibmcloud target -o [org] -s [space]```

**设置目标账户**

```ibmcloud target -c [account-id]```

**取消资源组**

```ibmcloud target --unset-resource-group```

# SYNOPSIS

**ibmcloud** **target** [_options_]

# PARAMETERS

**-r** _region_
> 目标区域。

**-g** _group_
> 目标资源组。

**-c** _account_
> 目标账户 ID。

**-o** _org_
> 目标 Cloud Foundry 组织。

**-s** _space_
> 目标 Cloud Foundry 空间。

**--cf**
> 目标设为 Cloud Foundry 环境并自动选择组织/空间。

**--cf-api** _URL_
> 目标设为指定的 Cloud Foundry API 端点。

**--unset-resource-group**
> 清除已设置的资源组。

**--output** _FORMAT_
> 输出格式（例如 `json`）。

# DESCRIPTION

**ibmcloud target** 设置或显示目标账户、区域、资源组以及 Cloud Foundry 组织/空间。后续的 CLI 命令都在该目标上下文中运行。不带选项运行可显示当前目标。

# SEE ALSO

[ibmcloud](/man/ibmcloud)(1), [ibmcloud-login](/man/ibmcloud-login)(1)
