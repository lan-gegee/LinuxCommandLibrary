# TAGLINE

通用命令行音频处理器

# TLDR

**转换音频格式**

```sox [input.wav] [output.mp3]```

**连接多个文件**

```sox [file1.wav] [file2.wav] [output.wav]```

**更改采样率**

```sox [input.wav] -r [44100] [output.wav]```

**混音为单声道**

```sox [input.wav] [output.wav] channels 1```

**添加混响**

```sox [input.wav] [output.wav] reverb```

**裁剪音频**

```sox [input.wav] [output.wav] trim [0] [10]```

**标准化音量**

```sox [input.wav] [output.wav] norm```

**录制音频**

```sox -d [output.wav]```

# SYNOPSIS

**sox** [_options_] _infiles_ _outfile_ [_effects_...]

# DESCRIPTION

**sox**（Sound eXchange）是一款命令行音频处理工具。它可以在格式之间转换、应用效果，还能录制和播放音频。

该工具支持多种音频格式，并提供丰富的处理能力，包括滤波、混音和格式转换。

# PARAMETERS

**-r** _rate_
> 采样率。

**-c** _channels_
> 通道数。

**-b** _bits_
> 采样位深。

**-e** _encoding_
> 采样编码。

**-t** _type_
> 文件类型。

**-v** _factor_
> 音量调整系数。

**-d**
> 默认音频设备。

**--combine** _type_
> 组合方式（concatenate、merge、mix）。

# EFFECTS

**trim**: 裁剪片段
**fade**: 淡入/淡出
**reverb**: 添加混响
**norm**: 标准化
**speed**: 更改速度
**pitch**: 变调
**equalizer**: EQ 调节
**compand**: 压缩

# CAVEATS

某些格式需要外部库。复杂的效果链可能较慢。质量取决于参数设置。某些效果会改变时长。

# HISTORY

**SoX** 由 **Lance Norskog** 于 **1991 年**发起，此后由众多贡献者共同开发。它成为 Unix 系统上的"音频处理瑞士军刀"。

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

[ffmpeg](/man/ffmpeg)(1), [lame](/man/lame)(1), [flac](/man/flac)(1), [aplay](/man/aplay)(1)
