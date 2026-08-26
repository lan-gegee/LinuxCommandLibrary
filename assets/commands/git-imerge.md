# TAGLINE

增量式、类似 bisect 的合并

# TLDR

**开始某个分支的增量合并**

```git imerge start --name=[merge-name] [branch]```

**开始向当前分支的增量变基**

```git imerge rebase [branch]```

**修复冲突后继续解决**

```git imerge continue```

**显示可视化的合并**进度图

```git imerge diagram```

**所有冲突解决后完成合并**

```git imerge finish```

**列出所有进行中的**增量合并

```git imerge list```

**中止并移除**增量合并

```git imerge remove```

# SYNOPSIS

**git imerge** _command_ [_options_]

# PARAMETERS

**start**
> 开始增量合并。

**merge**
> 开始增量合并（start --goal merge 的简写）。

**rebase**
> 开始增量变基（start --goal rebase 的简写）。

**continue**
> 继续解决冲突。

**finish**
> 完成增量合并。

**remove**
> 中止并移除增量合并状态。

**diagram**
> 显示可视化的合并状态网格。

**list**
> 列出所有进行中的增量合并。

**autofill**
> 尝试自动填充所有合并块。

**simplify**
> 在完成后简化合并历史。

**init**
> 从现有合并状态初始化一个 imerge。

**record**
> 记录手动完成的合并的结果。

**drop**
> 从合并中丢弃一个提交。

**revert**
> 在合并中还原一个提交。

**--name** _NAME_
> 增量合并的名称。

**--goal** _GOAL_
> 合并目标：merge、rebase、rebase-with-history、border、border-with-history。

**--first-parent**
> 只处理 first-parent 历史。

**--force**
> 即使已有进行中的合并也强制开始。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git imerge** 执行增量式的、类似 bisect 的合并。它不是一次性进行包含大量冲突的大合并，而是逐个提交地合并，使冲突解决更易于管理，并帮助精确定位是哪些提交引发了冲突。

该工具通过 diagram 命令以可视化方式跟踪合并进度，并允许独立解决各个冲突。这种方式对于长期分叉的分支之间难以处理的合并尤其有价值。

# CAVEATS

需要单独安装。比简单合并更复杂。最适合用于困难的合并场景。

# HISTORY

git imerge 由 **Michael Haggerty** 创建，通过把庞大且冲突繁多的合并拆分为更小的片段来化解其痛点。

# INSTALL

```dnf: sudo dnf install git-imerge```

```brew: brew install git-imerge```

```nix: nix profile install nixpkgs#git-imerge```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-merge](/man/git-merge)(1), [git-rebase](/man/git-rebase)(1)
