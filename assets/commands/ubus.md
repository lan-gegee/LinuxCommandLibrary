# TAGLINE

OpenWrt 系统消息总线客户端

# TLDR

**列出**可用对象

```ubus list```

获取**系统**信息

```ubus call system board```

**订阅**事件

```ubus subscribe [event_name]```

显示**帮助**

```ubus```

# SYNOPSIS

**ubus** _COMMAND_ [_OPTIONS_]

# COMMANDS

**list**
> 列出可用的 ubus 对象

**call** _OBJECT_ _METHOD_
> 调用对象上的某个方法

**subscribe** _EVENT_
> 订阅事件通知

**send** _EVENT_
> 发送一个事件

# DESCRIPTION

**ubus** 是用于与 OpenWrt ubusd 消息总线服务器交互的命令行界面。它允许不同系统服务之间通信，并提供对系统信息和配置的访问。

ubus 系统为 OpenWrt 路由器和嵌入式系统提供 IPC（进程间通信）能力，让脚本和应用程序能够查询和控制系统服务。

# CAVEATS

OpenWrt 专用。需要 ubusd 守护进程在运行。可用方法取决于已安装的服务。输出通常为 JSON 格式。

# HISTORY

**ubus** 作为 **OpenWrt** 系统架构的一部分开发，旨在为这款运行于路由器和嵌入式设备的轻量级 Linux 发行版提供统一的 IPC 机制。

# INSTALL

```nix: nix profile install nixpkgs#ubus```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[uci](/man/uci)(1), [opkg](/man/opkg)(1)
