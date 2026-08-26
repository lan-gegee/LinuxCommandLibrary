# TAGLINE

反转最近一次仓库操作

# TLDR

撤销上一次操作

```jj undo```

撤销最近两次操作

```jj undo 2```

查看操作日志以找到操作 ID

```jj operation log```

按 ID 恢复到特定操作

```jj operation restore [op_id]```

# SYNOPSIS

**jj undo** [_options_] [_count_]

# PARAMETERS

_COUNT_
> 要撤销的操作数量。

**-R**, **--repository** _path_
> 要操作的仓库路径。

**--what** _what_
> 要恢复本地状态的哪些部分（可以是 `repo` 或 `remote-tracking`）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**jj undo** 通过创建一个从操作日志恢复先前状态的新操作来反转最近一次仓库操作。`jj operation restore` 会丢弃中间操作，而 `jj undo` 则保留完整的操作历史。

该命令支持安全地试验历史。任何 jj 操作都可以被撤销，包括合并、变基和书签更改。

# CAVEATS

jj 的子命令。只能撤销 jj 操作。操作日志有保留上限。

# HISTORY

jj undo 是 **Jujutsu** 的一部分，利用其操作日志提供强大的撤销能力。

# SEE ALSO

[jj](/man/jj)(1), [jj-operation](/man/jj-operation)(1), [jj-restore](/man/jj-restore)(1)
