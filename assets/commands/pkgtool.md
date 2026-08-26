# TAGLINE

交互式 Slackware 软件包管理工具

# TLDR

启动**交互式**软件包工具

```sudo pkgtool```

交互式地**移除**软件包

```sudo pkgtool --remove_menu```

**查看**已安装的软件包

```pkgtool --view_menu```

从当前目录**安装**软件包

```sudo pkgtool --install_menu```

**设置**软件包（运行安装脚本）

```sudo pkgtool --setup_menu```

# SYNOPSIS

**pkgtool** [_options_]

# DESCRIPTION

**pkgtool** 是一个交互式的菜单驱动 Slackware 软件包管理工具。它提供基于 ncurses 的界面，用于安装、移除和查看软件包。

# PARAMETERS

**--remove_menu**
> 打开移除软件包菜单

**--view_menu**
> 打开查看已安装软件包菜单

**--install_menu**
> 打开安装软件包菜单（从当前目录）

**--setup_menu**
> 打开设置菜单（运行 doinst.sh 脚本）

# CAVEATS

如需命令行软件包管理，请直接使用 installpkg、removepkg 和 upgradepkg。pkgtool 需要能显示 ncurses 对话框的终端。

# HISTORY

**pkgtool** 是 Slackware 软件包管理系统的一部分，为管理 Slackware Linux 上的软件包提供了友好的界面。

# SEE ALSO

[installpkg](/man/installpkg)(8), [removepkg](/man/removepkg)(8), [upgradepkg](/man/upgradepkg)(8), [makepkg](/man/makepkg)(8)
