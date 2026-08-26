# TAGLINE

声音合成与音频编程语言

# TLDR

将乐队与乐谱**渲染为音频**

```csound [orchestra.orc] [score.sco]```

渲染统一的 csd 文件

```csound [file.csd]```

输出到 WAV 文件

```csound -o [output.wav] [file.csd]```

实时音频输出

```csound -odac [file.csd]```

**设置采样率**

```csound -r [44100] [file.csd]```

**设置控制率**

```csound -k [4410] [file.csd]```

# SYNOPSIS

**csound** [_options_] _files_...

# DESCRIPTION

**csound** 是一个声音合成程序和音频编程语言。它从基于文本的乐谱和乐队定义生成音频，可以对声音的生成与处理进行精确控制。

系统由两个主要部分组成：orchestra（乐队），用合成算法定义乐器；score（乐谱），规定何时以及如何演奏它们。现代用法通常将这些合并到 CSD（统一格式）文件中。

# PARAMETERS

**-o** _file_
> 输出音频文件（实时输出用 dac）。

**-i** _file_
> 输入音频文件（实时输入用 adc）。

**-r** _rate_
> 采样率（Hz）。

**-k** _rate_
> 控制率（Hz）。

**-b** _size_
> 软件缓冲区大小。

**-B** _size_
> 硬件缓冲区大小。

**-d**
> 抑制显示。

**-m** _level_
> 消息级别（0-231）。

**-W**
> 生成 WAV 格式输出。

**-A**
> 生成 AIFF 格式输出。

**--midi-device=** _dev_
> MIDI 输入设备。

# CAVEATS

合成编程的学习曲线陡峭。实时性能取决于缓冲区设置。乐队文件的报错信息可能晦涩难懂。需要配置音频系统。

# HISTORY

**Csound** 由 **Barry Vercoe** 于 **1986** 年在 **MIT** 开发，其源头可追溯到 **1957** 年起的 Music N 语言。它源自 Max Mathews 在贝尔实验室创建的 MUSIC 系列。Csound 至今仍在积极开发中，被广泛应用于学术研究、电子音乐和多媒体装置。

# INSTALL

```apt: sudo apt install csound```

```pacman: sudo pacman -S csound```

```zypper: sudo zypper install csound```

```brew: brew install csound```

```nix: nix profile install nixpkgs#csound```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sox](/man/sox)(1), [supercollider](/man/supercollider)(1), [ffmpeg](/man/ffmpeg)(1)
