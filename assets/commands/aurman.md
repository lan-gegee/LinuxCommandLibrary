# TAGLINE

具有 pacman 风格界面的 AUR 助手

# TLDR

**同步并更新**所有软件包

```aurman -Syu```

更新所有软件包且**不显示 PKGBUILD** 变更

```aurman -Syu --noedit```

**安装**一个新软件包

```aurman -S [package]```

安装软件包且**不进行任何提示**

```aurman -S --noedit --noconfirm [package]```

在软件仓库和 AUR 中**搜索**关键字

```aurman -Ss [keyword]```

**删除**一个软件包及其依赖

```aurman --remove --recursive --nosave [package]```

**清理**软件包缓存

```aurman -Sc```

# SYNOPSIS

**aurman** [_options_] [_packages_]

# DESCRIPTION

**aurman** 是一个面向 Arch Linux 的 AUR 助手，提供类似 pacman 的界面，可用于安装来自官方软件仓库和 Arch 用户仓库（AUR）的软件包。它能处理依赖解析、PKGBUILD 审查和软件包构建，主要面向已熟悉 pacman、makepkg 和 AUR 的高级用户。

该命令遵循 pacman 的选项语法，Arch Linux 用户很容易上手。它将软件仓库和 AUR 软件包管理整合到同一个工作流中。注意，aurman 已不再维护，并已从 AUR 中移除；以下条目仅作历史参考保留。

# PARAMETERS

**-S, --sync**
> 同步软件包

**-y, --refresh**
> 下载最新的软件包数据库

**-u, --sysupgrade**
> 升级已安装的软件包

**-s, --search**
> 搜索匹配模式的软件包

**-c, --clean**
> 从缓存中删除旧软件包

**--noedit**
> 构建前不显示 PKGBUILD 变更

**--noconfirm**
> 不请求确认

**--remove**
> 删除软件包

**--recursive**
> 删除其他软件包不再需要的依赖

**--devel**
> 升级时同时考虑开发版软件包（如 -git 等 VCS 来源）

**--pgp_fetch**
> 自动获取验证源码所需的未知 PGP 密钥

**--aur**
> 将操作限制为 AUR 软件包

**--repo**
> 将操作限制为官方软件仓库的软件包

# CAVEATS

**aurman** 已不再维护，并已从 AUR 中移除。请改用仍在维护的 AUR 助手，例如 **yay** 或 **paru**。从 AUR 安装时务必审查 PKGBUILD，因为其中包含以你的权限运行的用户提交代码。

# HISTORY

**aurman** 曾是一个广受欢迎的 AUR 助手，以其先进的依赖求解器和交互式软件包选择而闻名。其开发已停止，软件包最终也从 AUR 中移除，**yay** 和 **paru** 成为通常推荐的替代品。

# INSTALL

```aur: yay -S aurman```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[pacman](/man/pacman)(8), [yay](/man/yay)(1), [paru](/man/paru)(1), [makepkg](/man/makepkg)(8)

# RESOURCES

```[Source code](https://github.com/polygamma/aurman)```

<!-- verified: 2026-06-17 -->
