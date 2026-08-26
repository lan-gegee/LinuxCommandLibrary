# TAGLINE

用于 MQTT 监控的 Nagios 插件

# TLDR

**检查 MQTT broker**

```mqtt_check.py -H [broker.example.com]```

**带身份验证进行检查**

```mqtt_check.py -H [host] -u [user] -p [password]```

**检查特定端口**

```mqtt_check.py -H [host] -P [1883]```

**使用 SSL 进行检查**

```mqtt_check.py -H [host] --ssl```

**设置超时时间**

```mqtt_check.py -H [host] -t [10]```

# SYNOPSIS

**mqtt_check.py** [_options_]

# PARAMETERS

**-H** _HOST_
> MQTT broker 的主机名。

**-P** _PORT_
> MQTT broker 的端口。

**-u** _USER_
> 用于身份验证的用户名。

**-p** _PASSWORD_
> 用于身份验证的密码。

**--ssl**
> 使用 SSL/TLS 连接。

**-t** _SECONDS_
> 连接超时时间。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mqtt_check.py** 是一个用于 MQTT 监控的 Nagios 插件。它检查 MQTT broker 的可用性。

该工具验证与 broker 的连通性，并返回供监控系统使用的状态码。

# CAVEATS

Nagios 插件格式。需要 paho-mqtt。Python 脚本。

# HISTORY

mqtt_check.py 为 **Nagios/Icinga** 监控而创建，用于提供 MQTT broker 健康检查。

# INSTALL

```apk: sudo apk add py3-impacket```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mosquitto](/man/mosquitto)(1), [mosquitto_pub](/man/mosquitto_pub)(1), [nagios](/man/nagios)(1)
