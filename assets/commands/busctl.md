# TAGLINE

内省和监视 D-Bus 消息总线

# TLDR

显示总线上的所有**对等端**

```busctl list```

显示**用户会话总线**上的所有对等端

```busctl --user list```

显示服务或 PID 的**进程信息**

```busctl status [service|pid]```

**监视**总线上的消息

```busctl monitor [service1] [service2] ...```

**捕获** pcap 格式的总线流量

```busctl capture [service] > [bus-traffic.pcap]```

显示服务的**对象树**

```busctl tree [service1] [service2] ...```

**内省**对象的接口

```busctl introspect [service] [path/to/object]```

从对象**获取属性**值

```busctl get-property [service] [path/to/object] [interface_name] [property_name]```

在对象上**调用方法**

```busctl call [service] [path/to/object] [interface_name] [method_name]```

# SYNOPSIS

**busctl** [_command_] [_options_] [_arguments_]

# DESCRIPTION

**busctl** 用于内省和监视 D-Bus 消息总线。D-Bus 是一种进程间通信系统，在 Linux 上被广泛用于系统服务和桌面应用之间的通信。

该工具可以列出服务、监视消息流量、检查对象层级结构，以及调用 D-Bus 对象上的方法。

# SUBCOMMANDS

**list**
> 列出总线上的所有对等端

**status**
> 显示服务或 PID 的进程信息

**monitor**
> 监视消息流量

**capture**
> 捕获 pcap 格式的总线流量

**tree**
> 显示对象层级结构

**introspect**
> 检查对象接口

**get-property**
> 读取属性值

**set-property**
> 设置属性值

**call**
> 调用方法

**emit**
> 发出信号

**wait-signal**
> 等待特定信号

# PARAMETERS

**--system**
> 连接到系统总线（默认）。

**--user**
> 连接到用户会话总线。

**--address** _ADDRESS_
> 连接到 ADDRESS 指定的总线。

**-j**, **--json**=_MODE_
> 以 JSON 格式输出。MODE 为 short、pretty 或 off。

**--verbose**
> 为 call 或 get-property 命令显示详细输出。

**--expect-reply**=_BOOL_
> 是否等待方法调用完成。默认为 yes。

**--auto-start**=_BOOL_
> 方法调用是否应自动启动目标服务。默认为 yes。

**--list**
> tree 命令时显示扁平列表而不是树形结构。

**--unique**
> 只显示唯一的总线名称（如 :1.42）。

**--acquired**
> 只显示广为人知的总线名称。

**--activatable**
> 只显示尚未启动但可激活的服务。

**--no-pager**
> 禁用分页器。

**--no-legend**
> 不打印列头和页脚信息。

# INSTALL

```apt: sudo apt install elogind```

```apk: sudo apk add busctl```

```nix: nix profile install nixpkgs#elogind```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dbus-send](/man/dbus-send)(1), [dbus-monitor](/man/dbus-monitor)(1), [gdbus](/man/gdbus)(1), [systemctl](/man/systemctl)(1)
