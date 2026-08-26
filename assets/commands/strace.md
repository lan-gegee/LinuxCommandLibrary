# TAGLINE

跟踪系统调用和信号

# TLDR

**附加**到运行中的进程

```sudo strace -p 1234```

以**过滤**的系统调用跟踪进程

```sudo strace -p 1234 -e read,write```

显示调用与错误的**汇总**

```sudo strace -p 1234 -c```

显示每次调用的**耗时**

```sudo strace -p 1234 -T -s 32```

从头**跟踪**一个程序

```strace ./program```

仅跟踪**文件操作**

```strace -e trace=file ./program```

连同子进程一起跟踪**网络**操作

```strace -f -e trace=network -o trace.txt ./program```

# SYNOPSIS

**strace** [_-e expr_] [_-o file_] [_-p pid_] [_-f_] [_-c_] [_command_ [_args_]]

# DESCRIPTION

**strace** 拦截并记录进程发起的系统调用及其接收的信号。它对于调试、诊断和理解系统行为极具价值，而且不需要访问源代码。

# PARAMETERS

**-p, --attach pid**
> 附加到具有给定 PID 的运行中进程

**-f, --follow-forks**
> 跟踪由 fork/vfork/clone 创建的子进程

**-e trace=set**
> 仅跟踪指定的系统调用（file、network、process 等）

**-e signal=set**
> 仅跟踪指定的信号

**-o, --output file**
> 将跟踪输出写入文件

**-c, --summary-only**
> 退出时显示汇总统计

**-C, --summary**
> 在正常输出的同时显示汇总

**-t, -tt, -ttt**
> 添加时间戳（-t：HH:MM:SS，-tt：含微秒，-ttt：epoch 秒）

**-T, --syscall-times**
> 显示每次系统调用的耗时

**-s, --string-limit size**
> 打印字符串的最大长度（默认为 32）

**-v, --no-abbrev**
> 显示未缩写的输出

**-y, --decode-fds**
> 打印文件描述符关联的文件路径

**-z, --successful-only**
> 仅显示成功的系统调用

**-Z, --failed-only**
> 仅显示失败的系统调用

**-P, --trace-path path**
> 仅跟踪访问指定路径的系统调用

**-k, --stack-traces**
> 为每个系统调用打印堆栈跟踪

**-u, --user username**
> 以指定用户身份运行命令

# TRACE EXPRESSIONS

**%file**：文件操作（open、stat、chmod 等）
**%network**：网络操作（socket、connect 等）
**%process**：进程操作（fork、exec 等）
**%memory**：内存映射操作
**%signal**：信号相关调用
**%ipc**：IPC 操作（msgget、semop 等）
**%desc**：文件描述符操作（read、write、select 等）

# CAVEATS

跟踪会显著拖慢被跟踪的进程。在生产系统上使用时务必小心。请使用 **-f** 跟踪 fork 出的子进程，否则可能遗漏部分调用。

# HISTORY

**strace** 由 Paul Kranenburg 于 1991 年最初为 SunOS 编写。它已成为 Linux 系统上不可或缺的调试工具。

# INSTALL

```apt: sudo apt install strace```

```dnf: sudo dnf install strace```

```pacman: sudo pacman -S strace```

```apk: sudo apk add strace```

```zypper: sudo zypper install strace```

```brew: brew install strace```

```nix: nix profile install nixpkgs#strace```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ltrace](/man/ltrace)(1), [ptrace](/man/ptrace)(2), [perf](/man/perf)(1)
