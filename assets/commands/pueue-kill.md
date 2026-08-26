# TAGLINE

向正在运行的 pueue 任务发送信号

# TLDR

**终止特定任务**

```pueue kill [task_id]```

**终止所有运行中的任务**

```pueue kill --all```

**终止分组内的任务**

```pueue kill --group [group_name]```

**发送特定信号**

```pueue kill --signal [SIGTERM] [task_id]```

# SYNOPSIS

**pueue kill** [_options_] [_task_ids_]

# PARAMETERS

**--all**, **-a**
> 终止所有任务。

**--group**, **-g** _name_
> 针对特定分组。

**--signal**, **-s** _signal_
> 要发送的信号。

**--children**, **-c**
> 连同子进程一起终止。

# DESCRIPTION

**pueue kill** 向 pueue 任务队列中正在运行的任务发送信号。默认发送 SIGKILL 立即终止任务。

# EXAMPLES

```bash
# Kill task by ID
pueue kill 5

# Kill all running tasks
pueue kill --all

# Kill group
pueue kill --group compilation

# Send SIGTERM instead
pueue kill --signal SIGTERM 3

# Kill with children
pueue kill --children 7

# Multiple tasks
pueue kill 1 2 3
```

# SIGNALS

```
SIGTERM (15) - Graceful termination
SIGKILL (9)  - Force kill (default)
SIGINT (2)   - Interrupt
SIGSTOP (19) - Stop process
```

# CAVEATS

SIGKILL 无法被捕获。如需优雅关闭请使用 SIGTERM。pueue 任务管理器的一部分。

# HISTORY

pueue kill 是 **Arne Beer** 开发的命令行任务管理器 **pueue** 的一部分，用于管理长时间运行的任务。

# INSTALL

```pacman: sudo pacman -S pueue```

```apk: sudo apk add pueue```

```zypper: sudo zypper install pueue```

```brew: brew install pueue```

```nix: nix profile install nixpkgs#pueue```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pueue](/man/pueue)(1), [pueue-start](/man/pueue-start)(1), [pueue-pause](/man/pueue-pause)(1), [kill](/man/kill)(1)
