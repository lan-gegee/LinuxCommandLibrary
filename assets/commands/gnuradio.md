# TAGLINE

软件无线电信号处理工具集

# TLDR

**启动 GNU Radio Companion**

```gnuradio-companion```

**运行流图**

```python3 [flowgraph.py]```

**检查版本**

```gnuradio-config-info --version```

不启动图形界面直接**编译流图**

```gnuradio-companion -c [flowgraph.grc]```

**将流图编译**到指定的输出目录

```gnuradio-companion -c -d [output_dir] [flowgraph.grc]```

**创建 OOT 模块**

```gr_modtool newmod [mymodule]```

# SYNOPSIS

**gnuradio-companion** [_options_] [_file.grc_...]

# PARAMETERS

_file.grc_
> GNU Radio Companion 流图文件。

**-c**, **--compile**
> 只把 GRC 文件编译为 Python，不启动图形界面。

**-d**, **--output-dir** _DIR_
> 生成的 Python 文件的输出路径。

**-v**, **--version**
> 显示程序版本号并退出。

**-h**, **--help**
> 显示帮助消息并退出。

# DESCRIPTION

**GNU Radio** 是一个自由软件信号处理工具集。它提供各种处理块，用于构建软件无线电（SDR）和信号处理系统。

GNU Radio Companion（GRC）是图形化的流图编辑器。流图将处理块连接起来，构建无线电接收机、发射机和信号分析仪。流图会编译为 Python 代码。

# COMPONENTS

```
gnuradio-companion     Graphical flowgraph editor
gr_modtool             Out-of-tree module management
gnuradio-config-info   Show installed GNU Radio details
uhd_fft                Spectrum analyzer (for USRP)
```

# COMMON BLOCKS

- **Signal Sources（信号源）**：噪声、振荡器、文件源
- **Filters（滤波器）**：低通/高通/带通、FFT
- **Modulation（调制）**：AM、FM、PSK、QAM
- **Hardware（硬件）**：RTL-SDR、USRP、HackRF

# CONFIGURATION

**~/.gnuradio/config.conf**
> 用户配置文件，保存 GNU Radio 偏好设置和处理块路径。

# CAVEATS

射频工作需要兼容的 SDR 硬件。复杂的信号处理需要 DSP 知识。高采样率需要较快的 CPU。懂 Python 会有帮助。

# HISTORY

GNU Radio 由 **Eric Blossom** 于 **2001** 年启动。它已成长为领先的开源 SDR 框架，广泛应用于学术界、业余无线电和商业领域。该项目现由社区维护。

# INSTALL

```dnf: sudo dnf install gnuradio```

```pacman: sudo pacman -S gnuradio```

```zypper: sudo zypper install gnuradio```

```brew: brew install gnuradio```

```nix: nix profile install nixpkgs#gnuradio```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rtl_sdr](/man/rtl_sdr)(1), [gqrx](/man/gqrx)(1), [python3](/man/python3)(1)
