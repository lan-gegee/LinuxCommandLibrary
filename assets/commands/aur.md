# TAGLINE

通过本地仓库管理 AUR 软件包的脚本集合。

# TLDR

在 AUR 数据库中**搜索**软件包

```aur search [keyword]```

将软件包**下载、构建并添加**到本地仓库

```aur sync [package1] [package2] ...```

**列出**本地仓库中可用的软件包

```aur repo -l```

**升级**本地仓库中的软件包

```aur sync -u```

同步后**清理**构建文件

```aur sync -c [package]```

安装软件包时**不弹出审查提示**

```aur sync --no-view --no-confirm [package]```

只从 AUR **获取**软件包源码而不构建

```aur fetch [package]```

显示软件包的**依赖树**

```aur depends [package]```

# SYNOPSIS

**aur** _command_ [_options_]

# DESCRIPTION

**aur**（aurutils）是一套通过本地 pacman 仓库管理 AUR 软件包的脚本集合。它自动完成下载 PKGBUILD、在干净 chroot 中构建软件包，以及将其加入可供 pacman 直接使用的本地仓库等步骤。

与直接安装软件包的 AUR 助手不同，aurutils 维护一个规范的本地仓库，实现更清晰的依赖管理，还能在不同系统之间共享构建好的软件包。

# SUBCOMMANDS

**search**
> 在 AUR 中搜索匹配模式的软件包

**sync**
> 下载、构建软件包并添加到本地仓库

**repo**
> 管理本地仓库

**fetch**
> 下载 AUR 软件包源码

**build**
> 用下载的源码构建软件包

**depends**
> 显示软件包依赖树

# CAVEATS

需要在 **/etc/pacman.conf** 中配置本地仓库。默认使用 **vifm** 审查 PKGBUILD（可通过 **AUR_PAGER** 环境变量配置）。构建发生在干净的 chroot 中，需要 **devtools** 软件包。初始配置比 yay 或 paru 这类简单的 AUR 助手更繁琐。

# HISTORY

**aurutils** 的诞生是为了给 Arch Linux 上的 AUR 软件包管理提供更稳健、更可脚本化的方案。它遵循 Unix 哲学，采用小巧、可组合的工具，而非一体化的 AUR 助手。

# SEE ALSO

[aur-sync](/man/aur-sync)(1), [pacman](/man/pacman)(8), [makepkg](/man/makepkg)(8), [yay](/man/yay)(1)
