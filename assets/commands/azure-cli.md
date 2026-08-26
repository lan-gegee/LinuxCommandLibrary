# TAGLINE

从命令行管理 Azure 云资源。

# TLDR

**交互式登录**（会打开浏览器）

```az login```

**验证**已安装的版本

```az --version```

**列出**你的订阅

```az account list --output table```

**设置**活动订阅

```az account set --subscription [name_or_id]```

**创建**资源组

```az group create --name [name] --location [eastus]```

使用 JMESPath **查询**输出

```az vm list --query "[].{name:name, rg:resourceGroup}" --output table```

通过 pip **安装**

```pip install azure-cli```

**就地更新** Azure CLI

```az upgrade```

# SYNOPSIS

**az** [_group_] [_subgroup_] _command_ [_options_]

# DESCRIPTION

**azure-cli** 是 Microsoft Azure 的跨平台命令行界面。它提供 `az` 命令，通过命令组树来管理 Azure 资源（例如 `az vm`、`az storage`、`az group`、`az aks`、`az network`），并以 Python 软件包及配套服务模块的形式分发。

命令遵循 `az <group> <subgroup> <command>` 模式。输出默认为 JSON，但可以切换为 table、TSV、YAML 或 none；JMESPath `--query` 表达式可筛选并重塑结果。更多功能可通过由 `az extension` 管理的扩展添加。

该软件包可以通过 pip、操作系统软件包管理器或独立安装程序安装。

# PARAMETERS

**-o**, **--output** _format_
> 输出格式：json（默认）、jsonc、table、tsv、yaml、yamlc 或 none。

**--query** _jmespath_
> 用于筛选和投影响应的 JMESPath 查询字符串。

**--subscription** _name_or_id_
> 此命令要使用的订阅的名称或 ID。

**-h**, **--help**
> 显示命令或命令组的帮助。

**--verbose**
> 提高日志详细程度。

**--debug**
> 显示完整的调试日志，提交问题反馈时很有用。

**--only-show-errors**
> 抑制警告，仅显示错误。

# COMMON COMMANDS

**az login** / **az logout**
> 登录或登出 Azure。

**az account**
> 管理订阅和活动上下文。

**az group**
> 管理资源组。

**az upgrade**
> 将 CLI 和已安装的扩展更新到最新版本。

**az extension**
> 安装和管理 CLI 扩展。

**az interactive**
> 启动带有自动补全和示例的交互式 Shell。

**az config**
> 管理 CLI 的持久化默认值（在默认值管理上取代 `az configure`）。

# INSTALLATION METHODS

**Python pip**
```bash
pip install azure-cli
```

**macOS Homebrew**
```bash
brew install azure-cli
```

**Ubuntu/Debian**
```bash
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

**Windows**
> 从微软官网下载 MSI 安装程序

**Docker**
```bash
docker run -it mcr.microsoft.com/azure-cli
```

# COMPONENTS

该软件包包含：
- 核心 CLI（`az` 命令）
- 全部服务模块
- 扩展框架
- 自动补全支持
- 遥测（可禁用）

# CONFIGURATION

**~/.azure/config**
> 用户专属的 Azure CLI 配置文件，用于保存默认值、输出格式和扩展设置。

# CAVEATS

需要 Python 3.8+。安装体积较大（数百 MB）。需要定期更新才能获得新功能。一些较旧的 Linux 发行版需要手动安装依赖。扩展需要单独安装。

# HISTORY

**azure-cli**（2.0 及以上版本）于 **2017** 年发布，是以 Python 完全重写的版本，取代了基于 Node.js 的 1.0 版本。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [az-login](/man/az-login)(1), [az-account](/man/az-account)(1), [az-extension](/man/az-extension)(1), [azcopy](/man/azcopy)(1), [pip](/man/pip)(1)

# RESOURCES

```[Source code](https://github.com/Azure/azure-cli)```

```[Documentation](https://learn.microsoft.com/en-us/cli/azure/)```

<!-- verified: 2026-06-19 -->
