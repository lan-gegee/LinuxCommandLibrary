# TAGLINE

已弃用的 Arch Linux AUR 助手

# TLDR

**更新**包括 AUR 在内的所有软件包

```yaourt -Syua```

**安装**软件包

```yaourt -S [package]```

**移除**软件包及其不再需要的依赖

```yaourt -Rs [package]```

在仓库和 AUR 中**搜索**软件包

```yaourt -Ss [query]```

**列出**已安装的软件包

```yaourt -Q```

从 AUR **下载并构建**软件包但不安装

```yaourt -Sb [package]```

**获取**软件包的**信息**

```yaourt -Si [package]```

# SYNOPSIS

**yaourt** [_OPTIONS_] [_PACKAGE..._]

# PARAMETERS

**-S** _PACKAGE_
> 从仓库或 AUR 安装软件包。

**-Syua**
> 同步数据库并更新所有软件包，包括 AUR 软件包。

**-Sb** _PACKAGE_
> 下载并构建软件包，但不安装。

**-Rs** _PACKAGE_
> 移除软件包及其不再需要的依赖。

**-Ss** _QUERY_
> 在同步数据库和 AUR 中搜索软件包。

**-Si** _PACKAGE_
> 显示软件包的详细信息。

**-Q**
> 列出已安装的软件包。

**-Qm**
> 列出外来软件包（从 AUR 安装的）。

**--noconfirm**
> 不请求任何确认。

# DESCRIPTION

**yaourt**（Yet AnOther User Repository Tool）是一款面向 Arch Linux 的 AUR 助手，它封装了 pacman，并为从 Arch User Repository 构建软件包提供了额外功能。

它在单一界面中结合了官方仓库与 AUR 的软件包管理，提供彩色输出、交互式搜索/安装以及孤立软件包检测。由于 yaourt 的大多数选项与 pacman 相同，它可以作为 pacman 的直接替代品使用。

# HISTORY

**yaourt** 是最早流行的 AUR 助手之一，但现已弃用。建议用户改用 yay、paru 或其他仍在维护的替代品。

# CAVEATS

已弃用且不再维护。请考虑改用 yay 或 paru。AUR 软件包不受官方支持。

# SEE ALSO

[yay](/man/yay)(8), [paru](/man/paru)(8), [pacman](/man/pacman)(8)
