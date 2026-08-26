# TAGLINE

Arch Linux 软件包管理器 pacman 的封装工具

# TLDR

**搜索软件包**

```paci [package_name]```

**安装软件包**

```paci -S [package]```

**移除软件包**

```paci -R [package]```

**更新所有软件包**

```paci -Syu```

**显示软件包信息**

```paci -Qi [package]```

**列出已安装的软件包**

```paci -Q```

**清理软件包缓存**

```paci -Sc```

**搜索已安装的软件包**

```paci -Qs [query]```

# SYNOPSIS

**paci** [_-S_] [_-R_] [_-Q_] [_-Syu_] [_options_] [_package_]

# PARAMETERS

**-S** _PACKAGE_
> 安装软件包。

**-R** _PACKAGE_
> 移除软件包。

**-Q**
> 查询已安装的软件包。

**-Qi** _PACKAGE_
> 显示软件包信息。

**-Qs** _QUERY_
> 搜索已安装的软件包。

**-Syu**
> 系统升级。

**-Sc**
> 清理缓存。

**-Ss** _QUERY_
> 搜索仓库。

# DESCRIPTION

**paci** 是 Arch Linux 软件包管理器 pacman 的封装工具。它在保持 pacman 强大功能的同时提供简化的接口。

该工具对常见操作使用熟悉的语法：安装、移除、更新和查询。复杂的 pacman 标志被抽象为更简单的命令。

搜索功能可以直接在仓库中查找软件包而无需显式标志。根据配置不同，可能支持交互式选择。

可能集成了 AUR 助手，从而可以在官方仓库之外安装社区软件包。

该封装旨在降低 pacman 的学习曲线，同时保持与其行为兼容。

# CAVEATS

仅限 Arch Linux。它封装了 pacman，因此必须可用 pacman。可能不支持 pacman 的全部功能。不同实现之间的行为可能有所差异。

# HISTORY

存在多种作为 pacman 封装的 **paci** 实现。它们源于 Arch Linux 社区希望获得更简单的软件包管理接口、同时保留 pacman 功能的需求。

# SEE ALSO

[pacman](/man/pacman)(8), [yay](/man/yay)(1), [paru](/man/paru)(1), [trizen](/man/trizen)(1)
