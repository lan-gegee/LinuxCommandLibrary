# TAGLINE

恢复对已锁定文件的改动跟踪

# TLDR

**解锁文件**

```git unlock [file]```

# SYNOPSIS

**git** **unlock** _file_

# DESCRIPTION

**git unlock** 对文件执行 `git update-index --no-skip-worktree`，清除 **skip-worktree** 位，使 Git 恢复对该文件本地改动的跟踪。它是 `git lock` 的逆操作——后者通过 `--skip-worktree` 让 Git 忽略某个文件的修改（通常是存放本地配置或不应提交的机密的文件）。

属于 **git-extras** 软件包。

# CAVEATS

使用的是 `skip-worktree` 位而非 `assume-unchanged`；两者相似但用途不同，检查其中一个的工具不一定会看到另一个。

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

[git-lock](/man/git-lock)(1), [git-update-index](/man/git-update-index)(1), [git-extras](/man/git-extras)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

```[Documentation](https://github.com/tj/git-extras/blob/master/Commands.md#git-unlock)```

<!-- verified: 2026-07-17 -->
