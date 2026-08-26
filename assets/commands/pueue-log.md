# TAGLINE

显示 pueue 任务输出日志

# TLDR

**查看任务日志**

```pueue log [task_id]```

**查看所有任务日志**

```pueue log```

**显示最后 N 行**

```pueue log --lines [100] [task_id]```

**完整输出**

```pueue log --full [task_id]```

# SYNOPSIS

**pueue log** [_options_] [_task_ids_]

# PARAMETERS

_TASK_IDS_
> 要查看日志的任务。

**--lines** _N_
> 行数。

**--full**
> 显示完整输出。

# DESCRIPTION

**pueue log** 显示 pueue 任务（无论正在运行还是已完成）捕获的 stdout 和 stderr 输出。默认只显示最后几行；使用 **--full** 查看完整输出，或用 **--lines** 控制显示的行数。

# CAVEATS

输出保存在磁盘上。pueue 的一部分。

# HISTORY

pueue log 提供**任务输出**查看功能。

# INSTALL

```pacman: sudo pacman -S pueue```

```apk: sudo apk add pueue```

```zypper: sudo zypper install pueue```

```brew: brew install pueue```

```nix: nix profile install nixpkgs#pueue```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pueue](/man/pueue)(1), [pueue-follow](/man/pueue-follow)(1)
