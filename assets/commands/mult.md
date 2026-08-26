# TAGLINE

多次运行一条命令并比较输出结果

# TLDR

**将命令运行 5 次**

```mult -n 5 "[command]"```

**在每次执行之间加入延迟**

```mult -n 5 -d 1s "[command]"```

**首次失败即停止**

```mult -n 10 --fail-fast "[command]"```

# SYNOPSIS

**mult** [_options_] _command_

# PARAMETERS

**-n** _COUNT_
> 命令运行的次数。

**-d**, **--delay** _DURATION_
> 各次执行之间的延迟。

**--fail-fast**
> 出现第一次失败时停止执行。

# DESCRIPTION

**mult** 是一款 TUI 工具，它会多次执行 shell 命令并显示每次运行的输出以便比较。它适合用于发现服务器行为的不一致、排查不稳定的测试结果，以及进行快速的性能评估。

TUI 提供各次运行输出的并排对比视图。

# CAVEATS

带有副作用的命令会在每次运行时都执行这些副作用。对具有破坏性的命令请谨慎使用。

# HISTORY

**mult** 由 **dhth** 创建，使用 **Go** 编写。

# INSTALL

```aur: yay -S mult```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[watch](/man/watch)(1)
