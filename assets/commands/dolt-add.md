# TAGLINE

暂存表变更以待提交

# TLDR

**暂存所有变更**

```dolt add .```

**暂存指定的表**

```dolt add [table_name]```

**暂存多个表**

```dolt add [table1] [table2]```

**暂存全部内容**，相当于 `.`

```dolt add -A```

**暂存被 `dolt_ignore` 忽略的表**

```dolt add --force [table_name]```

# SYNOPSIS

**dolt** **add** [_table_...]

# PARAMETERS

**-A**, **--all**
> 暂存一切变更（新增、删除和修改），被忽略的表除外。

**-f**, **--force**
> 允许添加原本会被忽略的表。

# DESCRIPTION

**dolt add** 将表变更暂存，等待下一次提交。`git add` 操作的对象是文件，而 `dolt add` 暂存的对象是数据库表——即行或表结构被修改、新增或删除的表。

该命令标记存在待处理变更的表，将其纳入下一次提交。借助暂存，可以在多张表之间进行选择性提交——这与 Git 的索引是同一个概念，只是作用对象从文件内容变成了表结构和数据的修改。

显式指定表名时只暂存这些表；`.` 或 **-A** 则会暂存工作集中所有已修改的表。

# CAVEATS

被 `dolt_ignore` 系统表匹配的表即使使用 **-A** 也会被跳过；此时可用 **--force** 强制暂存。暂存仅对 CLI 工作流有意义：通过 `dolt sql-server` 执行的写入会直接进入工作集，而且根据会话的 `@@dolt_transaction_commit` 设置，这些写入可能根本不经过暂存区就被提交。

# INSTALL

```pacman: sudo pacman -S dolt```

```brew: brew install dolt```

```nix: nix profile install nixpkgs#dolt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dolt](/man/dolt)(1), [dolt-commit](/man/dolt-commit)(1), [dolt-status](/man/dolt-status)(1), [git-add](/man/git-add)(1)

# RESOURCES

```[Source code](https://github.com/dolthub/dolt)```

```[Documentation](https://www.dolthub.com/docs/cli-reference/cli/)```

<!-- verified: 2026-07-14 -->
