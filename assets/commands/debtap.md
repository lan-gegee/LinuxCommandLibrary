# TAGLINE

将 Debian 软件包转换为 Arch Linux 软件包

# TLDR

**更新** debtap 数据库（首次必须执行）

```sudo debtap -u```

**转换** Debian 软件包

```debtap [path/to/package.deb]```

以**最少的提示**转换

```debtap -q [path/to/package.deb]```

仅生成 **PKGBUILD** 文件

```debtap -p [path/to/package.deb]```

# SYNOPSIS

**debtap** [_options_] _package.deb_

# DESCRIPTION

**debtap** 将 Debian 软件包（.deb）转换为 Arch Linux 软件包。它会转换软件包元数据、依赖和文件路径，生成兼容 Arch 的软件包。

首次使用前必须先更新数据库，以获取依赖映射关系。

# PARAMETERS

**-u, --update**
> 更新 debtap 数据库

**-q, --quiet**
> 跳过除元数据编辑之外的所有提问

**-Q, --Quiet**
> 跳过所有提问

**-p, --pkgbuild**
> 生成 PKGBUILD 文件而非软件包

**-P, --pseudo**
> 创建伪 64 位软件包

# CAVEATS

仅适用于 Arch Linux。由于各发行版软件包命名不同，转换后的软件包可能存在依赖问题。生产使用前请先审查并测试转换后的软件包。更新数据库需要联网。

# INSTALL

```aur: yay -S debtap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pacman](/man/pacman)(8), [makepkg](/man/makepkg)(8), [dpkg](/man/dpkg)(1)

# RESOURCES

```[Source code](https://github.com/helixarch/debtap)```

<!-- verified: 2026-07-11 -->
