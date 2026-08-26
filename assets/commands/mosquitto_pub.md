# TAGLINE

向 MQTT 代理发布消息

# TLDR

**向主题发布消息**

```mosquitto_pub -t [topic] -m "[message]"```

**向远程代理发布消息**

```mosquitto_pub -h [broker.example.com] -t [topic] -m "[message]"```

**带身份验证发布消息**

```mosquitto_pub -h [host] -u [user] -P [password] -t [topic] -m "[message]"```

**发布文件内容**

```mosquitto_pub -t [topic] -f [file.txt]```

**以指定 QoS 发布消息**

```mosquitto_pub -t [topic] -m "[message]" -q [1]```

**发布保留消息**

```mosquitto_pub -t [topic] -m "[message]" -r```

# SYNOPSIS

**mosquitto_pub** [_options_]

# PARAMETERS

**-h** _HOST_
> MQTT 代理主机名。

**-t** _TOPIC_
> 要发布到的主题。

**-m** _MESSAGE_
> 消息负载。

**-u** _USER_
> 用户名。

**-P** _PASSWORD_
> 密码。

**-q** _QOS_
> 服务质量（0、1、2）。

**-r**
> 保留消息。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mosquitto_pub** 用于向 MQTT 代理发布消息。它是 Mosquitto 软件包的一部分。

该工具发送单条消息，支持身份验证、TLS 和多种 QoS 级别。

# CAVEATS

属于 mosquitto-clients 的一部分。需要能够访问代理。默认 QoS 为 0。

# HISTORY

mosquitto_pub 是随 Eclipse Mosquitto MQTT 代理一起分发的**发布客户端**。

# INSTALL

```apt: sudo apt install mosquitto-clients```

```apk: sudo apk add mosquitto-clients```

```zypper: sudo zypper install mosquitto-clients```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mosquitto_sub](/man/mosquitto_sub)(1), [mosquitto](/man/mosquitto)(1)
