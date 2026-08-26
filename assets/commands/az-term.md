# TAGLINE

管理 Azure Marketplace 条款的接受状态

# TLDR

**接受计划的 Marketplace 条款**

```az term accept --publisher [publisher] --product [product] --plan [plan]```

**显示计划的 Marketplace 条款**

```az term show --publisher [publisher] --product [product] --plan [plan]```

**接受特定镜像 URN 的条款**

```az vm image terms accept --urn [publisher:offer:sku:version]```

**显示特定镜像 URN 的条款**

```az vm image terms show --urn [publisher:offer:sku:version]```

**限定到指定订阅**

```az term accept --publisher [pub] --product [prod] --plan [plan] --subscription [sub_id]```

# SYNOPSIS

**az** **term** _subcommand_ [_options_]

# SUBCOMMANDS

**accept**
> 接受计划的 Marketplace 条款。

**show**
> 显示计划的 Marketplace 条款。

# PARAMETERS

**--publisher**
> 要部署的镜像的发布者标识字符串（必需）。

**--product**
> 要部署的镜像的商品（offer）标识字符串（必需）。

**--plan**
> 要部署的镜像的计划（plan）标识字符串（必需）。

**--subscription**
> 要使用的订阅的名称或 ID。

**--output**, **-o**
> 输出格式：json, jsonc, none, table, tsv, yaml, yamlc。

**--query**
> JMESPath 查询字符串。

**--debug**
> 提高日志详细程度以显示所有调试日志。

# DESCRIPTION

**az term** 通过 **marketplaceordering** 提供程序管理 Azure Marketplace 协议的接受状态。许多第三方 Marketplace 镜像要求先接受条款和条件才能部署。该命令让你能以编程方式接受并查看这些条款。

等价的 **az vm image terms** 子命令接受单个 **--urn**（形如 _publisher:offer:sku:version_），而不是三个独立的标识符。

该命令组被微软标记为**实验性**，可能会有变化。

# CAVEATS

需要安装并完成 Azure CLI 身份验证。条款必须按订阅逐个接受。某些镜像在首次部署前需要接受条款。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [az-vm](/man/az-vm)(1), [az-image](/man/az-image)(1)
