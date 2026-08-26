# TAGLINE

查询 Arch Linux 系统上的本地软件包数据库

# TLDR

**列出**所有已安装的软件包

```pacman -Q```

列出**显式**安装的软件包

```pacman -Qe```

查找**拥有**某文件的软件包

```pacman -Qo filename```

显示软件包**信息**

```pacman -Qi package```

**列出**软件包拥有的文件

```pacman -Ql package```

列出**孤儿**软件包

```pacman -Qdtq```

列出**外部**软件包

```pacman -Qm```

列出**可升级**的软件包

```pacman -Qu```

# SYNOPSIS

**pacman -Q** [_OPTIONS_] [_PACKAGE_...]

# DESCRIPTION

**pacman -Q**（query）查询 Arch Linux 系统上的本地软件包数据库。它提供已安装软件包的信息，包括版本、依赖、文件和安装状态。

# PARAMETERS

**-Q, --query**
> 查询本地软件包数据库

**-e, --explicit**
> 仅筛选显式安装的软件包

**-d, --deps**
> 筛选作为依赖安装的软件包

**-t, --unrequired**
> 筛选不被任何其他软件包需要的软件包

**-o, --owns** _file_
> 查找拥有指定文件的软件包

**-i, --info**
> 显示详细的软件包信息

**-l, --list**
> 列出软件包拥有的文件

**-m, --foreign**
> 筛选同步数据库中不存在的软件包（AUR 软件包）

**-n, --native**
> 筛选存在于同步数据库中的软件包

**-u, --upgrades**
> 筛选已过期的软件包

**-q, --quiet**
> 显示更少的信息（仅软件包名称）

# CAVEATS

查询只作用于本地数据库。同步数据库操作请使用 **pacman -S**。孤儿软件包（作为依赖安装但不再被需要）可用 **-Qdt** 找到。

# HISTORY

**pacman** 是 **Arch Linux** 及其衍生发行版的软件包管理器，以简洁和快速为设计目标。

# INSTALL

```apt: sudo apt install pacman-package-manager```

```dnf: sudo dnf install pacman```

```pacman: sudo pacman -S pacman```

```apk: sudo apk add pacman```

```nix: nix profile install nixpkgs#pacman```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pacman](/man/pacman)(8), [pacman-sync](/man/pacman-sync)(8), [paru](/man/paru)(1), [yay](/man/yay)(1)
