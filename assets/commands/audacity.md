# TAGLINE

用于录制和编辑声音的开源图形化音频编辑器。

# TLDR

**启动 Audacity** 图形界面

```audacity```

**打开音频文件**进行编辑

```audacity [path/to/audio.wav]```

**打开多个音频文件**

```audacity [file1.wav] [file2.mp3] [file3.ogg]```

**显示版本**信息

```audacity -version```

**显示**命令行选项的**帮助**

```audacity -help```

设置磁盘写入的**块大小**

```audacity -blocksize [4096] [path/to/audio.wav]```

# SYNOPSIS

**audacity** [**-help**]

**audacity** [**-version**]

**audacity** [**-blocksize** _nnn_] [_AUDIO-FILE_] ...

# PARAMETERS

**-help**
> 显示命令行选项的简要列表。

**-version**
> 显示 Audacity 版本号。

**-blocksize** _nnn_
> 将 Audacity 写文件到磁盘时的块大小设置为 nnn 字节。

**-test**
> 运行自检测试（仅存在于开发版本中）。

# DESCRIPTION

**Audacity** 是一款免费开源的图形化音频编辑器，用于录制和编辑声音。它支持多种音频格式，包括未压缩格式（WAV、AIFF、AU），以及借助外部库支持的压缩格式（MP3、Ogg Vorbis、FLAC）。

Audacity 提供多轨编辑、多来源录音、效果处理和格式转换功能。它支持 LADSPA 和 Nyquist 插件以扩展功能。编辑器基于磁盘工作，即编辑期间音频数据存储在临时目录中，而不是完全放在内存里。

Audacity 本质上是一个交互式图形应用程序。若需批处理或命令行音频处理，sox 或 ecasound 等工具更为合适。

# FILES

**~/.audacity-data/audacity.cfg**
> 用户级配置文件（Linux）。较新版本中可能位于 **~/.config/audacity/audacity.cfg**。

**/var/tmp/audacity-_user_/**
> 临时目录的默认位置。应放置在有充足空闲空间的快速本地磁盘上。

# ENVIRONMENT

**AUDACITY_PATH**
> 在标准位置之前搜索插件和配置文件的目录。

**LADSPA_PATH**
> 额外搜索 LADSPA 插件的目录。

# CAVEATS

Audacity 的命令行功能有限，并非为批处理设计。临时目录在大项目下需要大量磁盘空间。部分音频格式（MP3、FFmpeg 格式）需要额外安装相关库。

# HISTORY

Audacity 由卡内基梅隆大学的 Dominic Mazzoni 和 Roger Dannenberg 于 **1999** 年发起。它成为最受欢迎的开源音频编辑器之一，覆盖 Linux、macOS 和 Windows 平台。**2021** 年，该项目被 Muse Group 收购，引发了社区对遥测与隐私问题的担忧。项目仍在持续开发并定期发布。

# INSTALL

```apt: sudo apt install audacity```

```dnf: sudo dnf install audacity```

```pacman: sudo pacman -S audacity```

```apk: sudo apk add audacity```

```zypper: sudo zypper install audacity```

```nix: nix profile install nixpkgs#audacity```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[sox](/man/sox)(1), [ardour](/man/ardour)(1), [lame](/man/lame)(1)
