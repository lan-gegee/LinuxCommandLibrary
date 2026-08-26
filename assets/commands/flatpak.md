# TAGLINE

面向 Linux 的沙箱化应用分发系统

# TLDR

**运行**已安装的应用

```flatpak run com.example.app```

从远程仓库**安装**应用

```flatpak install flathub com.example.app```

**列出**已安装的应用

```flatpak list --app```

**更新**所有应用和运行时

```flatpak update```

**添加**远程仓库

```flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo```

**移除**应用

```flatpak remove com.example.app```

**移除**未使用的应用和运行时

```flatpak remove --unused```

显示某个应用的**信息**

```flatpak info com.example.app```

# SYNOPSIS

**flatpak** [_OPTION_...] {_COMMAND_}

# DESCRIPTION

**flatpak** 是一款管理应用程序及其关联运行时的工具。它使应用的构建和分发独立于宿主系统，同时在运行时提供沙箱隔离。该系统同时支持系统级和按用户两种安装模式。

# PARAMETERS

**-h, --help**
> 显示帮助选项并退出

**-v, --verbose**
> 显示调试信息（用 -vv 获取更多细节）

**--version**
> 打印版本信息并退出

**--default-arch**
> 打印默认架构并退出

**--supported-arches**
> 按优先顺序打印支持的架构

**--gl-drivers**
> 打印活动 GL 驱动的列表

**--installations**
> 打印系统安装位置的路径

**--print-updated-env**
> 打印使用 flatpak 所需的环境变量

**--user**
> 仅作用于按用户的安装

**--system**
> 作用于系统级安装（默认）

**--installation=**_NAME_
> 作用于指定的安装位置（来自 /etc/flatpak/installations.d/）

# CAVEATS

系统级数据存储在 $prefix/var/lib/flatpak/ 中，而按用户的数据存储在 $HOME/.local/share/flatpak/ 中。Flatpak 内部使用 OSTree 仓库，可以直接用 **ostree** 工具操作。

# HISTORY

**flatpak** 最初由 Red Hat 的 Alexander Larsson 以 xdg-app 之名开发，2016 年更名为 Flatpak。它为 Linux 桌面应用提供了与发行版无关的打包格式。

# INSTALL

```apt: sudo apt install flatpak```

```dnf: sudo dnf install flatpak```

```pacman: sudo pacman -S flatpak```

```apk: sudo apk add flatpak```

```zypper: sudo zypper install flatpak```

```nix: nix profile install nixpkgs#flatpak```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[flatpak-install](/man/flatpak-install)(1), [flatpak-run](/man/flatpak-run)(1), [ostree](/man/ostree)(1)
