# TAGLINE

使用 CUE 表拆分音频文件

# TLDR

使用 CUE 表拆分 **WAV 文件**

```shnsplit -f [path/to/file.cue] [path/to/file.wav]```

拆分并输出为 **FLAC**

```shnsplit -f [path/to/file.cue] -o flac [path/to/file.flac]```

以**自定义文件名格式**拆分

```shnsplit -f [path/to/file.cue] -t "%n - %a - %t" [path/to/file.wav]```

将输入文件拆分为**等长片段**

```shnsplit -l [5:00] [path/to/file.wav]```

拆分到**指定目录**

```shnsplit -f [path/to/file.cue] -d [output_directory] [path/to/file.wav]```

只从 CUE 表中提取**特定音轨**

```shnsplit -f [path/to/file.cue] -x [1-3,5] [path/to/file.wav]```

# SYNOPSIS

**shnsplit** [_OPTIONS_] [_file_]

**shntool split** [_OPTIONS_] [_file_]

# PARAMETERS

**-f** _file_
> 从 CUE 表或切分点文件读取切分点

**-o** _format_
> 输出格式（wav、flac、ape、shn、wv）

**-d** _dirname_
> 拆分文件的输出目录

**-t** _fmt_
> 使用 CUE 字段命名文件（%n=音轨、%a=专辑、%t=标题、%p=演奏者）

**-a** _str_
> 用 str 作为输出文件名前缀（默认：split-track）

**-z** _str_
> 用 str 作为输出文件名后缀

**-c** _num_
> 命名输出文件时从 num 开始计数（默认：0）

**-l** _len_
> 将输入文件拆分为长度为 len 的片段

**-m** _str_
> 针对 CUE 表生成文件名的字符替换字符串（交替的 from/to 对）

**-n** _fmt_
> 指定文件计数的输出格式（默认：%02d）

**-x** _list_
> 只提取特定音轨（例如 "2-6,9,11-13"）

**-e** _len_
> 加入上一音轨的导入部分（lead-in）

**-u** _len_
> 加入下一音轨的导出部分（lead-out）

**-i** _fmt_
> 指定输入文件的格式解码器和/或参数

**-O** _val_
> 覆盖已有文件：ask、always 或 never

**-q**
> 抑制非关键输出（安静模式）

**-w**
> 抑制警告

**-D**
> 打印调试信息

**-h**
> 显示帮助信息

# DESCRIPTION

**shnsplit** 依据 CUE 表中定义的切分点，将单个大音频文件拆分为多个独立的音轨文件。它是 **shntool** 套件的一部分，支持多种无损音频格式，包括 WAV、FLAC、APE 和 Shorten。

切分点可用几种格式指定：字节数、m:ss（分:秒）、m:ss.ff（CD 帧，每秒 75 帧）或 m:ss.nnn（毫秒）。该工具常用于将 CD 抓轨、现场录音或连续混音拆分为单个音轨。

# CAVEATS

非 WAV 格式需要安装相应的编码器/解码器（flac、wavpack、mac）。拆分精度完全取决于 CUE 表的正确性。不会向输出文件传递元数据；拆分后请用 **cuetag.sh** 打标签。除非用 **-d** 另行指定，否则输出文件会创建在当前目录。

# HISTORY

**shntool** 和 **shnsplit** 由 **Jason Jordan** 开发，属于 shntool 音频处理套件。项目始于 **2000 年代初**，旨在为 Unix/Linux 用户提供处理 Shorten（.shn）文件的工具——这种格式曾在无损音频分发中流行。该套件后来扩展为支持多种格式，至今仍是处理音频文件的标准工具之一。

# INSTALL

```apt: sudo apt install shntool```

```dnf: sudo dnf install shntool```

```zypper: sudo zypper install shntool```

```brew: brew install shntool```

```nix: nix profile install nixpkgs#shntool```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cuebreakpoints](/man/cuebreakpoints)(1), [cuetag](/man/cuetag)(1), [flac](/man/flac)(1), [sox](/man/sox)(1), [ffmpeg](/man/ffmpeg)(1)
