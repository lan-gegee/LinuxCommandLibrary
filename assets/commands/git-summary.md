# TAGLINE

显示带贡献统计的仓库概要

# TLDR

**显示仓库概要**，包含每位作者的提交统计

```git summary```

改为**显示基于行数的统计**

```git summary --line```

**显示指定路径的行数统计**

```git summary --line [path/to/dir]```

**按邮箱去重作者**

```git summary --dedup-by-email```

**排除合并提交**

```git summary --no-merges```

**以表格形式输出**

```git summary --output-style tabular```

# SYNOPSIS

**git** **summary** [_options_] [_path_]

# PARAMETERS

**--line**
> 显示行数统计而不是提交数。可接受一个可选路径作为过滤条件。

**--dedup-by-email**
> 按邮箱地址对作者去重。

**--no-merges**
> 从概要中排除合并提交。

**--output-style** _style_
> 输出格式：tabular 或 oneline。

# DESCRIPTION

**git summary** 输出仓库的整体概况，包括项目年龄、活跃天数、总提交数以及每位作者的贡献统计。它属于 git-extras，可以快速了解项目的活跃状况。

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

[git-log](/man/git-log)(1), [git-shortlog](/man/git-shortlog)(1), [git-extras](/man/git-extras)(1)
