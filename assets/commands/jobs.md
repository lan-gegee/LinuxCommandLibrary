# TAGLINE

Shell 内建命令，显示当前 shell 中已启动作业的状态

# TLDR

查看当前 shell 启动的**作业**

```jobs```

列出作业及其**进程 ID**

```jobs -l```

显示**状态发生变化**的作业

```jobs -n```

仅显示**进程 ID**

```jobs -p```

显示**正在运行**的进程

```jobs -r```

显示**已停止**的进程

```jobs -s```

# SYNOPSIS

**jobs** [_options_] [_jobspec_]

# PARAMETERS

**-l**
> 除常规信息外，还列出进程 ID

**-n**
> 仅显示自上次通知以来状态发生变化的作业

**-p**
> 仅显示进程 ID

**-r**
> 仅显示正在运行的作业

**-s**
> 仅显示已停止的作业

**-x** _command_
> 将 command 中的 jobspec 替换为进程组 ID 并执行

# DESCRIPTION

**jobs** 是一个 shell 内建命令，用于显示当前 shell 会话中启动的作业状态。作业是指用 &（后台方式）启动或用 Ctrl+Z 挂起的进程。

每个作业都有一个作业号（显示在方括号中），可在 fg、bg 和 kill 命令中以 %n 语法引用。+ 表示当前作业，- 表示上一个作业。

# CAVEATS

这是 shell 内建命令——不同 shell 的行为可能有所差异。-n、-r、-s 选项为 Bash 特有。作业只属于当前 shell 会话，对其他 shell 不可见。

# HISTORY

作业控制于 **20 世纪 70 年代末**引入 C shell（csh），随后被包括 Bash 在内的其他 shell 采用。它让用户可以在单个终端会话内管理多个进程。

# SEE ALSO

[fg](/man/fg)(1), [bg](/man/bg)(1), [disown](/man/disown)(1), [kill](/man/kill)(1)
