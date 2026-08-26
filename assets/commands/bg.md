# TAGLINE

在后台恢复已暂停的作业

# TLDR

**在后台恢复最近停止的作业**

```bg```

**按编号恢复指定作业**

```bg %[1]```

**恢复命令以某字符串开头的作业**

```bg %[string]```

# SYNOPSIS

**bg** [_job-spec_]

# DESCRIPTION

**bg** 在后台恢复已挂起的作业。它是一个 shell 内建命令，用于继续执行已停止的作业（通常由 Ctrl+Z 触发），同时允许你继续使用终端。若未指定作业，则恢复最近停止的作业。

该命令属于 POSIX shell 作业控制功能的一部分，在 bash、zsh、ksh 及其他 POSIX 兼容 Shell 中均可用。

# PARAMETERS

_job-spec_
> 作业标识符（%1、%2 等）

如果未指定作业，bg 会作用于最近停止的作业。

# JOB SPECIFICATIONS

**%n**
> 编号为 n 的作业

**%string**
> 命令以 string 开头的作业

**%?string**
> 命令包含 string 的作业

**%%** 或 **%+**
> 当前作业

**%-**
> 上一个作业

# WORKFLOW

```bash
# Start long-running command
./long_process

# Suspend with Ctrl+Z
[Ctrl+Z]

# Resume in background
bg

# Or resume specific job
bg %1

# List jobs
jobs

# Bring to foreground
fg %1
```

# CAVEATS

仅在启用了作业控制的 Shell 中有效。后台作业在尝试从终端读取时可能停止。除非重定向，输出仍会发送到终端。Shell 退出时作业会终止，除非使用 nohup 或 disown。

# HISTORY

自 C shell（csh）在 **1970 年代**末引入作业控制功能以来，**bg** 就一直是 Unix Shell 作业控制的一部分。

# SEE ALSO

[fg](/man/fg)(1), [jobs](/man/jobs)(1), [disown](/man/disown)(1), [nohup](/man/nohup)(1)
