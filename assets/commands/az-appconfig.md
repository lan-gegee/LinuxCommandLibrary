# TAGLINE

管理 Azure App Configuration 存储

# TLDR

**创建 App Configuration 存储**

```az appconfig create --name [MyAppConfig] --resource-group [MyResourceGroup] --location [westus] --sku [Standard]```

**列出资源组中的所有 App Configuration 存储**

```az appconfig list --resource-group [MyResourceGroup]```

**显示**某个 App Configuration 存储的**详情**

```az appconfig show --name [MyAppConfig] --resource-group [MyResourceGroup]```

在存储中**设置键值对**

```az appconfig kv set --name [MyAppConfig] --key [myKey] --value [myValue]```

**列出存储中的键值对**

```az appconfig kv list --name [MyAppConfig]```

从文件**导入配置**

```az appconfig kv import --name [MyAppConfig] --source file --path [config.json] --format json```

**启用功能开关**

```az appconfig feature enable --name [MyAppConfig] --feature [myFeature]```

**删除 App Configuration 存储**

```az appconfig delete --name [MyAppConfig] --resource-group [MyResourceGroup]```

# SYNOPSIS

**az** **appconfig** _subcommand_ [_options_]

# SUBCOMMANDS

**create**
> 创建 App Configuration 存储。

**delete**
> 删除 App Configuration 存储。

**list**
> 列出所有 App Configuration 存储。

**show**
> 显示存储的属性。

**update**
> 更新 App Configuration 存储。

**kv**
> 管理键值对（set、get、list、delete、lock、unlock）。

**kv import/export**
> 导入/导出配置。

**feature**
> 管理功能开关（enable、disable、set、delete）。

**credential**
> 管理访问密钥。

**replica**
> 管理副本（Premium 层级）。

**snapshot**
> 管理配置快照。

# DESCRIPTION

**az appconfig** 管理 Azure App Configuration 存储，该服务用于集中管理应用程序设置和功能开关。App Configuration 通过将配置与代码分离，帮助实现 Twelve-Factor App 方法论。

可用的 SKU 有 Free、Developer、Standard 和 Premium（默认为 Standard），其中 Premium 提供通过副本实现异地复制等额外功能。

# CAVEATS

需要安装 Azure CLI 并已通过 **az login** 完成身份验证。副本等功能仅在 Premium 层级可用。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [az-config](/man/az-config)(1), [az-advisor](/man/az-advisor)(1)

# RESOURCES

```[Source code](https://github.com/Azure/azure-cli)```

```[Documentation](https://learn.microsoft.com/en-us/cli/azure/appconfig)```

<!-- verified: 2026-06-18 -->
