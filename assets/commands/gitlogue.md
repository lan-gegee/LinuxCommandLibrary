# TAGLINE

电影感动画回放 Git 提交历史

# TLDR

**回放**当前仓库的历史

```gitlogue```

**回放**一段提交范围

```gitlogue --commit [HEAD~10..HEAD]```

**回放**特定提交

```gitlogue --commit [abc123]```

# SYNOPSIS

**gitlogue** [*options*]

# DESCRIPTION

**gitlogue** 将 Git 历史变成一段终端动画故事——在回放提交时呈现打字效果、语法高亮和文件树切换。适合演示、新人入门以及可视化代码库的演进过程。可通过安装脚本、Homebrew、Cargo 或 Nix 安装。

# PARAMETERS

**--commit** *rev*|*range*

> 从某个提交开始，或动画化一个范围。

其他标志控制速度和主题——参见 **gitlogue --help**。

# CAVEATS

庞大的历史需要很长时间才能动画完成。需要 git 仓库和一个功能完善的终端。

# INSTALL

```pacman: sudo pacman -S gitlogue```

```brew: brew install gitlogue```

```nix: nix profile install nixpkgs#gitlogue```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-log](/man/git-log)(1), [gource](/man/gource)(1), [git-blame](/man/git-blame)(1)

# RESOURCES

```[Source code](https://github.com/unhappychoice/gitlogue)```

<!-- verified: 2026-07-19 -->
