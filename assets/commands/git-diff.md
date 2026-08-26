# TAGLINE

显示提交与文件之间的差异

# TLDR

**显示未暂存的改动**

```git diff```

**显示已暂存的改动**

```git diff --staged```

**分支之间的差异**

```git diff [branch1]..[branch2]```

**指定文件的差异**

```git diff [file.txt]```

**显示词级别的差异**

```git diff --word-diff```

**显示统计摘要**

```git diff --stat```

**提交之间的差异**

```git diff [commit1] [commit2]```

**与合并基准比较差异**（分支自分叉以来的改动）

```git diff [main]...[feature-branch]```

# SYNOPSIS

**git diff** [_options_] [_commit_] [**--**] [_path_...]

# PARAMETERS

**--staged**, **--cached**
> 将已暂存的改动与上一次提交进行比较。

**--stat**
> 显示 diffstat 摘要。

**--word-diff**
> 显示词级别的改动。

**--color-words**
> 带颜色的词级差异。

**--name-only**
> 只显示被更改的文件名。

**--name-status**
> 显示文件名和更改状态。

**-U** _n_, **--unified** _n_
> 上下文行数。

**--no-index**
> 比较仓库之外的文件。

**--diff-filter** _filter_
> 按更改类型过滤（A、D、M、R）。

**-b**, **--ignore-space-change**
> 忽略空白字符的变化。

**-w**, **--ignore-all-space**
> 忽略所有空白字符。

**-M**, **--find-renames**
> 检测并报告重命名的文件。

**-C**, **--find-copies**
> 检测并报告复制的文件。

# DESCRIPTION

**git diff** 显示提交、分支、工作目录和暂存区之间的差异。它对于在提交前审查改动以及了解版本之间发生了什么变化至关重要。

默认情况下，它显示未暂存的改动（工作目录与索引的比较）。使用 --staged 时，它显示将要提交的内容。给定两个提交或分支时，它会显示两者之间的所有改动。

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

[git](/man/git)(1), [git-log](/man/git-log)(1), [diff](/man/diff)(1), [vimdiff](/man/vimdiff)(1)
