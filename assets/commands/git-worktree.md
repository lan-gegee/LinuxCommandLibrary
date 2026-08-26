# TAGLINE

管理一个仓库的多个工作树

# TLDR

**添加工作树**

```git worktree add [../feature-branch] [branch-name]```

**为新分支添加工作树**

```git worktree add -b [new-branch] [path]```

**列出工作树**

```git worktree list```

**锁定一个工作树**（例如位于可移动介质上时）

```git worktree lock [path] --reason "[reason]"```

**移动一个工作树**

```git worktree move [path] [new-path]```

**移除工作树**

```git worktree remove [path]```

**清理失效的工作树**

```git worktree prune```

# SYNOPSIS

**git worktree** _command_ [_options_]

# PARAMETERS

**add** _PATH_ [_COMMIT-ISH_]
> 添加一个新的工作树。若未给出 commit-ish，则以路径的最后一个组件为名创建新分支。

**list**
> 列出工作树，每行一个。

**lock** _WORKTREE_
> 防止某个工作树被清理、移动或删除。

**unlock** _WORKTREE_
> 解锁一个工作树。

**move** _WORKTREE_ _NEW-PATH_
> 将工作树移动到新位置。

**remove** _WORKTREE_
> 移除工作树，前提是它是干净的（没有未跟踪或已修改的文件）。

**prune**
> 删除不再存在的工作树的管理信息文件。

**repair** [_PATH_...]
> 在工作树或主仓库被手动移动后，修复其管理信息文件。

**-b** _BRANCH_, **-B** _BRANCH_
> 添加工作树时创建（配合 **-B** 则为重置）新分支。

**-d**, **--detach**
> 在新工作树中使 HEAD 处于分离状态，而不是检出分支。

**--lock**
> 在 `add` 之后立即保持新工作树处于锁定状态。

**--reason** _STRING_
> 随 **lock** 一起记录的说明。

**-f**, **--force**
> 覆盖安全检查（例如允许对含未跟踪文件的工作树执行 **remove**，或在分支已被检出时执行 **add**）。

**-n**, **--dry-run**
> 报告 **prune** 会删除哪些内容，但不实际删除。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git worktree** 管理挂接到同一个仓库的多个工作树。每个工作树可以检出不同的分支，从而无需 stash 或切换分支即可并行工作。

各工作树共享同一份仓库数据，但拥有各自独立的工作目录。这适用于在功能分支开发期间修复 bug，或者在一个分支上编辑的同时在另一个分支上运行测试等场景。

# CAVEATS

同一个分支不能同时检出到两个工作树。各工作树共享大部分引用（分支、标签），但 `HEAD` 和少数其他引用是按工作树隔离的。移除工作树不会删除其分支。如果工作树目录是通过手动删除而非 `remove` 移除的，请运行 `git worktree prune`（若是主工作树或仓库本身被移动了则运行 `repair`）来清理失效的元数据。

# HISTORY

git worktree 在 **Git 2.5**（2015 年）中加入，使得单个仓库克隆可以派生多个工作目录。后续版本加入了 **move**、**lock** 和 **repair** 子命令，以改进对可移动存储和网络存储上工作树的支持。

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

[git-checkout](/man/git-checkout)(1), [git-branch](/man/git-branch)(1)

# RESOURCES

```[Documentation](https://git-scm.com/docs/git-worktree)```

<!-- verified: 2026-07-17 -->
