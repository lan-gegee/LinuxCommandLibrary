# TAGLINE

在不触碰索引或工作区的情况下执行合并

# TLDR

**预览合并结果**（现代模式，Git 2.38+）

```git merge-tree [branch1] [branch2]```

**以显式 base 执行三方合并**（已弃用模式）

```git merge-tree [base] [branch1] [branch2]```

**检查合并冲突并显示提示信息**

```git merge-tree --write-tree --messages [branch1] [branch2]```

**检查分支能否干净地合并**（退出码 0 = 干净，1 = 有冲突）

```git merge-tree --write-tree --no-messages [branch1] [branch2]```

# SYNOPSIS

**git merge-tree** [**--write-tree**] [_options_] _branch1_ _branch2_

**git merge-tree** [**--trivial-merge**] _base_ _branch1_ _branch2_

# PARAMETERS

_BRANCH1_
> 要合并的第一个分支。

_BRANCH2_
> 要合并的第二个分支。

_BASE_
> 共同祖先提交（仅限已弃用的 trivial-merge 模式）。

**--write-tree**
> 现代模式（Git 2.38 起为默认）：自动查找合并基并写入结果树对象。通过退出码和 stdout 报告冲突。

**--trivial-merge**
> 已弃用模式：读取三棵树并输出平凡合并的结果。需要显式指定 base。

**--[no-]messages**
> 输出提示性信息，例如 "Auto-merging" 和 CONFLICT 通知。默认：存在冲突时包含。

**--name-only**
> 输出中只显示文件名，而不显示完整合并细节。

**--allow-unrelated-histories**
> 允许合并没有共同历史的分支。

**--merge-base** _commit_
> 指定合并基，而不是自动计算。使用该选项后，分支参数可以是树而非提交。与 --stdin 不兼容。

**--stdin**
> 从标准输入读取要合并的提交，每行一对。隐含 -z。

**-z**
> 使用 NUL 字符而非换行符作为行终止符（便于脚本处理）。

# DESCRIPTION

**git merge-tree** 在不触碰索引或工作区的情况下执行三方合并。它会展示合并将产生的结果，因此适合预览合并或进行脚本化的合并分析。

现代模式（Git 2.38 起为默认）会自动查找合并基、写入结果树对象并报告冲突。退出码表示成功（0）或有冲突（1）。这使它非常适合需要在修改任何文件之前检查可合并性的 CI 流水线和自动化脚本。

已弃用的 trivial-merge 模式要求显式指定 base 提交，且只能处理平凡合并。

# CAVEATS

底层（plumbing）命令，主要为脚本编写而设计。现代模式与弃用模式的输出格式不同。现代模式要求 Git 2.38 或更高版本。

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

[git-merge](/man/git-merge)(1), [git-merge-file](/man/git-merge-file)(1)
