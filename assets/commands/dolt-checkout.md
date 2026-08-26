# TAGLINE

切换分支或恢复工作表

# TLDR

**切换分支**

```dolt checkout [branch_name]```

**创建并切换**到新分支

```dolt checkout -b [new_branch]```

**将表恢复**为 HEAD 版本，丢弃变更

```dolt checkout [table_name]```

**将表恢复**为指定提交时的状态

```dolt checkout [commit_hash] -- [table_name]```

**创建跟踪**远程分支的分支

```dolt checkout --track [origin]/[branch_name]```

**丢弃本地变更**并强制切换

```dolt checkout --force [branch_name]```

# SYNOPSIS

**dolt checkout** _branch_

**dolt checkout** _table_...

**dolt checkout** _commit_ [--] _table_...

**dolt checkout** **-b** _new-branch_ [_start-point_]

**dolt checkout** **--track** _remote_/_branch_

# PARAMETERS

**-b** _new-branch_ [_start-point_]
> 创建名为 _new-branch_ 的分支（起点为 _start-point_，默认 HEAD），并切换过去。

**-B** _new-branch_ [_start-point_]
> 与 **-b** 类似，但当分支已存在时会将其强制重置到 _start-point_。

**-f**, **--force**
> 丢弃当前变更并照常检出新分支。

**-t**, **--track**
> 创建分支时设置上游跟踪配置。

**--overwrite-ignore**
> 切换分支时静默覆盖被忽略的表。

**--no-overwrite-ignore**
> 若会覆盖被忽略的表，则中止检出。

# DESCRIPTION

**dolt checkout** 用于切换分支或恢复工作集中的表。与 `git checkout` 相同，它身兼数职：在分支之间移动、创建分支，以及放弃未提交的变更。

给定分支名时，它会把工作数据库指向该分支；配合 **-b** 则会先创建分支。给定一个或多个表名时，它会把这些表恢复成与 HEAD 一致，丢弃未提交的变更；若在 `--` 之前给出提交，则改为恢复到该提交时的状态。

Dolt 的分支非常轻量，因为它们只是指向同一套内容寻址存储的指针，所以无论是围绕功能、导入还是实验建立分支，在数据和表结构上都是常规工作流。

# CAVEATS

恢复表会丢弃其中未提交的变更且无法找回：工作集没有 reflog。与 Git 不同，**dolt checkout** 不接受裸提交哈希进入分离 HEAD 状态；要基于旧提交工作，请使用 `dolt checkout -b <branch> <commit>`。当有 `dolt sql-server` 正在该数据库上运行时，CLI 会共享服务器的会话状态，因此在 Shell 中执行的检出对所有已连接的客户端可见。

# HISTORY

dolt checkout 在 Dolt 的版本化数据库上复刻了 **git checkout**，让 Git 用户可以用熟悉的方式在数据分支之间切换。Dolt 后来也引入了 Git 较新的拆分方式——用 `dolt branch` 管理分支、用 `dolt reset`/`dolt revert` 撤销工作——但 `checkout` 仍是日常使用的入口。

# INSTALL

```pacman: sudo pacman -S dolt```

```brew: brew install dolt```

```nix: nix profile install nixpkgs#dolt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dolt](/man/dolt)(1), [dolt-branch](/man/dolt-branch)(1), [dolt-merge](/man/dolt-merge)(1), [git-checkout](/man/git-checkout)(1)

# RESOURCES

```[Source code](https://github.com/dolthub/dolt)```

```[Documentation](https://www.dolthub.com/docs/cli-reference/cli/)```

<!-- verified: 2026-07-14 -->
