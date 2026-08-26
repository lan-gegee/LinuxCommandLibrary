# TAGLINE

跨发行版的软件包管理器封装器

# TLDR

**搜索软件包**

```pkgz search [query]```

**安装软件包**

```pkgz install [package]```

**列出已安装软件包**

```pkgz list```

**更新软件包**

```pkgz update```

# SYNOPSIS

**pkgz** [_command_] [_options_]

# PARAMETERS

**search** _QUERY_
> 搜索软件包。

**install** _PACKAGE_
> 安装软件包。

**list**
> 列出已安装的软件包。

**update**
> 更新软件包。

**--help**
> 显示帮助。

# DESCRIPTION

**pkgz** 是一个软件包管理器封装器，为各 Linux 发行版提供统一的命令接口。它将安装、搜索、更新等常见操作转换为底层软件包管理器（apt、dnf、pacman、zypper 等）的相应命令。

这让用户和脚本无论运行在哪个发行版上都能使用同一套命令，简化了跨发行版的工作流和文档编写。

# CAVEATS

封装工具。需要底层软件包管理器。

# HISTORY

pkgz 提供跨发行版的 **简化软件包管理**。

# SEE ALSO

[apt](/man/apt)(1), [yum](/man/yum)(1), [pacman](/man/pacman)(1)
