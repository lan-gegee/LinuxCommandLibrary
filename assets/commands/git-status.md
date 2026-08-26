# TAGLINE

显示工作树状态

# TLDR

**显示工作树状态**

```git status```

**短格式输出**

```git status -s```

**显示带分支信息的短格式**

```git status -sb```

**显示被忽略的文件**

```git status --ignored```

供脚本使用的**机器可读输出**

```git status --porcelain```

**显示未跟踪的文件**

```git status -u```

**显示已暂存改动的详细差异**

```git status -v```

**显示指定路径的状态**

```git status [path/to/file_or_directory]```

# SYNOPSIS

**git** **status** [_options_] [_--_] [_paths_...]

# PARAMETERS

**-s**, **--short**
> 短格式输出，使用两列状态码（XY）。

**-b**, **--branch**
> 在短格式中显示分支和跟踪信息。

**--porcelain**[**=v1**|**v2**]
> 机器可读格式。版本 2 包含更多细节。

**-u**[_mode_], **--untracked-files**[**=**_mode_]
> 显示未跟踪的文件。模式可为：no、normal（默认）、all。

**--ignored**[**=**_mode_]
> 显示被忽略的文件。模式可为：traditional、no、matching。

**-v**, **--verbose**
> 显示已暂存的差异。使用 **-vv** 可同时显示未暂存的差异。

**--ahead-behind**
> 显示相对于上游分支的超前/落后计数。

**--no-ahead-behind**
> 不显示超前/落后计数（对大型仓库更快）。

**--long**
> 长格式输出（默认）。

**--column**[**=**_options_]
> 以多列形式显示未跟踪文件。

**-z**
> 条目以 NUL 而不是换行符结尾（便于脚本处理）。

**--renames**, **--no-renames**
> 启用或禁用重命名检测。

# DESCRIPTION

**git status** 显示工作树和暂存区的状态。它会展示哪些改动已暂存、哪些未暂存，以及哪些文件未被 Git 跟踪。

在短格式（**-s**）下，每个文件都带有一个两字符状态码：第一列表示索引（暂存区）状态，第二列表示工作树状态。常见的代码包括 **M**（修改）、**A**（新增）、**D**（删除）、**R**（重命名）、**?**（未跟踪）和 **!**（忽略）。

**--porcelain** 格式提供稳定、机器可读的输出，适合脚本处理；默认的长格式则面向人类阅读。需要更丰富的机器可读输出（含重命名和复制信息）时，可使用 **--porcelain=v2**。

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

[git-diff](/man/git-diff)(1), [git-add](/man/git-add)(1), [git-commit](/man/git-commit)(1), [git-stash](/man/git-stash)(1)
