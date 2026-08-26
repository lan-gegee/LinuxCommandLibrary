# TAGLINE

管理 GNU Guix（一款函数式软件包管理器）中的软件包

# TLDR

**安装**软件包

```guix package -i [package]```

**移除**软件包

```guix package -r [package]```

**搜索**软件包

```guix package -s "[search_pattern]"```

列出**已安装**的软件包

```guix package -I```

列出**代际**（先前的配置）

```guix package -l```

**回滚**到上一个代际

```guix package --roll-back```

# SYNOPSIS

**guix package** [_options_]

# PARAMETERS

**-i**, **--install** _PACKAGE_
> 安装指定的软件包

**-r**, **--remove** _PACKAGE_
> 移除指定的软件包

**-s**, **--search** _PATTERN_
> 使用正则表达式模式搜索软件包数据库

**-I**, **--list-installed**
> 列出所有已安装的软件包

**-l**, **--list-generations**
> 列出所有代际（快照）

**--roll-back**
> 切换到上一个代际

**-u**, **--upgrade**
> 升级已安装的软件包

# DESCRIPTION

**guix package** 管理 GNU Guix 中的软件包，后者是一款函数式软件包管理器。与传统软件包管理器不同，Guix 将多个版本和配置保存在不同的代际中，可以轻松回滚到先前的状态。

每次操作都会创建一个新代际，同时保留之前的状态。这种事务性方法意味着失败的升级不会让系统陷入损坏状态，用户始终可以回到已知良好的配置。

软件包默认按用户安装，不需要 root 权限。函数式模型确保了可复现构建，并且能够运行同一软件包的多个版本。

# CAVEATS

Guix 使用不同于传统系统的文件系统层次结构，软件包存放在 /gnu/store 中。Shell 集成可能需要 source Guix profile。没有替代二进制源（substitute）可用时构建时间可能很长。

# HISTORY

GNU Guix 由 Ludovic Courtès 于 **2012 年**发布，是一款基于 Nix 概念但使用 GNU Guile Scheme 的函数式软件包管理器。后来它发展为完整的 GNU/Linux 发行版（Guix System），同时仍可作为软件包管理器在其他发行版上使用。

# SEE ALSO

[nix](/man/nix)(1), [apt](/man/apt)(8), [pacman](/man/pacman)(8)
