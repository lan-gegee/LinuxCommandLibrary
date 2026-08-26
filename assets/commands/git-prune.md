# TAGLINE

从对象数据库中清除不可达的对象

# TLDR

**清除不可达的**松散对象

```git prune```

**试运行**查看将被移除的内容

```git prune -n```

**详细**输出

```git prune -v```

**只清除早于指定时间的对象**

```git prune --expire=2.weeks.ago```

**立即清除所有仅当前不可达的内容**（无宽限期）

```git prune --expire=now```

**保留可从一个额外 head 到达的对象**

```git prune -- [refs/heads/topic]```

# SYNOPSIS

**git prune** [**-n**] [**-v**] [**--progress**] [**--expire** _time_] [**--**] [_heads_...]

# PARAMETERS

**-n**, **--dry-run**
> 不移除任何内容，只报告将会移除什么。

**-v**, **--verbose**
> 报告所有被移除的对象。

**--progress**
> 清除过程中显示进度。

**--expire** _time_
> 只清除早于 _time_ 的松散对象（例如 `now`、`2.weeks.ago`）。

**--**
> 将其余参数视为 heads 而非选项。

_heads_
> 除所有已打包引用之外，额外需要保持其可达对象不被清除的引用。

# DESCRIPTION

**git prune** 从 `.git/objects` 中移除无法从任何引用到达的松散对象。当提交被 amend、被 rebase 丢弃、分支被删除或 stash 被丢弃时，对象就会变得不可达，在对象数据库中留下悬空内容。

该命令通常经由 **git gc** 间接调用，后者会设置合适的 **--expire** 时间（即 `gc.pruneExpire` 配置，默认 `2.weeks.ago`），以便出于安全考虑暂时保留非常新的对象。这个过期宽限期用于保护并发操作以及 reflog 尚未开始引用的新建对象。

注意 **git prune** 只处理松散对象。已经位于包文件内的不可达对象由 **git repack -A** 移除。

# CAVEATS

激进的过期设置（`--expire=now`)可能删除仍可用于通过 reflog 恢复的对象，或其他 git 进程正在写入的对象。同一仓库中还有其他 git 命令运行时，不要手动执行 prune。要清除 `.git/worktrees` 下过期的工作区元数据，请改用 **git worktree prune**。

# HISTORY

**git prune** 是 Git 最初发布时就自带的底层（plumbing）命令之一。它的日常角色已逐渐转变为 **git gc** 的内部步骤，但在大型改写操作之后进行显式清理时仍然有用。

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

[git-gc](/man/git-gc)(1), [git-fsck](/man/git-fsck)(1), [git-reflog](/man/git-reflog)(1)
