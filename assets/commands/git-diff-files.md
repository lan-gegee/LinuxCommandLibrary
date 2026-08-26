# TAGLINE

比较工作树文件与索引

# TLDR

**显示未暂存的改动**

```git diff-files```

**显示指定文件的差异**

```git diff-files [file]```

**原始格式输出**

```git diff-files --raw```

**检查是否有改动**

```git diff-files --quiet```

# SYNOPSIS

**git** **diff-files** [_options_] [_files_...]

# PARAMETERS

**--raw**
> 原始 diff 格式（默认）。

**--quiet**
> 有差异时以 1 退出，否则以 0 退出。禁用输出。

**-p**, **--patch**
> 生成补丁格式的输出。

**--stat**
> 显示 diffstat 摘要。

**--name-only**
> 只显示被更改文件的名称。

**--name-status**
> 显示被更改文件的名称和状态（新增、修改、删除）。

**-0**
> 省略未合并条目的 diff 输出，仅显示 "Unmerged"。

# DESCRIPTION

**git diff-files** 将工作树与索引（暂存区）进行比较，是一个底层（plumbing）命令，用于显示未暂存的改动。git diff 在不带参数调用时内部会使用它，它也为更高层的 diff 操作提供了基础。

该命令属于 Git 的底层 plumbing 层，专为脚本和自动化设计而非日常交互使用。它可以生成多种输出格式，包括原始 diff 数据、补丁格式或简单的文件列表，因此适合集成到构建工具、pre-commit 钩子或自定义 Git 工作流中。

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

[git-diff](/man/git-diff)(1), [git-diff-index](/man/git-diff-index)(1), [git-diff-tree](/man/git-diff-tree)(1)
