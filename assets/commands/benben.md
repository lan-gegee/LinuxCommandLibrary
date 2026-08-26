# TAGLINE

支持 VGM 芯片仿真的快速命令行音频播放器与转换器

# TLDR

**播放单个音频文件**

```benben [path/to/song.mp3]```

**播放一个目录中的所有文件**

```benben [path/to/album/]```

**循环播放 VGM 文件**

```benben --loop [2] [path/to/song.vgz]```

**并行渲染文件为 WAV**

```benben --render [*.ogg] [*.flac]```

**渲染到指定输出目录**并做响度归一化

```benben --render --normalize --outdir [path/to/output] [*.vgm]```

**使用指定的音频驱动和采样率播放**

```benben --driver [alsa] --sample-rate [48000] [path/to/file]```

**播放 SID 文件**并选择指定曲目

```benben [path/to/file.sid@2,4,7]```

**随机乱序并重复播放**一个目录

```benben --shuffle --repeat [path/to/music/]```

# SYNOPSIS

**benben** [_options_] [_files_|_directories_|_playlists_]

# PARAMETERS

**-h**, **--help**
> 显示帮助信息并退出

**-v**, **--version**
> 显示简短版本信息并退出

**--long-version**
> 显示详细版本信息并退出

**--scan-only**
> 仅扫描文件，然后终止

**--recurse**
> 递归搜索子目录

**--no-recurse**
> 禁用递归子目录搜索

**--dump-config**
> 生成一份全新配置并输出到 stdout

**--basedir** _path_
> 从备用目录加载配置和主题

**--remote**
> 启用 UNIX 域套接字以进行远程控制

**--remote-socket** _path_
> 为远程控制指定备用的套接字位置

**--list-themes**
> 显示所有可用主题

**-T** _name_, **--theme** _name_
> 使用指定的主题

**--ui** _type_
> 选择用户界面：original 或 minimal

**-L**, **--no-listenbrainz**
> 禁用 ListenBrainz 提交

**-d** _driver_, **--driver** _driver_
> 选择音频驱动（alsa、out123、ao、any）

**--alsa-device** _name_
> 使用指定的 ALSA 设备（默认：default）

**--volume** _x_
> 设置输出音量，范围 0.0 到 3.0（默认：1.0）

**-S** _hz_, **--sample-rate** _hz_
> 设置输出采样率（Hz），范围 8000 到 48000（默认：44100）

**--replay-gain** _mode_
> 设置 ReplayGain 模式：disabled、mix 或 album

**--resampler** _mode_
> 设置重采样器模式

**-e**, **--no-eq**
> 以均衡器禁用状态启动

**-c**, **--soft-clipping**
> 以软削波启用状态启动

**-C**, **--no-soft-clipping**
> 以软削波禁用状态启动

**--soft-clipping-oversampling** _n_
> 软削波启用时的过采样倍数（默认：1）

**-t**, **--stereo-enhancer**
> 启用立体声增强效果

**-E** _amount_, **--stereo-enhancement** _amount_
> 设置立体声增强强度，范围 0.0 到 1.5（默认：0.5）

**--dc-filter**
> 启用直流偏移滤波器

**--no-dc-filter**
> 禁用直流偏移滤波器

**-r**, **--reverb**
> 启用混响效果

**-R**, **--no-reverb**
> 禁用混响效果

**--reverb-type** _type_
> 设置混响单元类型：mverb 或 zita

**--reverb-preset** _name_
> 使用备用的混响预设（默认：gm-default）

**--reverb-amount** _x_
> 设置混响强度，范围 0.0 到 1.0（默认：0.5）

**-l** _n_, **--loop** _n_
> 循环次数；0 表示无限循环（默认：1）

**-p**, **--repeat**
> 播放完毕后循环整个队列

**-P**, **--no-repeat**
> 禁用队列循环

**--shuffle**
> 随机打乱播放队列

**--start-paused**
> 以暂停状态开始播放

**--fadeout-seconds** _n_
> 淡出时长（秒）（默认：5）

**--vgm-chip-info**
> 显示受支持的 VGM 芯片仿真器并退出

**--vgm-strict-gd3-loading**
> 在加载 VGM 时严格校验 GD3 标签

**--vgm-ym2612-pseudo-stereo**
> 为 YM2612 仿真器启用伪立体声

**--sid-mono**
> 强制以单声道播放 2SID/3SID

**--sid-def-length** _seconds_
> SID 曲目的默认长度（秒）（默认：180）

**--midi-soundfont** _path_
> 为 MIDI 播放指定 SoundFont 文件

**-n**, **--render**
> 将文件渲染为 WAV 或 Au 格式而不是播放

**-Q**, **--quiet**
> 渲染期间抑制非错误消息

**-N**, **--normalize**
> 将渲染出的文件归一化到 0 dBFS 峰值

**-A**, **--au**
> 渲染为 Au 格式而不是 WAV

**-F**, **--float**
> 渲染时输出 IEEE 浮点数据

**-b** _depth_, **--bit-depth** _depth_
> 设置位深：8、16、24、32 或 64（PCM 默认 16，浮点默认 32）

**-o** _dir_, **--outdir** _dir_
> 渲染文件的输出目录

**--overwrite**
> 覆盖已存在的渲染文件

