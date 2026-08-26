# TAGLINE

在 CRUX Linux 上安装软件包

# TLDR

**安装**本地软件包

```pkgadd [package]```

**更新**已有的软件包

```pkgadd -u [package]```

# SYNOPSIS

**pkgadd** [**-u**] [**-f**] [**-r** _root_] _package_

# PARAMETERS

**-u**
> 升级模式，更新已有软件包

**-f**
> 强制安装，覆盖已有文件

**-r _root_**
> 使用备用的根目录

# DESCRIPTION

**pkgadd** 在 CRUX Linux 系统上安装软件包。软件包是具有特定结构的 tar 归档文件，包含二进制文件、库和元数据。

该工具将软件包内容解压到文件系统，并在系统数据库中注册该软件包。它会处理文件冲突，并能升级已有的安装。

# CAVEATS

CRUX 特有的软件包管理器。软件包必须在本地构建或下载。没有自动依赖解析，需要手动管理依赖关系。

# HISTORY

**pkgadd** 是 **pkgutils** 的一部分，后者是 **CRUX Linux** 原生的软件包管理系统。CRUX 强调简洁：软件包只是简单的 tar 归档文件，工具也极为精简。

# SEE ALSO

[pkgrm](/man/pkgrm)(8), [pkginfo](/man/pkginfo)(1), [pkgmk](/man/pkgmk)(8)
