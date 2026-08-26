# TAGLINE

安装、升级和管理软件包。

# TLDR

**更新**可用软件包的列表

```sudo apt-get update```

**安装**软件包或将其更新到最新版本

```sudo apt-get install [package]```

**移除**软件包

```sudo apt-get remove [package]```

**移除**软件包及其配置文件

```sudo apt-get purge [package]```

**升级**所有已安装的软件包

```sudo apt-get upgrade```

**清理**本地仓库中被中断的下载

```sudo apt-get autoclean```

**移除**所有不再需要的软件包

```sudo apt-get autoremove```

**升级**并处理发生变化的依赖关系

```sudo apt-get dist-upgrade```

# SYNOPSIS

**apt-get** [_options_] _command_ [_package_...]

# DESCRIPTION

**apt-get** 是 Debian 和 Ubuntu 的命令行软件包管理工具，负责软件包的安装、升级和移除。对于交互式使用，推荐使用更友好的 **apt**。

# PARAMETERS

**update**
> 从软件源重新同步软件包索引文件

**upgrade**
> 安装所有当前已安装软件包的最新版本

**dist-upgrade**
> 升级并处理发生变化的依赖关系

**install package**
> 安装或升级指定的软件包

**remove package**
> 移除软件包

**purge package**
> 移除软件包及其配置文件

**autoremove**
> 移除不再需要的自动安装的软件包

**autoclean**
> 清理本地仓库中已无法再下载的已获取软件包文件

**clean**
> 清理本地仓库中所有已获取的软件包文件

**download package**
> 将二进制软件包下载到当前目录

**source package**
> 获取源码包

**build-dep package**
> 安装源码包的构建依赖

**satisfy string**
> 满足依赖字符串（如 Build-Depends 中所用）；在参数前加 'Conflicts: ' 前缀可表达冲突关系

**-y, --yes**
> 对提示自动回答 yes；非交互式运行

**-s, --simulate**
> 不执行实际操作；模拟将发生的事件而不改变系统

**-d, --download-only**
> 只下载软件包，不解压也不安装

**--no-install-recommends**
> 不安装推荐的软件包

**--reinstall**
> 重新安装已是最新版本的软件包

**--only-upgrade**
> 只升级已安装的软件包；忽略安装新软件包的请求

**-f, --fix-broken**
> 尝试修复损坏的依赖关系

# CONFIGURATION

**/etc/apt/sources.list**
> 软件包源仓库列表。

**/etc/apt/apt.conf**
> APT 主配置文件。

**/etc/apt/apt.conf.d/**
> 存放即插式配置片段的目录。

# CAVEATS

在执行其他命令前先运行 **apt-get update**，以确保软件包列表是最新的。

# HISTORY

属于 **APT**（Advanced Package Tool）工具套件，由 APT Development Team 于 **1998** 年为 Debian 开发。

# INSTALL

```apt: sudo apt install apt```

```dnf: sudo dnf install apt```

```pacman: sudo pacman -S apt```

```apk: sudo apk add apt```

```brew: brew install apt```

```nix: nix profile install nixpkgs#apt```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apt](/man/apt)(8), [apt-cache](/man/apt-cache)(8), [dpkg](/man/dpkg)(1), [aptitude](/man/aptitude)(8)

# RESOURCES

```[Source code](https://salsa.debian.org/apt-team/apt)```

```[Documentation](https://manpages.debian.org/apt-get)```

<!-- verified: 2026-06-11 -->
