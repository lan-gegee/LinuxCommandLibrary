# TAGLINE

以自定义格式输出每个引用的信息

# TLDR

**列出所有引用**

```git for-each-ref```

**列出分支**

```git for-each-ref refs/heads```

**列出标签**

```git for-each-ref refs/tags```

**自定义格式**

```git for-each-ref --format='%(refname:short) %(objectname:short)' refs/heads```

**按日期排序**

```git for-each-ref --sort=-committerdate refs/heads```

**显示最新的 N 个引用**

```git for-each-ref --count=[10] --sort=-committerdate refs/heads```

# SYNOPSIS

**git** **for-each-ref** [_options_] [_patterns_...]

# PARAMETERS

**--format** _format_
> 使用 %(fieldname) 占位符的输出格式字符串（默认：`%(objectname) %(objecttype)\t%(refname)`）。

**--sort** _key_
> 按字段名排序；加 **-** 前缀表示降序。可重复指定，最后一个键为主键。

**--count** _n_
> 显示 _n_ 个引用后停止。

**--points-at** _object_
> 只列出指向给定对象的引用。

**--merged**[=_commit_]
> 只列出其末端可从 _commit_（默认 HEAD）到达的引用。

**--no-merged**[=_commit_]
> 只列出其末端不可从 _commit_（默认 HEAD）到达的引用。

**--contains**[=_commit_]
> 只列出包含给定提交的引用。

**--exclude** _pattern_
> 省略匹配 _pattern_ 的引用。

**--stdin**
> 从标准输入而不是参数列表读取模式列表。

**--ignore-case**
> 不区分大小写的排序与过滤。

**--shell**, **--perl**, **--python**, **--tcl**
> 以指定脚本语言的字符串字面量形式为插值后的值加引号。

# DESCRIPTION

**git for-each-ref** 是一个 plumbing 命令，以高度可定制的格式输出 Git 引用（分支、标签、远程分支）的详细信息。它是许多需要处理仓库引用的高层 Git 命令和脚本的基础。

格式字符串语法支持使用 %(fieldname) 占位符提取字段，可用字段包括 refname、objecttype、objectname、author、committer 等。排序功能支持按任意字段对引用排序，并可通过减号前缀实现反向排序。

该命令主要用于脚本和 Git 别名中，而非直接的用户交互。过滤选项（--merged、--no-merged、--points-at）为查找符合特定条件的引用提供了强大的选择机制。

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

[git-branch](/man/git-branch)(1), [git-tag](/man/git-tag)(1), [git-rev-parse](/man/git-rev-parse)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-for-each-ref)```

<!-- verified: 2026-07-17 -->
