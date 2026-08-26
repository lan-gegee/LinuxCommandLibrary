# TAGLINE

在 CRUX Linux 上从源码构建软件包

# TLDR

**构建**并下载软件包

```pkgmk -d```

构建并**安装**软件包

```pkgmk -d -i```

构建并**升级**已有软件包

```pkgmk -d -u```

**忽略 footprint** 差异

```pkgmk -d -if```

**忽略 MD5** 校验和

```pkgmk -d -im```

**更新 footprint** 文件

```pkgmk -uf```

# SYNOPSIS

**pkgmk** [**-d**] [**-i**] [**-u**] [**-if**] [**-im**] [**-uf**] [**-um**]

# PARAMETERS

**-d**
> 下载源码文件

**-i**
> 构建后安装软件包

**-u**
> 构建后升级软件包

**-if**
> 忽略 footprint 不一致

**-im**
> 忽略 MD5 校验和不一致

**-uf**
> 更新 footprint 文件

**-um**
> 更新 MD5 校验和文件

**-ns**
> 不对二进制文件做 strip 处理

# DESCRIPTION

**pkgmk** 在 CRUX Linux 上从源码构建二进制软件包。它读取包含构建指令的 Pkgfile（类似 Arch 的 PKGBUILD），下载源码、编译软件并创建软件包归档。

该工具使用 MD5 校验和验证源码完整性，并使用 footprint 文件跟踪已安装的文件以保证可重现性。

# CAVEATS

需要在当前目录中有 Pkgfile。构建依赖必须手动安装。下载源码需要联网。footprint 不一致可能表明构建环境存在差异。

# HISTORY

**pkgmk** 是 CRUX Linux **pkgutils** 的一部分。它提供一种简单的、脚本化的从源码构建软件包的方式，强调构建过程的透明度和用户控制。

# SEE ALSO

[pkgadd](/man/pkgadd)(8), [pkginfo](/man/pkginfo)(1), [prt-get](/man/prt-get)(8)
