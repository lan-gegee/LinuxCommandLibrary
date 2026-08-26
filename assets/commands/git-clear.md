# TAGLINE

重置并清理工作目录

# TLDR

**清空工作目录**

```git clear```

**强制清空**

```git clear -f```

# SYNOPSIS

**git** **clear** [_options_]

# PARAMETERS

**-f**, **--force**
> 强制执行而不确认。

# DESCRIPTION

**git clear** 是一个 **git-extras** 命令，它将 **git clean -d -f -x** 和 **git reset --hard** 合并为一条便捷命令。它会移除所有未提交的更改——无论已跟踪还是未跟踪，包括被 **.gitignore** 匹配的文件——使仓库回到与 **HEAD** 一致的原始状态。

它是 git-extras 清理命令中最激进的一个：单独的 **git reset --hard** 只作用于已跟踪的文件，**git-clear-soft** 会保留被忽略的文件，而 **git clear** 则清除所有未提交的内容。默认情况下，它在执行前会询问 **"Sure? - This command may delete files that cannot be recovered, including those in .gitignore [y/N]:"**。

该操作具有破坏性且无法撤销，因为它会永久删除未提交的工作。-f 标志可跳过确认提示，让自动化脚本无需用户交互即可清理仓库。在包含有价值的未提交工作或打算保留的被忽略构建产物的仓库中，请谨慎使用。

# CAVEATS

在硬重置的同时不可逆地删除未跟踪和被忽略的文件；无法撤销。需要安装 **git-extras**。

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

[git-clear-soft](/man/git-clear-soft)(1), [git-reset](/man/git-reset)(1), [git-clean](/man/git-clean)(1), [git-extras](/man/git-extras)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

```[Documentation](https://github.com/tj/git-extras/blob/master/Commands.md#git-clear)```

<!-- verified: 2026-07-17 -->
