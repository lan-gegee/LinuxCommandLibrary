# TAGLINE

SUSE 和 openSUSE 的软件包管理器

# TLDR

**同步**可用软件包及其版本的列表

```sudo zypper refresh```

**安装**新软件包

```sudo zypper install [package]```

**移除**软件包

```sudo zypper remove [package]```

**升级**已安装软件包到最新可用版本

```sudo zypper update```

**搜索**软件包（按关键字）

```zypper search [keyword]```

**显示**已配置软件仓库的信息

```zypper repos --sort-by-priority```

# SYNOPSIS

**zypper** [_global-options_] _command_ [_command-options_] [_arguments_]

# PARAMETERS

**ref, refresh**
> 刷新所有软件仓库

**in, install _package_**
> 安装软件包

**rm, remove _package_**
> 移除软件包

**up, update**
> 更新已安装的软件包

**se, search _pattern_**
> 搜索软件包

**lr, repos**
> 列出所有已配置的软件仓库

**dup, dist-upgrade**
> 执行发行版升级

**--no-confirm**
> 不询问确认

**--sort-by-priority**
> 按优先级排序仓库列表

# DESCRIPTION

**zypper** 是 SUSE 和 openSUSE Linux 的命令行软件包管理工具。它提供完整的包管理功能，涵盖安装、移除、更新和软件仓库管理。

Zypper 支持依赖解析和补丁管理，也能处理发行版升级。它基于 libzypp 库构建，是 YaST 软件管理功能的 CLI 前端。

# CAVEATS

软件包操作需要 root 权限。更新前应先刷新仓库（**zypper ref**）。发行版升级（**zypper dup**）须谨慎执行。

# INSTALL

```apt: sudo apt install zypper```

```dnf: sudo dnf install zypper```

```pacman: sudo pacman -S zypper```

```zypper: sudo zypper install zypper```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rpm](/man/rpm)(8), [yast2](/man/yast2)(8)
