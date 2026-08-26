# TAGLINE

终端 YouTube 搜索与播放客户端

# TLDR

**搜索视频**

```youtube-viewer [search query]```

**播放视频 URL**

```youtube-viewer [https://youtube.com/watch?v=...]```

**仅音频**（无视频）

```youtube-viewer -n [query]```

**下载视频**

```youtube-viewer -d [query]```

**使用指定播放器播放**

```youtube-viewer --player=[vlc] [query]```

**搜索频道**

```youtube-viewer -sc [channel_name]```

**显示热门**视频

```youtube-viewer --trending```

**列出频道**的上传内容

```youtube-viewer -u [channel_name]```

**搜索播放列表**

```youtube-viewer -sp [query]```

# SYNOPSIS

**youtube-viewer** [_options_] [_query_|_URL_]

# PARAMETERS

**-n**, **--novideo**
> 仅播放音频（无视频）。

**-d**, **--download**
> 下载视频而非流式播放。

**--player** _PLAYER_
> 指定视频播放器（例如 mpv、vlc、mplayer）。

**-sv**, **--search-videos**
> 搜索 YouTube 视频（默认模式）。

**-sc**, **--search-channels**
> 搜索 YouTube 频道。

**-sp**, **--search-playlists**
> 搜索播放列表。

**-u**, **--uploads** _NAME_
> 列出某频道/用户上传的视频。

**--trending**
> 显示热门视频。

**-r**, **--resolution** _RES_
> 设置视频分辨率（例如 best、1080p、720p）。

**-f**, **--fullscreen**
> 启用全屏播放。

**-i**, **--info**
> 显示视频信息。

**-S**, **--subscriptions**
> 显示订阅的频道。

# DESCRIPTION

**youtube-viewer** 是一款命令行客户端，可直接在终端中搜索、流式播放和下载 YouTube 视频。它查询 YouTube API，展示带编号的搜索结果，并启动你选择的媒体播放器进行播放。

支持多种视频播放器，包括 mpv、VLC 和 MPlayer，可通过 **--player** 选项配置。仅音频模式（**-n** / **--novideo**）只流式传输音轨，减少带宽占用。**-d** 选项将视频下载到本地而非流式播放。

频道浏览（**-u**）列出特定创作者的上传内容，**-sc** 搜索频道，**--trending** 显示当前热门视频。分辨率可用 **-r** 控制，全屏播放可用 **-f** 启用。播放列表支持通过 **-sp** 进行搜索、通过 **--pid** 按播放列表 ID 播放。

# CAVEATS

需要有效的 YouTube Data API v3 密钥。可能因 YouTube API 变更而失效。必须安装受支持的视频播放器（mpv、vlc 或 mplayer）。替代分支 **pipe-viewer** 通过 Invidious 实例工作，无需 API 密钥。

# HISTORY

**youtube-viewer** 由 **trizen** 创建，是一款以 Perl 编写的轻量级命令行 YouTube 客户端。它通过 YouTube Data API v3 在终端中实现 YouTube 内容的搜索、流式播放与下载。

# INSTALL

```apk: sudo apk add youtube-viewer```

```nix: nix profile install nixpkgs#youtube-viewer```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[yt-dlp](/man/yt-dlp)(1), [mpv](/man/mpv)(1), [vlc](/man/vlc)(1)
