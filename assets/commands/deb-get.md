# TAGLINE

面向第三方 .deb 软件包的类 apt-get 功能

# TLDR

**更新**可用软件包列表

```deb-get update```

**搜索**软件包

```deb-get search [package]```

显示软件包**信息**

```deb-get show [package]```

**安装**或升级软件包

```deb-get install [package]```

**移除**软件包

```deb-get remove [package]```

**升级**所有已安装的软件包

```deb-get upgrade```

**列出**所有可用软件包

```deb-get list```

# SYNOPSIS

**deb-get** _command_ [_package_]

# DESCRIPTION

**deb-get** 为来自第三方软件仓库或直接下载的 .deb 软件包提供类 apt-get 的功能。它简化了官方 Debian/Ubuntu 软件仓库中没有的软件的安装。

支持 Chrome、Discord、Slack、VS Code 等众多流行应用。

# PARAMETERS

**update**
> 更新软件包列表

**search** _pattern_
> 搜索软件包

**show** _package_
> 显示软件包信息

**install** _package_
> 安装或升级软件包

**remove** _package_
> 移除软件包

**purge** _package_
> 移除软件包及其配置

**reinstall** _package_
> 重新安装软件包

**upgrade**
> 升级所有软件包

**list** [_--installed_|_--not-installed_|_--raw_]
> 列出可用软件包。用 --installed 或 --not-installed 过滤，用 --raw 跳过安装状态检查。

**clean**
> 移除缓存的 .deb 文件

**fix-installed**
> 修复损坏的软件包

# CAVEATS

仅适用于基于 Debian 的发行版。软件包来自第三方来源。请定期更新以获取最新的软件包信息。

# SEE ALSO

[apt-get](/man/apt-get)(8), [apt](/man/apt)(8), [dpkg](/man/dpkg)(1)
