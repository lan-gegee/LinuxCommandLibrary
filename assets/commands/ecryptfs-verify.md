# TAGLINE

校验 eCryptfs 加密设置

# TLDR

**校验 eCryptfs 设置**

```ecryptfs-verify```

**校验主目录**加密

```ecryptfs-verify --home```

以**详细输出**校验

```ecryptfs-verify -v```

# SYNOPSIS

**ecryptfs-verify** [_options_]

# PARAMETERS

**--home**
> 校验主目录加密。

**-v**, **--verbose**
> 详细输出。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**ecryptfs-verify** 检查用户的 eCryptfs 加密是否配置正确。它会验证挂载点、包装口令和加密设置。

该工具验证加密私有目录是否正确挂载且可访问。它检查常见的配置错误并报告问题。

在设置完成或系统升级后运行校验，可确保加密持续正常工作。

# CAVEATS

必须以待校验加密的用户身份运行。无法校验未挂载的加密目录。报告的是配置问题而非内容完整性。

# HISTORY

ecryptfs-verify 是 **eCryptfs** 工具集的一部分，为 Ubuntu 及其他使用 eCryptfs 的发行版提供加密文件系统配置的验证功能。

# INSTALL

```apt: sudo apt install ecryptfs-utils```

```dnf: sudo dnf install ecryptfs-utils```

```pacman: sudo pacman -S ecryptfs-utils```

```apk: sudo apk add ecryptfs-utils```

```zypper: sudo zypper install ecryptfs-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ecryptfs](/man/ecryptfs)(7), [ecryptfs-setup-private](/man/ecryptfs-setup-private)(1), [ecryptfs-find](/man/ecryptfs-find)(1)
