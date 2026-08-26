# TAGLINE

应用现有提交中的更改

# TLDR

**将一个提交应用到当前分支**

```git cherry-pick [commit]```

**拣选多个提交**

```git cherry-pick [commit1] [commit2]```

**拣选一个开区间范围（不含起点，含终点）**

```git cherry-pick [start]..[end]```

**拣选一个闭区间范围（起点和终点都包含）**

```git cherry-pick [start]^..[end]```

**只应用更改而不创建提交**

```git cherry-pick -n [commit]```

**解决冲突后继续**

```git cherry-pick --continue```

**中止并回到拣选前的状态**

```git cherry-pick --abort```

**在提交信息末尾追加 "cherry picked from" 说明**

```git cherry-pick -x [commit]```

# SYNOPSIS

**git** **cherry-pick** [_options_] _commit_...

**git** **cherry-pick** (**--continue** | **--skip** | **--abort** | **--quit**)

# PARAMETERS

**-e**, **--edit**
> 在创建提交前编辑提交信息。

**-n**, **--no-commit**
> 将更改应用到工作区和索引，但不创建提交。

**-x**
> 在原提交信息后追加一行 "(cherry picked from commit ...)"。便于追踪公共分支上的向后移植。

**-s**, **--signoff**
> 在提交信息中添加 `Signed-off-by` 尾注。

**-m** _parent-number_, **--mainline** _parent-number_
> 拣选合并提交时，指定以哪个父提交（从 1 开始编号）作为主线。

**--ff**
> 如果 HEAD 与被拣选提交的父提交相同，则直接快进 HEAD 而不创建新提交。

**--continue**
> 解决冲突后继续操作。

**--skip**
> 跳过当前提交并继续处理序列中的其余提交。

**--abort**
> 取消操作并返回到拣选前的状态。

**--quit**
> 忘记当前操作但不恢复 HEAD，保持工作区现状。

# DESCRIPTION

**git cherry-pick** 将现有提交所引入的更改应用到当前分支上，创建内容相同但谱系不同的新提交。这样可以选择性地整合特定更改，而无需合并整个分支。

该命令对于将缺陷修复向后移植到维护分支、从开发分支引入特定功能，以及从被放弃的分支找回提交都必不可少。每个被拣选的提交都会获得一个新的 SHA-1 哈希，反映其新的父提交。

使用 `..` 指定范围时不包含起始提交。若要包含两端，请使用 `start^..end`。当更改无法干净地套用到目标分支的上下文时，拣选会遇到冲突。操作可以暂停以便手动解决冲突，然后用 `--continue` 继续。

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

[git-rebase](/man/git-rebase)(1), [git-revert](/man/git-revert)(1), [git-cherry](/man/git-cherry)(1)
