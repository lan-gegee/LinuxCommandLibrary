# TAGLINE

继续进行中的变基、合并、拣选或还原操作

# TLDR

**继续当前暂停的任何操作**

```git continue```

# SYNOPSIS

**git continue**

# DESCRIPTION

**git continue** 是一个 **git-extras** 命令，用于恢复 Git 当前暂停的操作，无需记住或查找具体的命令。

它会检查仓库 git-dir 中 Git 在操作中途留下的状态文件（**CHERRY_PICK_HEAD**、**MERGE_HEAD**、**REBASE_HEAD**、**REVERT_HEAD**），判断当前是 cherry-pick、merge、rebase 还是 revert 进行中，然后执行对应的 **--continue**，例如 **git rebase --continue**。

同一个脚本还实现了 **git-abort**（作为指向同一文件的另一个名字安装）：它根据自身被调用的名称决定行为，对检测到的操作执行 **--abort** 而非 **--continue**。

# CAVEATS

如果没有暂停的操作，会报错 "No active operation found"；如果检测到多个操作，则会把它们全部列出。冲突仍需你自己解决并暂存后才能继续；该命令只是省去了输入特定操作的 continue 命令。需要安装 **git-extras**。

# HISTORY

git continue 是社区维护的 Git 实用脚本合集 **git-extras** 的一部分。

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

[git-abort](/man/git-abort)(1), [git-rebase](/man/git-rebase)(1), [git-merge](/man/git-merge)(1), [git-cherry-pick](/man/git-cherry-pick)(1), [git-revert](/man/git-revert)(1), [git-extras](/man/git-extras)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

```[Documentation](https://github.com/tj/git-extras/blob/master/Commands.md#git-continue)```

<!-- verified: 2026-07-17 -->
