# TAGLINE

打印并修改 Java VM 配置

# TLDR

显示 JVM 标志

```jinfo [pid]```

显示系统属性

```jinfo -sysprops [pid]```

显示特定标志

```jinfo -flag [HeapDumpOnOutOfMemoryError] [pid]```

动态设置标志

```jinfo -flag +[HeapDumpOnOutOfMemoryError] [pid]```

取消标志

```jinfo -flag -[PrintGC] [pid]```

打印所有标志

```jinfo -flags [pid]```

# SYNOPSIS

**jinfo** [_options_] _pid_

# PARAMETERS

_PID_
> 目标 Java 进程 ID。

**-flags**
> 打印 VM 标志。

**-sysprops**
> 打印系统属性。

**-flag** _NAME_
> 打印或修改特定标志。

**+**_FLAG_
> 启用布尔型标志。

**-**_FLAG_
> 禁用布尔型标志。

**--help**
> 显示帮助信息。

# DESCRIPTION

**jinfo** 打印并修改 Java VM 配置。它显示运行中进程的系统属性和 VM 标志。

该工具可以动态修改可管理的标志。适合在不重启的情况下调整 JVM 行为。

# CAVEATS

JDK 的组成部分。并非所有标志都可修改。可能需要与目标进程相同的用户身份。

# HISTORY

jinfo 自 Java 5 起就是 **JDK** 的组成部分，提供运行时配置的查看与修改能力。

# SEE ALSO

[java](/man/java)(1), [jps](/man/jps)(1), [jstack](/man/jstack)(1)
