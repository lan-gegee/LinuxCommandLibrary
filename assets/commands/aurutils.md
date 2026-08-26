# TAGLINE

在本地仓库中管理 AUR 软件包的工具集

# TLDR

**构建**软件包并将其加入本地仓库

```aur build [package]```

将一个 AUR 软件包及其依赖**构建**到本地仓库

```aur sync [package]```

**升级**本地仓库中的所有 AUR 软件包

```aur sync -u```

**搜索** AUR

```aur search [query]```

**检查**已安装的外来软件包是否有 AUR 更新

```pacman -Qm | aur vercmp```

**获取** PKGBUILD 源码

```aur fetch [package]```

# SYNOPSIS

**aur** _command_ [_options_] [_arguments_]

# DESCRIPTION

**aurutils** 是一套用于管理本地 Arch 用户仓库（AUR）软件包的工具集。它帮助在本地仓库中构建、维护和部署 AUR 软件包。

该套件与 pacman 集成，让 AUR 软件包可以像官方软件包一样被管理。

# PARAMETERS

**build**
> 从 AUR 构建软件包

**sync**
> 将软件包同步到本地仓库

**fetch**
> 下载 PKGBUILD

**search**
> 搜索 AUR

**vercmp**
> 从标准输入读取名称和版本对，与 AUR 进行比较

**repo**
> 检查或管理本地仓库数据库

**depends**
> 递归下载并解析 AUR 依赖

**graph**
> 生成用于拓扑排序的依赖图

# CAVEATS

需要先设置本地仓库。对于日常使用而言比 yay 或 paru 更复杂。面向希望精细控制的高级用户。

# HISTORY

**aurutils** 为追求可复现、基于本地仓库的 AUR 软件包管理的用户而开发，有别于直接安装类助手。它以 ISC 许可证发布。

# INSTALL

```aur: yay -S aurutils```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[pacman](/man/pacman)(8), [yay](/man/yay)(1), [paru](/man/paru)(1), [makepkg](/man/makepkg)(8)

# RESOURCES

```[Source code](https://github.com/aurutils/aurutils)```

<!-- verified: 2026-06-17 -->
