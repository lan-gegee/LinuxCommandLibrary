# TAGLINE

解码电子游戏音频格式

# TLDR

**转换为 WAV**

```vgmstream_cli -o [output.wav] [input.adx]```

**直接播放音频**

```vgmstream_cli -p [file.brstm]```

**显示文件信息**

```vgmstream_cli -m [file.fsb]```

**循环两次**

```vgmstream_cli -l 2 -o [output.wav] [input.hca]```

**选择子音轨**

```vgmstream_cli -s 3 [file.awb]```

**禁用循环**

```vgmstream_cli -i -o [output.wav] [input.adx]```

# SYNOPSIS

**vgmstream_cli** [_-o file_] [_-p_] [_-m_] [_-l loops_] [_-s subsong_] [_-i_] _file_

# PARAMETERS

**-o** _FILE_
> 输出 WAV 文件。

**-p**
> 播放到音频设备。

**-m**
> 仅显示元数据。

**-l** _N_
> 循环次数。

**-s** _N_
> 选择子音轨。

**-i**
> 忽略循环。

**-S** _N_
> 从指定子音轨开始。

**-E** _N_
> 到指定子音轨结束。

# DESCRIPTION

**vgmstream_cli** 将来自电子游戏的音频文件解码为标准 WAV 格式，或直接播放。它支持游戏主机和引擎使用的数百种专有音频格式，包括 ADX、HCA、FSB、BRSTM 等。

该工具能处理游戏特有的功能，例如无缝循环、从多音轨归档中提取子音轨以及精确到采样级别的播放。元数据模式无需解码音频即可显示格式细节、采样率和循环点。

# CAVEATS

仅支持解码。不能编码为游戏格式。某些格式需要配套文件。

# HISTORY

**vgmstream** 是一个用于播放流式游戏音频的库，支持众多游戏引擎和平台的格式。

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1), [sox](/man/sox)(1), [audacity](/man/audacity)(1)
