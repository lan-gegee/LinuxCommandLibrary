# TAGLINE

D-Bus 消息总线监控与调试工具

# TLDR

**监控会话总线**

```dbus-monitor```

**监控系统总线**

```dbus-monitor --system```

**按接口过滤**

```dbus-monitor "interface='[org.freedesktop.Notifications]'"```

**监控指定发送者**

```dbus-monitor "sender='[org.gnome.Shell]'"```

**仅监控方法调用**

```dbus-monitor "type='method_call'"```

**profile 模式**（机器可读）

```dbus-monitor --profile```

# SYNOPSIS

**dbus-monitor** [_options_] [_filter_...]

# DESCRIPTION

**dbus-monitor** 显示经过消息总线的 D-Bus 消息。它适用于调试 D-Bus 服务、理解进程间通信以及对应用行为进行逆向分析。

该工具连接到总线后成为一名窃听者，显示所有匹配指定过滤条件的消息。不带过滤器时显示全部消息。

# PARAMETERS

**--system**
> 监控系统总线。

**--session**
> 监控会话总线（默认）。

**--address** _addr_
> 连接到指定的总线地址。

**--profile**
> 以 profile 格式输出。

**--monitor**
> 以 monitor 格式输出（默认）。

**--pcap**
> 以 pcap 格式输出（可在 Wireshark 中加载）。

**--binary**
> 输出原始二进制消息。

# FILTER EXPRESSIONS

**type='signal'**: 信号消息
**type='method_call'**: 方法调用
**type='method_return'**: 方法返回
**type='error'**: 错误消息
**sender='name'**: 来自指定发送者
**destination='name'**: 发往指定目的地
**interface='name'**: 特定接口
**member='name'**: 特定方法/信号
**path='path'**: 特定对象路径

# CAVEATS

可能需要权限才能窃听。某些总线限制监控。高流量总线会产生大量输出。安全策略可能限制可见性。

# HISTORY

**dbus-monitor** 是 **Red Hat** 于 **2002 年**启动的 **D-Bus** 项目的一部分。D-Bus 成为 Linux 桌面的标准 IPC 机制，而 dbus-monitor 自项目早期起就是调试与开发的重要工具。

# INSTALL

```apt: sudo apt install dbus-bin```

```dnf: sudo dnf install dbus```

```pacman: sudo pacman -S dbus```

```apk: sudo apk add dbus```

```brew: brew install dbus```

```nix: nix profile install nixpkgs#dbus```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dbus-send](/man/dbus-send)(1), [busctl](/man/busctl)(1), [gdbus](/man/gdbus)(1), [qdbus](/man/qdbus)(1)

# RESOURCES

```[Source code](https://gitlab.freedesktop.org/dbus/dbus)```

```[Homepage](https://www.freedesktop.org/wiki/Software/dbus/)```

```[Documentation](https://dbus.freedesktop.org/doc/dbus-monitor.1.html)```

<!-- verified: 2026-07-11 -->
