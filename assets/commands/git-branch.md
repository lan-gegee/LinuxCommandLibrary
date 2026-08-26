# TAGLINE

列出、创建、重命名和删除分支

# TLDR

**列出所有本地分支**

```git branch```

**列出包括远程在内的所有分支**

```git branch -a```

**创建新分支**

```git branch [branch_name]```

**创建并切换**到新分支

```git branch [branch_name] && git checkout [branch_name]```

**删除本地分支**

```git branch -d [branch_name]```

**强制删除**含有未合并更改的分支

```git branch -D [branch_name]```

**重命名当前分支**

```git branch -m [new_name]```

**设置上游跟踪**分支

```git branch -u [origin/branch_name]```

**显示分支及其最近提交**

```git branch -v```

# SYNOPSIS

**git branch** [_OPTIONS_] [_BRANCH-NAME_] [_START-POINT_]

# PARAMETERS

**-a**, **--all**
> 同时列出本地和远程跟踪分支。

**-r**, **--remotes**
> 仅列出远程跟踪分支。

**-d**, **--delete**
> 删除分支（必须已完全合并）。

**-D**
> 无论合并状态如何都强制删除分支。

**-m**, **--move**
> 重命名分支。

**-M**
> 即使目标名称已存在也强制重命名。

**-c**, **--copy**
> 复制分支。

**-u**, **--set-upstream-to**=_UPSTREAM_
> 设置上游跟踪分支。

**--unset-upstream**
> 移除上游跟踪信息。

**-v**, **--verbose**
> 显示每个分支的 SHA1 和提交主题。

**--merged**
> 列出已合并入当前分支的分支。

**--no-merged**
> 列出尚未合并入当前分支的分支。

**--contains** _COMMIT_
> 列出包含指定提交的分支。

**--show-current**
> 输出当前分支的名称（分离 HEAD 状态下不输出任何内容）。

**--sort** _KEY_
> 按键排序输出（如 **-committerdate**）；加 **-** 前缀表示降序。

**-f**, **--force**
> 将分支重置为起始点，即使该分支已存在；与 **-d** 或 **-m** 组合使用时表示强制删除/重命名。

**--points-at** _OBJECT_
> 列出指向指定对象的分支。

# DESCRIPTION

**git branch** 用于列出、创建、重命名和删除分支。不带参数时，它会列出现有的本地分支，并用星号标记当前分支。

分支是指向提交的轻量级指针，支持并行的开发工作流。创建分支并不会切换到该分支；请使用 **git checkout** 或 **git switch** 来切换分支。

远程跟踪分支（origin/main 等）是对远程仓库上分支状态的只读引用，由 **git fetch** 更新。

# CAVEATS

如果分支有未合并的更改，使用 **-d** 删除会失败。可用 **-D** 强制删除，但未合并的工作将会丢失（不过这些提交暂时仍可通过 reflog 找回）。无法删除当前检出的分支。

# HISTORY

自 Linus Torvalds 于 **2005 年** 创建 Git 以来，分支一直是其核心特性。Git 的轻量级分支模型——分支只是指向提交的指针而非完整的目录副本——具有革命性，催生了 GitFlow 和 GitHub Flow 等工作流。

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

[git-checkout](/man/git-checkout)(1), [git-switch](/man/git-switch)(1), [git-merge](/man/git-merge)(1), [git-fetch](/man/git-fetch)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-branch)```

<!-- verified: 2026-07-17 -->
