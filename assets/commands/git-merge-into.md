# TAGLINE

将当前分支合并到目标分支

# TLDR

**将当前分支合并到目标分支**

```git merge-into [target-branch]```

**将当前分支合并到 main**

```git merge-into main```

**将指定的源分支合并到目标分支**

```git merge-into [source-branch] [target-branch]```

# SYNOPSIS

**git merge-into** [_source-branch_] _target-branch_ [**--ff-only**]

# PARAMETERS

_SOURCE-BRANCH_
> 可选的要合并的分支（默认为当前分支）。

_TARGET-BRANCH_
> 接收合并的分支。

**--ff-only**
> 拒绝合并，除非它能以 fast-forward 方式完成。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git merge-into** 将当前（或指定）分支合并到另一个分支，无需手动切换上下文。它颠倒了常规的合并流程——通常你得先检出目标分支、执行合并、然后再切回来。

该命令会检出目标分支、执行合并，然后自动返回原来的分支。这省去了为了简单合并操作而反复切换分支的重复流程。

# CAVEATS

属于 git-extras 软件包。要求工作目录干净。发生冲突时你可能会停留在目标分支上。

# HISTORY

git merge-into 是 **git-extras** 的一部分，为这种反向合并工作流提供了便捷命令。

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

[git-merge](/man/git-merge)(1), [git-checkout](/man/git-checkout)(1)
