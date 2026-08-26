# TAGLINE

用于进程间通信的消息总线守护进程

# TLDR

以**配置文件**运行

```dbus-daemon --config-file [path/to/file]```

运行**会话**消息总线

```dbus-daemon --session```

运行**系统**消息总线

```dbus-daemon --system```

设置要监听的**地址**

```dbus-daemon --address [address]```

将 **PID** 输出到 stdout

```dbus-daemon --print-pid```

以**前台**方式运行而不 fork

```dbus-daemon --session --nofork```

打印**版本**

```dbus-daemon --version```

# SYNOPSIS

**dbus-daemon** [_options_]

# DESCRIPTION

**dbus-daemon** 是 D-Bus 消息总线守护进程，用于在 Linux 和 Unix 系统上实现应用间的进程间通信（IPC）。它充当消息路由器，从一个应用接收消息，并依据总线名称和对象路径将其送达合适的目的地。

主要有两种总线类型：供桌面应用和用户服务使用的**会话总线**（每用户一个），以及供系统服务和硬件事件使用的**系统总线**（全系统）。会话总线在用户登录时创建，并在其会话期间存在。系统总线在启动时开启，并以提升的权限运行。

D-Bus 是现代 Linux 桌面环境和系统服务的基础设施。从通知投递到硬件管理，各种功能都依赖它。例如 NetworkManager、systemd、PulseAudio 以及大多数桌面应用都通过 D-Bus 通信。

该守护进程执行配置文件中定义的安全策略，控制哪些应用可以拥有总线名称、向特定服务发送消息以及接收广播。这防止了对敏感系统功能的未授权访问。

# PARAMETERS

**--config-file** _file_
> 使用指定的配置文件

**--session**
> 使用会话总线配置

**--system**
> 使用系统总线配置

**--address** _address_
> 覆盖监听地址

**--print-pid**[=_DESCRIPTOR_]
> 将 PID 打印到 stdout 或给定的文件描述符

**--print-address**[=_DESCRIPTOR_]
> 将总线地址打印到 stdout 或给定的文件描述符

**--syslog**
> 在 stderr 之外同时启用 syslog 日志

**--nofork**
> 即使配置为后台运行也不 fork

**--fork**
> 即使未配置也 fork 到后台

**--nopidfile**
> 即使配置要求也不写 PID 文件

**--nosyslog**
> 强制只输出到 stderr，不使用 syslog

**--syslog-only**
> 强制只记录到 syslog，不向 stderr 复制消息

**--introspect**
> 打印所有 D-Bus 内部接口的自省信息后退出

**--systemd-activation**
> 启用 systemd 风格的服务激活

**--version**
> 打印守护进程版本并退出

# CONFIGURATION

**/etc/dbus-1/system.conf**
> 系统总线配置文件，控制安全策略和允许的服务。

**/etc/dbus-1/session.conf**
> 会话总线配置模板，定义每用户的会话设置。

# CAVEATS

通常由 systemd 或会话管理器自动启动，很少需要直接调用。系统总线需要 root 权限。配置影响安全性和可用服务。

# INSTALL

```apt: sudo apt install dbus-daemon```

```dnf: sudo dnf install dbus-daemon```

```pacman: sudo pacman -S dbus```

```apk: sudo apk add dbus```

```brew: brew install dbus```

```nix: nix profile install nixpkgs#dbus```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dbus-send](/man/dbus-send)(1), [dbus-monitor](/man/dbus-monitor)(1), [dbus-launch](/man/dbus-launch)(1), [busctl](/man/busctl)(1)
