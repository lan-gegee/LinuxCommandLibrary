# TAGLINE

列出用 git lock 锁定的文件

# TLDR

**显示锁定的文件**

```git locked```

# SYNOPSIS

**git locked**

# DESCRIPTION

**git locked** 是一个 git-extras 命令，列出当前仓库中通过 `git lock` 被设置了 skip-worktree 位的文件。它内部运行 `git ls-files -v` 并筛选出标记为 **S** 的条目——这是 Git 对 skip-worktree 文件的指示符。

由此可以快速了解哪些本地跟踪的文件拥有仅存在于本地的修改、且这些修改不会被 `git status`/`git add` 拾取，例如机器特定的配置文件。

# CAVEATS

该命令属于 git-extras 软件包，并非 Git 核心命令。它只显示本地、单个克隆范围内的 skip-worktree 状态，不反映与队友或远程共享的任何锁定。

# HISTORY

git locked 是 **git-extras** 的一部分，与 git lock 和 git unlock 相辅相成。

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

[git-lock](/man/git-lock)(1), [git-unlock](/man/git-unlock)(1), [git-ls-files](/man/git-ls-files)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

```[Documentation](https://github.com/tj/git-extras/blob/master/Commands.md)```

<!-- verified: 2026-07-17 -->
