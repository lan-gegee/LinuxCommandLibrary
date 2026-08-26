# TAGLINE

通过 hub 原样运行 git 自带的 branch 命令

# TLDR

**列出本地和远程分支**

```hub branch -a```

**创建新分支**

```hub branch [branch-name]```

**删除分支**

```hub branch -d [branch-name]```

**强制删除分支**

```hub branch -D [branch-name]```

**重命名当前分支**

```hub branch -m [new-name]```

# SYNOPSIS

**hub** **branch** [_options_] [_branch_]

# PARAMETERS

**-a**, **--all**
> 同时列出本地和远程分支。

**-r**, **--remotes**
> 只列出远程分支。

**-d**
> 删除分支（仅限已合并的分支）。

**-D**
> 强制删除分支。

**-m**
> 重命名分支。

**-v**, **--verbose**
> 显示更多信息。

# DESCRIPTION

**hub** 是 git 的命令行包装器，它为特定的 git 子命令（**clone**、**fetch**、**remote**、**checkout**、**merge** 以及少数几个其他命令）添加 GitHub 特有的行为，同时把其余所有子命令原样透传给真正的 git 二进制文件。**branch** 并不是 hub 扩展的命令之一，因此 `hub branch` 的行为与 `git branch` 完全一致：列出、创建、重命名和删除分支，不附加任何 GitHub 集成功能。

之所以收录此条目，是因为当 hub 被别名为 `git` 时（参见 `hub alias`），任何 git 子命令——包括 **branch**——都可以通过它来调用。

# CAVEATS

Hub 已不再活跃维护，已被官方 GitHub CLI（**gh**）取代。如需真正感知 GitHub 的分支操作（例如将 pull request 检出为分支），请改用 **hub checkout** 或 **gh pr checkout**。

# INSTALL

```apt: sudo apt install hub```

```pacman: sudo pacman -S hub```

```zypper: sudo zypper install hub```

```brew: brew install hub```

```nix: nix profile install nixpkgs#hub```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hub](/man/hub)(1), [git-branch](/man/git-branch)(1), [gh](/man/gh)(1)

# RESOURCES

```[Source code](https://github.com/mislav/hub)```

<!-- verified: 2026-07-19 -->
