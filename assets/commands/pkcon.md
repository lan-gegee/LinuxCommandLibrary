# TAGLINE

PackageKit 的命令行客户端

# TLDR

**安装**软件包

```pkcon install [package]```

**移除**软件包

```pkcon remove [package]```

**刷新**软件包缓存

```pkcon refresh```

**更新**所有软件包

```pkcon update```

**搜索**软件包

```pkcon search [package]```

列出**所有软件包**

```pkcon get-packages```

# SYNOPSIS

**pkcon** [**install**|**remove**|**update**|**search**|**refresh**] [_options_] [_package_]

# COMMANDS

**install**
> 安装软件包

**remove**
> 移除软件包

**update**
> 更新所有已安装的软件包

**search**
> 按名称搜索软件包

**refresh**
> 刷新软件包缓存

**get-packages**
> 列出所有可用软件包

**get-updates**
> 列出可用更新

**get-details**
> 显示软件包详情

# PARAMETERS

**-y, --noninteractive**
> 对提示自动回答 yes

**-p, --plain**
> 纯文本输出

**--filter _filter_**
> 过滤结果（installed、devel 等）

# DESCRIPTION

**pkcon** 是 PackageKit 的命令行客户端。PackageKit 是一个跨发行版的软件包管理抽象层，无论底层是哪种软件包管理器（apt、dnf、zypper 等），它都提供一致的接口。

GNOME Software 和 KDE Discover 等图形化软件中心都使用 PackageKit。pkcon 则从命令行提供相同的功能。

# CAVEATS

操作可能比原生软件包管理器慢。并非所有后端特性都对外暴露。某些发行版并未启用全部 PackageKit 后端。需要 PackageKit 守护进程正在运行。

# HISTORY

**PackageKit** 由 **Richard Hughes** 创建，旨在为 Linux 软件包管理提供统一接口。它的设计目标是让桌面应用无需了解发行版使用哪种软件包管理器即可管理软件包。

# INSTALL

```apt: sudo apt install packagekit-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[apt](/man/apt)(8), [dnf](/man/dnf)(8), [flatpak](/man/flatpak)(1)
