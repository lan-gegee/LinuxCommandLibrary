# TAGLINE

从 APT 软件包数据库列出符合条件的软件包

# TLDR

**列出已配置仓库中的所有软件包**

```apt list```

只列出**已安装的软件包**

```apt list --installed```

列出具**有可用升级**的软件包

```apt list --upgradable```

显示每个软件包的**所有可用版本**

```apt list --all-versions```

使用 **shell 模式**过滤软件包名称

```apt list "[nginx*]"```

将 **installed** 过滤器与模式组合使用

```apt list --installed "[python3-*]"```

# SYNOPSIS

**apt list** [_options_] [_pattern_...]

# DESCRIPTION

**apt list** 显示由 APT 软件包管理器跟踪的软件包列表。默认情况下，它会打印已配置源所知的每个软件包，每一行包含软件包名称、版本、架构以及状态标签，例如 **[installed]**、**[installed,automatic]** 或 **[upgradable from: ...]**。

该命令接受一个或多个 shell 风格的模式来按软件包名称过滤输出。过滤器可与 **--installed**、**--upgradable** 或 **--manual-installed** 组合，将结果缩小到特定状态。其输出面向交互式使用，不同发行版之间可能有所变化。

用于脚本时，APT 会向 stderr 打印警告；如果需要稳定的输出，请重定向 stderr 或改用 **dpkg-query** / **apt-cache pkgnames**。

# PARAMETERS

**--installed**
> 只显示系统上当前已安装的软件包。

**--upgradable**
> 只显示有更新版本可用的已安装软件包。

**--manual-installed**
> 只显示被显式安装（而非作为依赖）的软件包。

**--all-versions**
> 显示每个软件包的所有可用版本，而不仅仅是候选版本。

**-v**, **--verbose**
> 打印额外细节，如来源仓库。

**-q**, **--quiet**
> 隐藏进度指示；输出更安静，适合日志记录。

**-o** _OPTION=VALUE_
> 为本次调用设置任意的 APT 配置选项。

# CONFIGURATION

**/etc/apt/sources.list**
> apt list 查询的主仓库列表。

**/etc/apt/sources.list.d/**
> 存放额外仓库定义的即插式目录。

**/var/lib/apt/lists/**
> 缓存的软件包索引；需先运行 **apt update** 刷新后，列表才能反映新版本。

# CAVEATS

APT 明确警告 **apt** 的 CLI 并不稳定；输出格式在不同版本之间可能变化。脚本中请使用 **dpkg-query -l** 或 **apt-cache**。如果需要看到最近的仓库变更，请先运行 **apt update**。模式参数由 Shell 解释，因此要为通配符加引号以防止本地文件名展开。

# HISTORY

**list** 子命令随 **apt** 在 **Debian 8（Jessie，2015）** 中发布而引入，作为 apt-get 和 apt-cache 更友好的前端。它将此前分散在 **dpkg -l** 和 **apt-cache pkgnames** 中的功能整合为一个面向用户的单一命令。

# INSTALL

```apt: sudo apt install apt```

```dnf: sudo dnf install apt```

```pacman: sudo pacman -S apt```

```apk: sudo apk add apt```

```brew: brew install apt```

```nix: nix profile install nixpkgs#apt```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apt](/man/apt)(8), [apt-cache](/man/apt-cache)(8), [apt-get](/man/apt-get)(8), [dpkg-query](/man/dpkg-query)(1), [dpkg](/man/dpkg)(1)
