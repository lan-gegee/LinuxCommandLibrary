# TAGLINE

从已配置的仓库安装软件包。

# TLDR

**安装**软件包或将其更新到最新版本

```sudo apt install [package]```

安装时显示**详细的版本信息**

```sudo apt install -V [package]```

安装软件包的**特定版本**

```sudo apt install [package]=[version]```

**不经确认提示**直接安装

```sudo apt install -y [package]```

**重新安装**已安装的软件包

```sudo apt install --reinstall [package]```

安装时**不包含推荐的**软件包

```sudo apt install --no-install-recommends [package]```

**修复损坏的**依赖关系

```sudo apt install -f```

# SYNOPSIS

**apt install** [_options_] _package_...

# DESCRIPTION

**apt install** 是在基于 Debian 的发行版上安装软件包的标准命令。它负责解析依赖关系、从已配置的仓库下载软件包并将其安装到系统中。

如果指定的软件包已经安装，该命令会将其升级到最新的可用版本。单条命令可以指定多个软件包。

# PARAMETERS

**-y, --yes**
> 对提示自动回答 yes；将 "yes" 作为所有提示的答案

**-V, --verbose-versions**
> 显示被升级和被安装软件包的完整版本号

**--reinstall**
> 即使软件包已是最新也重新安装

**--no-install-recommends**
> 不安装推荐的软件包

**-d, --download-only**
> 只下载软件包，不进行安装

**-f, --fix-broken**
> 尝试修复存在损坏依赖的系统

**-s, --simulate**
> 模拟安装过程而不做任何更改

**--no-install-suggests**
> 不安装建议的软件包

# CONFIGURATION

**/etc/apt/sources.list**
> 软件包源仓库列表。

**/etc/apt/apt.conf**
> APT 主配置文件。

**/etc/apt/apt.conf.d/**
> 存放即插式配置片段的目录。

# CAVEATS

需要 root 权限。为了满足依赖关系，该命令可能会移除冲突的软件包。在脚本中建议使用 **apt-get install**，其输出格式更稳定。

# INSTALL

```apt: sudo apt install apt```

```dnf: sudo dnf install apt```

```pacman: sudo pacman -S apt```

```apk: sudo apk add apt```

```brew: brew install apt```

```nix: nix profile install nixpkgs#apt```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apt](/man/apt)(8), [apt-get](/man/apt-get)(8), [apt-cache](/man/apt-cache)(8), [dpkg](/man/dpkg)(1)
