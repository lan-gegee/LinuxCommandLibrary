# TAGLINE

在 CRUX Linux 上移除已安装的软件包

# TLDR

卸载用 **pkgadd** 安装的软件包

```pkgrm [package]```

# SYNOPSIS

**pkgrm** [**-r** _root_] _package_

# PARAMETERS

**-r _root_**
> 使用备用的根目录

**package**
> 要移除的软件包名称

# DESCRIPTION

**pkgrm** 从 CRUX Linux 系统中移除已安装的软件包。它会删除属于该软件包的所有文件，并从系统数据库中移除该软件包的条目。

该工具不检查依赖关系，因此移除其他软件所依赖的软件包可能会破坏系统。用户必须手动管理依赖。

# CAVEATS

不检查依赖。安装后被修改过的文件不会被删除。只有空目录才会被移除。移除前可用 pkginfo 检查软件包内容。

# HISTORY

**pkgrm** 是 **pkgutils** 的一部分，后者是 CRUX Linux 原生的软件包管理系统。它遵循 CRUX 的理念：工具简单透明，相信用户能够自己管理好系统。

# SEE ALSO

[pkgadd](/man/pkgadd)(8), [pkginfo](/man/pkginfo)(1), [pkgmk](/man/pkgmk)(8)
