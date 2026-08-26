# TAGLINE

设置或读取 ALSA 设备上的 IEC958（S/PDIF）状态位

# TLDR

**显示当前 IEC958 状态**

```iecset```

**以 AES 字节格式转储状态**

```iecset -x```

**设置专业模式**

```iecset pro on```

**设置音频模式**

```iecset audio on```

**设置采样率**

```iecset rate [48000]```

**使用指定的声卡**

```iecset -c [1]```

**从 stdin 读取命令**

```iecset -i```

# SYNOPSIS

**iecset** [_options_] [_commands_]

# PARAMETERS

**pro** _on|off_
> 专业模式（true）或消费模式（false）。

**audio** _on|off_
> 音频模式（true）或非音频模式（false）。

**rate** _RATE_
> 采样率，单位 Hz。

**emphasis** _0|1|2_
> 预加重：0 = 无，1 = 50/15us，2 = CCITT。

**copyright** _on|off_
> 版权标志（仅限消费模式）。

**category** _VALUE_
> 类别代码 0-0x7f（仅限消费模式）。

**lock** _on|off_
> 速率锁定（仅限专业模式）。

**sbits** _VALUE_
> 采样位数：2 = 20bit，4 = 24bit，6 = 未定义（仅限专业模式）。

**-c** _CARD_
> 声卡索引号。

**-D** _DEVICE_
> 设备名称。

**-n** _INDEX_
> 多个 IEC958 设备时使用的 IEC958 控件元素索引。

**-x**
> 以 AESx 字节格式转储状态。

**-i**
> 从 stdin 读取命令序列。

# DESCRIPTION

**iecset** 设置或读取 ALSA 设备上的 IEC958（S/PDIF）状态位。不带命令启动时，它以人类可读的形式显示当前 IEC958 状态。

该工具控制专业/消费模式、采样率、预加重以及其他数字音频输出的 S/PDIF 参数。

# CAVEATS

属于 alsa-utils。设备必须支持 IEC958。设置可能会被重置。

# HISTORY

iecset 是 **ALSA** 工具集的一部分，用于 Linux 数字音频配置。

# INSTALL

```apt: sudo apt install alsa-utils```

```dnf: sudo dnf install alsa-utils```

```pacman: sudo pacman -S alsa-utils```

```apk: sudo apk add alsa-utils```

```zypper: sudo zypper install alsa-utils```

```nix: nix profile install nixpkgs#alsa-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aplay](/man/aplay)(1), [amixer](/man/amixer)(1), [alsactl](/man/alsactl)(1)
