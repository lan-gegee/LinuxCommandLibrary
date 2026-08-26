# TAGLINE

将单个文件重置到指定版本

# TLDR

**将文件重置到 HEAD**

```git reset-file [file]```

**将文件重置到指定提交**

```git reset-file [file] [commit]```

# SYNOPSIS

**git** **reset-file** _file_ [_commit_]

# DESCRIPTION

**git reset-file** 将单个已跟踪文件重置到它在 HEAD（或给定提交，如果提供了的话）时的状态。它属于 git-extras，会取消该文件的暂存并从该版本检出其内容，不影响工作树和索引中的其他部分。

# CAVEATS

文件参数在前，可选的提交在后；顺序传错会静默失败，因为第二个参数会被当作 commit-ish。该文件当前必须存在于工作树中。

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

[git-reset](/man/git-reset)(1), [git-checkout](/man/git-checkout)(1), [git-extras](/man/git-extras)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

```[Documentation](https://github.com/tj/git-extras/blob/master/Commands.md#git-reset-file)```

<!-- verified: 2026-07-17 -->
