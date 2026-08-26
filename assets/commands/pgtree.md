# TAGLINE

显示特定进程的 Unix 进程层级树

# TLDR

**显示某个命令名的进程树**

```pgtree [process_name]```

**显示进程树并发送信号**

```pgtree -s [SIGNAL] [process_name]```

# SYNOPSIS

**pgtree** [_options_] _pattern_

# PARAMETERS

**-s** _SIGNAL_
> 向匹配的进程及其子进程发送信号。

# DESCRIPTION

**pgtree** 是一个 Unix 进程层级树显示工具，结合了 pgrep 和 pstree 的功能。它会找到与模式匹配的进程并显示其完整的进程树，还能向匹配的进程及其全部子进程发送信号。在任何使用操作系统默认 Python 安装的 Unix 系统上开箱即用。

# HISTORY

**pgtree** 由 **joknarf** 创建，用 **Python** 编写。

# SEE ALSO

[pstree](/man/pstree)(1), [pgrep](/man/pgrep)(1), [ps](/man/ps)(1), [kill](/man/kill)(1)
