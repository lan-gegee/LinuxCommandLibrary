# TAGLINE

面向 Arch Linux 和 AUR 的安全多语言软件包管理器。

# TLDR

**搜索** AUR 软件包

```aura -As [keyword]```

从 AUR **安装**

```aura -A [package]```

**更新** AUR 软件包

```aura -Akua```

从**官方**仓库安装

```aura -S [package]```

**同步并升级**官方软件包

```aura -Syu```

**移除**软件包及其依赖

```aura -Rsu [package]```

**保存**当前软件包状态

```aura -B```

**恢复**已保存的软件包状态

```aura -Br```

移除**孤儿**软件包

```aura -Oj```

# SYNOPSIS

**aura** [_OPTIONS_] [_PACKAGE_...]

# DESCRIPTION

**aura** 是一款面向 Arch Linux 的安全多语言软件包管理器，同时处理官方仓库软件包和 AUR（Arch User Repository）软件包。它为所有软件包管理任务提供统一接口。

# PARAMETERS

**-A, --aursync**
> 与 AUR 同步

**-As, --search**
> 搜索 AUR 软件包

**-S, --sync**
> 与官方仓库同步

**-Syu**
> 同步数据库并升级软件包

**-R, --remove**
> 移除软件包

**-s, --recursive**
> 递归移除依赖

**-u, --unneeded**
> 移除不再需要的软件包

**-B, --backup**
> 保存或恢复软件包状态快照

**-O, --orphans**
> 列出孤儿软件包

**-j, --abandon**
> 移除孤儿软件包

**-k, --diff**
> 构建前显示 PKGBUILD 差异

**--hotedit**
> 构建前编辑 PKGBUILD

**--delmakedeps**
> 安装后移除构建依赖

# CAVEATS

AUR 软件包由用户提交，不受官方支持。出于安全考虑，安装前应审查 PKGBUILD。从源码构建可能需要额外的依赖。

# HISTORY

**aura** 作为其他 AUR 助手的 Haskell 实现替代品而创建，强调安全性和多语言支持。

# INSTALL

```aur: yay -S aura```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[pacman](/man/pacman)(8), [yay](/man/yay)(1), [paru](/man/paru)(1)
