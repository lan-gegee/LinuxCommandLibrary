# TAGLINE

订阅 MQTT 主题并打印收到的消息

# TLDR

**订阅主题**

```mosquitto_sub -t [sensors/temperature]```

**订阅所有主题**

```mosquitto_sub -t '#'```

**使用通配符订阅**

```mosquitto_sub -t '[sensors/+/temperature]'```

**连接远程代理**

```mosquitto_sub -h [broker.example.com] -t [topic]```

**带身份验证订阅**

```mosquitto_sub -h [broker] -u [username] -P [password] -t [topic]```

**以 TLS 订阅**

```mosquitto_sub -h [broker] --cafile [ca.crt] -t [topic]```

**显示详细输出**

```mosquitto_sub -v -t '[sensors/#]'```

**读取单条消息后退出**

```mosquitto_sub -t [topic] -C 1```

# SYNOPSIS

**mosquitto_sub** [_-h host_] [_-p port_] [_-t topic_] [_-u user_] [_-P pass_] [_options_]

# PARAMETERS

**-t** _TOPIC_
> 要订阅的主题（可重复）。

**-h** _HOST_
> 代理主机名。

**-p** _PORT_
> 代理端口（默认 1883）。

**-u** _USER_
> 用户名。

**-P** _PASSWORD_
> 密码。

**-i** _ID_
> 客户端 ID。

**-v**
> 详细输出（连同消息一起打印主题）。

**-C** _COUNT_
> 收到 count 条消息后退出。

**-q** _QOS_
> 服务质量（0、1、2）。

**--cafile** _FILE_
> 用于 TLS 的 CA 证书。

**--cert** _FILE_
> 客户端证书。

**--key** _FILE_
> 客户端私钥。

**-F** _FORMAT_
> 输出格式字符串。

**-N**
> 不在消息后追加换行符。

**--retained-only**
> 仅显示保留消息。

# DESCRIPTION

**mosquitto_sub** 用于订阅 MQTT 主题并打印收到的消息。MQTT 是一种面向 IoT 和遥测的轻量级发布/订阅消息协议。

主题采用以 / 分隔的分层命名。通配符可扩展订阅范围：+ 匹配一个层级，# 匹配其余所有层级。例如，sensors/+/temperature 匹配任意传感器的温度主题。

服务质量级别决定投递保证：QoS 0 为发完即忘，QoS 1 保证至少投递一次，QoS 2 保证恰好投递一次。

保留消息由代理存储，并在订阅时立即发送。这样新的订阅者就能获得最近一次已知的值。

TLS 加密保护通信安全。客户端证书可实现双向认证。代理必须配置为接受 TLS 连接。

# CAVEATS

在繁忙的代理上订阅 # 会产生巨大的消息量。QoS 2 的开销较大。命令行上的密码会在进程列表中可见。

# HISTORY

**mosquitto_sub** 是 **Eclipse Mosquitto** 项目（一套 MQTT 代理和客户端）的一部分。Mosquitto 由 **Roger Light** 自 **2009 年**前后创建，并于 **2014 年**加入 **Eclipse 基金会**。

# INSTALL

```apt: sudo apt install mosquitto-clients```

```apk: sudo apk add mosquitto-clients```

```zypper: sudo zypper install mosquitto-clients```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mosquitto_pub](/man/mosquitto_pub)(1), [mosquitto](/man/mosquitto)(8), [mosquitto_passwd](/man/mosquitto_passwd)(1)
