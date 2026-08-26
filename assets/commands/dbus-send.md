# TAGLINE

命令行 D-Bus 方法调用与信号发送

# TLDR

**向服务发送方法调用**

```dbus-send --session --dest=[org.freedesktop.Notifications] [/org/freedesktop/Notifications] [org.freedesktop.Notifications.GetCapabilities]```

**通过 D-Bus 发送通知**

```dbus-send --session --dest=org.freedesktop.Notifications /org/freedesktop/Notifications org.freedesktop.Notifications.Notify string:"app" uint32:0 string:"" string:"[Title]" string:"[Body]" array:string:"" dict:string:string:"" int32:5000```

**列出会话总线上可用的服务**

```dbus-send --session --dest=org.freedesktop.DBus --print-reply /org/freedesktop/DBus org.freedesktop.DBus.ListNames```

**调用系统总线**的方法

```dbus-send --system --print-reply --dest=[org.freedesktop.hostname1] [/org/freedesktop/hostname1] [org.freedesktop.DBus.Properties.GetAll] string:"[org.freedesktop.hostname1]"```

**获取属性值**

```dbus-send --session --print-reply --dest=[destination] [object_path] org.freedesktop.DBus.Properties.Get string:"[interface]" string:"[property]"```

# SYNOPSIS

**dbus-send** [_options_] **--dest=**_NAME_ _object-path_ _message_ [_args_...]

# PARAMETERS

**--session**
> 发送到会话总线。

**--system**
> 发送到系统总线。

**--dest** _NAME_
> 目标服务名。

**--print-reply**
> 阻塞等待回复，并以人类可读的形式打印结果。

**--print-reply=literal**
> 打印回复时不对字符串值转义、不加引号。

**--type** _TYPE_
> 消息类型：method_call（默认）或 signal。

**--reply-timeout=**_MSEC_
> 等待回复的超时时间（毫秒）（默认：25000）。

_OBJECT-PATH_
> D-Bus 对象路径（例如 /org/freedesktop/DBus）。

_MESSAGE_
> 包含接口的方法或信号名（例如 org.freedesktop.DBus.ListNames）。

**string:**, **int32:**, **uint32:**, **boolean:**, **double:**, **byte:**, **objpath:**
> 追加到消息中的带类型参数。

**--help**
> 显示帮助信息。

# DESCRIPTION

**dbus-send** 向 D-Bus 消息总线（系统总线或会话总线）发送消息。它可以调用 D-Bus 对象上的方法或发出信号，并可选择等待并打印回复。

该命令适用于在脚本中与 D-Bus 服务交互、调试 D-Bus 接口以及测试服务实现。参数需带类型标注（string:、int32:、boolean: 等），以构造类型正确的 D-Bus 消息。

常见用例包括发送桌面通知、查询系统属性，以及控制媒体播放器或其他暴露 D-Bus 接口的桌面服务。

# CAVEATS

包含嵌套类型的复杂方法调用难以构造。系统总线上的方法通常需要提升的权限。缺少 --print-reply 时响应会被忽略。类型标注必须与服务端的期望完全匹配。

# HISTORY

dbus-send 是 **D-Bus** 参考实现的一部分，由 **Red Hat** 和 freedesktop.org 自 **2003 年**起开发。它为 Linux 桌面环境中广泛使用的 D-Bus 进程间通信系统提供命令行访问方式。

# INSTALL

```apt: sudo apt install dbus-bin```

```dnf: sudo dnf install dbus```

```pacman: sudo pacman -S dbus```

```apk: sudo apk add dbus```

```brew: brew install dbus```

```nix: nix profile install nixpkgs#dbus```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dbus-daemon](/man/dbus-daemon)(1), [dbus-launch](/man/dbus-launch)(1), [dbus-monitor](/man/dbus-monitor)(1), [busctl](/man/busctl)(1), [gdbus](/man/gdbus)(1), [qdbus](/man/qdbus)(1)
