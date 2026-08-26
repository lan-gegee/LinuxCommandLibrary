# TAGLINE

通过 PC 扬声器发出蜂鸣音

# TLDR

播放一声**蜂鸣**

```beep```

播放**重复**的蜂鸣

```beep -r [repetitions]```

以指定的**频率**和**时长**播放蜂鸣

```beep -f [frequency] -l [duration]```

播放**多个不同的蜂鸣**

```beep -f [frequency] -l [duration] -n -f [frequency] -l [duration]```

播放 **C 大调音阶**

```beep -f 262 -n -f 294 -n -f 330 -n -f 349 -n -f 392 -n -f 440 -n -f 494 -n -f 523```

# SYNOPSIS

**beep** [_options_]

# DESCRIPTION

**beep** 使用 PC 扬声器发出指定频率和时长的声音。它可以演奏简单的旋律、警报声，或在脚本中充当音频通知。

可以使用 **-n**（new）选项分隔多个不同的蜂鸣，从而将多个音调串联起来。这样可以创建简单的乐曲序列或多音调警报。

# PARAMETERS

**-f** _frequency_
> 频率，单位为赫兹（默认：440 Hz）

**-l** _duration_
> 时长，单位为毫秒（默认：200 ms）

**-r** _count_
> 重复次数

**-d** _delay_
> 每次重复之间的延迟，单位为毫秒（默认：100 ms，最后一次重复之后不生效）

**-n, --new**
> 开始一个新的蜂鸣（用于序列）

**-D** _delay_
> 包括最后一次在内的每次重复之后的延迟，单位为毫秒

**-e** _device_, **--device=**_device_
> 显式设置用于生成蜂鸣音的设备

**-s**
> 从 stdin 读取，每遇到一个换行符就响一声

**-c**
> 从 stdin 读取，每读到一个字符就响一声

**-h**, **--help**
> 显示用法信息

**-v**, **-V**, **--version**
> 显示版本信息

**--verbose**, **--debug**
> 启用调试输出

# CAVEATS

需要访问 PC 扬声器设备（**/dev/input/by-path/platform-pcspkr-event-spkr** 或类似路径）。可能需要 root 权限或加入相应的组。并非所有系统都有可用的 PC 扬声器。

# HISTORY

**beep** 由 Johnathan Nightingale 创建，自 21 世纪初以来一直是 Linux 音频通知的主力工具。它提供了一种无需音频子系统就能发声的轻量方式。

# INSTALL

```apt: sudo apt install beep```

```dnf: sudo dnf install beep```

```pacman: sudo pacman -S beep```

```apk: sudo apk add beep```

```nix: nix profile install nixpkgs#beep```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[speaker-test](/man/speaker-test)(1), [aplay](/man/aplay)(1), [play](/man/play)(1)
