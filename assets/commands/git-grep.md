# TAGLINE

在被跟踪的文件中搜索模式

# TLDR

**搜索模式**

```git grep "[pattern]"```

**显示行号搜索**

```git grep -n "[pattern]"```

**不区分大小写搜索**

```git grep -i "[pattern]"```

**在指定提交中搜索**

```git grep "[pattern]" [commit]```

**只显示文件名**

```git grep -l "[pattern]"```

# SYNOPSIS

**git grep** [_options_] _pattern_ [_revision_] [_--_] [_path_]

# PARAMETERS

_PATTERN_
> 搜索模式（正则表达式）。

_REVISION_
> 要搜索的提交/分支。

**-n**, **--line-number**
> 显示行号。

**-i**, **--ignore-case**
> 不区分大小写。

**-l**, **--files-with-matches**
> 只显示文件名。

**-c**, **--count**
> 显示匹配次数。

**-w**, **--word-regexp**
> 匹配整个单词。

**-v**, **--invert-match**
> 选择不匹配的行。

**-A** _n_, **-B** _n_, **-C** _n_
> 在每个匹配之后、之前或前后各显示 _n_ 行上下文。

**-E**, **--extended-regexp**
> 使用扩展（ERE）正则表达式，而非默认的基础（BRE）正则表达式。

**-F**, **--fixed-strings**
> 将模式视为字面字符串，而不是正则表达式。

**--cached**
> 搜索索引而不是工作树。

**--untracked**
> 同时搜索未跟踪的文件。

**-e** _PATTERN_
> 模式参数；可将多个 **-e** 与 **--and**/**--or**/**--not** 组合使用。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git grep** 在被跟踪的文件中搜索模式，专门针对 Git 仓库进行了优化。与普通的 grep 不同，它会忽略未跟踪的文件，并且可以搜索仓库历史中的任意提交。

由于它使用 Git 的索引而不是直接扫描文件系统，因此在大型仓库上速度明显更快。它支持与 grep 相同的正则表达式语法，并与 Git 的修订版本和路径规范无缝集成。

# CAVEATS

只搜索被跟踪的文件。正则表达式语法与 grep 有所不同。默认跳过二进制文件。

# HISTORY

git grep 是 **Git** 的核心命令，提供理解 git 对象模型和历史的优化搜索能力。

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

[grep](/man/grep)(1), [git-log](/man/git-log)(1), [rg](/man/rg)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-grep)```

<!-- verified: 2026-07-17 -->
