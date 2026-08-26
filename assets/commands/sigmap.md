# TAGLINE

在信号传递给子进程的途中进行映射

# TLDR

为 sleep **将 SIGWINCH（28）转换为 SIGINT（2）**

```sigmap -m 28:2 /bin/sleep 30```

向长期运行的守护进程**以 SIGHUP 形式转发 SIGTERM**

```sigmap -m 15:1 [path/to/program] [args]```

通过重复 -m **一次重映射多个信号**

```sigmap -m 1:15 -m 2:15 [path/to/program]```

# SYNOPSIS

**sigmap** **-m** _from_:_to_ [**-m** _from_:_to_ ...] _program_ [_arguments_]

# PARAMETERS

**-m** _from_:_to_, **--map=**_from_:_to_
> 在转发给子进程时把信号 _from_ 转换为信号 _to_。两个值都是 **signal(7)** 中列出的整数信号编号。该选项可重复使用以安装多个映射。

_program_
> 要启动的可执行文件路径。由于 **sigmap** 使用 **execve(2)**，必须是绝对或相对路径；**不会**进行 **PATH** 查找。

_arguments_
> 原样转发给被启动的程序。

# DESCRIPTION

**sigmap** 是一个小型包装器，用于启动子进程并改写传递给它的信号。包装器为命令行上列出的每个 _from_ 信号安装处理程序；当内核把 _from_ 递送给 **sigmap** 时，包装器改为向子进程发送对应的 _to_ 信号。未列出的信号原样通过。

当某个进程坚持发出被包装程序不理解的信号、shell 与应用对哪个信号表示"重新加载"意见不一而需要桥接，或要让旧软件适配不同的监督进程时，这个工具就很有用。由于改写完全发生在包装器内，子进程只会看到转换后的信号，无需任何修改。

**sigmap** 使用 **execve(2)** 启动子进程，因此解析出的二进制文件必须是带完整路径的真实可执行文件。Shell 内建命令、别名以及依赖 **PATH** 的裸程序名都无法使用。

# EXAMPLES

让 SIGTERM 表现得像守护进程的一次优雅 SIGHUP 重载：

```sigmap -m 15:1 /usr/local/sbin/myd```

捕获终端尺寸变化事件并转为 SIGINT，使脚本在窗口改变大小时退出：

```sigmap -m 28:2 /usr/local/bin/myscript```

# CAVEATS

信号编号在不同架构间**不可移植**：**SIGUSR1** 在 x86 Linux 上是 **10**，但在 Alpha 上是 **30**。硬编码数字之前务必查阅目标平台上的 **signal(7)**。实时信号（**SIGRTMIN**+_n_）可以重映射，但其数值取决于 C 库。**SIGKILL (9)** 和 **SIGSTOP (19)** 无法被捕获，因此不能重映射。

# HISTORY

**sigmap** 是 Martin Jacobsson 发布在 GitHub 上的开源工具，作为一个极简的 Unix 信号转换器。它刻意保持小巧，仅依赖 POSIX C 运行时，便于放入容器和精简的 init 系统中。

# SEE ALSO

[kill](/man/kill)(1), [trap](/man/trap)(1)
