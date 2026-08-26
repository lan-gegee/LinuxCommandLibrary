# TAGLINE

改写提交的作者信息历史

# TLDR

**更改匹配提交的邮箱地址**

```git reauthor -o [old@email.com] -e [new@email.com]```

**同时更改姓名和邮箱**

```git reauthor -o [old@email.com] -n "[New Name]" -e [new@email.com]```

**使用 `git config user.name` / `user.email` 中的值**

```git reauthor --use-config -o [old@email.com]```

**改写所有身份**（交互式询问）

```git reauthor --all```

**只改写 committer**（不改 author）

```git reauthor -o [old@email.com] -e [new@email.com] -t committer```

# SYNOPSIS

**git reauthor** [_options_]

# PARAMETERS

**-o**, **--old-email** _EMAIL_
> 用于匹配现有提交的邮箱地址。

**-e**, **--correct-email** _EMAIL_
> 替换后的邮箱地址。

**-n**, **--correct-name** _NAME_
> 替换后的作者/committer 姓名。

**-c**, **--use-config**
> 从当前的 **git config** 值中取替换用的姓名/邮箱。

**-a**, **--all**
> 改写历史中发现的所有身份（交互式）。

**-t**, **--type** _TYPE_
> 要改写的身份：**author**、**committer** 或 **both**（默认）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git reauthor** 改写提交历史以修正作者（和/或 committer）信息。对于身份与所给旧邮箱匹配的每个提交，它会更新所有本地分支和标签上的姓名与邮箱地址。

该命令适合修正错误的归属、在更换邮箱后合并多个身份，或在发布仓库之前修正作者信息。由于它会改写历史并改变改写范围内每个提交的 SHA，因此只应用于尚未共享的分支。

# CAVEATS

属于 git-extras 软件包。**会改写历史。**不要在共享分支上使用。所有提交哈希都会改变。

# HISTORY

git reauthor 是 **git-extras** 的一部分，为修正作者信息这一常见任务提供了便捷封装。

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

[git-commit](/man/git-commit)(1), [git-rebase](/man/git-rebase)(1), [git-filter-repo](/man/git-filter-repo)(1)
