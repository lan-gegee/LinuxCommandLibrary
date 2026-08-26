# TAGLINE

统一 Yay、Flatpak 和 Snap 操作的元包管理器

# TLDR

**搜索**软件包

```paxs [search_term]```

**升级**所有软件包

```paxs -u```

**安装**软件包（提示选择来源）

```paxs -i [package]```

**删除**软件包

```paxs -r [package]```

**检查**更新

```paxs -c```

显示**帮助**

```paxs -h```

# SYNOPSIS

**paxs** [**-u**|**--upgrade-all**] [**-i**|**--install** _pkg_] [**-r**|**--remove** _pkg_] [**-c**|**--check-update**] [_search_term_]

# PARAMETERS

**-u, --upgrade-all**
> 升级所有包管理器中的全部软件包

**-i, --install _package_**
> 安装软件包（在多个来源中都存在时提示选择来源）

**-r, --remove _package_**
> 删除软件包（存在于多个来源时提示选择来源）

**-c, --check-update**
> 检查所有管理器中的更新

**-h, --help**
> 显示帮助信息

# DESCRIPTION

**paxs** 是一个元包管理器，统一了 Yay（AUR）、Flatpak 和 Snap 的操作。它通过单一界面对来自多个来源的软件包进行搜索、安装、删除和升级。

当某个软件包存在于多个来源时，paxs 会提示用户选择要使用的来源。这简化了使用多种软件包格式的系统上的软件包管理。

# CAVEATS

需要安装 yay、flatpak 和/或 snap。只能通过受支持的包管理器管理软件包。根据底层管理器的不同，某些操作可能需要 root 权限。

# HISTORY

**paxs** 由 **zamhedonia** 创建，旨在解决现代 Linux 系统上管理多个包管理器的复杂问题。它提供统一界面，同时不替代底层包管理器。

# INSTALL

```aur: yay -S paxs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[yay](/man/yay)(1), [flatpak](/man/flatpak)(1), [snap](/man/snap)(1), [pacman](/man/pacman)(8)
