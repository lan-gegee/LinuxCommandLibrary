# TAGLINE

用 RTL-SDR USB 电视棒接收调频信号

# TLDR

**收听 FM 广播**

```rtl_fm -f [100.1M] -M wbfm -s 200000 -r 48000 | aplay -f S16_LE -r 48000```

**窄带 FM（业余无线电）**

```rtl_fm -f [145.5M] -M fm -s 12000 | aplay -f S16_LE -r 12000```

**AM 模式**

```rtl_fm -f [1000k] -M am -s 12000 | aplay -f S16_LE -r 12000```

**保存到文件**

```rtl_fm -f [100.1M] -M wbfm -s 200000 > [radio.raw]```

# SYNOPSIS

**rtl_fm** [_options_]

# PARAMETERS

**-f** _freq_
> 中心频率。

**-M** _mode_
> 解调方式（fm、wbfm、am、usb、lsb）。

**-s** _rate_
> 采样率。

**-r** _rate_
> 输出采样率。

**-g** _gain_
> 增益（0 表示自动）。

**-d** _index_
> 设备索引。

**-p** _ppm_
> 补偿电视棒晶振误差的 PPM 频率校正。

**-l** _level_
> 静噪电平；信号强度低于该阈值时静音输出。

**-A** _method_
> 输出音频滤波方式：**fast**（默认）或 **lut**（查找表法，更慢但音质略好）。

**-E** _option_
> 启用附加特性：**edge**（边缘调谐）、**dc**（直流阻塞滤波器）、**deemp**（FM 去加重滤波器）、**direct**（直接采样模式）、**offset**（偏移调谐模式）。

# DESCRIPTION

**rtl_fm** 是一款面向 RTL-SDR 电视棒的 FM 解调器。它把廉价的 DVB-T USB 接收器（基于 RTL2832U 芯片组）当作软件定义无线电来接收并解调无线电信号。输出是写到 stdout 的原始 16 位有符号 PCM 音频，通常会通过管道交给音频播放器或写入文件。

# EXAMPLES

```bash
# FM broadcast
rtl_fm -f 100.1M -M wbfm -s 200000 -r 48000 | aplay -r 48000 -f S16_LE

# With squelch
rtl_fm -f 145.5M -M fm -s 12000 -l 50 | aplay -r 12000 -f S16_LE

# Scan frequencies
rtl_fm -f 145.0M:148.0M:25k -M fm -s 12000 | aplay -r 12000 -f S16_LE

# Record to WAV
rtl_fm -f 100.1M -M wbfm -s 200000 | sox -r 200000 -e s -b 16 -c 1 -t raw - radio.wav rate 48000
```

# MODES

```
wbfm - Wideband FM (broadcast)
fm   - Narrow FM
am   - Amplitude modulation
usb  - Upper sideband
lsb  - Lower sideband
```

# CAVEATS

需要 RTL-SDR 电视棒。可能需要进行 PPM 校正。播放输出需要音频播放器。

# HISTORY

rtl_fm 是 **osmocom** 出品的 **rtl-sdr** 工具集的一部分，让 RTL2832U 电视棒得以实现软件定义无线电。

# INSTALL

```apt: sudo apt install rtl-sdr```

```dnf: sudo dnf install rtl-sdr```

```pacman: sudo pacman -S rtl-sdr```

```apk: sudo apk add rtl-sdr```

```zypper: sudo zypper install rtl-sdr```

```brew: brew install rtl-sdr```

```nix: nix profile install nixpkgs#rtl-sdr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rtl_sdr](/man/rtl_sdr)(1), [rtl_power](/man/rtl_power)(1), [gqrx](/man/gqrx)(1)
