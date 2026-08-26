# TAGLINE

使用 SoundFont 2 的实时软件 MIDI 合成器

# TLDR

**用 SoundFont 播放 MIDI 文件**

```fluidsynth [/usr/share/soundfonts/soundfont.sf2] [path/to/file.mid]```

**指定音频驱动**

```fluidsynth -a [pipewire|pulseaudio|alsa|jack] [soundfont.sf2] [file.mid]```

**将 MIDI 文件渲染成 WAV 音频文件（不实时播放）**

```fluidsynth -T wav -F [output.wav] [soundfont.sf2] [file.mid]```

**作为接受外部 MIDI 输入的服务器运行**

```fluidsynth -s [soundfont.sf2]```

**批量处理多个 MIDI 文件而不进入交互式 shell**

```fluidsynth -ni [soundfont.sf2] [file1.mid] [file2.mid]```

**设置采样率和主增益**

```fluidsynth -r [44100] -g [1.0] [soundfont.sf2] [file.mid]```

**禁用混响和合唱效果**

```fluidsynth -R 0 -C 0 [soundfont.sf2] [file.mid]```

# SYNOPSIS

**fluidsynth** [_options_] [_soundfont_] [_midifile..._]

# PARAMETERS

**-a**, **--audio-driver** _driver_
> 音频输出驱动（pulseaudio、pipewire、alsa、jack、oss 等）。

**-m**, **--midi-driver** _driver_
> MIDI 输入驱动（alsa_seq、alsa_raw、jack、oss 等）。

**-F**, **--fast-render** _file_
> 以尽可能快的速度渲染到音频文件（不实时播放）。

**-T**, **--audio-file-type** _type_
> fast-render 输出的文件类型（wav、raw、aiff、au、flac、oga）。

**-n**, **--no-midi-in**
> 禁用 MIDI 输入。

**-i**, **--no-shell**
> 禁用交互式 shell。

**-s**, **--server**
> 作为后台服务器进程运行。

**-r**, **--sample-rate** _rate_
> 设置音频采样率（默认：44100）。

**-g**, **--gain** _value_
> 设置主增益（0.0-10.0，默认：0.2）。

**-L**, **--audio-channels** _num_
> 音频声道对的数量。

**-R**, **--reverb** _0|1_
> 启用或禁用混响效果。

**-C**, **--chorus** _0|1_
> 启用或禁用合唱效果。

**-o** _setting=value_
> 设置任意合成器选项（例如 `synth.polyphony`）。

**-c**, **--audio-bufcount** _count_
> 音频缓冲区的数量。

**-z**, **--audio-bufsize** _size_
> 每个音频缓冲区的大小（以帧为单位）。

**-V**, **--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**FluidSynth** 是一款实现 SoundFont 2 规范的实时软件 MIDI 合成器。它使用 SoundFont 乐器定义将 MIDI 输入或文件合成为音频输出。

该合成器可以在多种模式下运行：直接播放 MIDI 文件、作为接受外部 MIDI 输入（键盘、音序器）的服务器运行，或者快速渲染到音频文件。交互式 shell 允许实时控制合成参数。

FluidSynth 支持多种音频后端（PulseAudio、PipeWire、ALSA、JACK）和 MIDI 后端（ALSA 音序器、JACK MIDI），既适合独立使用，也适合集成到更大的音频系统中。

# CAVEATS

需要至少一个 SoundFont 文件（**.sf2** 或 **.sf3**）才能发声。许多发行版在 **/usr/share/soundfonts/** 中提供默认的 SoundFont。实时合成需要足够的 CPU 资源；复杂的 SoundFont 在较慢的系统上可能导致声音中断。**-F** 快速渲染选项会禁用实时音频输出。

# HISTORY

FluidSynth 由 **Peter Hanappe** 于 **2000 年**创建，是一款开源软件合成器。它最初名为 "IIWU Synth"，后来更名为 FluidSynth，如今已发展为 Linux、macOS 和 Windows 上广泛使用的 MIDI 合成器。该项目仍在积极开发中，2.x 版本对 API 和音质进行了重大改进。

# INSTALL

```apt: sudo apt install fluidsynth```

```dnf: sudo dnf install fluidsynth```

```pacman: sudo pacman -S fluidsynth```

```apk: sudo apk add fluidsynth```

```zypper: sudo zypper install fluidsynth```

```brew: brew install fluidsynth```

```nix: nix profile install nixpkgs#fluidsynth```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[timidity](/man/timidity)(1), [aplaymidi](/man/aplaymidi)(1), [aconnect](/man/aconnect)(1), [amidi](/man/amidi)(1)
