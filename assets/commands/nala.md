# TAGLINE

面向 Debian 系系统的现代软件包管理工具

# TLDR

**安装**软件包

```sudo nala install [package]```

**移除**软件包

```sudo nala remove [package]```

**彻底清除（purge）**软件包（移除并删除配置文件）

```sudo nala purge [package]```

**搜索**软件包

```nala search "[pattern]"```

**更新并升级**系统

```sudo nala upgrade```

**移除不再使用的软件包**

```sudo nala autoremove```

**获取快速镜像**

```sudo nala fetch```

显示**事务历史**

```nala history```

# SYNOPSIS

**nala** _command_ [_options_] [_packages_]

# COMMANDS

**install _packages_**
> 安装软件包或更新到最新版本

**remove _packages_**
> 移除软件包

**purge _packages_**
> 移除软件包及其配置文件

**update**
> 从软件仓库更新软件包列表

**upgrade**
> 更新软件包列表并升级已安装的软件包

**search _pattern_**
> 使用正则表达式或 glob 搜索软件包名称和描述

**show _packages_**
> 显示软件包信息

**autoremove**
> 移除不再使用的软件包和依赖

**autopurge**
> 带 purge 的 autoremove（同时删除配置文件）

**fetch**
> 获取并选择快速镜像

**history**
> 显示事务历史

**clean**
> 清空软件包缓存

# PARAMETERS

**--assume-yes, -y**
> 对所有提示自动回答 yes

**--download-only, -d**
> 只下载软件包而不安装

**--no-install-recommends**
> 不安装推荐软件包

**--install-suggests**
> 同时安装建议软件包

**--verbose, -v**
> 启用详细输出

**--debug**
> 启用调试输出

# DESCRIPTION

**nala** 是面向 Debian 系系统的现代软件包管理工具，作为 apt 和 python-apt API 的前端。与传统 apt 相比，它提供了更美观的格式化输出、并行下载和更简洁的界面。

其特性包括：可查看和撤销变更的事务历史、加速操作的并行下载，以及基于延迟和吞吐量测试自动选择快速镜像的 fetch 命令。

# CAVEATS

Nala 封装了 apt，需要相同的权限。并非所有 apt 功能都通过 nala 暴露。fetch 命令会修改 /etc/apt/sources.list。事务历史存储在本地，可用于撤销/重做操作。

# HISTORY

**nala** 由 **Volian Linux** 项目开发，于 **2021 年 12 月**首次发布。它受 dnf 软件包管理器排版风格的启发，旨在为 apt 提供对用户更友好、视觉输出更好的界面。

# SEE ALSO

[apt](/man/apt)(8), [apt-get](/man/apt-get)(8), [dpkg](/man/dpkg)(1)
