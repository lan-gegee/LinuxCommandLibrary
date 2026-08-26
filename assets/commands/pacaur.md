# TAGLINE

Arch Linux 的 AUR 助手，在 pacman 基础上封装 AUR 支持

# TLDR

**同步并更新**所有软件包（包括 AUR）

```pacaur -Syu```

仅同步并更新 **AUR 软件包**

```pacaur -Syua```

**安装**新软件包（包括 AUR）

```pacaur -S [package]```

**移除**软件包及其依赖

```pacaur -Rs [package]```

在软件包数据库中**搜索**关键字

```pacaur -Ss [keyword]```

**列出**所有已安装的软件包

```pacaur -Q```

在已安装的软件包中**搜索**关键字

```pacaur -Qs [keyword]```

构建前**编辑** PKGBUILD

```pacaur -S -e [package]```

# SYNOPSIS

**pacaur** [_operation_] [_options_] [_targets_]

# PARAMETERS

**-S**, **--sync**
> 同步软件包（从仓库和 AUR 安装/升级）

**-Q**, **--query**
> 查询本地软件包数据库

**-R**, **--remove**
> 移除软件包

**-y**, **--refresh**
> 下载最新的软件包数据库

**-u**, **--sysupgrade**
> 升级所有过期的软件包

**-a**, **--aur**
> 将操作限制为仅 AUR 软件包

**-r**, **--repo**
> 将操作限制为仅官方仓库

**-e**, **--edit**
> 编译前编辑构建文件

**-s**, **--search**
> 搜索匹配模式的软件包

**-i**, **--info**
> 显示软件包信息

**-c**, **--clean**
> 从缓存中移除旧软件包

**--devel**
> 升级时考虑开发版软件包

**--needed**
> 不重装已是最新版本的软件包

**--noconfirm**
> 不请求确认

**--noedit**
> 不提示编辑 PKGBUILD

# DESCRIPTION

**pacaur** 是面向 Arch Linux 的 AUR（Arch User Repository）助手，它封装了 pacman 的功能并增加了从 AUR 构建和安装软件包的支持。它保持 pacman 的命令语法不变，让 Arch 用户感到熟悉，同时将功能扩展到用户贡献的软件包。

该工具自动化了以下流程：从 AUR 下载 PKGBUILD、解析依赖、用 makepkg 构建软件包并进行安装。它可以在单次操作中同时处理官方仓库软件包和 AUR 软件包。

# CAVEATS

**开发已停止**——pacaur 不再被积极维护。建议改用 **yay** 或 **paru** 等仍在维护的替代品。构建 AUR 软件包前务必检查 PKGBUILD，因为其中包含用户提交的代码，可能存在恶意内容。

# HISTORY

作为一款极简主义的 AUR 助手开发而成，其理念是尽量贴近 pacman 的接口。曾在偏好其非交互式方式和与 pacman 紧密集成的 Arch 用户中流行。开发于 **2018** 年前后停止，维护者建议用户迁移到仍在活跃维护的替代品。

# INSTALL

```aur: yay -S pacaur```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pacman](/man/pacman)(8), [yay](/man/yay)(8), [paru](/man/paru)(1), [makepkg](/man/makepkg)(8)
