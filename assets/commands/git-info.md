# TAGLINE

显示全面的仓库信息

# TLDR

**显示仓库信息**

```git info```

**显示标题带颜色的仓库信息**

```git info --color```

**显示不含配置详情的仓库信息**

```git info --no-config```

# SYNOPSIS

**git info** [_options_]

# PARAMETERS

**-c**, **--color**
> 为信息标题使用颜色。

**--no-config**
> 不显示配置信息区段。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git info** 以单一的格式化视图显示全面的仓库信息，包括远程 URL、远程分支、本地分支、子模块（如有）、最近一次提交以及配置设置。

它是 **git-extras** 套件的组成部分，无需运行多个单独的 git 命令即可获得当前仓库状态的快照。最近提交和配置信息的输出格式可以通过 `git config --global --add git-extras.info.log "<log-command>"` 和 `git config --global --add git-extras.info.config-grep "<config-grep-command>"` 自定义。

# CAVEATS

需要安装 **git-extras** 软件包。必须在 git 仓库内运行。所有信息均取自本地仓库，不需要网络访问。

# HISTORY

git info 是 **git-extras** 的组成部分，由 **TJ Holowaychuk** 创建，旨在用一条命令提供仓库概览。

# INSTALL

```apt: sudo apt install git```

```dnf: sudo dnf install git```

```pacman: sudo pacman -S git```

```apk: sudo apk add git```

```zypper: sudo zypper install git```

```brew: brew install git```

```nix: nix profile install nixpkgs#git```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-status](/man/git-status)(1), [git-remote](/man/git-remote)(1), [git-log](/man/git-log)(1)
