# TAGLINE

向 Arch Linux 软件仓库添加软件包

# TLDR

创建一个**空仓库**

```repo-add path/to/database.db.tar.gz```

向仓库**添加软件包**

```repo-add path/to/database.db.tar.gz package1.pkg.tar.zst package2.pkg.tar.zst```

添加所有软件包并**移除过期的**包

```repo-add -R path/to/database.db.tar.gz *.pkg.tar.zst```

以**安静模式**添加软件包

```repo-add -q path/to/database.db.tar.gz *.pkg.tar.zst```

添加软件包且**不带彩色**输出

```repo-add --nocolor path/to/database.db.tar.gz *.pkg.tar.zst```

# SYNOPSIS

**repo-add** [_options_] _database_ [_packages_...]

# PARAMETERS

**-R**, **--remove**
> 从仓库中移除过期的软件包文件

**-q**, **--quiet**
> 除警告和错误外尽量减少输出

**--nocolor**
> 禁用彩色输出

# DESCRIPTION

**repo-add** 是 Arch Linux 的软件包数据库维护工具。它通过向数据库文件添加软件包来创建和更新本地 pacman 仓库。

这使得可以通过 pacman 从本地或网络仓库安装自定义软件包。

# CAVEATS

数据库文件必须具有 .db.tar.gz 扩展名。软件包必须是有效的 pacman 软件包文件。

# HISTORY

属于 Arch Linux **pacman** 软件包管理工具集的一部分。用于创建自定义本地仓库。

# INSTALL

```apt: sudo apt install pacman-package-manager```

```dnf: sudo dnf install pacman```

```pacman: sudo pacman -S pacman```

```apk: sudo apk add pacman```

```nix: nix profile install nixpkgs#pacman```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[repo-remove](/man/repo-remove)(1), [pacman](/man/pacman)(8)
