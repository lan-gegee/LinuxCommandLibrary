# TAGLINE

重新配置 Void Linux 软件包

# TLDR

**重新配置一个软件包**

```sudo xbps-reconfigure [package_name]```

**强制重新配置一个软件包**

```sudo xbps-reconfigure -f [package_name]```

**重新配置所有软件包**

```sudo xbps-reconfigure -a```

**重新配置内核**

```sudo xbps-reconfigure -f linux[5.15]```

**详细输出**

```sudo xbps-reconfigure -v [package_name]```

**在替代根目录中重新配置**

```sudo xbps-reconfigure -r [/mnt] [package_name]```

# SYNOPSIS

**xbps-reconfigure** [_options_] _package_ | **-a**

# PARAMETERS

**-a**, **--all**
> 重新配置所有软件包。

**-f**, **--force**
> 即使已配置过也强制重新配置。

**-r** _rootdir_
> 使用替代根目录。

**-v**, **--verbose**
> 详细输出。

**-d**, **--debug**
> 调试模式。

**-h**, **--help**
> 显示帮助。

**-V**, **--version**
> 显示版本。

# DESCRIPTION

**xbps-reconfigure** 在 Void Linux 上为软件包运行安装后的配置脚本。它用于配置未正确完成配置的软件包，或在修改配置文件后进行重新配置。

该工具适用于从被中断的安装中恢复、手动修改配置后重新配置，或重建内核模块。默认只处理未配置的软件包；使用 -f 可强制重新配置。

常见用例包括更新后重新配置内核、重跑 DKMS 模块构建以及修复存在配置问题的软件包。

# CAVEATS

Void Linux 专用（XBPS 包管理器）。某些软件包在重新配置时可能会覆盖手动修改的配置。重新配置内核需要指定确切的版本号。

# HISTORY

**xbps-reconfigure** 是 XBPS（X Binary Package System）的一部分，后者是专为 Void Linux 开发的包管理器。XBPS 从零开始设计，追求快速、可移植和无缺陷，为传统包管理器提供了现代化的替代方案。

# INSTALL

```apk: sudo apk add xbps```

```nix: nix profile install nixpkgs#xbps```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xbps-install](/man/xbps-install)(1), [xbps-remove](/man/xbps-remove)(1), [xbps-query](/man/xbps-query)(1)
