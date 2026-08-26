# TAGLINE

从远程仓库同步软件包

# TLDR

**安装**软件包

```sudo pacman -S package```

**同步**数据库并**升级**

```sudo pacman -Syu```

升级时加入**新软件包**

```sudo pacman -Syu --noconfirm package```

**搜索**软件包数据库

```pacman -Ss "search_pattern"```

显示软件包**信息**

```pacman -Si package```

**覆盖**冲突的文件

```sudo pacman -Syu --overwrite path/to/file```

**清理**软件包缓存

```sudo pacman -Sc```

安装特定**版本**

```sudo pacman -S package=version```

# SYNOPSIS

**pacman -S** [_OPTIONS_] [_PACKAGE_...]

# DESCRIPTION

**pacman -S**（sync）从远程仓库同步软件包。它负责在 Arch Linux 系统上下载和安装软件包、更新系统以及管理本地软件包缓存。

# PARAMETERS

**-S, --sync**
> 从远程仓库同步软件包

**-y, --refresh**
> 从服务器下载最新的软件包数据库

**-u, --sysupgrade**
> 升级所有过期的软件包

**-s, --search** _regex_
> 搜索软件包名称和描述

**-i, --info**
> 显示详细的软件包信息

**-c, --clean**
> 从缓存中移除旧软件包

**--noconfirm**
> 跳过确认提示

**--overwrite** _glob_
> 覆盖冲突的文件

**--downloadonly**
> 只下载软件包而不安装

# CAVEATS

务必将 **-Syu** 一起运行，以确保数据库与软件包保持同步。单独运行 **-Sy** 可能导致部分升级问题。使用 **-Syyu** 可强制刷新，即使数据库看似最新。

# HISTORY

**pacman** 是 **Arch Linux** 及其衍生发行版的软件包管理器，以简洁和快速为首要设计目标。

# INSTALL

```apt: sudo apt install pacman-package-manager```

```dnf: sudo dnf install pacman```

```pacman: sudo pacman -S pacman```

```apk: sudo apk add pacman```

```nix: nix profile install nixpkgs#pacman```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pacman](/man/pacman)(8), [pacman-query](/man/pacman-query)(8), [pacman-remove](/man/pacman-remove)(8)
