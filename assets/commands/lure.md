# TAGLINE

面向所有 Linux 发行版的社区软件包管理器

# TLDR

从 LURE 软件仓库**安装**软件包

```lure install [package]```

**升级**所有已安装的 LURE 软件包

```lure upgrade```

**显示**软件包信息

```lure info [package]```

**列出** LURE 仓库中的所有软件包

```lure list```

**只列出已安装**的 LURE 软件包

```lure list --installed```

**添加**新的软件仓库

```lure addrepo -n [name] -u [https://github.com/user/repo]```

**移除**软件仓库

```lure removerepo -n [name]```

**刷新**所有软件仓库

```lure refresh```

# SYNOPSIS

**lure** [_command_] [_options_]

# PARAMETERS

**install**, **in**
> 从 LURE 仓库安装软件包。在 LURE 中找不到的软件包会转交给系统包管理器处理。

**remove**, **rm**
> 通过系统包管理器移除软件包。

**upgrade**, **up**
> 使用 rpmvercmp 版本比较升级已安装的 LURE 软件包。

**info**
> 显示来自 LURE 仓库的软件包信息。支持通配符（%）。

**list**, **ls**
> 列出 LURE 仓库中的所有软件包。可接受可选的模式用于过滤。

**build**
> 从当前目录的 lure.sh 脚本构建软件包。

**addrepo**, **ar**
> 添加新的软件仓库。需要 **-n**（名称）和 **-u**（URL）。

**removerepo**, **rr**
> 移除软件仓库并删除其内容。需要 **-n**（名称）。

**refresh**, **ref**
> 从所有 LURE 仓库拉取最新更改。

**fix**
> 删除并重建 LURE 的缓存以解决问题。

**version**
> 打印当前 LURE 版本号。

**-c**, **--clean**
> 安装或升级时强制重新构建。

**-I**, **--installed**
> 列出时只显示已安装的软件包。

**-s** _path_
> 构建时指定自定义的 lure.sh 脚本路径。

# DESCRIPTION

**LURE**（Linux User REpository）是一个不依赖特定发行版的包管理器，为所有 Linux 发行版带来类似 AUR 的功能。它从 git 仓库读取 **lure.sh** 构建脚本，构建原生软件包（.deb、.rpm、.pkg.tar.zst、.apk），并使用系统原生的包管理器安装它们。

LURE 支持 **apt**、**pacman**、**apk**、**dnf**、**yum** 和 **zypper**。软件包由 lure.sh 脚本构建，其格式类似 Arch 的 PKGBUILD。软件仓库就是标准的 git 仓库，其中包含带有 lure.sh 文件的目录，描述如何构建每个软件包。

# CONFIGURATION

LURE 使用环境变量来指定目标发行版和架构：

**LURE_DISTRO** — 目标发行版（arch、alpine、opensuse、debian）
**LURE_PKG_FORMAT** — 软件包格式（archlinux、apk、rpm、deb）
**LURE_ARM_VARIANT** — ARM 变体（arm5、arm6、arm7）

# CAVEATS

LURE 用纯 Go 编写，除一个提权命令（sudo、doas）和受支持的包管理器外没有任何运行时依赖。来自社区仓库的构建脚本未经官方审查——安装软件包前务必先审阅 lure.sh 文件，就像 AUR 中审阅 PKGBUILD 的做法一样。

# HISTORY

LURE 的创建是为了解决为多个 Linux 发行版打包软件的问题。它受 **Arch 用户仓库**（AUR）启发，旨在将同样的社区驱动包构建模式带给所有主流 Linux 发行版。它使用 **Go** 编写，于 **2022 年**首次发布，目前在 **lure.sh** 活跃维护。

# INSTALL

```aur: yay -S lure```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[yay](/man/yay)(1), [pacman](/man/pacman)(8), [apt](/man/apt)(8), [dnf](/man/dnf)(8), [zypper](/man/zypper)(8)
