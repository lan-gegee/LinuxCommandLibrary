# TAGLINE

列出 Java 虚拟机进程

# TLDR

**列出 Java 进程**

```jps```

**显示完整类名**

```jps -l```

**显示 JVM 参数**

```jps -v```

**显示主类参数**

```jps -m```

**显示全部信息**

```jps -lvm```

**查询远程主机**

```jps -l [hostname]```

# SYNOPSIS

**jps** [_options_] [_hostid_]

# PARAMETERS

_HOSTID_
> 要查询的远程主机。

**-l**
> 显示主类的完整包名或 JAR 文件的完整路径。

**-v**
> 显示传给 JVM 的参数。

**-m**
> 显示传给 main 方法的参数。

**-q**
> 不显示类名/参数，仅显示本地 JVM 标识符（PID）。

**-V**
> 与 -q 相同：仅列出本地 JVM 标识符。

**-help**
> 显示 jps 的帮助信息。

# DESCRIPTION

**jps** 列出 Java 虚拟机进程。它显示正在运行的 Java 应用程序及其 PID。

该工具相当于面向 Java 进程的 ps，可快速识别系统中的 Java 应用。

# CAVEATS

属于 JDK 的一部分。仅显示 JVM 进程。需要相同用户身份或相应权限。

# HISTORY

自 Java 5 起，jps 就是 **JDK** 的组成部分，为 Java 应用管理提供进程列表功能。

# SEE ALSO

[java](/man/java)(1), [jstack](/man/jstack)(1), [jmap](/man/jmap)(1), [ps](/man/ps)(1)
