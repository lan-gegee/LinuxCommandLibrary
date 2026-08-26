# TAGLINE

从工作区移除未跟踪的文件

# TLDR

**预览将要删除的文件**

```git clean -n```

**删除未跟踪文件**

```git clean -f```

**删除未跟踪目录**

```git clean -fd```

**删除被忽略的文件**

```git clean -fX```

**交互式清理**

```git clean -i```

# SYNOPSIS

**git clean** [_options_] [_path_]

# PARAMETERS

**-n**, **--dry-run**
> 显示将会删除的内容。

**-f**, **--force**
> 实际执行删除。

**-d**
> 删除未跟踪的目录。

**-x**
> 连同被忽略的文件一起删除。

**-X**
> 只删除被忽略的文件。

**-i**, **--interactive**
> 交互模式。

**-e** _PATTERN_
> 排除匹配的模式。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git clean** 从工作区中移除未跟踪的文件。它可以清理生成的文件、构建产物以及其他未被 git 跟踪的文件。

该命令要求必须带 **-f** 才会真正删除文件，以防意外丢失数据。试运行模式（**-n**）只显示将被删除的内容而不实际删除。选项可以控制是否包含被忽略的文件（**-x**/**-X**）和目录（**-d**）。

与 **git reset --hard** 组合使用时，git clean 提供了将工作区完全恢复到最后一次提交原始状态的完整手段。请务必先用 **-n** 预览，因为被删除的未跟踪文件无法通过 Git 找回。

# CAVEATS

**删除的文件无法恢复。** 务必先用 -n 预览。必须强制执行以防误删。

# HISTORY

git clean 是 **Git** 的核心命令之一，用于维护干净的工作目录，在清理构建产物和重新开始工作时尤其有用。

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

[git-status](/man/git-status)(1), [git-reset](/man/git-reset)(1)
