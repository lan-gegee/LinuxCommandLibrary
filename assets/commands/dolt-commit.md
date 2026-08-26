# TAGLINE

记录已暂存的数据库表变更

# TLDR

**提交已暂存的变更**

```dolt commit -m "[message]"```

**提交所有变更**，包括未暂存的已修改表

```dolt commit -am "[message]"```

**修补最后一次提交**

```dolt commit --amend```

以指定的作者**提交**

```dolt commit -m "[message]" --author "[Name <email>]"```

**创建空提交**（例如用于触发 CI）

```dolt commit --allow-empty -m "[message]"```

# SYNOPSIS

**dolt** **commit** [_options_]

# PARAMETERS

**-m**, **--message** _string_
> 提交消息。

**-a**, **--all**
> 暂存所有已修改的表并提交。

**--amend**
> 修补上一次提交而不是新建提交。

**--author** _string_
> 覆盖提交作者（格式："Name <email>"）。

**--date** _string_
> 覆盖提交日期。

**--allow-empty**
> 允许创建不含任何变更的提交。

**--force**
> 强制提交，忽略任何警告。

**-A**, **--ALL**
> 暂存所有表（包括新增和未跟踪的表）并提交。

# DESCRIPTION

**dolt commit** 通过创建一个包含已暂存表修改的新提交来记录数据库仓库的变更。它会捕获当前所有已暂存表的状态快照，把那一刻的数据和表结构保存在仓库历史中。

每个提交都需要一条描述变更的消息，由此形成数据库随时间演进的审计轨迹。该命令沿用 Git 的提交流程，只是操作对象从文件换成了数据库表，从而实现数据的版本控制。

提交可以被修补，可以指定不同的作者，也可以用 -a 标志自动纳入所有已修改的表。使用大写的 -A 还会包括新增的未跟踪表。默认拒绝空提交，以免产生无意义的历史条目。

# INSTALL

```pacman: sudo pacman -S dolt```

```brew: brew install dolt```

```nix: nix profile install nixpkgs#dolt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dolt-add](/man/dolt-add)(1), [dolt-status](/man/dolt-status)(1), [dolt-branch](/man/dolt-branch)(1), [dolt-merge](/man/dolt-merge)(1)
