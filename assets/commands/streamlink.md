# TAGLINE

将直播流管道传输给媒体播放器

# TLDR

**在默认播放器中打开流**

```streamlink [URL] [best]```

**在指定播放器中打开流**

```streamlink --player [mpv] [URL] [best]```

**列出可用画质**

```streamlink [URL]```

**将流录制到文件**

```streamlink -o [output.ts] [URL] [best]```

**以指定画质打开**

```streamlink [URL] [720p]```

**打开 Twitch 直播流**

```streamlink [twitch.tv/streamername] [best]```

**传递播放器参数**

```streamlink --player [mpv] --player-args "[--no-border]" [URL] [best]```

# SYNOPSIS

**streamlink** [_--player player_] [_-o file_] [_options_] _URL_ [_quality_]

# PARAMETERS

**-p** _PLAYER_, **--player** _PLAYER_
> 要使用的播放器。

**-a** _ARGS_, **--player-args** _ARGS_
> 传递给播放器的参数。

**-o** _FILE_, **--output** _FILE_
> 录制到文件。

**-r** _FILE_, **--record** _FILE_
> 边播放边录制。

**-f**, **--force**
> 覆盖输出文件。

**--default-stream** _QUALITY_
> 默认的流画质。

**--stream-url**
> 仅打印流 URL。

**--json**
> 以 JSON 格式输出。

**--retry-streams** _SEC_
> 流不在线时进行重试。

**--retry-max** _NUM_
> 最大重试次数。

**--retry-open** _NUM_
> 重试打开流的次数。

**--hls-live-edge** _SEG_
> 从直播边缘获取的分段数量。

**--twitch-disable-ads**
> 禁用 Twitch 广告。

**--twitch-low-latency**
> 启用低延迟模式。

**--http-header** _HEADER_
> 添加 HTTP 头。

**--http-cookie** _COOKIE_
> 添加 HTTP Cookie。

# DESCRIPTION

**streamlink** 从网站提取视频流并将其管道传输给媒体播放器。它绕过基于浏览器的播放器，让你可以使用 mpv 或 VLC 等轻量高效的播放器。

画质选择使用 best、worst 或具体分辨率（720p、1080p60）等标识符。列出画质可查看某个流的可选项。回退式选择（720p,480p,best）会依次尝试多种画质。

录制功能可将流保存为文件。结合播放器使用时，可以一边观看一边存档。输出格式取决于流的类型（通常是 TS 或 MP4）。

平台支持包括 Twitch、YouTube 和数百个其他站点。插件架构让社区可以为更多平台提供支持。

Twitch 专属特性包括广告跳过、低延迟模式，以及用于订阅者直播流的 OAuth 身份验证。配置可保存在 ~/.config/streamlink/config 中。

HTTP 选项可用于访问需要身份验证的流或添加自定义请求头，处理各种 DRM 与地域限制场景。

# CONFIGURATION

**~/.config/streamlink/config**
> 主配置文件，用于默认选项、播放器设置和插件参数。

**~/.config/streamlink/plugins/**
> 存放自定义或第三方流提取插件的目录。

# CAVEATS

站点支持依赖插件，站点改版可能导致失效。某些站点会阻止第三方访问。通常不支持 DRM 内容。画质选项因平台而异。广告屏蔽可能违反服务条款。

# HISTORY

**streamlink** 是 **livestreamer** 的分支，livestreamer 创建于 **2012 年**前后。在 livestreamer 开发停滞之后，streamlink 于 **2016 年**分支出来并获得积极维护。该项目支持大量流媒体网站，并持续由社区驱动开发。

# INSTALL

```pacman: sudo pacman -S streamlink```

```apk: sudo apk add streamlink```

```zypper: sudo zypper install streamlink```

```brew: brew install streamlink```

```nix: nix profile install nixpkgs#streamlink```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[youtube-dl](/man/youtube-dl)(1), [yt-dlp](/man/yt-dlp)(1), [mpv](/man/mpv)(1), [vlc](/man/vlc)(1)
