# TAGLINE

检查 AUR 软件包更新

# TLDR

列出 **AUR 软件包**的待更新项

```checkupdates-aur```

以**调试模式**列出待更新项

```CHECKUPDATES_DEBUG=1 checkupdates-aur```

# SYNOPSIS

**checkupdates-aur** [_options_]

# DESCRIPTION

**checkupdates-aur** 检查 Arch 用户仓库（AUR）中的待更新项。它将本地安装的 AUR 软件包与 AUR 上的最新版本进行比较。

该工具弥补了标准 checkupdates 命令的不足，覆盖了官方软件仓库之外的软件包。

# PARAMETERS

**--help**
> 显示帮助信息

# ENVIRONMENT

**CHECKUPDATES_DEBUG**
> 设为 1 以启用调试输出

# CAVEATS

仅限 Arch Linux。只检查最初从 AUR 安装的软件包。需要网络访问才能查询 AUR API。

# SEE ALSO

[checkupdates](/man/checkupdates)(1), [yay](/man/yay)(1), [paru](/man/paru)(1), [pacman](/man/pacman)(8)
