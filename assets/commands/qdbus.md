# TAGLINE

查询并与 D-Bus 服务交互

# TLDR

**列出 D-Bus 服务**

```qdbus```

**列出服务的对象**

```qdbus [org.freedesktop.DBus]```

**调用方法**

```qdbus [service] [object] [method]```

**获取属性**

```qdbus [service] [object] [property]```

# SYNOPSIS

**qdbus** [_options_] [_service_] [_object_] [_method_]

# PARAMETERS

_SERVICE_
> D-Bus 服务名。

_OBJECT_
> 对象路径。

_METHOD_
> 方法或属性。

**--system**
> 使用系统总线。

**--session**
> 使用会话总线。

**--literal**
> 原样输出回复内容。

# DESCRIPTION

**qdbus** 是一个基于 Qt 的命令行工具，用于与 Linux 桌面上的 D-Bus 服务交互。它可以列出可用的服务、浏览服务的对象层级、读写属性以及调用方法，因此非常适合调试、脚本编写和与桌面应用集成。

不带参数调用时，它会列出会话总线上的所有服务。加上服务名可以显示其对象路径，再加上对象路径则显示其接口和方法。**--system** 标志会切换到系统总线，用于与 NetworkManager 或 systemd 等系统级服务交互。

# CAVEATS

依赖 Qt。用于 D-Bus 交互。

# HISTORY

qdbus 是 **Qt** 中用于 D-Bus 交互的组成部分。

# INSTALL

```apt: sudo apt install qtchooser```

```dnf: sudo dnf install qtchooser```

```apk: sudo apk add qt5-qttools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dbus-send](/man/dbus-send)(1), [gdbus](/man/gdbus)(1)
