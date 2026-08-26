# TAGLINE

调试 PipeWire 的 ALSA 声卡配置（profile）

# TLDR

**列出**所有 ALSA 对象

```spa-acp-tool list```

**探测**指定的 ALSA 声卡

```spa-acp-tool card [card_id]```

列出声卡可用的 **profile**

```spa-acp-tool list-profiles [card_id]```

**设置**活动 profile

```spa-acp-tool set-profile [profile_id]```

列出可用的**设备**

```spa-acp-tool list-devices [card_id]```

**获取设备音量**

```spa-acp-tool get-volume [device_id]```

**设置设备音量**

```spa-acp-tool set-volume [device_id] [volume]```

**切换设备静音状态**

```spa-acp-tool toggle-mute [device_id]```

# SYNOPSIS

**spa-acp-tool** [_OPTIONS_] [_COMMAND_]

# PARAMETERS

**-h, --help**
> 显示帮助信息

**-v, --verbose**
> 提高输出详细程度

**-c, --card** _number_
> 选择要探测的指定声卡

**-p, --properties** _key=value_
> 向 ACP 传递额外属性

# COMMANDS

**list, l**
> 列出所有 ALSA 对象

**list-verbose, lv**
> 列出对象及其详细信息

**card, c** _id_
> 探测指定的声卡

**info, i**
> 显示声卡信息

**list-profiles, lpr**
> 列出可用的 profile

**set-profile, spr** _id_
> 设置活动 profile

**list-ports, lp** [_id_]
> 列出可用的端口

**set-port, sp** _id_
> 设置活动端口

**list-devices, ld** [_id_]
> 列出可用的设备

**get-volume, gv** _id_
> 获取设备音量

**set-volume, v** _id_ _level_
> 设置设备音量

**inc-volume, v+** _id_
> 增大设备音量

**dec-volume, v-** _id_
> 减小设备音量

**get-mute, gm** _id_
> 获取设备静音状态

**set-mute, sm** _id_ _value_
> 设置设备静音状态

**toggle-mute, m** _id_
> 切换设备静音状态

**help, h**
> 显示可用命令

**quit, q**
> 退出工具

# DESCRIPTION

**spa-acp-tool** 是一个调试工具，用于在不运行完整 PipeWire 守护进程的情况下测试 ALSA Card Profile（ACP）探测。它有助于诊断 PipeWire 错误配置 ALSA 声卡 profile 的各类问题。

该工具允许以交互方式探索声卡、profile、端口和设备。它还可以测试音量控制和静音状态，以便在 PipeWire 应用这些设置之前验证硬件配置是否正确。

# CAVEATS

仅用于调试；更改可能不会持久保存。需要相应权限才能访问 ALSA 设备。某些操作可能与正在运行的 PipeWire 实例冲突。属于 PipeWire/SPA 生态系统的一部分。

# HISTORY

**spa-acp-tool** 是 **PipeWire** 的一部分，这是由 Red Hat 的 **Wim Taymans** 自 **2017 年**前后开始开发的现代多媒体框架。PipeWire 旨在统一 Linux 上的音频与视频处理，取代 PulseAudio 和 JACK。SPA（Simple Plugin API）工具用于调试底层插件基础设施。

# INSTALL

```apt: sudo apt install pipewire-bin```

```apk: sudo apk add pipewire-spa-tools```

```zypper: sudo zypper install pipewire-spa-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pipewire](/man/pipewire)(1), [pw-cli](/man/pw-cli)(1), [pactl](/man/pactl)(1), [alsamixer](/man/alsamixer)(1)
