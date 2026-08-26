# TAGLINE

免费无损音频编解码器

# TLDR

**将 WAV 编码为 FLAC**

```flac [audio.wav]```

**将 FLAC 解码为 WAV**

```flac -d [audio.flac]```

**最高压缩级别**

```flac -8 [audio.wav]```

**快速压缩**

```flac --fast [audio.wav]```

**测试文件完整性**

```flac -t [audio.flac]```

编码时**添加元数据标签**

```flac -T "ARTIST=[Name]" -T "TITLE=[Song]" [audio.wav]```

**输出到指定文件**

```flac -o [output.flac] [input.wav]```

# SYNOPSIS

**flac** [_options_] _files_...

# DESCRIPTION

**flac** 对 Free Lossless Audio Codec 格式的音频进行编码和解码。FLAC 提供无损压缩，即解码之后的音频与原始音频完全相同。

该工具负责编码、解码、测试以及元数据操作。FLAC 文件通常只有原文件的 50-60% 大小，同时保持完美的音频保真度。

# PARAMETERS

**-d**, **--decode**
> 将 FLAC 解码为 WAV。

**-t**, **--test**
> 测试文件完整性。

**-a**, **--analyze**
> 分析文件。

**-0** 到 **-8**
> 压缩级别（0 最快，8 效果最好）。

**--fast**
> 等价于 -0。

**--best**
> 等价于 -8。

**-o** _file_
> 输出文件名。

**-c**, **--stdout**
> 将输出写入标准输出。

**-f**, **--force**
> 强制覆盖输出文件。

**-T**, **--tag=** _FIELD=VALUE_
> 添加一个 Vorbis 注释标签（可重复使用）。

**--tag-from-file=** _FIELD=FILENAME_
> 从文件中读取标签值。

**--delete-input-file**
> 成功编码/解码后删除输入文件。

**-s**, **--silent**
> 不显示运行时的统计信息。

**-V**, **--verify**
> 编码过程中并行解码以校验结果。

**-w**, **--warnings-as-errors**
> 把所有警告视为错误。

# CAVEATS

更高的压缩级别编码更慢，但体积并不会小多少。解码速度不受压缩级别影响，始终如一。部分播放器不支持所有 FLAC 特性。

# HISTORY

**FLAC** 由 **Josh Coalson** 从 **2000 年**开始开发。它已成为最主要的开源无损音频格式，得到大多数媒体播放器和设备的支持。该项目与 Ogg Vorbis 一起归入 Xiph.Org 基金会。

# INSTALL

```apt: sudo apt install flac```

```dnf: sudo dnf install flac```

```pacman: sudo pacman -S flac```

```apk: sudo apk add flac```

```zypper: sudo zypper install flac```

```brew: brew install flac```

```nix: nix profile install nixpkgs#flac```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sox](/man/sox)(1), [lame](/man/lame)(1), [ffmpeg](/man/ffmpeg)(1), [metaflac](/man/metaflac)(1)
