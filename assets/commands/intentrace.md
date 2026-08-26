# TAGLINE

带有意图分析的 strace，实现更有意义的系统调用追踪

# TLDR

**追踪一条命令**

```intentrace [command]```

**按 PID 追踪运行中的进程**

```intentrace -p [pid]```

**只显示汇总表**

```intentrace -c [command]```

**跟踪子进程**（fork）

```intentrace -f [command]```

**只显示失败的系统调用**

```intentrace -Z [command]```

**将输出重定向到文件**

```intentrace -o [file] [command]```

# SYNOPSIS

**intentrace** [_options_] [_command_ [_args_...]]

# PARAMETERS

**-p** _pid_, **--attach** _pid_
> 按 PID 附着到运行中的进程。

**-c**, **--summary-only**
> 只显示汇总表。

**-C**, **--summary**
> 在正常输出之外额外显示汇总表。

**-f**, **--follow-forks**
> 当被追踪的程序创建子进程时一并追踪。

**-Z**, **--failed-only**
> 只显示失败的系统调用。

**-o** _file_, **--output** _file_
> 将输出重定向到文件。

**-q**, **--mute-stdout**
> 抑制被追踪程序的标准输出。

**--trace**=_syscall1,syscall2_
> 只追踪指定的系统调用。

# DESCRIPTION

**intentrace** 是一款系统调用追踪器，它在原始系统调用日志的基础上，借助大量积累的推断启发式规则来解释每个系统调用实际想完成什么。由于 Linux 系统调用经常被各种库以双重用途混淆，看到系统调用背后的意图在调试崩溃的二进制程序时极其有用。

传统 strace 输出只显示原始的系统调用号和参数，而 intentrace 会结合上下文提供每个系统调用所做事情的人类可读解释。

# CAVEATS

目前仅支持 **x86-64** Linux。覆盖 Linux 380 多个系统调用中的约 166 个，聚焦最常用的那些。该项目处于 beta 阶段；多线程程序可能无法可靠追踪。

# HISTORY

**intentrace** 由 **sectordistrict** 创建，使用 **Rust** 编写。它被设计为 strace 更具信息量的替代品，为每个系统调用提供上下文和含义，而不只是原始数据。

# INSTALL

```nix: nix profile install nixpkgs#intentrace```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[strace](/man/strace)(1), [ltrace](/man/ltrace)(1), [ptrace](/man/ptrace)(2)
