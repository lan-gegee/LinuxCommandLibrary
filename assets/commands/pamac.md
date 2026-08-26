# TAGLINE

面向基于 Arch 发行版的图形与命令行软件包管理器

# TLDR

**安装**软件包

```pamac install [package]```

**移除**软件包及其孤立依赖

```pamac remove --orphans [package]```

**搜索**软件包

```pamac search [package]```

**列出**已安装的软件包

```pamac list --installed```

**检查**更新

```pamac checkupdates```

**升级**所有软件包

```pamac upgrade```

# SYNOPSIS

**pamac** [**install**|**remove**|**search**|**list**|**upgrade**|**checkupdates**] [_options_] [_packages_...]

# COMMANDS

**install**
> 从仓库或 AUR 安装软件包

**remove**
> 移除已安装的软件包

**search**
> 搜索软件包数据库

**list**
> 列出软件包（已安装、孤立包等）

**upgrade**
> 升级已安装的软件包

**checkupdates**
> 检查可用更新

**build**
> 从 AUR 构建软件包

**clean**
> 清理软件包缓存

# PARAMETERS

**--orphans**
> 移除时包含孤立的依赖

**--aur**
> 在操作中包含 AUR

**--no-confirm**
> 跳过确认提示

**-a, --all**
> 应用于所有软件包

**--installed**
> 只筛选已安装的软件包

# DESCRIPTION

**pamac** 是面向基于 Arch 的发行版（主要是 Manjaro）的图形与命令行软件包管理器。它为 pacman 提供友好的用户界面，并支持 AUR（Arch 用户仓库）集成。

该工具将软件包的安装、移除、搜索和系统更新整合在统一界面中。AUR 支持需要在 /etc/pamac.conf 或 GUI 设置中启用。

# CAVEATS

AUR 软件包需要先在配置中启用。某些操作需要 root 权限。AUR 软件包的构建依赖可能需要手动处理。更新可能需要重启系统。

# HISTORY

**pamac** 由 **Manjaro** 团队开发，是用户体验更佳的 pacman 替代品。它同时提供 GTK 和 CLI 界面，让不熟悉命令行工具的用户也能轻松管理软件包。

# SEE ALSO

[pacman](/man/pacman)(8), [yay](/man/yay)(1), [paru](/man/paru)(1)
