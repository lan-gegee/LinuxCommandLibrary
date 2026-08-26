# TAGLINE

实时诊断和排查 Java 应用。

# TLDR

**附加到** Java 进程

```java -jar arthas-boot.jar [PID]```

**交互式**选择进程

```java -jar arthas-boot.jar```

以**指定端口**附加

```java -jar arthas-boot.jar --telnet-port [3658] --http-port [8563] [PID]```

# SYNOPSIS

**arthas-boot.jar** [_--telnet-port port_] [_--http-port port_] [_pid_]

# DESCRIPTION

**Arthas** 是阿里巴巴开源的 Java 诊断工具。它可以在不停止应用、不修改代码的情况下对 Java 应用进行实时监控和故障排查。

功能包括方法追踪、类反编译、监控指标，以及对运行中的 JVM 进行 OGNL 表达式求值。

# PARAMETERS

**pid**
> 要附加的 Java 进程 ID

**--telnet-port** _port_
> Telnet 控制台端口

**--http-port** _port_
> HTTP API 端口

**--target-ip** _ip_
> 要绑定的 IP 地址

**--tunnel-server** _url_
> 隧道服务器 URL

# COMMON COMMANDS

**dashboard**
> 系统总览

**trace** _class_ _method_
> 追踪方法执行

**watch** _class_ _method_
> 观察方法的输入/输出

**jad** _class_
> 反编译类

**sc** _pattern_
> 搜索已加载的类

**thread**
> 显示线程信息

**monitor** _class_ _method_
> 监控方法的统计信息

# CONFIGURATION

**~/.arthas/arthas.properties**
> Telnet 端口、HTTP 端口、目标 IP 和隧道服务器等设置的默认配置。

# CAVEATS

附加到生产环境的 JVM 应当谨慎操作。部分功能可能影响性能。需要版本兼容的 JVM。

# HISTORY

**Arthas** 由阿里巴巴开发，于 **2018** 年开源。它已成为广受欢迎的 Java 诊断工具，在中文开发者社区尤为流行。

# INSTALL

```aur: yay -S arthas```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[jstack](/man/jstack)(1), [jmap](/man/jmap)(1)
