# TAGLINE

Java HotSpot Serviceability Agent 调试器

# TLDR

将调试器附加到进程

```jhsdb clhsdb --pid [pid]```

分析核心转储

```jhsdb hsdb --core [core] --exe [java]```

打印 Java 堆栈跟踪

```jhsdb jstack --pid [pid]```

堆分析

```jhsdb jmap --pid [pid] --heap```

混合模式堆栈跟踪

```jhsdb jstack --mixed --pid [pid]```

启动 GUI 调试器

```jhsdb hsdb --pid [pid]```

# SYNOPSIS

**jhsdb** _command_ [_options_]

# PARAMETERS

**clhsdb**
> 命令行 HotSpot 调试器。

**hsdb**
> GUI HotSpot 调试器。

**jstack**
> 打印堆栈跟踪。

**jmap**
> 内存映射工具。

**jinfo**
> 配置信息。

**--pid** _PID_
> 目标进程 ID。

**--core** _FILE_
> 核心转储文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**jhsdb** 是 Java HotSpot Serviceability Agent 调试器。它分析 JVM 进程和核心转储。

该工具提供低层级的 JVM 调试能力。它可以检查堆、栈和内部结构。

# CAVEATS

JDK 的组成部分。要求与目标相同的 JDK 版本。完整分析可能需要符号文件。

# HISTORY

jhsdb 于 **JDK 9** 中引入，作为统一工具取代了各自独立的服务性代理命令。

# SEE ALSO

[jstack](/man/jstack)(1), [jmap](/man/jmap)(1), [jinfo](/man/jinfo)(1)
