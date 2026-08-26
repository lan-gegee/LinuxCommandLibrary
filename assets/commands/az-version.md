# TAGLINE

显示 Azure CLI 版本信息

# TLDR

**显示**Azure CLI 版本

```az version```

以 **JSON** 格式显示版本

```az version -o json```

以 **table** 格式显示版本

```az version --output table```

# SYNOPSIS

**az version** [**-o**|**--output** _format_]

# PARAMETERS

**-o**, **--output** _format_
> 输出格式。接受值：**json**, **jsonc**, **none**, **table**, **tsv**, **yaml**, **yamlc**。默认：**json**。

# DESCRIPTION

**az version** 显示 Azure CLI 及所有已安装扩展的版本信息。它会显示 CLI 核心版本、Python 版本以及各个扩展的版本。

该命令可用于故障排查和验证安装。

# OUTPUT

显示的信息：
- Azure CLI 核心版本
- Python 版本与平台
- 已安装的扩展及其版本

# WORKFLOW

```bash
# Show all version info
az version

# JSON output for parsing
az version -o json

# Check specific extension
az version -o json | jq '.extensions."some-extension"'
```

# CAVEATS

输出格式可能因 Azure CLI 版本而异。扩展版本与 CLI 核心版本分开列出。默认输出格式为 JSON。

# HISTORY

**az version** 自 **2017** 年的 Azure CLI 2.0 起即可用，是一个用于查看版本信息的诊断命令。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [az-upgrade](/man/az-upgrade)(1), [az-extension](/man/az-extension)(1), [az-login](/man/az-login)(1)
