# TAGLINE

向 Azure CLI 团队发送反馈

# TLDR

打开表单以**报告**关于 Azure CLI 的**反馈**

```az feedback```

# SYNOPSIS

**az** **feedback**

# DESCRIPTION

**az feedback** 会打开一个交互式提示，用于向 Azure CLI 团队发送反馈。它收集关于你使用体验的信息，允许你报告问题、建议功能或提供关于 Azure CLI 的一般反馈。

该命令会引导你填写反馈细节，并可以自动附带诊断信息，帮助团队调查问题。

它会记录最近运行的命令，并提示你在 Azure CLI 仓库上创建 GitHub issue，同时预填环境详情。

# PARAMETERS

**az feedback** 没有专属选项。仅适用标准的 Azure CLI 全局参数（例如 **--help**、**--debug**、**--verbose**、**--output**）。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [az-config](/man/az-config)(1)

# RESOURCES

```[Source code](https://github.com/Azure/azure-cli)```

```[Documentation](https://learn.microsoft.com/en-us/cli/azure/reference-index)```

<!-- verified: 2026-06-18 -->
