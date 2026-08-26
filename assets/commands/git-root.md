# TAGLINE

显示仓库根目录路径

# TLDR

**显示仓库根目录**

```git root```

**切换到根目录**

```cd $(git root)```

# SYNOPSIS

**git root**

# DESCRIPTION

**git root** 显示仓库顶层目录的绝对路径。它属于 git-extras，是 `git rev-parse --show-toplevel` 的一个简洁替代方案。

在需要一致路径的脚本中，或者想无视当前工作目录快速跳转到仓库根目录时，这个命令很有用。

# CAVEATS

属于 git-extras 软件包。替代方案：git rev-parse --show-toplevel。在 git 仓库外会失败。

# HISTORY

git root 是 **git-extras** 的一部分，为"查找仓库根目录"这一常见操作提供了便捷的简写方式。

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

[git-extras](/man/git-extras)(1), [git-rev-parse](/man/git-rev-parse)(1)
