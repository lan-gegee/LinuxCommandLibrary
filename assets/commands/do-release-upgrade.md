# TAGLINE

将操作系统升级到最新发行版

# TLDR

**升级到最新发行版**

```sudo do-release-upgrade```

**升级到开发版**

```sudo do-release-upgrade -d```

**使用候选版升级器**升级

```sudo do-release-upgrade -p```

**只检查是否有可用升级而不实际执行**

```sudo do-release-upgrade -c```

以服务器模式运行升级，使用文本前端

```sudo do-release-upgrade -m server -f DistUpgradeViewText```

在沙盒中测试升级，不改动系统

```sudo do-release-upgrade -s```

# SYNOPSIS

**do-release-upgrade** [_options_]

# PARAMETERS

**-h**, **--help**
> 显示帮助信息并退出。

**-d**, **--devel-release**
> 若当前已在使用最新受支持的发行版，则升级到开发版。

**-p**, **--proposed**
> 尝试使用 ubuntu-proposed 中的升级器进行升级。

**-c**, **--check-dist-upgrade-only**
> 检查是否有新发行版可用，然后退出，不执行升级。

**-m** _MODE_, **--mode** _MODE_
> 以特殊升级模式运行。支持的模式有 "desktop" 和 "server"。

**-f** _FRONTEND_, **--frontend** _FRONTEND_
> 运行指定的前端（DistUpgradeViewGtk3、DistUpgradeViewText、DistUpgradeViewNonInteractive）。

**-s**, **--sandbox**
> 使用 aufs overlay 沙盒测试升级。

# DESCRIPTION

**do-release-upgrade** 将 Ubuntu 升级到新的发行版本。它负责更新软件源、升级软件包以及解决冲突等复杂流程。它是升级服务器和无图形环境系统时的推荐命令，也适用于通过远程连接执行升级的场景。

默认情况下，只会提供向下一个 LTS 发行版的升级（针对 LTS 用户）或下一个常规发行版的升级（针对非 LTS 用户）。若要升级到开发版，需要使用 **-d** 标志。

# CAVEATS

Ubuntu 专属命令。升级前请备份重要数据。升级可能耗费大量时间。第三方软件仓库会在升级期间被禁用，并可能导致问题。通过 SSH 升级时，请在终端复用器（screen 或 tmux）中运行，以避免连接中断带来的问题。

# HISTORY

**do-release-upgrade** 属于 **ubuntu-release-upgrader** 软件包，自 Ubuntu 8.04（Hardy Heron）起就是执行 Ubuntu 发行版升级的标准工具。它取代了手动编辑 sources.list 的做法，成为推荐的升级方式。

# SEE ALSO

[apt](/man/apt)(8), [apt-get](/man/apt-get)(8), [update-manager](/man/update-manager)(8), [screen](/man/screen)(1)
