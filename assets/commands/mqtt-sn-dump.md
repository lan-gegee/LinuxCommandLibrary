# TAGLINE

转储指定端口上的 MQTT-SN UDP 数据包

# TLDR

在默认的 MQTT-SN 端口上**监听**

```mqtt-sn-dump -p [1883]```

**转储所有**数据包类型

```mqtt-sn-dump -p [1883] -a```

**详细模式**转储

```mqtt-sn-dump -p [1883] -v```

**调试**

```mqtt-sn-dump -p [1883] -d```

# SYNOPSIS

**mqtt-sn-dump** [*opts*] **-p** *port*

# DESCRIPTION

**mqtt-sn-dump** 是 **mqtt-sn-tools** 中的一个诊断工具，用于显示发送到本地 UDP 端口的 MQTT-SN 数据包。它对于观察来自受限客户端的 QoS **-1** 发布消息尤其有用——这类客户端使用 MQTT-SN 但不建立完整会话。

在 POSIX 系统上使用 **make** 构建。相关工具：**mqtt-sn-pub**、**mqtt-sn-sub**、**mqtt-sn-serial-bridge**。

# PARAMETERS

**-p** *port*

> 要监听的 UDP 端口（默认 **1883**）。

**-a**

> 转储所有数据包类型（而不仅是默认子集）。

**-v**

> 详细消息，包括可获取时的主题名。

**-d**

> 提高调试级别（可重复）。

# CAVEATS

需要绑定所选 UDP 端口的权限。它只显示送达本主机/端口的流量，并非完整的网络嗅探器。仅适用于 MQTT-SN：不用于 MQTT TCP 流量（**tcpdump** / **mosquitto** 工具覆盖该场景）。

# SEE ALSO

[mqtt-sn-pub](/man/mqtt-sn-pub)(1), [mqtt-sn-sub](/man/mqtt-sn-sub)(1), [tcpdump](/man/tcpdump)(1)

# RESOURCES

```[Source code](https://github.com/njh/mqtt-sn-tools)```

<!-- verified: 2026-07-19 -->
