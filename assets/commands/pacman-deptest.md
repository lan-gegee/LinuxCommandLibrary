# TAGLINE

检查每个指定的依赖并返回当前未满足的依赖列表

# TLDR

打印未安装依赖的**软件包名称**

```pacman -T package1 package2```

检查已安装软件包是否满足给定的**最低版本**要求

```pacman -T "bash>=5"```

检查是否安装了软件包的**更高版本**

```pacman -T "bash>5"```

显示**帮助**

```pacman -Th```

# SYNOPSIS

**pacman --deptest** [_options_] [_package(s)_]

# PARAMETERS

**-T**, **--deptest**
> 检查指定的依赖并返回未满足的项

**-h**, **--help**
> 显示此操作的帮助信息

# DESCRIPTION

**pacman --deptest** 检查每个指定的依赖并返回系统中当前未满足的依赖列表。这有助于脚本判断哪些软件包需要安装。

版本比较可以使用 >=、>、=、< 和 <= 等运算符来检查特定的版本要求。

# CAVEATS

该操作只检查本地数据库；不会查询同步数据库中的可用软件包。

# HISTORY

属于 **pacman**，Arch Linux 及其衍生发行版的软件包管理器。

# INSTALL

```apt: sudo apt install pacman-package-manager```

```dnf: sudo dnf install pacman```

```pacman: sudo pacman -S pacman```

```apk: sudo apk add pacman```

```nix: nix profile install nixpkgs#pacman```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pacman](/man/pacman)(8), [pacman-sync](/man/pacman-sync)(8)
