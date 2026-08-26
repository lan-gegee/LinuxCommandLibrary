# TAGLINE

输出指定 Java 进程的线程堆栈跟踪

# TLDR

**输出 Java 进程的线程转储**

```jstack [pid]```

**对挂起进程强制线程转储**

```jstack -F [pid]```

**输出并发锁信息**

```jstack -l [pid]```

**输出混合模式堆栈跟踪**

```jstack -m [pid]```

# SYNOPSIS

**jstack** [_options_] _pid_

# PARAMETERS

**-F**
> 进程挂起时强制执行线程转储。

**-l**
> 长列表格式，包含锁信息。

**-m**
> 输出混合模式（Java 与本地方法）的堆栈跟踪。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**jstack** 输出指定 Java 进程的线程堆栈跟踪。它可用于诊断死锁和性能问题、分析线程状态。属于 JDK 诊断工具套件的组成部分。

# CAVEATS

目标进程必须以相同用户运行，否则需要 root 权限。-F 选项只应在进程无响应时使用。

# SEE ALSO

[jps](/man/jps)(1), [jmap](/man/jmap)(1)
