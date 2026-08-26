# TAGLINE

SlackBuilds 软件包管理工具

# TLDR

通过 rsync **更新** slackbuilds 树

```sudo sport rsync```

按名称**搜索**软件包

```sport search "[keyword]"```

**检查**软件包是否已安装

```sport check [package]```

显示**README 和 info** 文件

```sport cat [package]```

**安装**软件包

```sudo sport install [package]```

从**列表文件**安装多个软件包

```sudo sport install $(< [path/to/list])```

# SYNOPSIS

**sport** _command_ [_arguments_]

# COMMANDS

**rsync**
> 从 slackbuilds.org 更新本地 SlackBuilds 树

**search** _keyword_
> 按名称搜索软件包

**check** _package_
> 检查软件包是否已安装

**cat** _package_
> 显示软件包的 README 和 .info 文件

**install** _package_
> 构建并安装 SlackBuild 软件包

# DESCRIPTION

**sport** 是一款面向 Slackware Linux 的 SlackBuilds 软件包管理工具。它提供简单的界面，用于从 SlackBuilds.org 软件仓库搜索、查看信息和安装软件包。

该工具在 **/usr/ports** 中维护一份 SlackBuilds 树的本地副本，通过 rsync 同步。首次使用前必须先初始化该树。依赖项必须在安装前手动解决。

# INITIAL SETUP

首次使用的设置步骤：

```
sudo mkdir -p /usr/ports
sudo rsync -av rsync://slackbuilds.org/slackbuilds/$(awk '{print $2}' /etc/slackware-version)/ /usr/ports/
```

# CAVEATS

不会自动解析依赖；请检查 .info 文件了解所需依赖。构建需从源码编译，需要开发工具。必须用 **sport rsync** 保持 SlackBuilds 树更新。仅适用于基于 Slackware 的发行版。

# HISTORY

**sport** 为 Slackware Linux 而创建，用于简化 SlackBuilds.org 的使用。SlackBuilds.org 是为 Slackware 构建第三方软件的社区脚本仓库，成立于 **2006 年**，旨在提供一种标准化的第三方软件构建方式。

# SEE ALSO

[sbopkg](/man/sbopkg)(8), [slackpkg](/man/slackpkg)(8), [slapt-src](/man/slapt-src)(8)
