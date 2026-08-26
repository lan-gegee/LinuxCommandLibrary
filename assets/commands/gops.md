# TAGLINE

Go 进程诊断工具

# TLDR

**列出 Go 进程**

```gops```

**显示进程详情**

```gops [pid]```

**转储堆栈跟踪**

```gops stack [pid]```

**查看内存统计**

```gops memstats [pid]```

**生成 CPU 剖析**

```gops pprof-cpu [pid]```

# SYNOPSIS

**gops** [_command_] [_pid_]

# PARAMETERS

_PID_
> 进程 ID。

**stack** _PID_
> 打印堆栈跟踪。

**memstats** _PID_
> 显示内存统计。

**pprof-cpu** _PID_
> 生成 CPU 剖析。

**pprof-heap** _PID_
> 生成堆内存剖析。

**gc** _PID_
> 触发垃圾回收。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gops** 用于列出并诊断系统中运行的 Go 进程。它能识别 Go 程序，并提供堆栈跟踪、内存统计以及 CPU/堆剖析等调试命令。

要使用完整的诊断能力，必须在目标程序中引入 gops agent。不引入 agent 也可以进行基本的进程识别。

# CAVEATS

完整功能需要引入 agent。仅兼容特定版本的 Go。部分信息来自 /proc。

# HISTORY

gops 由 Google 的 **Jaana Dogan** 创建，用于为 Go 进程提供诊断工具。

# INSTALL

```dnf: sudo dnf install gops```

```apk: sudo apk add gops```

```zypper: sudo zypper install gops```

```brew: brew install gops```

```nix: nix profile install nixpkgs#gops```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[go-tool](/man/go-tool)(1), [pprof](/man/pprof)(1)

# RESOURCES

```[Source code](https://github.com/google/gops)```

<!-- verified: 2026-07-17 -->
