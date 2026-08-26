# TAGLINE

PipeWire 重采样器调试工具

# TLDR

将 WAV 文件**重采样**到不同采样率

```spa-resample -r [48000] [input.wav] [output.wav]```

以指定输出**格式**进行**重采样**

```spa-resample -r [48000] -f [s32] [input.wav] [output.wav]```

以**最高质量**设置进行**重采样**

```spa-resample -q 14 -r [48000] [input.wav] [output.wav]```

带**详细输出**进行**重采样**

```spa-resample -v -r [44100] -f [f32] [input.wav] [output.wav]```

# SYNOPSIS

**spa-resample** [_OPTIONS_] _INFILE_ _OUTFILE_

# PARAMETERS

**-r** _RATE_, **--rate=**_RATE_
> 输出采样率。

**-f** _FORMAT_, **--format=**_FORMAT_
> 输出采样格式（**s8** | **s16** | **s32** | **f32** | **f64**）。

**-q** _QUALITY_, **--quality=**_QUALITY_
> 重采样器输出质量（**0**-**14**）。数值越高质量越好，但 CPU 占用也越高。

**-c** _FLAGS_, **--cpuflags=**_FLAGS_
> 用于选择 SIMD 优化的 CPU 特性标志。详见 spa/support/cpu.h。

**-v**
> 详细输出模式。

**-h**
> 显示帮助。

# DESCRIPTION

**spa-resample** 是一个命令行工具，使用 PipeWire SPA 重采样器将音频文件从一种采样率和格式转换为另一种。它读取 WAV 输入文件，按指定参数应用重采样，并将结果写入 WAV 输出文件。

该工具主要用于**测试和调试** PipeWire 重采样器实现，而非作为通用的音频转换工具。它直接提供与 PipeWire 内部处理音频流相同的重采样算法，因此适合验证重采样器的行为和质量。

# CAVEATS

此工具仅用于测试和调试目的，不适用于生产环境的音频转换流程。通用音频格式转换更适合使用 **sox** 或 **ffmpeg** 等专用工具。输入和输出仅支持 WAV 格式。0-14 的质量参数范围是 PipeWire SPA 重采样器特有的，与其他重采样器使用的质量刻度不对应。

# HISTORY

**spa-resample** 是 **PipeWire** 多媒体框架的一部分，该框架由 **Wim Taymans** 创建并于 **2017 年**首次发布。PipeWire 被设计为统一的音视频服务器，用于取代 Linux 系统上的 **PulseAudio** 和 **JACK**。spa-resample 工具提供了对 PipeWire 内置 SPA（Simple Plugin API）重采样器的独立访问方式，该重采样器支持多个 SIMD 优化的后端以高效完成采样率转换。

# INSTALL

```apt: sudo apt install pipewire-bin```

```apk: sudo apk add pipewire-spa-tools```

```zypper: sudo zypper install pipewire-spa-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pipewire](/man/pipewire)(1), [pw-cli](/man/pw-cli)(1), [pw-cat](/man/pw-cat)(1), [sox](/man/sox)(1), [ffmpeg](/man/ffmpeg)(1)
