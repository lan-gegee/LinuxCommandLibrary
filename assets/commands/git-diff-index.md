# TAGLINE

比较树对象与工作树或索引

# TLDR

**比较索引与提交**

```git diff-index HEAD```

**比较工作树与提交**

```git diff-index [commit]```

**检查是否存在差异**

```git diff-index --quiet HEAD```

**原始格式输出**

```git diff-index --raw HEAD```

# SYNOPSIS

**git** **diff-index** [_options_] _tree-ish_ [_files_...]

# PARAMETERS

**--cached**
> 只比较树对象与索引，而不比较工作树。

**-m**
> 将未检出的文件（存在于索引中但工作树缺失）视为已修改而非已删除。

**--merge-base**
> 使用 _tree-ish_ 与 HEAD 的合并基准作为比较起点。

**--raw**
> 原始 diff 输出（该命令的默认格式）。

**--quiet**
> 有差异时以 1 退出。

**--name-only**
> 只显示文件名。

**--name-status**
> 显示文件名和状态。

# DESCRIPTION

**git diff-index** 将一个树对象与工作树或索引进行比较，是一个底层（plumbing）命令，git diff 在进行提交比较时会在内部使用它。它接受一个 tree-ish（提交、分支、标签或树对象），并将其与索引（使用 --cached 时）或工作树进行比较。

该工具特别适用于需要检测自特定提交以来文件是否发生变化的自动化场景，例如在 CI/CD 流水线中检查未提交的改动，或在脚本中验证工作目录是否干净。其 --quiet 选项支持对改动做简单的布尔判断，而无需处理完整的 diff 输出。

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

[git-diff](/man/git-diff)(1), [git-diff-tree](/man/git-diff-tree)(1)
