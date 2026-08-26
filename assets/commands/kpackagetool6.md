# TAGLINE

安装、列出和移除 KDE Plasma 6 软件包

# TLDR

**列出所有可用的软件包类型**

```kpackagetool6 --list-types```

从目录或文件**安装软件包**

```kpackagetool6 -t [Plasma/Applet] -i [path/to/package]```

**升级已安装的软件包**

```kpackagetool6 -t [Plasma/Applet] -u [path/to/package]```

**列出已安装的小部件**

```kpackagetool6 -t Plasma/Applet -l```

**列出全局安装的小部件**（所有用户）

```kpackagetool6 -t Plasma/Applet -l -g```

按名称**移除一个小部件**

```kpackagetool6 -t Plasma/Applet -r "[name]"```

**显示已安装软件包的信息**

```kpackagetool6 -t [Plasma/Applet] -s "[name]"```

# SYNOPSIS

**kpackagetool6** [_options_]

# PARAMETERS

**--list-types**
> 列出所有可用的软件包类型。

**-t**, **--type** _TYPE_
> 软件包类型（Plasma/Applet、Plasma/Theme、Plasma/Wallpaper、Plasma/LookAndFeel 等）。

**-i**, **--install** _PATH_
> 从目录或文件安装软件包。

**-u**, **--upgrade** _PATH_
> 升级已有的软件包。

**-r**, **--remove** _NAME_
> 移除已安装的软件包。

**-l**, **--list**
> 列出给定类型的已安装软件包。

**-s**, **--show** _NAME_
> 显示某个已安装软件包的信息。

**-g**, **--global**
> 操作全局（系统级）软件包。

**-p**, **--packageroot** _PATH_
> 使用指定的软件包根目录绝对路径，而不是标准数据目录。

**--appstream-metainfo** _PATH_
> 为软件包输出 AppStream 元数据。

# DESCRIPTION

**kpackagetool6** 管理 KDE Plasma 6 软件包，包括 plasmoid（小部件）、主题、壁纸、KWin 脚本及其他 Plasma 组件。它是 KDE Frameworks 6 版本的软件包管理工具。

软件包类型包括 Plasma/Applet（小部件）、Plasma/Theme、Plasma/Wallpaper、Plasma/LookAndFeel、KWin/Script 等。用户级软件包存储在 `~/.local/share/plasma/` 中。它管理的是通过 KPackage 或 store.kde.org 安装的软件包，而不是来自发行版仓库的系统软件包。

# CAVEATS

仅适用于 KDE 6；KDE 5 请使用 kpackagetool5。某些软件包可能需要重启 Plasma 才能生效。全局安装需要 root 权限。

# HISTORY

kpackagetool6 是 KDE Frameworks 6 的一部分，是 KDE Frameworks 5 的后继者。它延续了面向 Plasma 组件的模块化软件包管理系统。

# INSTALL

```apt: sudo apt install kpackagetool6```

```pacman: sudo pacman -S kpackage```

```apk: sudo apk add kpackage```

```zypper: sudo zypper install kpackage```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kpackagetool5](/man/kpackagetool5)(1)
