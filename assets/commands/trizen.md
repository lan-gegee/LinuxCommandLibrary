# TAGLINE

Arch Linux AUR 软件包助手

# TLDR

同步并更新所有 AUR 软件包

```trizen -Syua```

安装软件包

```trizen -S [package]```

移除软件包及其依赖

```trizen -Rs [package]```

搜索软件包

```trizen -Ss [keyword]```

显示软件包信息

```trizen -Si [package]```

列出已安装的软件包

```trizen -Qe```

# SYNOPSIS

**trizen** [_OPTIONS_] [_TARGETS_...]

# PARAMETERS

**-S**
> 同步/安装软件包

**-Ss**
> 搜索软件包

**-Si**
> 显示软件包信息

**-Syua**
> 同步数据库并升级所有 AUR 软件包

**-Rs**
> 移除软件包及其依赖

**-Qe**
> 列出显式安装的软件包

# DESCRIPTION

**trizen** 是一个 Arch Linux 工具，用于从 Arch 用户仓库 (AUR) 构建和安装软件包。它采用 pacman 风格的命令，并提供依赖解析、PKGBUILD 审查和干净构建等特性。

该工具负责下载 PKGBUILD、构建软件包，并将其连同依赖一起从官方仓库和 AUR 安装。

# CAVEATS

AUR 软件包由用户提交，不受官方支持。构建前请审查 PKGBUILD。需要 base-devel 软件包组。构建过程可能消耗大量时间和资源。

# HISTORY

**trizen** 用 Perl 编写，是一个轻量级的 Arch Linux AUR 助手，在保持与 pacman 命令兼容的同时注重简洁与速度。

# INSTALL

```aur: yay -S trizen```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pacman](/man/pacman)(8), [yay](/man/yay)(8), [paru](/man/paru)(1)
