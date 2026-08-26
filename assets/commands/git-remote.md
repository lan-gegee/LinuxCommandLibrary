# TAGLINE

管理远程仓库连接

# TLDR

**列出远程**

```git remote -v```

**添加远程**

```git remote add [name] [url]```

**移除远程**

```git remote remove [name]```

**重命名远程**

```git remote rename [old] [new]```

**显示远程详情**

```git remote show [origin]```

# SYNOPSIS

**git remote** [_command_] [_options_]

# PARAMETERS

**add** _NAME_ _URL_
> 添加新远程。

**remove** _NAME_
> 移除远程。

**rename** _OLD_ _NEW_
> 重命名远程。

**show** _NAME_
> 显示远程信息。

**set-url** _NAME_ _URL_
> 更改远程 URL。

**prune** _NAME_
> 删除过期的跟踪分支。

**get-url** _NAME_
> 显示远程的 URL。

**-v**, **--verbose**
> 显示 URL。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git remote** 管理被跟踪的远程仓库。它为 fetch 和 push 操作配置 URL 和 refspec，使分布式工作流中可以与多个远程仓库交互。

常见操作包括：为基于 fork 的开发添加上游远程、仓库迁移后更改 URL、重命名远程，以及检查被跟踪分支、push/fetch URL 等远程配置细节。

# CONFIGURATION

**.git/config**
> 包含 URL 和 refspec 的仓库远程配置。

```
[remote "origin"]
    url = https://github.com/user/repo.git
    fetch = +refs/heads/*:refs/remotes/origin/*
```

# CAVEATS

远程名称只是本地别名。fetch 与 push 可使用不同 URL。移除远程不会删除已抓取的对象。

# HISTORY

git remote 是 **Git** 用于管理远程仓库连接的核心命令，而远程连接正是分布式版本控制的关键。

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

[git-fetch](/man/git-fetch)(1), [git-push](/man/git-push)(1), [git-clone](/man/git-clone)(1)
