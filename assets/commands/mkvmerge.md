# TAGLINE

创建 Matroska 文件

# TLDR

**合并文件**

```mkvmerge -o [output.mkv] [input1.mp4] [input2.mp4]```

**添加字幕**

```mkvmerge -o [output.mkv] [video.mkv] [subtitles.srt]```

**提取轨道**

```mkvmerge -o [output.mkv] --audio-tracks [1] [input.mkv]```

**设置默认轨道标志**

```mkvmerge -o [output.mkv] --default-track-flag [0:1] [input.mkv]```

**按大小分割**

```mkvmerge -o [output.mkv] --split [700M] [input.mkv]```

**设置轨道语言**

```mkvmerge -o [output.mkv] --language [0:eng] [input.mkv]```

**添加标题**

```mkvmerge -o [output.mkv] --title "[Movie Title]" [input.mkv]```

**识别文件中的轨道**

```mkvmerge -i [input.mkv]```

# SYNOPSIS

**mkvmerge** [_options_] -o _output_ _inputs_

# PARAMETERS

**-o** _FILE_
> 输出文件。

_INPUTS_
> 输入文件。

**-i** _FILE_
> 识别输入文件的轨道、编解码器和属性。

**--audio-tracks** _IDS_
> 选择要包含的音频轨道。

**--video-tracks** _IDS_
> 选择要包含的视频轨道。

**--subtitle-tracks** _IDS_
> 选择要包含的字幕轨道。

**--no-audio**
> 排除所有音频轨道。

**--no-subtitles**
> 排除所有字幕轨道。

**--language** _TID:LANG_
> 设置轨道语言（ISO 639-2 代码）。

**--default-track-flag** _TID:BOOL_
> 设置或清除默认轨道标志。

**--split** _SIZE_|_duration:TIME_|_chapters:all_
> 按大小、时长或章节分割输出。

**--title** _TEXT_
> 设置段（segment）标题。

**--append-to** _SPEC_
> 将一个文件的轨道追加到另一个文件之后。

**-l, --list-types**
> 列出支持的源文件格式。

# DESCRIPTION

**mkvmerge** 通过合并来自各种源格式的视频、音频和字幕流来创建 Matroska（MKV/MKA/MKS）容器文件。它不做转码，只是将流重新封装（remux）进 Matroska 容器。

该工具属于 MKVToolNix。轨道 ID 可通过 **mkvmerge -i** 或 **mkvinfo** 查看。选项顺序很重要：先写全局选项，再在输入文件之前写适用于该文件的选项。

# CAVEATS

不做转码（仅重新封装）。属于 MKVToolNix。选项顺序很重要：针对特定文件的选项必须放在其适用的输入文件之前。轨道 ID 从 0 开始编号。

# HISTORY

mkvmerge 属于 **MKVToolNix**，提供 Matroska 容器操作工具。

# INSTALL

```apt: sudo apt install mkvtoolnix```

```dnf: sudo dnf install mkvtoolnix```

```apk: sudo apk add mkvtoolnix```

```zypper: sudo zypper install mkvtoolnix```

```brew: brew install mkvtoolnix```

```nix: nix profile install nixpkgs#mkvtoolnix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1), [mkvpropedit](/man/mkvpropedit)(1)
