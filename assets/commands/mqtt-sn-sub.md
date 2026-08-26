# TAGLINE

从命令行订阅 MQTT-SN 主题

# TLDR

**订阅**主题

```mqtt-sn-sub -t [topic/name]```

**订阅**并显示详细的主题名

```mqtt-sn-sub -t [sensors/#] -v```

**订阅**并在收到一条消息后退出

```mqtt-sn-sub -t [topic] -1```

连接**远程网关**

```mqtt-sn-sub -h [192.168.1.10] -p [1883] -t [topic]```

**QoS 1** 订阅

```mqtt-sn-sub -t [topic] -q [1]```

带时间戳的详细输出

```mqtt-sn-sub -t [topic] -V```

# SYNOPSIS

**mqtt-sn-sub** [*opts*] **-t** *topic*

# DESCRIPTION

**mqtt-sn-sub** 是 **mqtt-sn-tools**（一个面向 MQTT-SN（MQTT for Sensor Networks）的 C 工具包）中的订阅工具。它通过 UDP 连接到 MQTT-SN 网关并打印收到的消息。主题参数可以重复；预定义主题 ID 可通过 **-T** 指定。

从上游仓库用 **make** 构建。配套工具包括 **mqtt-sn-pub**、**mqtt-sn-dump** 和 **mqtt-sn-serial-bridge**。

# PARAMETERS

**-t** *topic*

> 要订阅的主题（可重复）。在网关支持的情况下可包含 MQTT-SN 通配符。

**-T** *topicid*

> 要订阅的预定义主题 ID（可重复）。

**-1**

> 收到单条消息后退出。

**-c**

> 禁用干净会话（断开连接后仍保留订阅/待处理消息）。

**-h** *host* / **-p** *port*

> 网关主机（默认 **127.0.0.1**）和端口（默认 **1883**）。

**-q** *qos*

> 订阅 QoS **0** 或 **1**（默认 0）。

**-k** *seconds*

> 保活间隔（默认 10）。

**-i** *clientid*

> 客户端 ID（默认 **mqtt-sn-tools-** 加进程 ID）。

**-v** / **-V**

> 详细输出：显示主题名，或显示时间加主题名。

**-d**

> 提高调试级别（可重复）。

**--fe** / **--wlnid** / **--cport**

> 转发器封装、无线节点 id 和源端口选项。

# CAVEATS

需要 MQTT-SN 网关，而非普通 MQTT 代理。数据包大小限制为 255 字节；不支持 QoS 2。通配符行为取决于网关的支持程度。

# SEE ALSO

[mqtt-sn-pub](/man/mqtt-sn-pub)(1), [mqtt-sn-dump](/man/mqtt-sn-dump)(1), [mosquitto_sub](/man/mosquitto_sub)(1)

# RESOURCES

```[Source code](https://github.com/njh/mqtt-sn-tools)```

<!-- verified: 2026-07-19 -->
