# TAGLINE

用于订阅和发布 MQTT 消息的 TUI 工具

# TLDR

在 broker 上**订阅所有主题**

```mqttui```

**连接到特定的 broker**

```mqttui mqtt://[host]:[port]```

**订阅特定主题**

```mqttui "[topic]"```

**发布一条消息**

```mqttui publish "[topic]" "[message]"```

# SYNOPSIS

**mqttui** [_options_] [_topic_]

# PARAMETERS

**publish** _TOPIC_ _MESSAGE_
> 向某个主题发布消息。

**clean-retained** _TOPIC_
> 清除某个主题的保留消息。

# DESCRIPTION

**mqttui** 是一个 TUI 工具，可在终端中订阅 MQTT 主题并发布消息。它显示带有实时消息更新的主题树，并支持保留消息管理。

可以通过 **MQTTUI_BROKER** 环境变量配置默认的 broker，以免每次都要手动指定。

# CAVEATS

需要能够访问 MQTT broker。在消息繁忙的 broker 上订阅宽泛的主题可能产生大量消息。

# HISTORY

**mqttui** 由 **EdJoPaTo** 创建，使用 **Rust** 编写。

# INSTALL

```pacman: sudo pacman -S mqttui```

```apk: sudo apk add mqttui```

```brew: brew install mqttui```

```nix: nix profile install nixpkgs#mqttui```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mosquitto_sub](/man/mosquitto_sub)(1), [mosquitto_pub](/man/mosquitto_pub)(1)
