# TAGLINE

显示跨所有分支的装饰化提交图

# TLDR

**显示分支树**

```git show-tree```

# SYNOPSIS

**git show-tree**

# DESCRIPTION

**git show-tree** 是 `git log --all --graph --decorate --oneline --simplify-by-decoration` 的 git-extras 快捷方式。它会绘制一张横跨所有分支的 ASCII 提交图，只显示作为分支/标签顶端或合并点的提交，让仓库的整体拓扑一目了然。

# CAVEATS

属于 git-extras 软件包。只显示与图形形状相关的提交（分支顶端、合并点、标签）；如果需要每一个提交，请直接使用 `git log --graph`。

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

[git-log](/man/git-log)(1), [git-branch](/man/git-branch)(1), [git-extras](/man/git-extras)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

```[Documentation](https://github.com/tj/git-extras/blob/master/Commands.md#git-show-tree)```

<!-- verified: 2026-07-17 -->
