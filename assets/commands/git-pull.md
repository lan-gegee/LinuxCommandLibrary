# TAGLINE

抓取并整合远程更改

# TLDR

**从 origin 拉取**

```git pull```

**从特定远程拉取**

```git pull [remote]```

**拉取特定分支**

```git pull [remote] [branch]```

**以 rebase 方式拉取**

```git pull --rebase```

**拉取所有远程**

```git pull --all```

**拉取但不自动提交合并**

```git pull --no-commit```

**只允许 fast-forward 的拉取**

```git pull --ff-only```

# SYNOPSIS

**git** **pull** [_options_] [_remote_] [_branch_]

# PARAMETERS

**--rebase**[=_true|merges|false_]
> 抓取后将当前分支变基到上游之上，而不是合并。

**--no-rebase**
> 将上游合并进当前分支（覆盖 `pull.rebase` 配置）。

**--ff-only**
> 仅在可以 fast-forward 时更新，否则失败。

**--no-ff**
> 总是创建合并提交，即使可以 fast-forward。

**--no-commit**
> 执行合并但在创建提交前停止。

**--squash**
> 将所有抓取的提交压缩为当前分支上的单个提交。

**--all**
> 从所有远程抓取。

**--autostash**
> 自动 stash 未提交的更改并在之后重新应用。

**--set-upstream**
> 为被拉取的分支添加上游跟踪引用。

**--depth** _n_
> 将抓取限制在距远程末端指定数量的提交内。

**-t**, **--tags**
> 从远程抓取所有标签。

**-q**, **--quiet**
> 在抓取和合并过程中抑制输出。

**-v**, **--verbose**
> 详细输出。

# DESCRIPTION

**git pull** 从远程抓取更改并将其整合到当前分支。它等价于先运行 `git fetch` 再运行 `git merge`；若使用了 `--rebase` 选项，则等价于 `git rebase`。

拉取策略因工作流而异。有些团队偏好合并（保留全部历史），有些偏好变基（线性历史），还有些使用 `--ff-only` 拒绝非 fast-forward 更新、防止意外的合并提交。`pull.rebase` 配置项控制默认行为。

# CAVEATS

向脏工作区拉取可能引发冲突。可以使用 `--autostash` 自动 stash 并重新应用本地更改。默认的合并或变基行为由 `pull.rebase` 配置项控制。自 Git 2.27 起，未设置 `pull.rebase` 时 `git pull` 会发出警告。

# HISTORY

**git pull** 自 Linus Torvalds 于 **2005 年**发布 Git 之初就是其中一员。`--ff-only` 选项在 Git 1.6.6 中加入，`--autostash` 选项在 Git 2.9 中加入。

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

[git-fetch](/man/git-fetch)(1), [git-merge](/man/git-merge)(1), [git-rebase](/man/git-rebase)(1), [git-stash](/man/git-stash)(1)
