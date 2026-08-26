# TAGLINE

Java 堆分析工具——解析 HPROF 堆转储并通过 HTTP 提供浏览服务

# TLDR

**分析堆转储文件**（在 http://localhost:7000 上提供服务）

```jhat [dump.hprof]```

使用自定义 HTTP 端口

```jhat -port [8080] [dump.hprof]```

为分析器本身**分配更多堆内存**

```jhat -J-Xmx8g [dump.hprof]```

与基线转储进行对比

```jhat -baseline [old.hprof] [new.hprof]```

禁用对象引用跟踪（更快、更省内存）

```jhat -stack false -refs false [dump.hprof]```

# SYNOPSIS

**jhat** [_options_] _heap-dump-file_

# PARAMETERS

**-stack** _true|false_
> 跟踪对象分配的调用栈（默认 `true`）。关闭可加快大型转储文件的加载速度。

**-refs** _true|false_
> 跟踪对象引用（默认 `true`）。关闭可减少内存占用；大多数引用查询将不可用。

**-port** _port_
> HTTP 服务器的 TCP 端口（默认 7000）。

**-exclude** _file_
> 指定一个文件的路径，其中列出的数据成员将在可达性查询中被排除。

**-baseline** _file_
> 指定基线转储。同时存在于两个转储中的对象会被标记为"非新增"。

**-debug** _int_
> 调试级别。`0` = 关闭，`1` = 解析 HPROF，`2` = 仅解析而不启动服务器。

**-version**
> 打印版本并退出。

**-J**_flag_
> 将 _flag_ 直接传给运行 jhat 的 JVM（如 `-J-Xmx8g`）。

**-help**
> 显示帮助。

# DESCRIPTION

**jhat** 解析 HPROF 二进制格式的 Java 堆转储文件，并启动一个小型 HTTP 服务器供浏览堆内容。其 Web 界面提供预置查询（某个类的实例、引用链、可达对象、直方图），以及一个可用于对堆进行任意查询的对象查询语言（OQL）输入界面。

堆转储可通过 `jmap -dump`、`jcmd <pid> GC.heap_dump`、`jconsole` 生成，也可通过在崩溃 JVM 上设置 `-XX:+HeapDumpOnOutOfMemoryError` 获得。

# CAVEATS

**jhat 在 JDK 8 中已被弃用（JEP 241），并在 JDK 9 中被移除。** 在现代 JDK 上，请改用 **jcmd**、**jmap -histo**、**VisualVM**、**Eclipse MAT** 或 **JProfiler**。HTTP 服务器默认绑定所有网络接口——请使用防火墙规则或 SSH 隧道，避免将堆内容暴露到网络上。

# HISTORY

**jhat** 于 **Java 6** 中引入，用于取代较旧的 `hat` 工具。它在 Java 8 中被弃用，并在 Java 9 中被移除，由功能更强大的第三方分析器接替。

# SEE ALSO

[jmap](/man/jmap)(1), [jstack](/man/jstack)(1), [jps](/man/jps)(1)
