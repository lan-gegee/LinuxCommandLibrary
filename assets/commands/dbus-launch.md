# TAGLINE

启动 D-Bus 会话总线实例的工具

# TLDR

**启动 D-Bus 会话**总线

```dbus-launch```

**启动会话并导出**环境变量

```eval $(dbus-launch --sh-syntax)```

**以自动启动选项启动**

```dbus-launch --autolaunch=[machine-id]```

**配合 D-Bus 启动指定程序**

```dbus-launch [program] [arguments]```

**程序终止时退出**

```dbus-launch --exit-with-session [program]```

**X 会话结束时关闭总线**

```dbus-launch --exit-with-x11```

# SYNOPSIS

**dbus-launch** [_options_] [_program_] [_args_]

# PARAMETERS

_PROGRAM_
> 与 D-Bus 会话一起运行的程序。

**--sh-syntax**
> 输出 Bourne shell 兼容的语法。

**--csh-syntax**
> 输出 C shell 兼容的语法。

**--auto-syntax**
> 根据 SHELL 变量检测 shell 类型并使用相应语法。

**--binary-syntax**
> 以二进制格式输出总线地址和 PID。

**--autolaunch** _MACHINEID_
> 使用指定的 machine ID 启用自动启动。

**--exit-with-session**
> 被启动的程序终止时退出。

**--exit-with-x11**
> X11 连接关闭时退出。

**--close-stderr**
> 启动守护进程前关闭 stderr。

**--config-file** _FILE_
> 使用指定配置文件而非 --session。

**--version**
> 打印 dbus-launch 的版本。

# DESCRIPTION

**dbus-launch** 启动 D-Bus 消息总线守护进程的会话实例，并向客户端应用提供连接地址。它通常用来确保桌面应用可以使用 D-Bus 会话。

不带参数调用时，它会打印客户端连接所需的环境变量（DBUS_SESSION_BUS_ADDRESS 和 DBUS_SESSION_BUS_PID）。配合 shell 语法选项，输出可直接被 eval 执行来设置这些变量。

指定程序时，dbus-launch 先启动 D-Bus 守护进程、设置好环境，然后执行该程序。--exit-with-session 标志确保程序退出时守护进程也随之终止。

# CAVEATS

没有妥善的会话管理时，多次调用可能启动多个守护进程。必须正确终止守护进程以避免资源泄漏。X11 集成需要活动的显示连接。

# HISTORY

dbus-launch 是 **D-Bus** 参考实现的一部分，后者由 **Red Hat** 和 freedesktop.org 项目于 **2003 年**前后创建。它成为需要进程间通信的 Linux 桌面环境的关键基础设施。

# INSTALL

```apt: sudo apt install dbus-x11```

```dnf: sudo dnf install dbus-x11```

```apk: sudo apk add dbus-x11```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dbus-daemon](/man/dbus-daemon)(1), [dbus-send](/man/dbus-send)(1), [dbus-monitor](/man/dbus-monitor)(1), [dbus-cleanup-sockets](/man/dbus-cleanup-sockets)(1)
