# TAGLINE

下载、构建 AUR 软件包并将其加入本地 pacman 仓库

# TLDR

从 AUR **下载并构建**软件包

```aur sync [package1] [package2] ...```

**升级**本地仓库中的所有 AUR 软件包

```aur sync -u```

在干净的 chroot 中**构建**

```aur sync -c [package]```

**不查看** PKGBUILD 且不确认直接同步

```aur sync --noview --noconfirm [package]```

升级但**忽略**指定软件包

```aur sync -u --ignore [package1] --ignore [package2]```

无论版本如何都**强制重建**某个软件包

```aur sync -f [package]```

# SYNOPSIS

**aur sync** [_options_] _package_...

# DESCRIPTION

**aur sync** 是 **aurutils** 的核心命令，用于下载、构建 AUR 软件包并将其添加到本地 pacman 仓库。它会解析 AUR 依赖、获取 PKGBUILD、构建软件包并更新本地仓库数据库。

默认情况下，它在构建前会用 **AUR_PAGER**（或 **vifm**）指定的文件管理器打开 PKGBUILD 供审查。自动化场景可用 **--noview** 禁用此行为。

# PARAMETERS

**-u**, **--upgrades**
> 检查并构建已安装 AUR 软件包的升级版本。

**-c**, **--chroot**
> 使用 aur-chroot 在干净的 chroot 中构建软件包。

**-f**, **--force**
> 无论版本如何均强制重建。

**-n**, **--noconfirm**
> 不提示确认。

**--noview**
> 跳过 PKGBUILD 审查。

**--ignore** _package_
> 升级时跳过某个软件包（可重复使用）。

**-d**, **--database** _name_
> 使用指定的本地仓库数据库。

**--no-ver**
> 禁用版本检查（全部重建）。

**--no-ver-argv**
> 仅对命令行参数禁用版本检查。

**--provides**
> 解析依赖时考虑 provides 关系。

**-S**, **--sign**
> 用 GPG 为构建好的软件包签名。

**-k**, **--keep-going**
> 某个软件包失败后继续构建其余软件包。

**--makepkg-args** _args_
> 向 makepkg 传递额外参数。

# CAVEATS

需要正确配置的本地 pacman 仓库，chroot 构建还需要 **devtools**。审查 PKGBUILD 对安全至关重要；由于 AUR 软件包由用户提交、未经官方审核，请谨慎使用 **--noview**。**--ignore** 标志每次只能接受一个软件包（不支持逗号分隔）。

# SEE ALSO

[aur](/man/aur)(1), [pacman](/man/pacman)(8), [makepkg](/man/makepkg)(8)
