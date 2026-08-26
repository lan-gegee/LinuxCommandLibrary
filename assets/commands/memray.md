# TAGLINE

跟踪内存分配的 Python 内存分析器

# TLDR

**分析内存使用**

```memray run [script.py]```

**指定输出文件进行分析**

```memray run -o [output.bin] [script.py]```

**生成火焰图**

```memray flamegraph [output.bin]```

**生成摘要报告**

```memray summary [output.bin]```

**实时内存视图**

```memray run --live [script.py]```

**启用原生跟踪进行分析**

```memray run --native [script.py]```

**生成树状视图**

```memray tree [output.bin]```

**附加到正在运行的进程**

```memray attach [pid]```

# SYNOPSIS

**memray** [_run_] [_flamegraph_] [_summary_] [_tree_] [_attach_] [_options_] [_args_]

# PARAMETERS

**run** _SCRIPT_
> 分析脚本的执行过程。

**flamegraph** _FILE_
> 生成火焰图 HTML。

**summary** _FILE_
> 显示分配摘要。

**tree** _FILE_
> 以树状视图显示内存分配。

**stats** _FILE_
> 显示统计信息。

**table** _FILE_
> 以表格显示内存分配。

**attach** _PID_
> 附加到正在运行的进程。

**-o** _FILE_, **--output** _FILE_
> 分析数据的输出文件。

**--live**
> 显示实时内存视图。

**--native**
> 跟踪原生（C/C++）内存分配。

**--follow-fork**
> 跟踪子进程。

**-f**, **--force**
> 覆盖已有的输出文件。

# DESCRIPTION

**memray** 用于分析 Python 内存分配，跟踪内存在何处被分配、由哪些代码分配。它有助于发现内存泄漏、内存峰值和分配模式。

该工具会记录每次分配和释放的堆栈跟踪。运行结束后的分析可生成可视化图表，展示内存随时间及按位置的使用情况。

火焰图展示分配调用栈，宽度代表分配大小，可以快速找出分配内存最多的函数。

实时模式在执行期间提供实时可视化，有助于理解长时间运行应用的内存行为。

原生跟踪会将 C 扩展的内存分配也纳入统计，而不仅是 Python 对象。这可以揭示 numpy、pandas 等含原生组件的库所占用的内存。

进程附加功能可对已在运行的应用进行性能分析，适合无需重启的生产环境调试。

# CAVEATS

跟踪开销会拖慢执行速度。大型分析文件会占用磁盘空间。原生跟踪需要调试符号才能输出可读结果。高度优化的代码中某些分配可能无法被捕获。

# HISTORY

**memray** 由 **Bloomberg** 开发，于 **2022 年**开源发布。其设计初衷是调试金融服务中大规模 Python 应用的内存问题。

# INSTALL

```apt: sudo apt install python3-memray```

```dnf: sudo dnf install python3-memray```

```pacman: sudo pacman -S memray```

```brew: brew install memray```

```nix: nix profile install nixpkgs#memray```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[py-spy](/man/py-spy)(1), [valgrind](/man/valgrind)(1)
