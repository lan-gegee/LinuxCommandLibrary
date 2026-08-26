# TAGLINE

按名称模式搜索进程

# TLDR

**按名称搜索进程**

```psgrep [pattern]```

**不区分大小写搜索**

```psgrep -i [pattern]```

**显示完整命令行**

```psgrep -f [pattern]```

# SYNOPSIS

**psgrep** [_options_] _pattern_

# PARAMETERS

_PATTERN_
> 进程名称模式。

**-i**
> 不区分大小写。

**-f**
> 完整命令行。

**-v**
> 反转匹配。

# DESCRIPTION

**psgrep** 是一个便捷封装，结合 **ps** 和 **grep** 按名称或模式搜索正在运行的进程。它过滤进程列表并显示匹配的条目，并自动将 grep 进程自身从结果中排除，避免误匹配。

该工具为 `ps aux | grep pattern` 这一惯用法提供了更简单的替代方案。在许多系统上，内置的 **pgrep** 命令提供类似功能且选项更多。

# CAVEATS

存在多种不同的实现。部分系统使用 pgrep。

# HISTORY

psgrep 作为进程搜索的**便捷封装**而创建。

# INSTALL

```brew: brew install psgrep```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pgrep](/man/pgrep)(1), [ps](/man/ps)(1), [grep](/man/grep)(1)
