# TAGLINE

通过应用补丁进行变基

# TLDR

**变基并应用补丁**

```git rebase-patch [patch_file]```

# SYNOPSIS

**git** **rebase-patch** _patch_file_

# DESCRIPTION

**git rebase-patch** 查找旧补丁文件仍能应用的位置，并将其重放到当前 HEAD 上。这个 git-extras 命令针对的是无法再干净地应用到 HEAD 的补丁：它会沿父提交逐个向前回溯，用临时索引在每个历史树测试该补丁，直到找到一个可以应用的提交。随后它在该处构造一个提交，并通过 cherry-pick 将其带到当前分支上。

这适用于恢复一个因代码演进而过时的旧补丁，而无需手动查明它当初是基于哪个提交编写的。

# CAVEATS

属于 git-extras 软件包。只沿 HEAD 的 first-parent 链向后搜索；如果补丁基于该链之外的提交，将无法找到。

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

[git-rebase](/man/git-rebase)(1), [git-am](/man/git-am)(1), [git-cherry-pick](/man/git-cherry-pick)(1), [git-extras](/man/git-extras)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

```[Documentation](https://github.com/tj/git-extras/blob/master/Commands.md#git-rebase-patch)```

<!-- verified: 2026-07-17 -->
