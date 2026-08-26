# TAGLINE

以 JSON 格式显示网络接口状态的 OpenWRT 工具

# TLDR

以 JSON 格式显示**接口状态**

```ifstatus [interface_name]```

显示**帮助**

```ifstatus```

# SYNOPSIS

**ifstatus** _interface_

# PARAMETERS

_interface_
> 要查询的网络接口名称

# DESCRIPTION

**ifstatus** 是一个 OpenWRT 工具，以 JSON 格式显示网络接口的状态。它向 netifd（网络接口守护进程）查询关于接口配置和状态的详细信息。

输出包括 IP 地址、DNS 服务器、连接状态、协议类型以及其他接口相关信息，采用机器可读的格式，适合脚本和自动化处理。

# CAVEATS

仅在 OpenWRT/LEDE 系统上可用。接口名称对应的是 netifd 逻辑接口，而非内核设备名。要求 netifd 正在运行。

# HISTORY

ifstatus 是 netifd 的组成部分，后者是 OpenWRT **12.09**（Attitude Adjustment）中引入的网络接口守护进程。它用更健壮的守护进程方案取代了旧的基于热插拔（hotplug）的网络配置系统。

# INSTALL

```aur: yay -S ifstatus```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ubus](/man/ubus)(1), [uci](/man/uci)(1)
