# TAGLINE

通用的跨平台软件包管理器封装工具

# TLDR

**安装软件包**

```upt install [package]```

**移除软件包**

```upt remove [package]```

**更新软件包**

```upt upgrade```

**搜索软件包**

```upt search [query]```

**列出已安装**

```upt list```

**显示信息**

```upt info [package]```

# SYNOPSIS

**upt** _command_ [_options_] [_package_]

# PARAMETERS

**install**
> 安装软件包。

**remove**
> 移除软件包。

**upgrade**
> 更新全部软件包。

**search**
> 查找软件包。

**list**
> 显示已安装的软件包。

**info**
> 软件包详情。

# DESCRIPTION

**upt**（Universal Package Tool）提供一个统一且一致的命令行接口，用来封装任何系统上的原生软件包管理器。它会自动检测当前可用的软件包管理器，并把 upt 命令转换为 apt、pacman、brew 等对应的原生命令。

这样，用户和脚本就能在不同 Linux 发行版和 macOS 上使用相同的命令，而不必记住各软件包管理器之间语法上的差异。无论底层系统是什么，**install**、**remove**、**search** 和 **upgrade** 等命令的行为都保持一致。

该工具把所有实际软件包操作都委托给原生软件包管理器完成，因此不会引入任何兼容层或替代性的软件包格式。根据底层软件包管理器的要求，可能需要 root 权限。

# CAVEATS

封装工具。底层软件包管理器因系统而异。可能需要 sudo。

# HISTORY

**upt**（Universal Package Tool）为各种系统软件包管理器提供统一的接口。

# SEE ALSO

[apt](/man/apt)(1), [pacman](/man/pacman)(1), [brew](/man/brew)(1)
