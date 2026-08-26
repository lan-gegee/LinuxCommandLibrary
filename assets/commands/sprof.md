# TAGLINE

读取并显示共享对象的性能剖析数据

# TLDR

**设置剖析**：通过启用剖析的方式运行程序，为共享库收集数据

```LD_PROFILE=[libfoo.so.1] LD_PROFILE_OUTPUT=[/tmp/prof] [./myprogram]```

**显示平直剖析和调用图**（默认输出）

```sprof [libfoo.so.1] [libfoo.so.1.profile]```

**仅显示平直剖析**

```sprof -p [libfoo.so.1] [libfoo.so.1.profile]```

**仅显示调用图**

```sprof -q [libfoo.so.1] [libfoo.so.1.profile]```

**显示调用对**

```sprof -c [libfoo.so.1] [libfoo.so.1.profile]```

# SYNOPSIS

**sprof** [_option_ ...] _shared-object-path_ [_profile-data-path_]

# PARAMETERS

**-c**, **--call-pairs**
> 打印共享对象导出接口的调用路径对列表，以及每条路径被使用的次数。

**-p**, **--flat-profile**
> 生成被监控对象中所有函数的平直剖析，包含计数和时钟周期。

**-q**, **--graph**
> 生成调用图。

**-?**, **--help**
> 显示命令行选项和参数的摘要并退出。

**--usage**
> 显示简短的用法信息并退出。

**-V**, **--version**
> 显示程序版本并退出。

# DESCRIPTION

**sprof** 显示以第一个命令行参数指定的共享对象（共享库）的剖析摘要。剖析摘要基于可选的第二个参数中先前生成的剖析数据。如果省略剖析数据路径，sprof 会在当前目录下查找名为 **\<soname\>.profile** 的文件。

剖析数据通过将环境变量 **LD_PROFILE** 设为共享库的 soname 来生成，还可以选择把 **LD_PROFILE_OUTPUT** 设为存放剖析数据文件的目录。之后运行任何加载该库的应用程序时，动态链接器都会自动收集剖析数据。

如果未指定 **-c**、**-p**、**-q** 中的任何一个，默认行为是同时显示平直剖析和调用图。

# CAVEATS

通过 **LD_PROFILE** 一次只能剖析一个共享库。使用 sprof 时不要用 **-pg** 编译；gprof 的剖析标志会干扰 sprof，导致执行时间全为零。sprof 是 GNU 扩展，POSIX 未对其作规定。需要 glibc 2.5-34 或更新版本；较旧版本可能因缺少内部标志而失败。

# HISTORY

**sprof** 由 **Ulrich Drepper** 编写，是 **GNU C 库（glibc）** 的一部分，约在 **1997 年**的 **glibc 2.0** 中首次出现。它旨在填补 **gprof** 无法剖析共享库的空白。剖析数据的收集由 glibc 动态链接器本身完成，这使 sprof 独一无二地能够在不重新编译的情况下剖析共享对象。

# INSTALL

```apt: sudo apt install libc-devtools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gprof](/man/gprof)(1), [ldd](/man/ldd)(1), [ld](/man/ld)(1), [perf](/man/perf)(1)
