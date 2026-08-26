# TAGLINE

面向 RTL-SDR USB 电视棒的宽带频谱扫描器

# TLDR

以 125 kHz 的 bin 宽度**扫描调频广播频段**，每行耗时 10 秒

```rtl_power -f [88M:108M:125k] -g [50] -i [10] [fm_band.csv]```

对航空频段做**单次扫描**（不做积分）

```rtl_power -f [118M:137M:25k] -1 [airband.csv]```

以每行 60 秒的方式**持续积分**

```rtl_power -f [144M:148M:10k] -i [60] [ham2m.csv]```

**运行一小时后退出**

```rtl_power -f [88M:108M:125k] -e [1h] [fm.csv]```

**选择指定的设备**（存在多个电视棒时）

```rtl_power -d [1] -f [400M:410M:10k] [out.csv]```

**应用 PPM 频率校正**

```rtl_power -p [58] -f [400M:410M:10k] [out.csv]```

# SYNOPSIS

**rtl_power** [_options_] _filename_

# PARAMETERS

**-f** _lower:upper:bin-size_
> 频率范围与 bin 宽度（例如 `88M:108M:125k`）。bin 宽度决定 FFT 分辨率。

**-i** _seconds_
> 每行的积分时长。取值越长噪声越小，但行周期也随之拉长。默认：10。

**-g** _gain_
> 调谐器增益，单位 dB（可用范围取决于调谐器型号）。`0` 表示自动增益。

**-p** _ppm_
> 以百万分率（ppm）表示的频率校正量。

**-c** _crop_
> 裁剪比例（0–1），从每次调谐结果的边缘丢弃（以规避滤波器滚降）。

**-s** _sample-rate_
> 硬件采样率（默认 2048000）。

**-w** _window_
> FFT 窗函数：`rectangle`、`hamming`、`blackman`、`blackman-harris`、`hann-poisson`、`youssef`（默认）。

**-F** _n_
> 通过对 _n_ 个 FFT 缓冲取平均来增强积分（非常宽的扫描通常使用 `-F 9`）。

**-O**
> 启用偏移调谐（在某些调谐器上可用于避开 DC 尖峰）。

**-d** _index_
> 存在多个电视棒时使用的设备索引。

**-e** _duration_
> 在给定时间后退出（例如 `30s`、`15m`、`1h`、`1d`）。

**-1**
> 只执行一轮测量然后退出。

**-h**
> 保持当前调谐频率不变（调试用途）。

**-**
> 把 CSV 写到 stdout 而不是文件。

# OUTPUT

以制表符或逗号分隔的行：

```
date, time, freq_low, freq_high, step, samples, dB_bin_0, dB_bin_1, ...
```

将其管道传给 **heatmap.py**（随 rtl-sdr 附带）即可生成瀑布图。

# DESCRIPTION

**rtl_power** 让 RTL-SDR USB 电视棒变成宽带频谱分析仪：它在目标范围内反复重新调谐，每次调谐采集一小段 FFT 数据，并记录每个频率 bin 的平均功率。它是长时间频段普查、射频干扰（RFI）排查以及无人值守频谱记录的标准工具。

超出电视棒瞬时带宽（可用带宽约 2–3 MHz）的频率范围会通过快速重调谐拼接而成；在各段交界处预计会出现细微接缝。

# CAVEATS

需要兼容 RTL-SDR 的 DVB-T 电视棒以及 `rtl-sdr` 工具。范围越宽、bin 越小，CPU 占用和扫描时间会大幅增加。温度漂移会影响 PPM 精度；可在已知信标上用 `rtl_test -p` 校准。

# HISTORY

**rtl_power** 随 **rtl-sdr** 工具集一同发布，最初由 **Kyle Keen** 编写，目前由 Osmocom 维护。这个项目源于一项发现（约 2012 年）：Realtek RTL2832U DVB-T 解调芯片可以切换到 I/Q SDR 模式。

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

[rtl_fm](/man/rtl_fm)(1), [rtl_sdr](/man/rtl_sdr)(1)
