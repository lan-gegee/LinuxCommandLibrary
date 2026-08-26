# TAGLINE

管理 Azure CLI 配置设置

# TLDR

**获取所有配置**

```az config get```

**获取特定配置**节

```az config get [core]```

**获取特定配置**键

```az config get [core.no_color]```

**禁用彩色输出**

```az config set core.no_color=true```

**设置默认资源组**和位置

```az config set defaults.group=[MyResourceGroup] defaults.location=[westus2]```

**启用日志记录**到文件

```az config set logging.enable_log_file=true```

**取消某个配置**

```az config unset [core.no_color]```

为当前目录**设置本地配置**

```az config set defaults.group=[myRG] --local```

# SYNOPSIS

**az** **config** _subcommand_ [_options_]

# SUBCOMMANDS

**get**
> 获取配置值。

**set**
> 设置配置值。

**unset**
> 取消配置值。

**param-persist**
> 管理参数持久化。

**param-persist on**
> 启用参数持久化。

**param-persist off**
> 禁用参数持久化。

**param-persist show**
> 显示参数持久化数据。

**param-persist delete**
> 删除参数持久化数据。

# PARAMETERS

**--local**
> 将配置应用到本地作用域（工作目录）而非全局。

# DESCRIPTION

**az config** 管理 Azure CLI 的配置设置。它可以自定义 CLI 行为，包括输出格式化、默认值、遥测、日志记录和错误显示。配置可以全局设置，也可以按目录本地设置。

默认配置文件存储在 ~/.azure/config。

# CONFIGURATION

**~/.azure/config**
> 全局 Azure CLI 配置文件，采用 INI 格式分节，包含 core、defaults、logging 等设置。

**.azure/config**
> 本地目录作用域的配置文件，通过 --local 标志创建，会覆盖当前项目的全局设置。

# CAVEATS

该命令组标记为**实验性**且仍在开发中（并非已弃用）；行为和选项可能变化。自 Azure CLI 2.10.0 起可用。本地配置存储在当前工作目录中，优先级高于全局配置。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [az-appconfig](/man/az-appconfig)(1)

# RESOURCES

```[Source code](https://github.com/Azure/azure-cli)```

```[Documentation](https://learn.microsoft.com/en-us/cli/azure/config)```

<!-- verified: 2026-06-18 -->
