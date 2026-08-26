# TAGLINE

开源 MQTT 消息代理

# TLDR

**启动 MQTT 代理**

```mosquitto```

**使用配置文件启动**

```mosquitto -c [/etc/mosquitto/mosquitto.conf]```

**以详细模式启动**

```mosquitto -v```

**指定端口**

```mosquitto -p [1883]```

**以守护进程方式运行**

```mosquitto -d```

**指定日志文件**

```mosquitto -c [mosquitto.conf] --log-dest file [/var/log/mosquitto.log]```

# SYNOPSIS

**mosquitto** [_options_]

# PARAMETERS

**-c** _FILE_
> 配置文件。

**-p** _PORT_
> 监听端口。

**-v**
> 详细模式。

**-d**
> 以守护进程方式运行。

**--log-dest** _TYPE_
> 日志目标。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mosquitto** 是一个开源的 MQTT 消息代理。它实现了 MQTT 协议的 5.0、3.1.1 和 3.1 版本。

该工具处理发布/订阅消息，轻量且适用于 IoT（物联网）应用。

# CAVEATS

需要正确的安全配置。默认无身份验证。生产环境建议启用 TLS。

# HISTORY

mosquitto 由 **Roger Light** 于 **2009 年**前后创建，随后于 **2014 年**加入 **Eclipse 基金会**。它是一个轻量的开源 MQTT 代理，适合嵌入式和 IoT 应用。

# INSTALL

```apt: sudo apt install mosquitto```

```dnf: sudo dnf install mosquitto```

```pacman: sudo pacman -S mosquitto```

```apk: sudo apk add mosquitto```

```zypper: sudo zypper install mosquitto```

```brew: brew install mosquitto```

```nix: nix profile install nixpkgs#mosquitto```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mosquitto_pub](/man/mosquitto_pub)(1), [mosquitto_sub](/man/mosquitto_sub)(1)
