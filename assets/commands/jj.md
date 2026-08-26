# TAGLINE

jujutsu，一款与 Git 兼容的版本控制系统

# TLDR

在当前目录初始化新的 Git/jj 共存仓库

```jj git init --colocate```

克隆 Git 远程仓库

```jj git clone [https://github.com/owner/repo]```

显示工作副本状态

```jj status```

显示修订图

```jj log```

在当前变更之上创建新的（空）变更

```jj new```

描述当前变更

```jj describe -m "[message]"```

将当前变更压缩进其父修订

```jj squash```

将变更移动到新的父修订（变基）

```jj rebase -r [revision] -d [destination]```

废弃当前变更（丢弃其内容并变基后代）

```jj abandon```

撤销上一次操作

```jj undo```

与 Git 远程同步

```jj git fetch && jj git push```

# SYNOPSIS

**jj** [_global_options_] _command_ [_args_]

# COMMON COMMANDS

**git init** [--colocate]
> 初始化新仓库，可选择与 Git 共存（colocated），使 **jj** 和 **git** 看到相同的工作副本。

**git clone** _url_
> 将 Git 远程仓库克隆为 jj 仓库。

**status**
> 显示仓库/工作副本的高层状态。

**log**
> 显示修订图。

**new** [_revisions_...]
> 在给定修订之上创建新的（空）变更；默认为当前工作副本的父修订。

**describe** [**-m** _message_]
> 编辑变更的描述（提交说明）。

**edit** _revision_
> 将工作副本移动到现有修订（取代"checkout"式思维）。

**squash** [**--from** _rev_] [**--into** _rev_]
> 将改动从一个修订移入另一个修订（默认：当前 → 其父修订）。

**rebase** **-r** _rev_ **-d** _dest_
> 将修订（及其后代，可选）移动到新的目标位置。

**abandon** [_revision_]
> 丢弃变更；后代会变基到父修订上。

**undo**
> 反转上一次操作。配合 **jj op log** 和 **jj op restore** 可进行更精细的控制。

**bookmark** _subcommand_
> 管理命名引用（相当于 Git 分支）：**create**、**move**、**delete**、**track**、**untrack**、**list**。

**git** _subcommand_
> Git 互操作：**fetch**、**push**、**import**、**export**、**remote**。

**op log**, **op restore**
> 检查和回滚操作日志（每条命令都会被记录）。

# GLOBAL OPTIONS

**-R**, **--repository** _PATH_
> 在 _PATH_ 处的仓库上进行操作。

**--at-operation** _OP_, **--at-op** _OP_
> 在操作日志中某个先前操作的状态下运行命令（只读视图）。

**--no-pager**
> 本次调用禁用分页器。

**--config-toml** _TOML_
> 内联配置覆盖。

# DESCRIPTION

**jj**（Jujutsu）是一款与 Git 兼容的分布式版本控制系统。每个工作副本变更都会被记录为一等修订，冲突存储在提交中而不是阻塞操作，并且不存在 Git 意义上的分支——相反，每个提交都可以通过修订图访问，同时可以将人类友好的**书签**附加到任何修订上。

默认后端是 Git，因此 jj 仓库可以与真实的 Git 仓库**共存**（`jj git init --colocate`），让 Git 工具和其他开发者继续通过普通 Git 交互，而你在本地使用 jj。

# CAVEATS

该 CLI 尚处于 1.0 之前的阶段且仍在变化——**bookmark** 子命令在 0.18 中由 **branch** 更名而来，许多标志也在持续演变。**jj git push** 默认只推送与本地工作修订匹配的书签；显式推送需使用 **--bookmark** _name_ 或 **--all-bookmarks**。冲突会存储在磁盘上，但围绕冲突解决的配套工具仍不成熟。

# HISTORY

**Jujutsu** 由 **Martin von Zweigbergk** 于 **2019 年**在 **Google** 作为个人实验创建，于 **2022 年**开源，目前开发位于 **github.com/jj-vcs/jj**，贡献者社区不断壮大。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj-git](/man/jj-git)(1), [jj-log](/man/jj-log)(1), [git](/man/git)(1), [hg](/man/hg)(1)
