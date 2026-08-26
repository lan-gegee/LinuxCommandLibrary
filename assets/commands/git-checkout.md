# TAGLINE

切换分支或恢复工作区文件

# TLDR

**切换到分支**

```git checkout [branch-name]```

**创建并切换到分支**

```git checkout -b [new-branch]```

**恢复文件**

```git checkout -- [file.txt]```

**检出特定提交**

```git checkout [commit-hash]```

**从远程检出**

```git checkout -t origin/[branch]```

# SYNOPSIS

**git checkout** [_options_] _branch_|_commit_|_file_

# PARAMETERS

_BRANCH_
> 要切换到的分支。

**-b** _BRANCH_
> 创建并切换到新分支。

**-t**, **--track**
> 为远程分支设置跟踪。

**--** _FILE_
> 从索引恢复文件。

**-f**, **--force**
> 强制切换，丢弃更改。

**-d**, **--detach**
> 让 HEAD 分离到指定提交，而不是更新某个分支。

**-p**, **--patch**
> 交互式选择要从索引或树中恢复的代码块。

**-m**, **--merge**
> 在当前分支、本地更改和新分支之间执行三方合并。

**--orphan** _BRANCH_
> 创建孤儿分支。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git checkout** 用于切换分支或恢复文件。它会将工作区更新为与指定的分支、提交或历史中的文件版本一致。

该命令有多种用途：切换分支、用 **-b** 创建分支、用 **--** 恢复文件，以及分离 HEAD 操作。自 **Git 2.23** 起，官方建议改用 **git switch** 切换分支、用 **git restore** 恢复文件，两者职责划分更清晰。

尽管有更新的替代命令，git checkout 因其多功能性仍被广泛使用，深深嵌入现有的工作流、文档和脚本之中。

# CAVEATS

配合 -f 使用时未提交的更改可能丢失。分离 HEAD 状态需谨慎操作。为求语义清晰可考虑使用 git switch/restore。

# HISTORY

git checkout 是 **Git** 的原始命令之一，集多种操作于一身。**Git 2.23** 引入了职责更清晰的 git switch 和 git restore 作为替代。

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

[git-switch](/man/git-switch)(1), [git-restore](/man/git-restore)(1), [git-branch](/man/git-branch)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-checkout)```

<!-- verified: 2026-07-17 -->
