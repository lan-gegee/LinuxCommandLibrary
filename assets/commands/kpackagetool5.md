# TAGLINE

管理 KDE Plasma 软件包，包括小部件、主题和壁纸

# TLDR

**列出**所有已知的软件包类型

```kpackagetool5 --list-types```

从目录**安装**软件包

```kpackagetool5 -t [package_type] -i [path/to/directory]```

**更新**已安装的软件包

```kpackagetool5 -t [package_type] -u [path/to/directory]```

**列出**已安装的小部件

```kpackagetool5 -t Plasma/Applet -l```

列出**全局**小部件（所有用户）

```kpackagetool5 -t Plasma/Applet -l -g```

按名称**移除**一个小部件

```kpackagetool5 -t Plasma/Applet -r "[name]"```

# SYNOPSIS

**kpackagetool5** [_options_]

# PARAMETERS

**--list-types**
> 列出所有可用的软件包类型

**-t**, **--type** _TYPE_
> 软件包类型（Plasma/Applet、Plasma/Theme 等）

**-i**, **--install** _PATH_
> 从目录安装软件包

**-u**, **--upgrade** _PATH_
> 更新已有的软件包

**-r**, **--remove** _NAME_
> 移除已安装的软件包

**-l**, **--list**
> 列出已安装的软件包

**-g**, **--global**
> 操作全局（系统级）软件包

# DESCRIPTION

**kpackagetool5** 管理 KDE Plasma 软件包，包括 plasmoid（小部件）、主题、壁纸及其他 Plasma 组件。它负责软件包的安装、移除和列出。

软件包类型包括 Plasma/Applet（小部件）、Plasma/Theme、Plasma/Wallpaper、Plasma/LookAndFeel 等。用户级软件包存储在 ~/.local/share/plasma/ 中。

# CAVEATS

仅适用于 KDE 5；KDE 6 使用 kpackagetool6。某些软件包可能需要重启 Plasma 才能生效。全局安装需要 root 权限。

# HISTORY

kpackagetool5 是 KDE Frameworks 5 的一部分，为 Plasma 的模块化组件系统提供软件包管理。它让用户能够用社区创作的内容扩展 Plasma。

# INSTALL

```apt: sudo apt install kpackagetool5```

```pacman: sudo pacman -S kpackage5```

```apk: sudo apk add kpackage5```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kpackagetool6](/man/kpackagetool6)(1)
