# TAGLINE

显示版本和构建信息

# TLDR

**显示 Dolt 版本**

```dolt version```

**显示详细的版本**信息

```dolt version --verbose```

# SYNOPSIS

**dolt version** [_options_]

# PARAMETERS

**--verbose**, **-v**
> 显示详细的版本信息。

**--feature**
> 显示特性版本。

**--help**
> 显示帮助信息。

# DESCRIPTION

**dolt version** 显示已安装的 Dolt 版本和构建信息。verbose 标志会提供更多细节，包括编译所用的 Go 版本和构建元数据。

版本信息可用于故障排查、确认与仓库的兼容性以及验证安装是否正确。不同的 Dolt 版本可能采用不同的存储格式或支持不同的特性。

# CAVEATS

版本号遵循语义化版本规范。仓库格式版本可能与工具版本不同步。旧版本可能无法读取较新的仓库格式。

# HISTORY

dolt version 遵循标准的版本信息输出惯例，为 **Dolt** 生态中的技术支持和兼容性验证提供必要依据。

# INSTALL

```pacman: sudo pacman -S dolt```

```brew: brew install dolt```

```nix: nix profile install nixpkgs#dolt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dolt](/man/dolt)(1)
