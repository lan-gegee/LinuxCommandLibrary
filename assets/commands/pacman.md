# TAGLINE

Arch Linux 的软件包管理器

# TLDR

**同步**并更新所有软件包

```sudo pacman -Syu```

**安装**软件包

```sudo pacman -S package```

**移除**软件包及其依赖

```sudo pacman -Rs package```

**搜索**软件包数据库

```pacman -Ss "search_pattern"```

搜索包含特定**文件**的软件包

```pacman -F "file_name"```

列出**显式安装**的软件包

```pacman -Qe```

列出**孤儿**软件包

```pacman -Qtdq```

**清空**软件包缓存

```sudo pacman -Scc```

# SYNOPSIS

**pacman** _<operation>_ [_options_] [_targets_]

# DESCRIPTION

**pacman** 是 Arch Linux 的软件包管理器。它将简单的二进制软件包格式与易用的构建系统相结合，跟踪已安装的软件包并支持依赖、软件包组，以及与远程仓库的同步。

# OPERATIONS

**-S, --sync**
> 从远程仓库同步软件包

**-R, --remove**
> 从系统中移除软件包

**-Q, --query**
> 查询本地软件包数据库

**-U, --upgrade**
> 从本地文件或 URL 升级或添加软件包

**-D, --database**
> 作用于软件包数据库

**-F, --files**
> 查询文件数据库

**-T, --deptest**
> 检查依赖是否满足

# COMMON OPTIONS

**-y, --refresh**
> 从服务器下载最新的软件包数据库

**-u, --sysupgrade**
> 升级所有过期的软件包

**-s, --search**
> 搜索匹配模式的软件包

**-i, --info**
> 显示软件包信息

**-l, --list**
> 列出软件包拥有的文件

**-c, --cascade**
> 移除软件包及所有依赖它的软件包

**-n, --nosave**
> 移除时同时删除配置文件

**-w, --downloadonly**
> 只下载软件包而不安装

**--noconfirm**
> 绕过所有确认提示

**--needed**
> 跳过重装已是最新版本的软件包

**-d, --nodeps**
> 跳过依赖检查

**-q, --quiet**
> 减少输出

# CAVEATS

安装软件包之前务必运行 **-Syu** 而不是只运行 **-Sy**，以避免可能破坏系统的部分升级。移除软件包时配置文件会以 .pacsave 扩展名保存，除非使用 **-n**。

# HISTORY

**pacman** 由 Judd Vinet 为 Arch Linux 创建，于 2002 年首次发布。它是 libalpm（Arch Linux Package Management 库）的前端，因此也可以使用 pamac 或 octopi 等替代前端。

# INSTALL

```apt: sudo apt install pacman-package-manager```

```dnf: sudo dnf install pacman```

```pacman: sudo pacman -S pacman```

```apk: sudo apk add pacman```

```nix: nix profile install nixpkgs#pacman```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pacman.conf](/man/pacman.conf)(5), [makepkg](/man/makepkg)(8), [yay](/man/yay)(8), [paru](/man/paru)(8)
