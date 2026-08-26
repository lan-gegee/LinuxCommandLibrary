# TAGLINE

从 Arch Linux 系统中移除软件包

# TLDR

**移除软件包及其不再需要的依赖**

```sudo pacman -Rs [package]```

**移除且不保留配置备份文件**

```sudo pacman -Rsn [package]```

**移除时不请求确认**

```sudo pacman -R --noconfirm [package]```

**移除孤儿软件包（不再需要的依赖）**

```sudo pacman -Rsn $(pacman -Qdtq)```

**级联移除软件包及所有依赖它的软件包**

```sudo pacman -Rc [package]```

**预览将被移除的内容而不实际移除**

```pacman -Rp [package]```

# SYNOPSIS

**pacman -R** [_OPTIONS_] _PACKAGE_...

# DESCRIPTION

**pacman -R**（remove）从 Arch Linux 系统中移除软件包。它还可以移除依赖和配置文件，并对依赖它的软件包执行级联移除。

# PARAMETERS

**-R**, **--remove**
> 从系统中移除软件包。

**-s**, **--recursive**
> 移除指定的目标及其依赖中不被其他软件包需要且非显式安装的部分。传入两次（**-ss**）还会移除显式安装的依赖。

**-n**, **--nosave**
> 移除配置备份文件（阻止生成 **.pacsave** 文件）。

**-c**, **--cascade**
> 移除所有目标软件包以及所有依赖它们的软件包。此操作是递归的。

**-p**, **--print**
> 打印将要移除的内容而不实际移除。

**-u**, **--unneeded**
> 移除不被任何其他软件包需要的目标。在不使用 **-c** 的情况下移除组时很有用。

**-d**, **--nodeps**
> 跳过依赖版本检查。传入两次则跳过所有依赖检查。

**--dbonly**
> 只移除数据库条目，所有文件保持原样。

**--noscriptlet**
> 移除期间不执行安装脚本。

**--noconfirm**
> 跳过确认提示。

# CAVEATS

使用 **-c**（级联）移除核心依赖时可能会连带移除大量软件包。务必先用 **-p** 预览将要移除的内容。应定期用 **pacman -Rsn $(pacman -Qdtq)** 清理孤儿软件包。

# HISTORY

**pacman** 是 **Arch Linux** 及其衍生发行版的软件包管理器。

# INSTALL

```apt: sudo apt install pacman-package-manager```

```dnf: sudo dnf install pacman```

```pacman: sudo pacman -S pacman```

```apk: sudo apk add pacman```

```nix: nix profile install nixpkgs#pacman```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pacman](/man/pacman)(8), [pacman-query](/man/pacman-query)(8), [pacman-sync](/man/pacman-sync)(8), [pacman-database](/man/pacman-database)(8), [pacman-upgrade](/man/pacman-upgrade)(8)
