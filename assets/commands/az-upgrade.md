# TAGLINE

将 Azure CLI 更新到最新版本

# TLDR

**升级**Azure CLI 和已安装的扩展

```az upgrade```

升级并**跳过提示**，不查看发行说明

```az upgrade --yes```

仅升级 **CLI 本体**，扩展保持不变

```az upgrade --all false```

升级时包含**预览版**扩展包

```az upgrade --allow-preview true```

# SYNOPSIS

**az upgrade** [_options_]

# DESCRIPTION

**az upgrade** 将 Azure CLI 及其已安装的扩展（默认情况）升级到最新的可用版本。它会检查可用更新并加以安装，确保你能用上最新的功能和缺陷修复。

该命令会自动处理整个升级过程，包括依赖项更新。此命令处于**预览**阶段。

# PARAMETERS

**-y**, **--yes**
> 不提示检查发行说明。

**--all** _{false, true}_
> 是否同时更新扩展。默认：**true**。

**--allow-preview**, **--allow-preview-extensions** _{false, true}_
> 安装扩展时包含预览版软件包（如果存在）。

# WORKFLOW

```bash
# Upgrade CLI and extensions with confirmation
az upgrade

# Upgrade without the release-notes prompt
az upgrade --yes

# Upgrade only the CLI, skipping extensions
az upgrade --all false
```

# CAVEATS

需要有足够的权限修改安装目录。可能需要重启 Shell 才能让更改生效。该命令适用于通过官方安装程序（MSI、Homebrew、apt/yum 等）完成的安装；某些系统软件包管理器会自行处理更新，可能不受支持。没有提供只检查更新而不安装的选项。

# HISTORY

**az upgrade** 于 **2020** 年 **8 月**随 Azure CLI **2.11** 引入，提供了内置的更新机制，取代了手动更新流程。它目前仍是预览命令。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [az-version](/man/az-version)(1), [az-extension](/man/az-extension)(1)

# RESOURCES

```[Source code](https://github.com/Azure/azure-cli)```

```[Documentation](https://learn.microsoft.com/en-us/cli/azure/reference-index#az-upgrade)```

```[Homepage](https://learn.microsoft.com/en-us/cli/azure/)```

<!-- verified: 2026-06-19 -->