**--jobs** _n_
> 并行渲染任务数（默认：CPU 核心数）

**--tcp-driver-host** _host_
> 要连接的 TCP 主机（默认：localhost）

**--tcp-driver-port** _port_
> 要连接的 TCP 端口（默认：6969）

**--tcp-driver-format** _format_
> TCP 传输使用的音频格式（默认：float32）

# DESCRIPTION

**benben** 是一款面向 Linux 及其他类 Unix 系统、快速高效的命令行音频播放器和音频转换器，拥有复古风格（oldschool）的终端界面。它几乎完全使用 Common Lisp 编写，面向那些按文件夹整理音乐、偏好终端工具而非图形界面的用户。

benben 支持多种音频格式，包括 MP3、Ogg Vorbis、Opus、FLAC、WavPack、WAV、QOA、Sun Au、General MIDI、MUS、Commodore 64 SID、Doom WAD 文件，以及 libxmp 支持的所有 module/tracker 格式。它对 VGM（Video Game Music）格式有广泛支持，依托 SatouSynth 库提供对 30 多种声音芯片的仿真，包括 YM2612、YM2151、YM2610、NES APU、HuC6280、QSound 和 Sega MultiPCM。

该播放器提供多个音频输出后端（ALSA、libout123、libao），并支持 TCP 音频流传输。内置音频效果包括可配置过采样的软削波、任意频段数的参数均衡器、立体声增强、混响（mverb 与 zita 类型，带预设）以及直流偏移滤波器。它还支持 ReplayGain/RVA 音量归一化。

渲染模式可以利用多个 CPU 核心并行将音频文件转换为 WAV 或 Au 格式，并提供响度归一化、可配置位深和浮点输出等选项。它支持 XSPF 和 JSPF 播放列表，同时支持 ListenBrainz scrobbling 以及用于正在播放更新的 Matrix 协议集成。

多线程 UI 基于 S-Lang 构建，具有可自定义的主题、横幅动画、VU 电平表和完整的键盘控制。此外还提供一个极简无界面（headless）UI，适用于资源受限的系统，或通过 UNIX 域套接字配合配套工具 **remote-benben** 进行远程控制。SID 文件支持使用 @ 记法的曲目选择语法（如 file.sid@1-3）。

benben 仅提供命令行界面，设计上不带文件浏览器；用户需以参数形式指定文件、目录或播放列表。

# CONFIGURATION

配置以 YAML 格式存储在 **$XDG_CONFIG_HOME/benben/benben.yaml**（通常是 ~/.config/benben/benben.yaml）。命令行选项会覆盖配置文件中的设置。

关键配置部分包括：音频驱动与缓冲设置、播放默认值（音量、采样率、循环次数、淡出）、音频效果（均衡器频段、软削波、立体声增强、混响类型与预设、直流滤波）、VGM 仿真器偏好（芯片核心、GD3 语言、伪立体声）、MIDI 设置（soundfont 路径、混响、合唱、声部滤波器类型）、C64/SID 设置（ROM 路径、芯片型号、曲长数据库）、UI 自定义（主题、横幅样式与动画、显示偏好），以及 ListenBrainZ 和 Matrix 的集成令牌。

针对特定歌曲的配置文件可以放在 **$XDG_CONFIG_HOME/benben/song-configs/** 目录下，命名为 **song-config-*.yaml**，每个文件包含一个 **match** 键，其值为 glob 模式，用于将设置应用到特定文件。

主题存储在 **$XDG_CONFIG_HOME/benben/themes/** 目录下，命名为 **theme-\<name\>.yaml**，支持 8 位 ANSI、24 位 RGB 以及十六进制颜色表示法。

# CAVEATS

配置文件格式在 1.0 版本之前被视为不稳定，可能会有变动。MIDI 播放需要指定 SoundFont 文件。SID 曲目长度的准确性依赖已配置的 HVSC 曲长数据库；未配置时曲目默认长度为 180 秒。采样率被限制在 8000 到 48000 Hz 范围内。benben 没有内置文件浏览器，需要显式给出文件或目录参数。要使用 24 位终端色彩，可能需要将 COLORTERM 环境变量设置为 truecolor。

# HISTORY

**benben** 由 **Remilia Scarlet** 作为个人项目创建，最初使用 **Crystal** 编程语言编写。开发始于约 **2023** 年，v0.4.0 版本于 **2024 年 3 月 7 日**在 VGMRips 上发布。VGM 芯片仿真构建于作者的 **YunoSynth** 库之上，该库是对 VGMPlay 声音仿真器代码的面向对象重写。**2025 年 1 月**，作者开始将 benben 从 Crystal 移植到 **Common Lisp**，到 **2025 年 4 月**，基于 Lisp 的 **v0.7.0** 已成为作者日常使用的音乐播放器。VGM 库也在 Lisp 版本中被重写为 **SatouSynth**。版本 **0.7.1** 于 **2025 年 11 月 6 日**发布。该项目采用 **GNU Affero General Public License v3** 许可证，托管在一个 Fossil 仓库中。

# INSTALL

```aur: yay -S benben```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[mpv](/man/mpv)(1), [ffmpeg](/man/ffmpeg)(1), [sox](/man/sox)(1), [aplay](/man/aplay)(1), [cmus](/man/cmus)(1), [moc](/man/moc)(1)
