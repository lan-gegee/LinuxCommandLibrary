# TAGLINE

CRUX Linux 的软件包管理器

# TLDR

**安装**软件包

```prt-get install [package]```

连同**依赖**一起安装

```prt-get depinst [package]```

**升级**软件包

```prt-get upgrade [package]```

**删除**软件包

```prt-get remove [package]```

从 ports 进行**系统升级**

```prt-get sysup```

在 ports 树中**搜索**

```prt-get search [query]```

在软件包中搜索**文件**

```prt-get fsearch [filename]```

显示有**可用更新**的软件包

```prt-get diff```

显示软件包的**信息**

```prt-get info [package]```

**列出**软件包的**依赖**

```prt-get depends [package]```

**列出已安装**的软件包

```prt-get listinst```

# SYNOPSIS

**prt-get** [**install**|**depinst**|**upgrade**|**remove**|**search**|**sysup**] [_options_] [_package_]

# COMMANDS

**install**
> 安装软件包，不处理依赖

**depinst**
> 安装软件包及其依赖

**upgrade**
> 升级已安装的软件包

**remove**
> 删除已安装的软件包

**sysup**
> 升级所有已安装的软件包

**search**
> 按名称搜索软件包

**fsearch**
> 在软件包中搜索文件

**info**
> 显示软件包信息

**diff**
> 显示有可用更新的软件包

**listinst**
> 列出已安装的软件包

**dependent**
> 列出依赖于某软件包的其他软件包

**depends**
> 列出软件包的依赖

**deptree**
> 显示软件包的完整依赖树

**cat**
> 输出某个 port 的 Pkgfile

**path**
> 输出 port 目录的路径

**lock**
> 锁定软件包以阻止升级

**unlock**
> 解锁先前锁定的软件包

**listlocked**
> 列出已锁定的软件包

**isinst**
> 检查软件包是否已安装

# PARAMETERS

**-fr**
> 即使已是最新版本也强制重新构建

**-if**
> 忽略 footprint 不匹配

**-im**
> 忽略 MD5 不匹配

**-v**
> 在搜索结果中显示版本号

**-vv**
> 在搜索结果中显示版本号和描述

**-is**
> 忽略签名不匹配

**--margs**=_"args"_
> 向 pkgmk 传递额外参数

**--aargs**=_"args"_
> 向 pkgadd 传递额外参数

**--log**
> 启用构建日志记录

**--all**
> 在输出中包含已锁定的软件包

**--config**=_file_
> 使用替代的配置文件

# DESCRIPTION

**prt-get** 是 CRUX Linux 的高层软件包管理器。它在基础 pkgutils 之上提供依赖解析，使软件包管理更加便捷，同时保持 CRUX 的简洁性。

该工具从 ports 树读取软件包信息，能够自动构建并安装软件包及其依赖。

# CAVEATS

CRUX 专用工具。需要先同步 ports 树。从源码构建软件包，没有预构建的二进制软件包。

# HISTORY

**prt-get** 为 CRUX Linux 而创建，用于在基础 pkgutils 之上添加依赖处理能力。它至今仍是 CRUX 系统上管理软件包的主要方式。

# SEE ALSO

[pkgmk](/man/pkgmk)(8), [pkgadd](/man/pkgadd)(8), [pkgrm](/man/pkgrm)(8), [pkginfo](/man/pkginfo)(8), [ports](/man/ports)(8)
