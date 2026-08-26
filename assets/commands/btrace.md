# TAGLINE

Java 应用动态跟踪工具

# TLDR

在运行中的 Java 应用里**跟踪方法调用**

```btrace [pid] [script.java]```

**带类路径进行跟踪**

```btrace -cp [/path/to/classes] [pid] [script.java]```

**以不安全模式跟踪**（允许更多操作）

```btrace -u [pid] [script.java]```

**编译 BTrace 脚本**

```btracec [script.java]```

**以调试输出运行**

```btrace -v [pid] [script.java]```

# SYNOPSIS

**btrace** [_options_] _pid_ _script_

**btracec** [_options_] _script_

# DESCRIPTION

**BTrace** 是一个面向 Java 平台的安全动态跟踪工具。它可以将跟踪脚本附加到运行中的 Java 应用上，而无需重启应用。BTrace 脚本用 Java 编写，并通过注解定义跟踪点。

BTrace 通过对目标应用的字节码插桩来工作。脚本可以拦截方法进入、退出、异常等事件。其跟踪机制在设计上注重安全，防止脚本修改应用状态或引发死锁。

常见用例包括性能剖析、调试生产问题、监控方法调用模式，以及在不重启应用的情况下追踪内存分配。

# PARAMETERS

**pid**
> 目标 Java 应用的进程 ID。

**script**
> BTrace 脚本文件（.java）。

**-v**
> 详细输出模式。

**-u**
> 不安全模式（启用更多操作）。

**-d** _path_
> 将插桩后的类转储到指定路径。

**-pd** _path_
> 探针描述符搜索路径。

**-cp** _classpath_
> 用于脚本编译的类路径。

**-I** _path_
> 预处理器包含路径。

**-p** _port_
> 代理服务器端口。

**-statsd** _host:port_
> 将指标发送到 StatsD 服务器。

# CAVEATS

目标 JVM 的 Java 版本必须相近或兼容。为避免损害应用，安全模式限制了某些操作。无法跟踪本地方法。在高频调用的方法上可能带来性能开销。需要对目标应用进程的写权限。

# HISTORY

**BTrace** 由 Sun Microsystems 的 **A. Sundararajan** 于 **2007-2008 年**前后创建，是一个受 DTrace 启发的 Java 工具。Oracle 收购 Sun 之后，该项目转为开源并由社区维护。它被广泛用于 Java 应用的生产环境调试和性能分析，填补了 JVM 生态中动态插桩的空白。

# INSTALL

```apt: sudo apt install blktrace```

```dnf: sudo dnf install blktrace```

```zypper: sudo zypper install blktrace```

```nix: nix profile install nixpkgs#blktrace```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jstack](/man/jstack)(1), [jmap](/man/jmap)(1), [java](/man/java)(1)
