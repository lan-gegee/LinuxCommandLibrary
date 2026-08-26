# TAGLINE

BBC iPlayer 电视与广播节目下载器

# TLDR

**搜索节目**

```get_iplayer "[search term]"```

**下载节目**

```get_iplayer --get [index_number]```

**按 PID 下载**

```get_iplayer --pid [pid]```

**列出电视节目**

```get_iplayer --type=tv "[search]"```

**列出广播节目**

```get_iplayer --type=radio "[search]"```

**设置输出目录**

```get_iplayer --output [/path/to/dir] --get [index]```

**以指定画质下载**

```get_iplayer --tvmode=best --get [index]```

# SYNOPSIS

**get_iplayer** [_options_] [_search_...]

# PARAMETERS

**--get** _index_
> 按索引号下载。

**--pid** _pid_
> 按节目 PID 下载。

**--type** _type_
> 媒体类型（tv、radio、podcast）。

**--output** _dir_
> 输出目录。

**--tvmode** _mode_
> 电视画质偏好（fhd、hd、sd、web、mobile），以逗号分隔，按优先级从高到低排列。

**--radiomode** _mode_
> 广播音质偏好（high、std、med、low）。

**--pvr**
> 运行 PVR 调度器。

**--refresh**
> 刷新节目缓存。

**--url** _URL_
> 录制指定 iPlayer 节目 URL 中的 PID。

**--subtitles**
> 在可用时下载字幕。

**--audio-only**
> 只下载电视节目的音频流（生成 .m4a 文件）。

**--file-prefix** _TEMPLATE_
> 文件名前缀模板（不含目录和扩展名）。

**--attempts** _N_
> 建立或恢复失败连接的尝试次数。

# CONFIGURATION

**~/.get_iplayer/options**
> 用户偏好文件，存放默认选项和设置。

**~/.get_iplayer/presets**
> 自定义画质与录制预设。

# DESCRIPTION

**get_iplayer** 从 BBC 的流媒体服务下载 BBC iPlayer 的电视和广播节目。它提供跨 iPlayer 目录的搜索功能、画质选择，以及用于录制节目的自动化 PVR 式调度。

该工具可以下载点播和直播内容，并支持字幕和元数据。它维护一个本地可用节目缓存以加快搜索速度，并支持批量下载。

iPlayer 上的节目通常在播出后可观看 30 天，不过部分内容可能因 BBC 版权协议而有不同的可用时间窗口。

# CAVEATS

仅适用于 BBC 内容，且通常需要英国 IP 地址。节目在 iPlayer 上 30 天后过期（部分内容的可用窗口不同）。下载和转换流需要 ffmpeg。

# INSTALL

```dnf: sudo dnf install get_iplayer```

```brew: brew install get_iplayer```

```nix: nix profile install nixpkgs#get_iplayer```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[youtube-dl](/man/youtube-dl)(1), [yt-dlp](/man/yt-dlp)(1), [ffmpeg](/man/ffmpeg)(1)
