# TAGLINE

按时间倒序列出提交对象

# TLDR

**列出所有提交**

```git rev-list HEAD```

**统计提交数量**

```git rev-list --count HEAD```

**列出范围内的提交**

```git rev-list [commit1]..[commit2]```

**按日期顺序列出**

```git rev-list --date-order HEAD```

**列出从多个引用可达的提交**

```git rev-list [branch1] [branch2] --not [main]```

**仅沿第一父提交遍历**

```git rev-list --first-parent HEAD```

# SYNOPSIS

**git** **rev-list** [_options_] _commits_... [_--_] [_paths_...]

# PARAMETERS

**--count**
> 仅显示数量。

**--max-count** _n_
> 限制输出条数。

**--since** _date_
> 某日期之后的提交。

**--until** _date_
> 某日期之前的提交。

**--author** _pattern_
> 按作者过滤。

**--first-parent**
> 仅沿第一父提交遍历。

**--ancestry-path**
> 显示祖先路径。

**--objects**
> 包含所有被引用的对象 ID（树、blob），对打包很有用。

**--all**
> 遍历 `refs/` 下的所有引用，外加 HEAD。

**--branches**[=_pattern_], **--tags**[=_pattern_], **--remotes**[=_pattern_]
> 分别遍历对应命名空间下匹配的引用。

**--no-merges**, **--merges**
> 排除或包含合并提交（等价于 `--max-parents=1` / `--min-parents=2`）。

**--min-parents** _n_, **--max-parents** _n_
> 按父提交数量过滤提交。

**--reverse**
> 按时间顺序输出提交。

**--topo-order**, **--date-order**
> 按拓扑顺序或提交日期排序输出。

**--left-right**
> 配合 `A...B` 使用时，将提交标记为 `<`（来自 A）或 `>`（来自 B）。

**--boundary**
> 包含被排除的边界提交，并以 `-` 作为前缀。

**--grep** _pattern_, **--committer** _pattern_
> 在 **--author** 之外，再按提交信息 / 提交者身份过滤。

# DESCRIPTION

**git rev-list** 按时间倒序列出提交对象。它是一个底层（plumbing）命令，用于枚举可达的提交和对象，是许多上层 Git 命令的基础。

常见用途包括统计提交数量、查找合并基（merge base），以及为其他工具构建提交范围。

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

[git-log](/man/git-log)(1), [git-rev-parse](/man/git-rev-parse)(1), [git-cherry](/man/git-cherry)(1)
