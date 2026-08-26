# TAGLINE

移动或重命名已跟踪的文件

# TLDR

**重命名文件**

```git mv [old-name.txt] [new-name.txt]```

**移动文件到目录**

```git mv [file.txt] [directory/]```

**强制覆盖**

```git mv -f [source] [destination]```

**移动多个文件到目录**

```git mv [file1.txt] [file2.txt] [directory/]```

**试运行**

```git mv -n [source] [destination]```

# SYNOPSIS

**git mv** [_options_] _source_ _destination_
**git mv** [_options_] _source_... _destination-directory_

# PARAMETERS

_SOURCE_
> 要移动的文件或目录。

_DESTINATION_
> 目标路径或目录。

**-f**, **--force**
> 即使目标已存在也强制移动/重命名。

**-k**
> 跳过会导致错误条件的移动或重命名操作。

**-n**, **--dry-run**
> 显示将要执行的操作。

**-v**, **--verbose**
> 报告被移动的文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git mv** 在更新 Git 索引的同时移动或重命名文件和目录。它等价于先用 `mv` 移动文件，再用 `git rm` 删除旧路径，最后用 `git add` 添加新路径。

使用该命令可以确保重命名被正确暂存以备下次提交。虽然 Git 可以通过内容分析自动检测重命名，但使用 `git mv` 能让意图更明确，并一步完成索引更新。

# CAVEATS

它实际上只是一个便捷封装。Git 反正能检测出重命名。历史跟随的是内容而非命令。

# HISTORY

git mv 是 **Git** 的核心命令，提供显式的重命名/移动跟踪；不过 Git 本身也能通过内容分析自动检测重命名。

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

[git-rm](/man/git-rm)(1), [git-add](/man/git-add)(1), [mv](/man/mv)(1)
