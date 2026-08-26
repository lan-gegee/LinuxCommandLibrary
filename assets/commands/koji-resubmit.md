# TAGLINE

使用与原任务相同的参数重试已取消或失败的任务

# TLDR

**重新提交**失败的任务

```koji resubmit [task_id]```

重新提交但**不等待**

```koji resubmit [task_id] --nowait```

以**静默**模式重新提交

```koji resubmit [task_id] --quiet```

显示**帮助**

```koji resubmit --help```

# SYNOPSIS

**koji resubmit** [_options_] _task_id_

# DESCRIPTION

**koji resubmit** 使用与原任务相同的参数重试已取消或失败的任务。这对网络问题或临时资源耗尽等瞬时故障很有用。

# PARAMETERS

**task_id**
> 要重新提交的任务 ID

**--nowait**, **--nowatch**
> 不等待任务完成

**--quiet**
> 不输出任务信息

**-h, --help**
> 显示帮助信息

# CAVEATS

只有失败或已取消的任务才能重新提交。因源码问题而失败的任务，在不解决根本问题的情况下很可能再次失败。

# SEE ALSO

[koji](/man/koji)(1), [koji-cancel](/man/koji-cancel)(1), [koji-build](/man/koji-build)(1)
