# TAGLINE

从命令行发布 MQTT-SN 消息

# TLDR

向主题**发布**消息

```mqtt-sn-pub -t [topic/name] -m ["hello"]```

向远程主机和端口**发布**

```mqtt-sn-pub -h [192.168.1.10] -p [1883] -t [sensors/temp] -m ["22.5"]```

以 QoS 1 和保留标志**发布**

```mqtt-sn-pub -t [topic] -m ["payload"] -q [1] -r```

将文件内容作为负载**发布**

```mqtt-sn-pub -t [topic] -f [payload.bin]```

**发布** stdin 的各行内容

```mqtt-sn-pub -t [topic] -l```

**发布**一条完整的 stdin 消息

```mqtt-sn-pub -t [topic] -s```

发送**空**（零长度）消息

```mqtt-sn-pub -t [topic] -n```

# SYNOPSIS

**mqtt-sn-pub** [*opts*] **-t** *topic* **-m** *message*

# DESCRIPTION

**mqtt-sn-pub** 是 **mqtt-sn-tools** 的一部分，这是一组面向 MQTT-SN（MQTT for Sensor Networks）协议的小型 C 语言工具。它通过 UDP 向 MQTT-SN 网关或代理发布消息。

在 POSIX 系统上从上游仓库用 **make** 构建。相关工具：**mqtt-sn-sub**、**mqtt-sn-dump**、**mqtt-sn-serial-bridge**。

该工具套件支持的功能包括 QoS 0、1 和 -1，保活，保留消息和空消息，干净/非干净会话，以及可选的转发器封装（MQTT-SN v1.2）。数据包必须不超过 255 字节；不支持 QoS 2、LWT 或自动网关发现。

# PARAMETERS

**-t** *topic*

> 要发布到的主题名。

**-T** *topicid*

> 使用预定义主题 ID 而不是名称。

**-m** *message*

> 消息负载字符串。

**-f** *file*

> 从文件读取负载。

**-l**

> 从 stdin 读取，每行一条消息。

**-s**

> 从 stdin 读取一整条消息。

**-n**

> 发送空（零长度）消息。

**-h** *host*

> 网关/代理主机（默认 **127.0.0.1**）。

**-p** *port*

> UDP 端口（默认 **1883**）。

**-q** *qos*

> 服务质量：**0**、**1** 或 **-1**（默认 0）。

**-r**

> 保留消息。

**-k** *seconds*

> 保活间隔（默认 10）。

**-i** *clientid*

> 客户端 ID（默认 **mqtt-sn-tools-** 加进程 ID）。

**-d**

> 提高调试级别（可重复）。

**--fe** / **--wlnid**

> 转发器封装与无线节点 id 选项。

**--cport** *port*

> 发出数据包的源端口。

# CAVEATS

MQTT-SN 不是基于 TCP 的 MQTT；你需要一个 MQTT-SN 网关。数据包大小上限为 255 字节。不会自动重传丢失的数据包。默认端口 1883 与许多网关一致，但请确认你的部署配置。

# SEE ALSO

[mqtt-sn-sub](/man/mqtt-sn-sub)(1), [mqtt-sn-dump](/man/mqtt-sn-dump)(1), [mosquitto_pub](/man/mosquitto_pub)(1)

# RESOURCES

```[Source code](https://github.com/njh/mqtt-sn-tools)```

<!-- verified: 2026-07-19 -->
