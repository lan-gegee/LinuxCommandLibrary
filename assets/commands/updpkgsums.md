# TAGLINE

更新 Arch PKGBUILD 文件中的源码校验和

# TLDR

在当前目录下**更新 PKGBUILD 中的校验和**

```updpkgsums```

**更新特定 PKGBUILD 文件的校验和**

```updpkgsums [path/to/PKGBUILD]```

**更新校验和且不使用彩色输出**

```updpkgsums -m```

显示**帮助**

```updpkgsums -h```

# SYNOPSIS

**updpkgsums** [_OPTIONS_] [_build file_]

# PARAMETERS

**-h**, **--help**
> 显示帮助信息。

**-m**, **--nocolor**
> 输出不带颜色。

**-V**, **--version**
> 显示版本信息。

# DESCRIPTION

**updpkgsums** 对 PKGBUILD 文件中的校验和执行就地更新。它会按需下载源码并计算新的校验和，然后更新 PKGBUILD 文件。未指定文件时，默认处理当前目录下的 PKGBUILD。

除非 PKGBUILD 中已经指定了哈希算法，否则新的校验和将采用 SHA256。

# CAVEATS

Arch Linux 特有。必须在包含 PKGBUILD 的目录中运行。源码尚未缓存时会自动下载。获取远程源码需要网络连接。

# SEE ALSO

[makepkg](/man/makepkg)(8), [pacman](/man/pacman)(8)
