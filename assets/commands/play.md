# TAGLINE

通过 SoX 播放音频文件并可施加效果

# TLDR

**播放音频文件**

```play [audio.mp3]```

**带效果播放**

```play [audio.wav] reverb```

**以不同速度播放**

```play [audio.wav] speed 1.5```

**调整音量播放**

```play [audio.wav] vol 0.5```

**合并多个文件**

```play [file1.wav] [file2.wav]```

# SYNOPSIS

**play** [_options_] _file_ [_effects_...]

# PARAMETERS

_FILE_
> 要播放的音频文件。

_EFFECTS_
> 要应用的音频效果。

**-v** _VOLUME_
> 音量级别。

**-r** _RATE_
> 采样率。

**--help**
> 显示帮助。

# DESCRIPTION

**play** 从命令行播放音频文件，并可选地进行实时效果处理。它是 SoX（Sound eXchange）音频工具包的一部分，支持 WAV、MP3、FLAC、OGG 等众多格式。

混响、回声、变速、音量调节和均衡等音频效果可以在命令行上串联使用。多个文件可以连接起来按顺序播放。

# CAVEATS

属于 SoX 的一部分。格式支持因编译而异。可施加各种效果。

# HISTORY

play 是 **SoX**（Sound eXchange）音频处理工具包的一部分。

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

[sox](/man/sox)(1), [rec](/man/rec)(1), [soxi](/man/soxi)(1)
