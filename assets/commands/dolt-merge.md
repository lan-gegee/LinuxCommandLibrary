# TAGLINE

连接分支历史并合并表变更

# TLDR

将分支**合并到**当前分支

```dolt merge [branch_name]```

带提交消息**合并**

```dolt merge [branch_name] -m "[Merge message]"```

**中止进行中的合并**

```dolt merge --abort```

**压缩合并**进工作集，不产生合并提交

```dolt merge --squash [branch_name]```

**总是创建合并提交**，即使是快进合并

```dolt merge --no-ff -m "[Merge message]" [branch_name]```

**拒绝合并**，除非能够快进

```dolt merge --ff-only [branch_name]```

**检查合并遗留的冲突**

```dolt sql -q "SELECT * FROM dolt_conflicts"```

# SYNOPSIS

**dolt merge** [**--squash**] _branch_

**dolt merge** **--no-ff** [**-m** _message_] _branch_

**dolt merge** **--ff-only** _branch_

**dolt merge** **--abort**

# PARAMETERS

**-m**, **--message** _MSG_
> 使用 _MSG_ 作为合并提交的提交消息。

**--squash**
> 将变更并入工作集，但不更新提交历史。

**--no-ff**
> 即使合并以快进方式解决，也强制创建合并提交。

**--ff-only**
> 除非 HEAD 已经是最新的，或合并能以快进方式解决，否则拒绝合并。

**--commit**
> 执行合并并提交结果。这是默认行为。

**--no-commit**
> 执行合并，但在创建合并提交之前停下。

**--no-edit**
> 使用自动生成的提交消息，而不打开编辑器。

**--author** _NAME_ <_EMAIL_>
> 为合并提交记录明确的作者。

**--abort**
> 中止进行中的合并，让工作集回到合并前的状态。

# DESCRIPTION

**dolt merge** 通过把另一分支的变更并入当前分支来连接两条历史。由于 Dolt 的变更单位是行而不是文本行，合并是对表数据和表结构的三方合并：只有一侧触碰过的行会被直接采用；两侧都修改过的行则逐单元格比较，因此即便两个分支编辑了同一行的不同列，依然可以干净地合并。

当两侧把*同一个单元格*改成不同的值，或表结构发生不兼容的分叉时，就会产生冲突。与 Git 不同，Dolt 不会向你的数据写入冲突标记。冲突记录在 `dolt_conflicts` 和 `dolt_conflicts_<table>` 系统表中，需要在提交前用 SQL 查询并解决。表结构与约束问题则分别落在 `dolt_schema_conflicts` 和 `dolt_constraint_violations` 中。

# CAVEATS

冲突必须通过系统表解决，而不能靠编辑文件；只要 `dolt_conflicts` 里还有记录，合并就无法提交。**--squash** 应用变更后不会保留与被合并分支历史的关联，因此日后再次合并同一分支时，相同的提交会被重新考量。合并前工作集必须处于干净状态。合并也可能在行级别成功却违反外键或唯一约束——这种情况会表现为约束违规，而不是冲突。

# HISTORY

dolt merge 为关系型数据实现了 **git merge** 的语义，这正是整个项目的核心追求：让数据库变更能像代码一样被审阅和合并。逐单元格三方合并、表结构合并以及冲突系统表是在后续版本中逐步构建起来的，Dolt 也由此从一个数据共享工具成长为 MySQL 兼容数据库。

# INSTALL

```pacman: sudo pacman -S dolt```

```brew: brew install dolt```

```nix: nix profile install nixpkgs#dolt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dolt](/man/dolt)(1), [dolt-checkout](/man/dolt-checkout)(1), [dolt-branch](/man/dolt-branch)(1), [dolt-commit](/man/dolt-commit)(1), [git-merge](/man/git-merge)(1)

# RESOURCES

```[Source code](https://github.com/dolthub/dolt)```

```[Documentation](https://www.dolthub.com/docs/cli-reference/cli/)```

<!-- verified: 2026-07-14 -->
