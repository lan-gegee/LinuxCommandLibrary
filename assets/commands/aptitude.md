# TAGLINE

支持依赖解析的高级软件包管理工具

# TLDR

**同步**软件包及其版本列表

```sudo aptitude update```

**安装**新软件包

```sudo aptitude install [package]```

**搜索**软件包

```aptitude search [package]```

搜索**已安装**的软件包

```aptitude search '?installed([package])'```

**删除**软件包及所有依赖它的软件包

```sudo aptitude remove [package]```

**升级**已安装的软件包

```sudo aptitude upgrade```

**完整升级**，包括删除过时的软件包

```sudo aptitude full-upgrade```

**模拟**安装而不做任何更改

```sudo aptitude install -s [package]```

**查看**软件包为何被安装

```aptitude why [package]```

**锁定**软件包以阻止自动升级

```sudo aptitude hold '?installed([package])'```

# SYNOPSIS

**aptitude** [_options_] _command_ [_arguments_]

# DESCRIPTION

**aptitude** 是 Debian 和 Ubuntu 系统上功能强大的软件包管理工具。它同时提供命令行界面和基于 ncurses 的交互式界面，具有高级依赖解析和搜索能力。

# PARAMETERS

**update**
> 从软件源同步软件包索引文件

**install package**
> 安装或升级指定软件包

**remove package**
> 删除软件包及其依赖它的软件包

**purge package**
> 删除软件包、配置文件及依赖它的软件包

**upgrade**
> 将已安装的软件包升级到最新版本

**full-upgrade**
> 升级软件包，必要时删除过时的软件包

**search pattern**
> 搜索匹配模式的软件包

**show package**
> 显示软件包详细信息

**hold package**
> 阻止软件包被升级

**unhold package**
> 允许软件包被升级

**safe-upgrade**
> 以保守方式升级软件包

**clean**
> 删除已下载的软件包文件

**autoclean**
> 删除旧的已下载软件包文件

**why package**
> 解释某软件包为何被安装或需要

**why-not package**
> 解释某软件包为何无法安装

**download package**
> 下载 .deb 文件但不安装

**reinstall package**
> 重新安装已安装的软件包

**versions package**
> 列出软件包的可用版本

**forbid-version package**
> 阻止升级到特定软件包版本

**markauto package**
> 将软件包标记为自动安装

**unmarkauto package**
> 将软件包标记为手动安装

**-s**, **--simulate**
> 预览更改而不实际应用

**-y**, **--assume-yes**
> 跳过确认提示

**-D**, **--show-deps**
> 显示自动安装和删除的原因说明

**-V**, **--show-versions**
> 在列表中显示软件包版本详情

**-P**, **--prompt**
> 在更改前总是显示确认提示

**-R**, **--without-recommends**
> 不将推荐软件包视为依赖

**-t** _release_
> 设置安装软件包的目标发行版

**-q**, **--quiet**
> 抑制进度指示器

**changelog** _package_
> 下载并显示软件包的更新日志

# CONFIGURATION

**~/.aptitude/config**
> 用户专属的 aptitude 配置。

**/etc/apt/apt.conf**
> 与 apt 和 apt-get 共享的 APT 配置。

**/etc/apt/apt.conf.d/**
> 存放额外 APT 配置片段的目录。

# CAVEATS

Aptitude 使用自己的搜索语法，包含 **?installed**、**?automatic** 等特殊术语，与 apt-cache 的搜索语法不同。

# HISTORY

作为 apt-get 的替代品而开发，功能更高级。由 Daniel Burrows 于 **2001** 年首次为 Debian 发布。

# INSTALL

```apt: sudo apt install aptitude```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apt](/man/apt)(8), [apt-get](/man/apt-get)(8), [dpkg](/man/dpkg)(1), [nala](/man/nala)(8)
