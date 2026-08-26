# TAGLINE

管理进程的实时调度属性

# TLDR

显示进程的**调度属性**

```chrt -p PID```

显示进程**所有线程**的属性

```chrt -a -p PID```

显示优先级的**最小/最大**值

```chrt -m```

设置进程的**调度优先级**

```chrt -p priority PID```

设置 **FIFO** 调度策略

```chrt --fifo -p priority PID```

设置**轮转（round-robin）**调度策略

```chrt --rr -p priority PID```

以 **idle** 调度策略运行命令

```chrt --idle 0 command```

# SYNOPSIS

**chrt** [_options_] _priority_ _command_ [_argument_...]

**chrt** [_options_] **-p** [_priority_] _PID_

# DESCRIPTION

**chrt** 用于设置或获取现有进程的实时调度属性，或以指定的调度属性运行一个命令。它支持多种 Linux 调度策略，包括 FIFO、轮转（round-robin）、batch、idle 和 deadline。

实时调度策略（SCHED_FIFO、SCHED_RR）赋予进程高于普通任务的优先级，这对音频处理、工业控制和高频交易等时间敏感的应用至关重要。非实时策略（SCHED_BATCH、SCHED_IDLE）适用于应让位于交互式进程的后台工作负载。

该工具是 **util-linux** 软件包的一部分，通过 **sched_setscheduler**(2) 和 **sched_setattr**(2) 系统调用工作。

# PARAMETERS

**-p, --pid**
> 操作现有的 PID，而不启动新任务

**-a, --all-tasks**
> 为某个 PID 的所有线程设置或获取调度属性

**-m, --max**
> 显示每种策略的最小和最大有效优先级

**-v, --verbose**
> 显示状态信息

**-R, --reset-on-fork**
> 子进程不继承特权调度策略

**-o, --other**
> 设置 SCHED_OTHER 策略（Linux 默认的分时调度）

**-f, --fifo**
> 设置 SCHED_FIFO 策略（先进先出）

**-r, --rr**
> 设置 SCHED_RR 策略（轮转，未指定策略时的默认值）

**-b, --batch**
> 为批处理设置 SCHED_BATCH 策略（优先级必须为 0）

**-i, --idle**
> 为极低优先级任务设置 SCHED_IDLE 策略（优先级必须为 0）

**-d, --deadline**
> 为偶发式期限调度设置 SCHED_DEADLINE 策略（优先级必须为 0）

# CAVEATS

用户需要 CAP_SYS_NICE 能力才能修改调度属性。SCHED_BATCH、SCHED_IDLE 和 SCHED_DEADLINE 策略要求优先级为 0。只有 SCHED_FIFO、SCHED_OTHER 和 SCHED_RR 属于 POSIX 1003.1b。

# HISTORY

**chrt** 是 **util-linux** 软件包的一部分，自 Linux 2.6 起提供实时进程调度控制。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add util-linux-misc```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nice](/man/nice)(1), [renice](/man/renice)(1), [taskset](/man/taskset)(1)
