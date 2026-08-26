# TAGLINE

低开销的 Python 采样分析器

# TLDR

**分析运行中的进程**

```py-spy top --pid [pid]```

**记录到文件**

```py-spy record -o [profile.svg] --pid [pid]```

**转储调用栈**

```py-spy dump --pid [pid]```

**分析命令**

```py-spy record -o [output.svg] -- python [script.py]```

# SYNOPSIS

**py-spy** _command_ [_options_]

# PARAMETERS

**top**
> 类似 top 的实时视图。

**record**
> 记录到文件。

**dump**
> 转储栈回溯。

**--pid** _PID_
> 目标进程 ID。

**-o** _FILE_
> 输出文件。

**--rate** _N_
> 采样率。

# DESCRIPTION

**py-spy** 是一个针对 Python 程序的采样分析器，它通过读取运行中的 Python 解释器的进程内存来工作，无需修改任何代码或重启进程。这种方式带来的开销极小，因此适合分析生产环境的工作负载。

**top** 子命令提供 Python 时间花费位置的实时视图，类似于 Unix 的 **top** 工具。**record** 子命令生成 SVG、speedscope 或原始格式的火焰图以便详细分析，而 **dump** 在单个时间点捕获所有线程的栈回溯。py-spy 使用 Rust 编写，支持 CPython 解释器，并可通过 PID 附加到已在运行的进程。

# CAVEATS

分析其他用户的进程需要 root 权限。无需修改代码。

# HISTORY

py-spy 为 **低开销的 Python** 性能分析而生。

# INSTALL

```brew: brew install py-spy```

```nix: nix profile install nixpkgs#py-spy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[perf](/man/perf)(1), [python](/man/python)(1), [cProfile](/man/cProfile)(1)
