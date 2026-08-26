# TAGLINE

软件定义无线电接收器

# TLDR

**启动 Gqrx**

```gqrx```

**使用指定配置启动**

```gqrx -c [config.conf]```

**重置设置**

```gqrx -r```

**启动前编辑设置**

```gqrx -e```

# SYNOPSIS

**gqrx** [_options_]

# PARAMETERS

**-c** _file_
> 配置文件。

**-r**, **--reset**
> 将设置重置为默认值。

**-e**, **--edit**
> 启动前编辑配置。

**-s** _style_
> Qt 样式。

# DESCRIPTION

**Gqrx** 是一个开源的软件定义无线电（SDR）接收器。它提供图形界面，可使用 RTL-SDR、HackRF、Airspy 等 SDR 硬件接收无线电信号。

该应用具有瀑布图显示、频谱分析仪以及 AM、FM、SSB 和 CW 等多种解调模式。它还可以录制音频和 I/Q 数据。

# SUPPORTED HARDWARE

- RTL-SDR dongles
- HackRF
- Airspy
- SDRplay
- USRP
- FunCube Dongle
- Any GNU Radio source

# FEATURES

- 瀑布图和频谱显示
- AM、FM、WFM、SSB、CW 解调
- 可调节的滤波器和静噪
- 音频录制
- 通过 TCP 远程控制

# CONFIGURATION

**~/.config/gqrx/default.conf**
> 默认配置文件，存储频率、增益和解调设置。

# CAVEATS

需要 SDR 硬件。带宽越大 CPU 占用越高。某些模式需要特定硬件。RTL-SDR 存在频率限制。

# HISTORY

Gqrx 由 **Alexandru Csete**（OZ9AEC）于 **2011 年**前后创建，是一个基于 GNU Radio 构建的易用 SDR 应用。它成为 Linux SDR 用户首选的 GUI 应用程序。

# INSTALL

```apt: sudo apt install gqrx-sdr```

```dnf: sudo dnf install gqrx```

```pacman: sudo pacman -S gqrx```

```apk: sudo apk add gqrx```

```zypper: sudo zypper install gqrx```

```nix: nix profile install nixpkgs#gqrx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rtl_sdr](/man/rtl_sdr)(1), [gnuradio](/man/gnuradio)(1)
