# TAGLINE

限制进程的 CPU 使用率

# TLDR

**按 PID 将进程限制在 25% CPU**

```cpulimit -p [1234] -l [25]```

**按可执行文件名限制**

```cpulimit -e [program] -l [25]```

**以 50% CPU 限制启动程序**

```cpulimit -l [50] -- [program] [arg1] [arg2]```

**在后台运行 cpulimit**

```cpulimit -l [50] -b -- [program]```

**同时限制子进程**

```cpulimit -l [25] -m -- [program]```

**在多核系统上限制**（200% = 2 个完整核心）

```cpulimit -p [1234] -l [200]```

# SYNOPSIS

**cpulimit** [_TARGET_] [_OPTIONS_...] [**--** _PROGRAM_]

# DESCRIPTION

**cpulimit** 通过发送 SIGSTOP 和 SIGCONT 信号来节流 CPU 消耗，从而限制进程的 CPU 使用率。它既可以作用于正在运行的进程，也可以在施加 CPU 限制的情况下启动新进程。

# PARAMETERS

**-p, --pid=N**
> 按 PID 定位目标进程

**-e, --exe=FILE**
> 按可执行文件名定位目标进程

**-P, --path=PATH**
> 按可执行文件的绝对路径定位目标进程

**-l, --limit=N**
> CPU 百分比限制（必填）。每个核心 1-100；多核系统上允许超过 100 的值（例如双核用 200）。

**-b, --background**
> 以后台进程方式运行 cpulimit

**-f, --foreground**
> 在等待被启动的进程期间保持前台运行

**-c, --cpu=N**
> 指定 CPU 核心数（用于百分比计算）

**-k, --kill**
> 超过限制时终止进程而非节流

**-m, --monitor-forks**
> 同时监视并限制子进程

**-r, --restore**
> 恢复之前用 -k 终止的进程

**-q, --quiet**
> 抑制输出消息

**-v, --verbose**
> 显示控制统计信息

**-z, --lazy**
> 若目标进程不存在或已终止则退出

# CAVEATS

使用 SIGSTOP 和 SIGCONT 信号，可能在 Shell 中产生误导性的作业控制消息。使用 -e 或 -P 时只会命中第一个匹配的进程；如需指定具体实例，请配合 PID 使用 -p。-m 选项可能对会派生大量进程的 Shell 脚本造成问题。

# HISTORY

**cpulimit** 的诞生是为了给 Linux 进程提供 CPU 使用率限制功能，可用于防止失控进程占用全部 CPU 资源。

# INSTALL

```apt: sudo apt install cpulimit```

```dnf: sudo dnf install cpulimit```

```apk: sudo apk add cpulimit```

```zypper: sudo zypper install cpulimit```

```brew: brew install cpulimit```

```nix: nix profile install nixpkgs#cpulimit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nice](/man/nice)(1), [renice](/man/renice)(1), [cgroups](/man/cgroups)(7), [kill](/man/kill)(1)
