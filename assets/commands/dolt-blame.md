# TAGLINE

显示最后修改 Dolt 表每一行的提交、作者和时间戳

# TLDR

对表的**每一行执行 blame**

```dolt blame [table_name]```

**按主键值查看 blame**（事后过滤）

```dolt blame [table_name] | grep "[key_value]"```

通过 SQL **查询 blame** 以自定义列/过滤条件

```dolt sql -q "SELECT * FROM dolt_blame_[table_name]"```

**只显示某位作者修改的行**

```dolt sql -q "SELECT * FROM dolt_blame_[table_name] WHERE committer = '[alice]'"```

# SYNOPSIS

**dolt blame** _table_

# PARAMETERS

_TABLE_
> 要追溯的表。各条目通过其主键标识。

# DESCRIPTION

**dolt blame** 输出一张每个主键占一行的表格，显示最后一次修改该行的提交的时间戳、作者、提交消息和提交哈希。它相当于行级别的 `git blame`，适配到了数据库场景。

CLI 形式只显示一组固定列。如果需要更灵活的查询（与其他系统表连接、按提交范围过滤、自定义投影），请使用等价的 SQL 系统视图 `dolt_blame_$tablename` —— 它的列包含该表的全部主键以及 `commit_hash`、`committer`、`email`、`date` 和 `message`。

# CAVEATS

只报告每一行的**最近一次**修改——不提供完整历史。目前表结构变更会计为对所有行的修改，因此一条 `ALTER TABLE` 就会把所有行都归因于该提交。历史深长的大表可能耗时较久；这类情况建议改用带 `LIMIT`/`WHERE` 的 SQL 视图。

# HISTORY

**dolt blame** 是 **DoltHub** 出品的版本化 SQL 数据库 **Dolt**（"数据界的 Git"）的一部分。它把 Git 风格的行级溯源带到了关系型表中。

# INSTALL

```pacman: sudo pacman -S dolt```

```brew: brew install dolt```

```nix: nix profile install nixpkgs#dolt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dolt](/man/dolt)(1), [dolt-sql](/man/dolt-sql)(1), [git-blame](/man/git-blame)(1)
