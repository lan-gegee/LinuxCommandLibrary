# TAGLINE

显示被跟踪数据文件的更改

# TLDR

**显示自上次提交以来的更改**

```dvc diff```

**与特定修订版本比较**

```dvc diff [HEAD~1]```

**比较两个修订版本**

```dvc diff [rev1] [rev2]```

**显示详细输出**

```dvc diff --json```

**比较特定目标**

```dvc diff [target.dvc]```

# SYNOPSIS

**dvc** **diff** [_options_] [_a_rev_] [_b_rev_]

# PARAMETERS

**--json**
> 以 JSON 格式输出。

**--show-hash**
> 显示文件哈希值。

**--md**
> 以 markdown 格式输出。

# DESCRIPTION

**dvc diff** 比较 Git 提交之间 DVC 跟踪的数据，展示哪些数据发生了变化，就像 git diff 展示代码更改一样。它通过比较不同提交中 .dvc 元数据文件存储的哈希值，报告新增、删除和修改的文件。

这使数据版本控制工作流成为可能：你可以查看实验之间数据集的变化、跨分支比较模型检查点，或在合并前审查数据的修改。输出会显示文件路径及其哈希值变化，清楚地表明哪些数据文件有了新版本。

该工具接受 Git 修订版说明符（HEAD、分支名、提交哈希），可比较历史中的任意两个时间点。--json 输出格式适合程序化分析，而 --md 会生成 markdown 表格，适合用于文档或拉取请求描述。

# INSTALL

```brew: brew install dvc```

```nix: nix profile install nixpkgs#dvc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dvc](/man/dvc)(1), [git-diff](/man/git-diff)(1)
