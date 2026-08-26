# TAGLINE

PikaOS 统一软件包管理器

# TLDR

在原生仓库中**搜索**软件包

```pikman search [package_name]```

从原生仓库**安装**软件包

```pikman install [package]```

通过容器从 **AUR** **安装**软件包

```pikman --aur install [package]```

**安装** **Flatpak** 软件包

```pikman --flatpak install [package]```

**更新**可用软件包列表

```pikman update```

**升级**所有系统软件包

```pikman upgrade```

**移除**软件包

```pikman remove [package]```

**初始化** Arch/AUR 容器以获得跨发行版支持

```pikman --aur init```

# SYNOPSIS

**pikman** [_global options_] _command_ [_command options_] [_arguments..._]

# PARAMETERS

**--arch**, **--aur**
> 安装和管理包括 AUR 在内的 Arch Linux 软件包

**--fedora**, **--dnf**
> 安装和管理 Fedora 软件包

**--alpine**, **--apk**
> 安装和管理 Alpine Linux 软件包

**--flatpak**, **--fl**
> 安装和管理 Flatpak 软件包

**--name** _value_
> 指定受管容器的名称

**--help**, **-h**
> 显示帮助信息

**--version**, **-v**
> 显示版本号

# DESCRIPTION

**pikman** 是基于 Debian 的 Linux 发行版 **PikaOS** 的官方软件包管理器。它为管理多种打包系统中的软件包提供统一界面。在其原生环境 PikaOS 上，它封装 **APT** 进行原生软件包管理，同时也可通过底层使用 Podman 容器的 **APX** 从 **Arch/AUR**、**Fedora** 和 **Alpine** 仓库安装软件包。它还支持 **Flatpak** 软件包。从容器化的发行版中安装的应用会自动出现在宿主机的应用启动器中。

pikman 在内部处理权限提升，**不要**用 sudo 运行。它拒绝以 root 身份运行。

# COMMANDS

**install**, **i**
> 安装指定软件包

**remove**, **r**
> 移除已安装的软件包

**purge**
> 彻底清除软件包，包括配置文件

**search**, **s**
> 搜索软件包

**show**
> 显示软件包详情

**list**, **l**
> 列出已安装的软件包（支持 **--upgradable** 和 **--installed** 过滤器）

**update**
> 更新可用软件包列表

**upgrade**
> 通过安装/升级可用软件包来升级系统

**autoremove**
> 移除所有不再使用的软件包

**clean**, **cl**
> 清理软件包管理器缓存

**init**
> 初始化用于跨发行版支持的受管容器

**enter**
> 进入给定软件包管理器的容器实例

**export**
> 从容器导出程序的桌面入口

**unexport**
> 移除程序的桌面入口

**log**
> 显示软件包管理器日志

**run**
> 在受管容器内运行命令

**upgrades**
> 列出可用的升级

**help**, **h**
> 显示命令列表或特定命令的帮助

# CAVEATS

Pikman 专为 **PikaOS** 设计，不是适用于其他发行版的通用工具。在安装其他发行版（Arch、Fedora、Alpine）的软件包之前，必须先用 **pikman --aur init**（或 **--fedora init** 等）初始化相应容器。对于 Flatpak 软件包，请使用 **pikman --flatpak update** 而不是 **upgrade**，以符合 Flatpak 的惯例。

# HISTORY

Pikman 是 **PikaOS** 项目的一部分，该项目是一个专注于游戏和桌面应用的 Debian 系发行版。它用 **Go** 编写，最初托管在 GitHub 上。该仓库于 **2024 年 11 月**归档，开发转移到 PikaOS 自己的 Gitea 实例上继续。还有一个名为 **Pikman Update Manager** 的 GUI 对应工具，提供图形化软件包管理。

# SEE ALSO

[apt](/man/apt)(8), [flatpak](/man/flatpak)(1), [pacman](/man/pacman)(8), [dnf](/man/dnf)(8), [podman](/man/podman)(1)
