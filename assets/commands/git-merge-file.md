# TAGLINE

三方文件合并

# TLDR

**对文件进行三方合并**

```git merge-file [current] [base] [other]```

**以 diff3 风格合并**

```git merge-file --diff3 [current] [base] [other]```

**输出到标准输出**

```git merge-file -p [current] [base] [other]```

**安静模式**

```git merge-file -q [current] [base] [other]```

# SYNOPSIS

**git merge-file** [_options_] _current_ _base_ _other_

# PARAMETERS

_CURRENT_
> 当前版本的文件。

_BASE_
> 共同祖先文件。

_OTHER_
> 要合并的另一版本。

**-p**, **--stdout**
> 输出到标准输出。

**--diff3**
> 冲突中包含 base 版本。

**-q**, **--quiet**
> 抑制警告。

**--ours**
> 解决冲突时采用 "current" 版本。

**--theirs**
> 解决冲突时采用 "other" 版本。

**--union**
> 保留每个冲突的双方（追加而非标记）。

**-L** _label_
> 为某个文件提供标签（最多可传三次，分别对应 current/base/other）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git merge-file** 对单个文件执行三方合并。给定当前版本、共同祖先和另一版本，它生成合并结果，并在无法自动解决的位置留下冲突标记。

该命令在 Git 常规合并工作流之外操作文件，因此适合自定义合并场景或独立合并文件。第一个文件会被合并结果就地修改，退出码指示是否发生了冲突。

# CAVEATS

底层（plumbing）命令。就地修改第一个文件。退出码指示是否存在冲突。

# HISTORY

git merge-file 是 **Git** 的核心底层命令，实现了 git merge 内部使用的三方合并算法。

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

[git-merge](/man/git-merge)(1), [diff3](/man/diff3)(1)
