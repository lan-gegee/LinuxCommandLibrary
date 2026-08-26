# TAGLINE

创建软件包版本之间的增量文件

# TLDR

**创建增量软件包**

```pkgdelta [old_package] [new_package]```

**应用增量文件**

```xdelta3 -d -s [old_package] [delta] [new_package]```

# SYNOPSIS

**pkgdelta** [_options_] _old_pkg_ _new_pkg_

# PARAMETERS

_OLD_PKG_
> 原始软件包文件。

_NEW_PKG_
> 新软件包文件。

**-q**
> 安静模式。

# DESCRIPTION

**pkgdelta** 为 Arch Linux 软件包的两个版本之间创建二进制增量（delta）文件。生成的增量文件只包含差异部分，与下载完整的新软件包相比，可显著减少软件包升级所需的下载体积。

它是 pacman 软件包管理器套件的一部分，使用 xdelta3 算法计算高效的二进制差异。增量软件包用 xdelta3 应用，从旧软件包和增量文件重建出新的软件包。

# CAVEATS

仅适用于 Arch Linux。需要 xdelta3。节省的空间因情况而异。

# HISTORY

pkgdelta 为实现 **带宽高效** 的 Arch 软件包更新而生。

# SEE ALSO

[pacman](/man/pacman)(8), [xdelta3](/man/xdelta3)(1)
