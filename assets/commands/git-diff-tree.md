# TAGLINE

比较树对象的内容

# TLDR

**比较两棵树**

```git diff-tree [tree1] [tree2]```

**显示提交中的改动**

```git diff-tree -p [commit]```

**显示被更改的文件**

```git diff-tree --name-only [commit]```

**原始格式输出**

```git diff-tree --raw [commit]```

# SYNOPSIS

**git** **diff-tree** [_options_] _tree-ish_ [_tree-ish_] [_files_...]

# PARAMETERS

**-r**
> 递归进入子树。

**-p**, **--patch**
> 生成补丁。

**--raw**
> 原始 diff 格式。

**--name-only**
> 只显示文件名。

**--name-status**
> 显示状态和名称。

**-s**
> 抑制 diff 输出。

**--stdin**
> 从 stdin 读取提交，每行一个；每个提交与其父提交进行比较。

**--root**
> 将初始提交作为针对空树的巨大差异包含进来（仅在与 **--stdin** 或单个 _tree-ish_ 一起使用时有意义）。

**-c**, **--cc**
> 为合并提交显示组合差异，而不是只列出被更改的文件。

# DESCRIPTION

**git diff-tree** 比较通过两个树对象找到的 blob 的内容与模式，提供对 Git 内部树比较机制的底层访问。这个 plumbing 命令构成了检查 Git 对象数据库中提交、分支或任何树状结构之间差异的基础。

该命令接受一个或两个 tree-ish 参数，并以多种格式输出差异。它可以通过 stdin 处理提交，从而高效地批量处理历史。虽然在日常 Git 使用中很少直接用到，但它支撑着许多更高层的操作，对脚本和自定义 diff 工具而言不可或缺。

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

[git-diff](/man/git-diff)(1), [git-diff-index](/man/git-diff-index)(1)
