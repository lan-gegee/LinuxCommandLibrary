# TAGLINE

创建虚拟环回音频设备

# TLDR

以默认行为创建**环回设备**

```pw-loopback```

创建自动连接到**扬声器**的环回设备

```pw-loopback -m '[FL FR]' -i 'media.class=Audio/Sink'```

创建自动连接到**麦克风**的环回设备

```pw-loopback -m '[FL FR]' -o 'media.class=Audio/Source'```

创建不自动连接的**哑环回（dummy loopback）**设备

```pw-loopback -m '[FL FR]' -i 'media.class=Audio/Sink' -o 'media.class=Audio/Source'```

创建向扬声器播放时**交换左右声道**的环回

```pw-loopback -i 'media.class=Audio/Sink audio.position=[FL FR]' -o 'audio.position=[FR FL]'```

# SYNOPSIS

**pw-loopback** [_options_]

# PARAMETERS

**-m**, **--channel-map** _map_
> 设置环回的声道映射

**-i**, **--capture-props** _props_
> 设置采集侧（sink）的属性

**-o**, **--playback-props** _props_
> 设置播放侧（source）的属性

**-h**, **--help**
> 显示帮助信息

# DESCRIPTION

**pw-loopback** 在 PipeWire 中创建虚拟环回音频设备。环回设备从一个源采集音频并将其播放到另一个目的地，实现应用之间或设备之间的音频路由。

该工具可以创建 sink 设备（用于捕获音频输出）、source 设备（用于提供音频输入），或用于音频监听和路由的组合式环回配置。

# CAVEATS

要获得正确的自动连接行为，必须正确指定声道映射和 media class 属性。配置不当可能导致音频路由问题或设备静音。

# HISTORY

**PipeWire**（Linux 上的现代多媒体框架）的一部分。提供与 PulseAudio 的 module-loopback 类似但基于 PipeWire 图架构的灵活音频路由能力。

# INSTALL

```apt: sudo apt install pipewire-bin```

```apk: sudo apk add pipewire-tools```

```zypper: sudo zypper install pipewire-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pipewire](/man/pipewire)(1), [pw-cli](/man/pw-cli)(1), [pw-link](/man/pw-link)(1)
