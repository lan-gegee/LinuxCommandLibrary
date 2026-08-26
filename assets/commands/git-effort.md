# TAGLINE

显示每个文件的提交活动与开发投入

# TLDR

**显示所有文件的投入情况**

```git effort```

**显示指定目录的投入情况**

```git effort [src/]```

**只显示提交数超过 N 的文件**

```git effort --above [50]```

**显示指定文件的投入情况**

```git effort [path/to/file.js]```

# SYNOPSIS

**git effort** [_options_] [_path_]

# PARAMETERS

_PATH_
> 要分析的文件或目录路径。省略时分析整个仓库。

**--above** _N_
> 只显示提交数超过 N 的文件。有助于过滤掉低活跃度的文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git effort** 按时间维度显示文件的提交活动，通过提交频率和活跃天数展示哪些文件最受关注。输出按提交数和活跃天数对文件排序，帮助识别热点并了解代码库的维护模式。

它是 git-extras 套件的组成部分，能揭示代码库中哪些区域持续获得开发投入，可用于规划代码评审和理解项目动态。

# CAVEATS

属于 git-extras 软件包。在大型仓库上可能较慢。衡量的是提交数而非变更行数。

# HISTORY

git effort 是 **git-extras** 的组成部分，由 **TJ Holowaychuk** 创建，用于可视化开发投入的分布。

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

[git-fame](/man/git-fame)(1), [git-summary](/man/git-summary)(1), [git-extras](/man/git-extras)(1), [git-shortlog](/man/git-shortlog)(1)
