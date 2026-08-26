# TAGLINE

从本地归档文件而非远程仓库安装软件包

# TLDR

从本地文件**安装**

```sudo pacman -U path/to/package.pkg.tar.zst```

安装时**不**提示

```sudo pacman -U --noconfirm path/to/package.pkg.tar.zst```

**覆盖**冲突的文件

```sudo pacman -U --overwrite path/to/file path/to/package.pkg.tar.zst```

**跳过**依赖检查

```sudo pacman -Ud path/to/package.pkg.tar.zst```

**预览**升级

```pacman -Up path/to/package.pkg.tar.zst```

# SYNOPSIS

**pacman -U** [_OPTIONS_] _PACKAGE_...

# DESCRIPTION

**pacman -U**（upgrade）从本地归档文件而非远程仓库安装软件包。这适用于安装本地构建的软件包、AUR 软件包，或降级到较旧的软件包版本。

# PARAMETERS

**-U, --upgrade**
> 从软件包文件升级或安装

**-d, --nodeps**
> 跳过依赖版本检查

**-p, --print**
> 打印将要安装的内容而不实际安装

**--overwrite** _glob_
> 覆盖匹配 glob 模式的冲突文件

**--noconfirm**
> 跳过确认提示

**--asdeps**
> 将软件包标记为非显式安装（作为依赖）

**--asexplicit**
> 将软件包标记为显式安装

# CAVEATS

软件包文件必须与系统架构兼容。使用 **-U** 时不会自动从仓库解析依赖。使用 **-d** 跳过依赖检查可能破坏系统。

# HISTORY

**pacman** 是 **Arch Linux** 及其衍生发行版的软件包管理器。

# INSTALL

```apt: sudo apt install pacman-package-manager```

```dnf: sudo dnf install pacman```

```pacman: sudo pacman -S pacman```

```apk: sudo apk add pacman```

```nix: nix profile install nixpkgs#pacman```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pacman](/man/pacman)(8), [pacman-sync](/man/pacman-sync)(8), [makepkg](/man/makepkg)(8)
