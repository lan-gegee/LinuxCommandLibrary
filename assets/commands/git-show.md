# TAGLINE

显示提交、标签、blob 等各种 Git 对象

# TLDR

**显示最近一次提交**

```git show```

**显示指定提交**

```git show [commit-hash]```

**显示标签**

```git show [v1.0.0]```

**显示某次提交中的文件**

```git show [commit]:[file.txt]```

**仅显示统计信息**

```git show --stat```

# SYNOPSIS

**git show** [_options_] _object_

# PARAMETERS

_OBJECT_
> 要显示的提交、标签或树。

**--stat**
> 仅显示 diff 统计。

**--name-only**
> 显示变更的文件名。

**--name-status**
> 显示文件名和状态。

**--format** _FORMAT_
> 输出格式。

**-p**, **--patch**
> 显示差异（对提交而言是默认行为）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git show** 可以显示多种类型的 Git 对象。对于提交，它会显示提交信息和差异；对于标签，会显示标签附注；对于树和 blob，则直接显示其内容。

该命令把 log 和 diff 的功能结合成一个便捷的单对象查看器，是检查任意 Git 对象的首选工具。

# CAVEATS

输出因对象类型而异。大差异可能需要分页查看。二进制文件只显示为二进制。

# HISTORY

git show 是用于显示对象的核心 **Git** 命令，为检查各类 git 对象提供了统一接口。

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

[git-log](/man/git-log)(1), [git-diff](/man/git-diff)(1), [git-cat-file](/man/git-cat-file)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-show)```

<!-- verified: 2026-07-17 -->
