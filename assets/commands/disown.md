# TAGLINE

从 Shell 作业表中移除作业

# TLDR

**脱离最近的**后台作业

```disown```

按作业号**脱离特定作业**

```disown %[1]```

**脱离所有后台**作业

```disown -a```

仅**脱离正在运行的作业**

```disown -r```

**脱离并抑制** SIGHUP

```disown -h %[1]```

# SYNOPSIS

**disown** [_options_] [_jobspec_...]

# PARAMETERS

_JOBSPEC_
> 要脱离的作业标识（如 %1、%2）。

**-a**
> 脱离所有作业。

**-r**
> 仅脱离正在运行的作业。

**-h**
> 标记作业，使其在 Shell 退出时不接收 SIGHUP。

# DESCRIPTION

**disown** 是一个 Shell 内置命令，它将作业从 Shell 的作业表中移除，使其在 Shell 终止时不接收 SIGHUP 信号。这允许后台进程在注销后继续运行。

不带参数时，disown 作用于当前作业。作业标识（如 %1）可以指定特定作业。-h 选项将作业保留在表中但标记为不接收 SIGHUP，适用于既要继续监控作业又要防止其被终止的场景。

当长时间运行的进程启动时未使用 nohup、又需要在 Shell 退出后存活时，通常会用到 disown。它在 bash 和 zsh 中均可使用。

# CAVEATS

进程必须先放入后台才能 disown。若未重定向，输出仍可能写到终端。已脱离的作业无法重新归属。不同 Shell 的实现有所差异。

# HISTORY

disown 是 **bash**、**zsh** 和 **ksh** 中的 Shell 内置命令。它与 nohup 命令互补，提供了一种把已在运行的作业从当前 Shell 会话中分离的方式。

# SEE ALSO

[nohup](/man/nohup)(1), [bg](/man/bg)(1), [fg](/man/fg)(1), [jobs](/man/jobs)(1)

# RESOURCES

```[Documentation](https://www.gnu.org/software/bash/manual/html_node/Job-Control-Builtins.html)```

<!-- verified: 2026-07-11 -->
