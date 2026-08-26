# TAGLINE

高级软件包管理接口

# TLDR

**更新**可用软件包列表

```sudo apt update```

按名称或描述**搜索**软件包

```apt search [package]```

**查看**软件包的详细信息

```apt show [package]```

**安装**软件包或将其更新到最新版本

```sudo apt install [package]```

**删除**软件包

```sudo apt remove [package]```

将所有已安装的软件包**升级**到最新版本

```sudo apt upgrade```

列出所有**已安装**的软件包

```apt list --installed```

列出**可升级**的软件包

```apt list --upgradable```

**删除**不再使用的依赖

```sudo apt autoremove```

# SYNOPSIS

**apt** [_options_] _command_ [_arguments_]

# DESCRIPTION

**apt** 是基于 Debian 的发行版上软件包管理系统的高级命令行接口。它定位为 **apt-get** 的用户友好替代品，适用于交互式使用，拥有更合理的默认设置和进度显示。

# PARAMETERS

**update**
> 从配置的软件源下载软件包信息

**upgrade**
> 安装可用的升级，但不删除软件包

**full-upgrade**
> 执行升级，必要时删除软件包

**install package**
> 安装或升级指定软件包；使用 _package=version_ 锁定版本，或 _package/codename_ 选择发行版

**reinstall package**
> 重新安装已处于最新版本的软件包

**remove package**
> 删除指定软件包

**purge package**
> 删除软件包及其配置文件

**autoremove**
> 删除自动安装但已不再需要的软件包

**search pattern**
> 搜索匹配模式的软件包

**show package**
> 显示软件包信息

**list**
> 列出符合条件的软件包（可配合 **--installed**、**--upgradable** 或 **--all-versions** 使用）

**satisfy string**
> 满足依赖字符串（如 Build-Depends 中使用的格式）

**edit-sources**
> 编辑 sources.list 文件

**-y, --yes**
> 对所有询问自动回答 yes

**-q, --quiet**
> 安静输出

**-t, --target-release release**
> 优先使用指定发行版的软件包（如 backports 套件）

**--no-install-recommends**
> 不安装推荐软件包

# CONFIGURATION

**/etc/apt/sources.list**
> 软件仓库主列表文件。

**/etc/apt/sources.list.d/**
> 存放额外软件仓库列表文件的目录。

**/etc/apt/apt.conf**
> APT 主配置文件。

**/etc/apt/apt.conf.d/**
> 存放额外 APT 配置片段的目录。

**/etc/apt/preferences**
> 软件包版本锁定偏好设置。

**/etc/apt/preferences.d/**
> 存放额外版本锁定偏好文件的目录。

# CAVEATS

面向交互式使用；在脚本中建议改用 **apt-get**，其输出格式更稳定。

# HISTORY

**apt** 于 **Debian 8 (Jessie)** 和 **Ubuntu 14.04** 中引入，是一个统一前端，整合了 apt-get、apt-cache 和 apt-config 的功能。

# INSTALL

```apt: sudo apt install apt```

```dnf: sudo dnf install apt```

```pacman: sudo pacman -S apt```

```apk: sudo apk add apt```

```brew: brew install apt```

```nix: nix profile install nixpkgs#apt```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apt-get](/man/apt-get)(8), [apt-cache](/man/apt-cache)(8), [dpkg](/man/dpkg)(1), [aptitude](/man/aptitude)(8)

# RESOURCES

```[Source code](https://salsa.debian.org/apt-team/apt)```

```[Documentation](https://manpages.debian.org/apt)```

<!-- verified: 2026-06-11 -->
