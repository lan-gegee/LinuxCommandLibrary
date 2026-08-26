# TAGLINE

查找合并所需的共同祖先提交

# TLDR

**查找两个分支的最优共同祖先**

```git merge-base [branch1] [branch2]```

**查找所有共同祖先**（不只是最优的那个）

```git merge-base --all [branch1] [branch2]```

**检查某个提交是否是另一个提交的祖先**（脚本中很有用）

```git merge-base --is-ancestor [commit1] [commit2]```

**查找主题分支从上游分叉的分叉点**

```git merge-base --fork-point [upstream_ref] [branch]```

**为多个分支查找 octopus 合并基**

```git merge-base --octopus [branch1] [branch2] [branch3]```

**列出彼此不可达的独立提交**

```git merge-base --independent [commit1] [commit2] [commit3]```

# SYNOPSIS

**git** **merge-base** [**-a** | **--all**] _commit_ _commit_...
**git** **merge-base** [**-a** | **--all**] **--octopus** _commit_...
**git** **merge-base** **--is-ancestor** _commit_ _commit_
**git** **merge-base** **--independent** _commit_...
**git** **merge-base** **--fork-point** _ref_ [_commit_]

# PARAMETERS

**-a**, **--all**
> 输出这些提交的所有合并基，而不只是一个。

**--octopus**
> 计算所有给定提交的最优共同祖先，为 n 路合并做准备。

**--independent**
> 不打印合并基，而是打印与全部给定提交拥有相同祖先的最小子集。列出无法从其他任何提交到达的提交。

**--is-ancestor**
> 检查第一个提交是否是第二个提交的祖先。为真时以状态码 0 退出，否则为 1。错误通过非 0 且非 1 的状态码表示。

**--fork-point**
> 查找一个分支从另一引用分叉的位置。它会参考该引用的 reflog，以检测分支更早版本上的分叉（在历史被改写后很有用）。

# DESCRIPTION

**git merge-base** 查找两个提交之间用于三方合并的最优共同祖先。若某个共同祖先不是任何其他共同祖先的祖先，它就是"最优的"。如果某个共同祖先是所有最优共同祖先的祖先，那它就是一个"合并基"（merge base）。

`--fork-point` 选项查找分支从上游分支分叉的位置，会考虑 reflog 以应对历史改写的情况（例如上游 rebase 之后）。`--is-ancestor` 选项检查一个提交是否是另一个提交的祖先，在脚本中用于判断提交关系很有用。`--independent` 选项将一组提交过滤为仅剩无法从其他提交到达的那些。对于 octopus 合并（合并两个以上分支），`--octopus` 选项同时计算多个提交的共同基。

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

[git-merge](/man/git-merge)(1), [git-rebase](/man/git-rebase)(1), [git-log](/man/git-log)(1), [git-branch](/man/git-branch)(1), [git-show-branch](/man/git-show-branch)(1)
