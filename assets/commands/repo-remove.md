# TAGLINE

从 Arch Linux 软件仓库移除软件包

# TLDR

从本地仓库**移除**软件包

```repo-remove [path/to/database.db.tar.gz] [package_name]```

安静地**移除**（抑制输出）

```repo-remove -q [path/to/database.db.tar.gz] [package_name]```

**移除**并用 GnuPG 签署数据库文件

```repo-remove -s [path/to/database.db.tar.gz] [package_name]```

# SYNOPSIS

**repo-remove** [_options_] _database_ _package_ [_package_ ...]

# PARAMETERS

**-q**, **--quiet**
> 抑制输出消息。

**-s**, **--sign**
> 更新后使用 GnuPG 签署数据库文件。

**-k** _KEY_, **--key** _KEY_
> 使用指定的密钥签署数据库。

**-v**, **--verify**
> 读取前验证数据库签名。

# DESCRIPTION

**repo-remove** 从本地 pacman 仓库数据库中移除软件包。它会更新数据库文件，使其不再包含指定的软件包条目。

它是 repo-add 的配套工具，用于维护本地 Arch Linux 仓库。一次调用可以提供多个软件包名。

# CAVEATS

只移除数据库条目；不会从磁盘删除实际的软件包文件。可能需要手动清理软件包文件。

# HISTORY

属于 Arch Linux **pacman** 软件包管理工具集的一部分。与 repo-add 互补，用于仓库维护。

# INSTALL

```apt: sudo apt install pacman-package-manager```

```dnf: sudo dnf install pacman```

```pacman: sudo pacman -S pacman```

```apk: sudo apk add pacman```

```nix: nix profile install nixpkgs#pacman```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[repo-add](/man/repo-add)(1), [pacman](/man/pacman)(8)
