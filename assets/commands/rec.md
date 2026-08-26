# TAGLINE

从声音输入设备录制音频

# TLDR

**从默认输入设备录制音频**到文件

```rec [output.wav]```

**录制指定时长**（10 秒）

```rec [output.wav] trim 0 10```

**以特定格式录制**（MP3）

```rec [output.mp3]```

**以指定采样率和声道数录制**

```rec -r 44100 -c 2 [output.wav]```

**检测到静音时停止录制**

```rec [output.wav] silence 1 0.1 1% 1 1.0 1%```

**录制 16 位音频**

```rec -b 16 [output.wav]```

**监听输入电平**而不录制

```rec -n stat```

**录制并归一化**以防止削波

```rec --norm [output.wav]```

# SYNOPSIS

**rec** [_options_] _outfile_ [_effects_...]

# PARAMETERS

**-r** _rate_
> 设置采样率（Hz），如 44100、48000

**-c** _channels_
> 设置声道数（1=单声道，2=立体声）

**-b** _bits_
> 设置采样位深（8、16、24、32）

**-t** _type_
> 指定文件类型（wav、mp3、flac、ogg 等）

**-e** _encoding_
> 设置编码类型（signed-integer、unsigned-integer、floating-point、a-law、u-law）

**-C** _factor_
> 为输出格式设置压缩系数

**-S**
> 显示输入格式、处理进度和峰值电平表（rec 的默认行为）

**-q**
> 安静模式；抑制进度输出

**-V**[_level_]
> 设置详细程度（0=无，1=错误，2=警告，3=处理信息）

**-n**
> 使用空文件；配合 stat 等效果可在不录制的情况下进行监听

**--norm**[=_dBLevel_]
> 防止削波并对音频进行归一化

**-G**
> 通过自动增益调整防止削波

**trim** _start_ _duration_
> 从起始位置开始录制指定时长

**silence**
> 基于静音检测停止录制

**fade** _type_ _in_ _stop_ _out_
> 应用淡入淡出效果

# DESCRIPTION

**rec** 是 SoX（Sound eXchange，音频处理领域的瑞士军刀）的录音组件。它将来自默认输入设备（麦克风、线路输入）的音频录制成多种格式的文件。

输出格式通常由文件扩展名决定。SoX 支持数十种格式，包括 WAV、MP3、FLAC、OGG、AIFF 和原始音频。对于压缩格式可以指定特定于格式的编码选项。

录音过程中可以应用 SoX 效果，包括用于自动停止录制的静音检测、限制时长的裁剪以及增益调整。效果在输出文件名之后指定。

**rec** 等价于 **sox -d**（使用默认输入设备），并为录音设置了合适的默认值。类似地，**play** 是 **sox** 的播放别名。

# CAVEATS

MP3 编码要求 SoX 编译时带有 MP3 支持（libmp3lame）。由于许可原因，某些发行版会将其单独打包。

默认音频设备取决于系统配置和 AUDIODEV 环境变量。

录音需要访问音频设备的相应权限。在某些系统上，用户可能需要加入 **audio** 组。

如果未指定时长或静音检测，请用 Ctrl+C 手动停止录制。

# INSTALL

```apt: sudo apt install sox```

```dnf: sudo dnf install sox```

```pacman: sudo pacman -S sox```

```apk: sudo apk add sox```

```zypper: sudo zypper install sox```

```brew: brew install sox```

```nix: nix profile install nixpkgs#sox```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sox](/man/sox)(1), [play](/man/play)(1), [soxi](/man/soxi)(1), [arecord](/man/arecord)(1), [ffmpeg](/man/ffmpeg)(1)
