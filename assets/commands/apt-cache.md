# TAGLINE

查询 APT 软件包缓存

# TLDR

在当前软件源中**搜索**软件包

```apt-cache search [query]```

只在软件包名称中**搜索**

```apt-cache search --names-only [query]```

显示软件包的**信息**

```apt-cache show [package]```

显示软件包是否**已安装且为最新版本**

```apt-cache policy [package]```

显示软件包的**依赖关系**

```apt-cache depends [package]```

显示**依赖于**某个特定软件包的软件包

```apt-cache rdepends [package]```

以表格形式显示**可用版本**

```apt-cache madison [package]```

# SYNOPSIS

**apt-cache** [_options_] _command_ [_arguments_]

# DESCRIPTION

**apt-cache** 查询本地 APT 软件包缓存，用于搜索软件包、显示详细的软件包信息以及分析依赖关系。它读取由 **apt update** 下载的软件包索引文件，无需联系远程仓库即可快速离线访问软件包元数据。

常见操作包括按名称或描述搜索软件包、查看版本和依赖详情、检查安装策略以及列出反向依赖。其输出适合脚本处理，可帮助诊断依赖冲突或确定某个软件包来自哪个仓库。

# PARAMETERS

**search** _regex_
> 在名称和描述中搜索匹配 POSIX 正则表达式的软件包

**show** _package_
> 显示软件包的详细记录

**showpkg** _package_
> 显示包括版本和依赖在内的常规信息

**showsrc** _package_
> 显示软件包的所有源码包记录

**policy** [_package_]
> 显示策略设置、安装状态和仓库优先级

**depends** _package_
> 显示软件包的依赖关系

**rdepends** _package_
> 显示反向依赖（依赖于该软件包的软件包）

**madison** _package_
> 以表格形式显示可用版本

**pkgnames** [_prefix_]
> 列出缓存中的所有软件包名称，可选按前缀过滤

**stats**
> 显示缓存统计信息

**dump**
> 简要列出缓存中的每个软件包

**unmet**
> 显示缓存中所有未满足依赖的摘要

**-f, --full**
> 搜索时打印完整的软件包记录

**-n, --names-only**
> 只搜索软件包名称，不搜索描述

**-i, --important**
> 只打印 Depends 和 Pre-Depends 关系（配合 depends 和 unmet 使用）

**--installed**
> 将输出限制为当前已安装的软件包

**--recurse**
> 使 depends 和 rdepends 递归执行

# CONFIGURATION

**/etc/apt/sources.list**
> 列出已配置软件仓库的主文件。

**/etc/apt/sources.list.d/**
> 存放额外仓库源文件的目录。

**/etc/apt/preferences.d/**
> 存放软件包锁定（pinning）和优先级偏好设置的目录。

# CAVEATS

此工具基于本地缓存工作；请先运行 **apt update** 以确保缓存是最新的。

# HISTORY

属于 **APT**（Advanced Package Tool）工具套件，于 20 世纪 90 年代末为基于 Debian 的系统开发。

# INSTALL

```apt: sudo apt install apt```

```dnf: sudo dnf install apt```

```pacman: sudo pacman -S apt```

```apk: sudo apk add apt```

```brew: brew install apt```

```nix: nix profile install nixpkgs#apt```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apt](/man/apt)(8), [apt-get](/man/apt-get)(8), [aptitude](/man/aptitude)(8), [dpkg](/man/dpkg)(1)
