# TAGLINE

内部单文件合并辅助工具

# TLDR

**合并单个文件**

```git merge-one-file [base] [ours] [theirs] [path] [mode]```

# SYNOPSIS

**git merge-one-file** _base_ _ours_ _theirs_ _path_ _mode_

# PARAMETERS

_BASE_
> base 版本的 blob SHA。

_OURS_
> 我方版本的 blob SHA。

_THEIRS_
> 对方版本的 blob SHA。

_PATH_
> 文件路径。

_MODE_
> 文件模式。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git merge-one-file** 是用于单文件合并的辅助脚本，由 `git merge-index` 调用，使用标准三方合并算法处理单个文件的冲突。它接收 base、ours 和 theirs 版本的 blob SHA-1 哈希并执行合并。

该命令属于 Git 内部合并机制的一部分，用户通常不会直接调用。它的存在是为了支持自定义合并工作流，并作为单文件合并程序的参考实现。

# CAVEATS

底层（plumbing）命令。由 git merge 内部调用。通常不直接使用。

# HISTORY

git merge-one-file 是 **Git** 合并基础设施的一部分，作为整体合并流程中的一个组件实现单文件合并。

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

[git-merge](/man/git-merge)(1), [git-merge-file](/man/git-merge-file)(1), [git-merge-index](/man/git-merge-index)(1)
