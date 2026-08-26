# TAGLINE

Arch Linux 的 AUR 助手和 pacman 包装器

# TLDR

**同步**并更新所有软件包

```paru```

交互式**搜索**并安装软件包

```paru package_name```

只升级 **AUR 软件包**

```paru -Sua```

**移除**软件包及其配置和依赖

```paru -Rns package```

获取软件包的**信息**

```paru -Si package```

从 AUR 下载 **PKGBUILD**

```paru --getpkgbuild package```

**显示** PKGBUILD 文件

```paru --getpkgbuild --print package```

# SYNOPSIS

**paru** [_operation_] [_options_] [_targets_]

# DESCRIPTION

**paru** 是 Arch Linux 的 AUR 助手和 pacman 包装器。它简化了从 Arch User Repository（AUR）安装软件包的过程，同时对官方仓库的软件包保持完全的 pacman 兼容性。

# OPERATIONS

**-S, --sync**
> 从仓库同步软件包

**-R, --remove**
> 从系统中移除软件包

**-Q, --query**
> 查询本地软件包数据库

**-U, --upgrade**
> 从本地软件包文件进行升级

**-G, --getpkgbuild**
> 从 AUR 或 ABS 下载 PKGBUILD

**-P, --show**
> 打印各种软件包信息

# COMMON OPTIONS

**-u, --sysupgrade**
> 升级已安装的软件包

**-a, --aur**
> 把操作限定在 AUR 软件包范围内

**-s, --search**
> 搜索软件包

**-i, --info**
> 显示软件包信息

**-c, --clean**
> 移除不再需要的依赖

**--devel**
> 更新开发版软件包

**--print**
> 打印 PKGBUILD 而不是保存到文件

**--noconfirm**
> 跳过所有确认提示

**--needed**
> 不重新安装已是最新版的软件包

# CAVEATS

AUR 软件包由用户贡献，不受 Arch Linux 官方支持。安装前务必审查 PKGBUILD。默认情况下 paru 会提示查看已更新 PKGBUILD 的差异。

# HISTORY

**paru** 由 Morganamilo 开发，作为 yay 的后继者，采用 Rust 编写以获得更好的性能。它的目标是功能丰富，同时保持简洁性和与 pacman 的兼容性。

# INSTALL

```nix: nix profile install nixpkgs#paru```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pacman](/man/pacman)(8), [yay](/man/yay)(8), [makepkg](/man/makepkg)(8)
