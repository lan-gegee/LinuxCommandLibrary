# TAGLINE

管理 Azure AI 与认知服务账户

# TLDR

**创建认知服务账户**

```az cognitiveservices account create --name [myaccount] --resource-group [myRG] --kind [TextAnalytics] --sku [S1] --location [eastus]```

**列出所有认知服务账户**

```az cognitiveservices account list```

**显示账户详情**

```az cognitiveservices account show --name [myaccount] --resource-group [myRG]```

**列出 API 访问密钥**

```az cognitiveservices account keys list --name [myaccount] --resource-group [myRG]```

**重新生成 API 密钥**

```az cognitiveservices account keys regenerate --name [myaccount] --resource-group [myRG] --key-name [key1]```

**列出可用的账户类型**

```az cognitiveservices account list-kinds```

针对特定类型和位置**列出可用的 SKU**

```az cognitiveservices account list-skus --kind [TextAnalytics] --location [eastus]```

**删除账户**

```az cognitiveservices account delete --name [myaccount] --resource-group [myRG]```

# SYNOPSIS

**az** **cognitiveservices** **account** _subcommand_ [_options_]

# SUBCOMMANDS

**account create**
> 创建认知服务账户。

**account delete**
> 删除认知服务账户。

**account list**
> 列出所有认知服务账户。

**account show**
> 显示特定账户的详情。

**account keys list**
> 列出账户访问密钥。

**account keys regenerate**
> 重新生成账户密钥。

**account deployment**
> 管理模型部署。

**account commitment-plan**
> 管理承诺计划。

**account network-rule**
> 管理网络规则。

**account list-kinds**
> 列出可用的账户类型。

**account list-skus**
> 列出某种服务类型和位置可用的 SKU。

# DESCRIPTION

**az cognitiveservices** 管理 Azure 认知服务账户，这些服务提供视觉、语音、语言和决策等 AI 能力的 API。它负责 Text Analytics、Computer Vision、Speech Services 和 OpenAI 等服务的账户创建、配置、部署和订阅管理。

# CAVEATS

需要安装 Azure CLI 并已通过 **az login** 完成身份验证。不同的服务类型有不同的 SKU 可用性和定价。某些服务在创建前需要接受负责任的 AI 使用条款。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [az-config](/man/az-config)(1), [az-account](/man/az-account)(1), [az-group](/man/az-group)(1)
