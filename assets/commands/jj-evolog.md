# TAGLINE

显示变更的演化历史

# TLDR

显示演化日志

```jj evolog```

查看特定修订的演化日志

```jj evolog -r [revset]```

显示时附带 diff

```jj evolog -p```

限制条目数量

```jj evolog -n [10]```

扁平列表（无图形）

```jj evolog --no-graph```

最早的条目优先显示

```jj evolog --reversed```

# SYNOPSIS

**jj evolog** [_options_]

# PARAMETERS

**-r**, **--revisions** _REVSETS_
> 跟踪这些修订的演化（默认：_@_，即工作副本提交）。

**-n**, **--limit** _LIMIT_
> 限制显示的修订数量。

**--reversed**
> 以相反顺序显示修订（旧的在前）。

**-G**, **--no-graph**
> 隐藏 ASCII 图形，显示扁平的修订列表。

**-T**, **--template** _TEMPLATE_
> 使用自定义模板表达式渲染输出。

**-p**, **--patch**
> 显示每个变更与其前一版本之间的 diff。

**-s**, **--summary**
> 对每个路径，仅显示它是被修改、新增还是删除。

**--stat**
> 显示每个文件改动的直方图。

**--git**
> 以 Git 兼容格式呈现 diff。

**--name-only**
> 仅显示被更改文件的路径名。

**--help**
> 显示帮助信息。

# DESCRIPTION

**jj evolog** 显示变更的演化历史。它展示一个变更随时间被修改的过程。

该命令揭示改写、变基和修正的历史。它有助于理解变更如何演变。

# CAVEATS

jj 的子命令。显示内部演化信息。这是 Jujutsu 模型独有的功能。

# HISTORY

jj evolog 是 **Jujutsu** 的一部分，利用其对变更演化跟踪的一流支持。

# SEE ALSO

[jj](/man/jj)(1), [jj-log](/man/jj-log)(1), [jj-show](/man/jj-show)(1)
