# TAGLINE

Ubuntu 图形化软件更新管理器

# TLDR

**启动"软件更新器"**图形界面

```update-manager```

**检查发行版升级**

```update-manager -c```

**检查更新**并启动图形界面

```update-manager -d```

**启动时不抢占焦点**（用于通知）

```update-manager --no-focus-on-map```

**检查 proposed 软件仓库中的更新**

```update-manager -p```

# SYNOPSIS

**update-manager** [**-c**|**--check-dist-upgrades**] [**-d**|**--devel-release**] [**-p**|**--proposed**] [**--no-focus-on-map**]

# PARAMETERS

**-c**, **--check-dist-upgrades**
> 检查是否有新的发行版可供升级。

**-d**, **--devel-release**
> 检查是否可升级到最新的开发版本。

**-p**, **--proposed**
> 包含来自 proposed 软件仓库的更新（预发布更新）。

**--no-focus-on-map**
> 窗口出现时不抢占焦点。适合后台通知场景。

**--no-update**
> 启动时不检查更新。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**update-manager** 是 Ubuntu 的 apt 软件包管理系统图形前端。它在应用菜单中的名称为 "Software Updater"，为检查和安装系统更新提供了友好的界面。

该工具会检查可用的软件包更新，连同描述和大小一并展示，允许用户有选择地安装更新。它还能检测到新的 Ubuntu 发行版何时可用，并提供执行发行版升级的功能。

update-manager 统一处理安全更新、常规软件包更新和大版本升级。它集成了 Ubuntu 的通知系统，在有更新可用时提醒用户。对于服务器或命令行环境，等效功能由 **apt** 或 **apt-get** 提供。

# CAVEATS

需要图形环境（X11 或 Wayland）。无头服务器请改用 apt-get 或 apt。执行发行版升级前应做好充分的准备和备份。某些更新可能需要重启系统才能生效。

# HISTORY

**update-manager** 由 Canonical 开发，是 Ubuntu 易用桌面体验的一环。它首次出现在 **2004-2005** 年左右的早期 Ubuntu 版本中，目的是让不熟悉命令行软件包管理的用户也能轻松完成系统更新。该工具随后增加了发行版升级能力，并与 Ubuntu 的长期支持（LTS）发布周期相整合。

# SEE ALSO

[apt](/man/apt)(8), [apt-get](/man/apt-get)(8), [do-release-upgrade](/man/do-release-upgrade)(8), [unattended-upgrades](/man/unattended-upgrades)(8)
