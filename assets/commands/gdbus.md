# TAGLINE

用于 D-Bus 内省与交互的命令行工具

# TLDR

列出**会话总线**上的所有名称

```gdbus list-names --session```

列出**系统总线**上的所有名称

```gdbus list-names --system```

**内省**对象以查看其接口和方法

```gdbus introspect --session --dest [destination_bus_name] --object-path /[path/to/object]```

**调用对象的方法**并传递参数

```gdbus call --session --dest [destination_bus_name] --object-path /[path/to/object] --method [interface.method_name] [args...]```

**从对象发出信号**并附带参数

```gdbus emit --session --object-path /[path/to/object] --signal [interface.signal_name] [args...]```

**监视**会话总线上的所有消息

```gdbus monitor --session```

# SYNOPSIS

**gdbus** _command_ [_options_]

# PARAMETERS

**list-names**
> 列出总线上的所有名称

**introspect**
> 内省远程对象

**call**
> 调用远程对象上的方法

**emit**
> 发出信号

**monitor**
> 监视远程对象

**wait**
> 等待某个总线名出现

**--session**
> 连接到会话总线（用户专属）

**--system**
> 连接到系统总线（系统级）

**--dest** _NAME_
> 目标总线名

**--object-path** _PATH_
> D-Bus 对象路径

**--method** _INTERFACE.METHOD_
> 要调用的方法

**--signal** _INTERFACE.SIGNAL_
> 要发出的信号

# DESCRIPTION

**gdbus** 是一个与 D-Bus 交互的命令行工具。D-Bus 是 Linux 桌面环境中广泛使用的进程间通信系统。gdbus 属于 GLib 的一部分，可用于检查 D-Bus 对象、调用其方法并进行监视。

会话总线服务于用户应用程序（桌面通知、媒体播放器等），而系统总线处理系统级服务（NetworkManager、UPower 等）。

在与任何 D-Bus 对象交互之前，先用 **introspect** 发现其可用的接口和方法。

# CAVEATS

D-Bus 方法签名必须完全匹配。复杂类型需要正确的 GVariant 格式。某些系统总线操作需要提升权限或 PolicyKit 授权。

# HISTORY

gdbus 作为 GLib 的 GDBus 实现的一部分于 **2010 年**（GLib 2.26）推出，取代了较旧的 dbus-glib 绑定。它为 D-Bus 提供了更现代的、基于 GObject 的接口。

# INSTALL

```apt: sudo apt install libglib2.0-bin```

```dnf: sudo dnf install glib```

```apk: sudo apk add glib```

```brew: brew install glib```

```nix: nix profile install nixpkgs#glib```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dbus-send](/man/dbus-send)(1), [busctl](/man/busctl)(1), [qdbus](/man/qdbus)(1)

# RESOURCES

```[Documentation](https://docs.gtk.org/gio/gdbus.html)```

```[Source code](https://gitlab.gnome.org/GNOME/glib)```

<!-- verified: 2026-07-15 -->
