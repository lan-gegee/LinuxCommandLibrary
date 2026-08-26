# TAGLINE

将提交重新应用到新的基底上

# TLDR

**变基到某分支之上**

```git rebase [branch]```

**交互式变基**

```git rebase -i [commit]```

**对最近 N 个提交进行交互式变基**

```git rebase -i HEAD~[n]```

**解决冲突后继续**

```git rebase --continue```

**中止变基**

```git rebase --abort```

**跳过当前提交**

```git rebase --skip```

**变基到指定基底**

```git rebase --onto [newbase] [oldbase] [branch]```

# SYNOPSIS

**git** **rebase** [_options_] [_upstream_] [_branch_]

# PARAMETERS

**-i**, **--interactive**
> 交互模式。

**--onto** _newbase_
> 变基到另一个不同的基底。

**--continue**
> 解决冲突后继续。

**--abort**
> 取消变基。

**--skip**
> 跳过当前补丁。

**--autosquash**
> 自动应用 fixup/squash 提交。

**--autostash**
> 自动 stash 更改。

**-x** _cmd_
> 在每个提交之后运行命令。

**-r**, **--rebase-merges**
> 重建合并提交而不是将历史压平（取代已弃用的 `--preserve-merges`）。

# DESCRIPTION

**git rebase** 将提交重新应用到另一基底末端之上，从而产生线性的项目历史。它会查找当前分支与上游的共同祖先，然后将当前分支上的每个提交依次重放到上游末端。

交互模式（`-i`）允许在重放过程中重新排序、压缩、编辑或丢弃提交，是清理提交历史的强大工具。`--onto` 选项支持高级工作流，例如把分支移到全新的基底。Autosquash 会自动应用 fixup! 和 squash! 提交，支持迭代式的修补工作流。

# CAVEATS

变基会改写历史。不要对已经推送到共享分支的提交执行变基。

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

[git-merge](/man/git-merge)(1), [git-cherry-pick](/man/git-cherry-pick)(1), [git-reset](/man/git-reset)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-rebase)```

<!-- verified: 2026-07-17 -->
