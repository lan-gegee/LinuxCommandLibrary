# TAGLINE

GNOME 图形化软件管理器

# TLDR

启动 **GNOME Software 图形界面**

```gnome-software```

启动并跳转到**特定页面**

```gnome-software --mode [updates|updated|installed|overview]```

启动并查看特定软件包的**详情**

```gnome-software --details [package]```

显示**版本**

```gnome-software --version```

# SYNOPSIS

**gnome-software** [_options_]

# PARAMETERS

**--mode** _MODE_
> 在指定页面启动：updates、updated、installed、overview

**--details** _PACKAGE_
> 显示指定软件包的详情

**--search** _QUERY_
> 打开并显示查询的搜索结果

**--install** _PACKAGE_
> 提示安装指定的软件包

**--local-filename** _FILE_
> 从本地软件包文件安装

**--details-pkg** _PKGNAME_
> 按软件包名（而非应用 ID）显示详情

# DESCRIPTION

**gnome-software** 是 GNOME 的图形化软件管理应用。它提供友好的界面，用于浏览、安装、移除和更新应用程序。

该应用聚合来自多个来源的软件，包括发行版仓库（通过 PackageKit）、Flatpak 和 Snap，并以统一的应用商店界面呈现。它还负责系统和固件更新（通过 fwupd）。

# CAVEATS

需要配置 PackageKit、Flatpak 或 Snap 后端。首次启动时加载元数据可能较慢。某些仓库操作需要通过 PolicyKit 进行身份验证。

# HISTORY

gnome-software 于 GNOME 3.10（**2013** 年）推出，是重新设计的软件中心，在基于 GNOME 的发行版上取代了旧的 Ubuntu Software Center。它已发展为支持多种软件包格式并提供现代应用商店体验的工具。

# INSTALL

```apt: sudo apt install gnome-software```

```dnf: sudo dnf install gnome-software```

```pacman: sudo pacman -S gnome-software```

```apk: sudo apk add gnome-software```

```zypper: sudo zypper install gnome-software```

```nix: nix profile install nixpkgs#gnome-software```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[flatpak](/man/flatpak)(1), [snap](/man/snap)(1), [dnf](/man/dnf)(8), [apt](/man/apt)(8)

# RESOURCES

```[Source code](https://gitlab.gnome.org/GNOME/gnome-software)```

```[GNOME Help](https://help.gnome.org/users/gnome-software/stable/)```

<!-- verified: 2026-07-17 -->
