# TAGLINE

受 Winamp 2.x 启发的复古终端音乐播放器

# TLDR

**递归播放目录中**的所有音频文件

```cliamp ~/Music```

按格式**播放指定文件**

```cliamp *.mp3 *.flac *.wav *.ogg```

**随机播放**并自定义音量

```cliamp --shuffle --volume -5 [path/to/music]```

从 URL **流式播放音频**

```cliamp [https://example.com/song.mp3]```

**播放 M3U 播放列表**

```cliamp [path/to/playlist.m3u]```

从 RSS 源**播客播放**

```cliamp [https://example.com/podcast/feed.xml]```

# SYNOPSIS

**cliamp** [_options_] [_files/directories/URLs_]

# PARAMETERS

**--volume** _dB_
> 以 dB 计的音量，范围 -30 到 +6。默认 0。

**--shuffle**
> 启用随机播放模式。

**--repeat** _mode_
> 设置循环模式：**off**、**all** 或 **one**。默认 off。

**--mono** / **--no-mono**
> 启用或禁用单声道输出（L+R 下混）。

**--auto-play**
> 立即开始播放。

**--theme** _name_
> 按名称设置 UI 主题。

**--eq-preset** _name_
> 设置 EQ 预设：**Flat**、**Rock**、**Pop**、**Jazz**、**Classical**、**Bass Boost**、**Treble Boost**、**Vocal**、**Electronic**、**Acoustic**。

**--bit-depth** _n_
> PCM 位深：16（默认）或 32（无损）。

**--sample-rate** _Hz_
> 输出采样率：22050、44100、48000、96000、192000。默认 44100。

**--buffer-ms** _ms_
> 扬声器缓冲时长（毫秒），范围 50-500。默认 100。

**--resample-quality** _n_
> 重采样质量因子，范围 1-4。默认 4。

**--visualizer** _mode_
> 可视化模式：**Bars**、**Bricks**、**Columns**、**Wave**、**Scatter**、**Flame**、**Retro**、**None**。

**-h**, **--help**
> 显示帮助并退出。

**-v**, **--version**
> 输出版本并退出。

**--upgrade**
> 更新到最新版本。

# DESCRIPTION

**cliamp** 是一款受 Winamp 2.x 启发的复古终端音乐播放器。它支持播放 **MP3**、**WAV**、**FLAC**、**OGG**、**AAC**、**ALAC**、**Opus** 和 **WMA**，带有 10 段频谱可视化器、10 段参量 EQ 和播放列表管理功能。

它支持本地文件、目录（递归扫描）、HTTP 流媒体、M3U/M3U8 播放列表、播客 RSS 源，以及来自 YouTube、SoundCloud、Bandcamp、Bilibili 和 Spotify 的 URL（通过 yt-dlp）。内置的文件浏览器和播放列表管理器让你可以在终端内整理音乐。

cliamp 还可以通过环境变量连接 Navidrome 服务器进行远程音乐流式播放。

# KEYBOARD CONTROLS

```
Space        Play / Pause
s            Stop
> .          Next track
< ,          Previous track
Left/Right   Seek -/+5s
+ -          Volume up/down
m            Toggle mono
Tab          Toggle focus (Playlist / EQ)
j k          Playlist scroll / EQ band adjust
h l          EQ cursor left/right
Enter        Play selected track
e            Cycle EQ preset
t            Choose theme
v            Cycle visualizer
V            Full-screen visualizer
S            Save track to ~/Music
/            Search playlist
x            Expand/collapse playlist
o            Open file browser
a            Toggle queue (play next)
A            Queue manager
p            Playlist manager
r            Cycle repeat (Off / All / One)
z            Toggle shuffle
Ctrl+K       Show keymap
b Esc        Back to provider
q            Quit
```

# CONFIGURATION

配置存储在 **~/.config/cliamp/config.toml**：

```
# Default volume in dB (range: -30 to 6)
volume = 0

# Repeat mode: "off", "all", or "one"
repeat = "off"

# Start with shuffle enabled
shuffle = false

# Start with mono output (L+R downmix)
mono = false

# EQ preset: "Flat", "Rock", "Pop", "Jazz", "Classical",
#             "Bass Boost", "Treble Boost", "Vocal", "Electronic", "Acoustic"
eq_preset = "Flat"

# 10-band EQ gains in dB (range: -12 to 12)
# Bands: 70Hz, 180Hz, 320Hz, 600Hz, 1kHz, 3kHz, 6kHz, 12kHz, 14kHz, 16kHz
eq = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

自定义播放列表可以在 **~/.config/cliamp/playlists/** 中创建为 **.toml** 文件。不带参数运行 **cliamp** 会打开播放列表浏览器。

# CAVEATS

AAC、ALAC（.m4a）、Opus 和 WMA 播放需要安装 **ffmpeg**。MP3、WAV、FLAC 和 OGG 无需 ffmpeg 即可播放。YouTube/SoundCloud/Bandcamp 支持需要 **yt-dlp**。不可定位的 HTTP 流会显示静态的进度条，定位按键会被静默忽略。

# HISTORY

**cliamp** 是开发者 **bjarneo**（iamdothash）使用 **Go** 编写的终端音乐播放器，灵感来自 **Winamp 2.x**。它基于 **Bubbletea** TUI 框架构建，样式使用 **Lip Gloss**，音频播放使用 **Beep**。

# INSTALL

```nix: nix profile install nixpkgs#cliamp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mpv](/man/mpv)(1), [ffmpeg](/man/ffmpeg)(1), [ffplay](/man/ffplay)(1)
