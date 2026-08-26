# TAGLINE

输出 Java 进程的内存相关统计信息

# TLDR

**打印类加载器统计信息**

```jmap -clstats [pid]```

**将堆转储到文件**

```jmap -dump:format=b,file=[heap.hprof] [pid]```

**仅转储存活对象**

```jmap -dump:live,format=b,file=[heap.hprof] [pid]```

**对象直方图**

```jmap -histo [pid]```

**存活对象直方图**

```jmap -histo:live [pid]```

# SYNOPSIS

**jmap** [_options_] _pid_

# PARAMETERS

_PID_
> 目标 Java 进程 ID。

**-clstats** _pid_
> 打印 Java 堆的类加载器统计信息。

**-finalizerinfo** _pid_
> 打印等待 finalization 的对象信息。

**-histo**[**:live**]
> 打印 Java 对象堆的直方图。加上 :live 时只统计存活对象。

**-dump:**_options_
> 转储 Java 堆。子选项：

**:live**
> 仅存活对象。

**:format=b**
> 二进制 hprof 格式。

**:file=**_FILE_
> 输出文件路径。

# DESCRIPTION

**jmap** 输出 Java 进程的内存相关统计信息。它可以生成堆转储、对象直方图和类加载器统计信息。

该工具是内存分析和泄漏检测的利器。堆转储可以用 Eclipse MAT 或 VisualVM 等工具进行分析。

# CAVEATS

属于 JDK 的一部分。此命令是实验性且不受官方支持的，未来的 JDK 版本中可能不再提供。转储堆期间可能暂停应用程序。大堆会生成很大的转储文件。

# HISTORY

自 Java 5 起，jmap 就是 **JDK** 的组成部分，为运行中的 Java 进程提供内存分析能力。

# SEE ALSO

[jhat](/man/jhat)(1), [jstack](/man/jstack)(1), [jinfo](/man/jinfo)(1)
