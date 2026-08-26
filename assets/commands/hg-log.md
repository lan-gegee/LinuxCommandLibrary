# TAGLINE

显示仓库的提交历史

# TLDR

**显示提交历史**

```hg log```

**显示最近 n 条提交**

```hg log -l [5]```

**显示特定文件的历史**

```hg log [file]```

**显示补丁**

```hg log -p```

**图形视图**

```hg log -G```

**显示特定修订版本**

```hg log -r [revision]```

**显示特定用户的提交**

```hg log -u [username]```

**显示匹配关键字的提交**

```hg log -k [keyword]```

# SYNOPSIS

**hg log** [_options_] [_file_]

# PARAMETERS

_FILE_
> 限定为特定文件。

**-l**, **--limit** _N_
> 限制条目数量。

**-r**, **--rev** _REV_
> 显示特定修订版本。

**-p**, **--patch**
> 显示补丁。

**-G**, **--graph**
> 显示 DAG 图。

**-b**, **--branch** _BRANCH_
> 显示分支上的提交。

**-u**, **--user** _USER_
> 显示指定用户的提交。

**-k**, **--keyword** _TEXT_
> 搜索提交信息。

**--template** _TPL_
> 输出模板。

**--help**
> 显示帮助信息。

# DESCRIPTION

**hg log** 显示仓库的提交历史。它展示变更集及其作者、日期、摘要等元数据。

该命令支持按文件、分支或修订版本范围过滤。图形模式可可视化分支和合并结构。

# CAVEATS

大型历史可能较慢。请用 -l 加以限制。可用模板自定义输出。

# HISTORY

log 是 **Mercurial** 自 1.0 版本以来查看仓库历史的核心命令。

# SEE ALSO

[hg](/man/hg)(1), [hg-status](/man/hg-status)(1), [hg-commit](/man/hg-commit)(1), [git-log](/man/git-log)(1)
