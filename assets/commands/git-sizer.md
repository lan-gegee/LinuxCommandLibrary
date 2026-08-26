# TAGLINE

计算并报告仓库的体积指标

# TLDR

**分析仓库体积**

```git-sizer```

**详细输出**，显示所有统计信息

```git-sizer -v```

用于机器处理的 **JSON 输出**

```git-sizer --json```

**仅显示关键**统计信息

```git-sizer --critical```

# SYNOPSIS

**git-sizer** [_options_]

# PARAMETERS

**-v**, **--verbose**
> 报告全部统计信息，等价于 --threshold=0

**--json**
> JSON 输出格式

**--json-version** _n_
> JSON 格式版本（1 或 2）

**--threshold** _n_
> 要报告的最低关注级别（0=全部，1=默认，30=仅关键项）

**--critical**
> 只报告关键统计信息（等价于 --threshold=30）

**--names** _mode_
> 显示大对象的名称（none、hash 或 full）

**--no-progress**
> 抑制进度输出

**--show-refs**
> 列出正在处理的引用

**--version**
> 显示版本信息

# DESCRIPTION

**git-sizer** 为 Git 仓库计算多项体积指标，找出可能导致性能问题的因素，例如过大的文件、过深的历史或过宽的目录树。

该工具以星号（*）标示各项指标的关注级别，帮助维护者判断仓库结构是否会在克隆、拉取或其他常规 Git 操作中引发问题。必须在 Git 仓库内运行。

# INSTALL

```apt: sudo apt install git-sizer```

```pacman: sudo pacman -S git-sizer```

```apk: sudo apk add git-sizer```

```brew: brew install git-sizer```

```nix: nix profile install nixpkgs#git-sizer```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-filter-repo](/man/git-filter-repo)(1), [git-gc](/man/git-gc)(1)
