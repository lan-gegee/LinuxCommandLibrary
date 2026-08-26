# TAGLINE

检查 MQTT 代理是否允许连接的简易工具，可选择

# TLDR

**检查 MQTT 代理**是否允许匿名访问

```impacket-mqtt_check [192.168.1.100]```

**检查特定端口上的 MQTT**

```impacket-mqtt_check [192.168.1.100] -port [1883]```

使用凭据**检查 MQTT**

```impacket-mqtt_check [192.168.1.100] -user [username] -password [password]```

# SYNOPSIS

**impacket-mqtt_check** [_-h_] [_-port PORT_] [_-user USERNAME_] [_-password PASSWORD_] _target_

# PARAMETERS

**-port** _PORT_
> MQTT 代理端口（默认：1883）

**-user** _USERNAME_
> 用于 MQTT 身份验证的用户名

**-password** _PASSWORD_
> 用于 MQTT 身份验证的密码

# DESCRIPTION

**impacket-mqtt_check** 是一款简单的工具，用于检查 MQTT（Message Queuing Telemetry Transport）代理是否允许连接，并可选择测试匿名访问。MQTT 是一种轻量级消息协议，常见于 IoT 设备和应用中。

该工具尝试连接到指定的代理，并报告连接是否成功，帮助识别允许未经身份验证访问的错误配置代理。

# CAVEATS

仅测试连接能力，不枚举主题或消息。基于 TLS 的 MQTT（端口 8883）可能需要额外配置。某些代理允许建立连接，但会根据 ACL 限制操作。

# HISTORY

属于 SecureAuth 的 **Impacket** 库。加入此工具是为了应对围绕 IoT 协议日益增长的安全担忧，尤其是暴露在互联网上且缺乏适当身份验证的 MQTT 代理。

# INSTALL

```pacman: sudo pacman -S impacket```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mosquitto_sub](/man/mosquitto_sub)(1), [mosquitto_pub](/man/mosquitto_pub)(1), [nmap](/man/nmap)(1)
