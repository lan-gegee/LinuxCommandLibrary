# TAGLINE

下载 RTMP 流媒体

# TLDR

**将 RTMP 流下载**到文件

```rtmpdump -r "[rtmp://server/path]" -o [output.flv]```

**使用单独的 playpath 下载**

```rtmpdump -r "[rtmp://server/app]" -y "[playpath]" -o [output.flv]```

**录制直播流**

```rtmpdump -r "[rtmp://server/live]" -v -o [output.flv]```

**带 SWF 验证下载**

```rtmpdump -r "[rtmp://server/path]" -W "[http://example.com/player.swf]" -o [output.flv]```

**恢复中断的下载**

```rtmpdump -r "[rtmp://server/path]" -o [output.flv] --resume```

**带进度指示下载**

```rtmpdump -r "[rtmp://server/path]" -o [output.flv] --hashes```

# SYNOPSIS

**rtmpdump** **-r** _url_ [**-o** _file_] [_options_]

# PARAMETERS

**-r** _URL_, **--rtmp** _URL_
> 要下载的流的 RTMP URL。

**-o** _FILE_, **--flv** _FILE_
> 输出文件名。若未指定，则流式输出到标准输出。

**-y** _PATH_, **--playpath** _PATH_
> 覆盖从 RTMP URL 中解析出的 playpath。

**-a** _APP_, **--app** _APP_
> 要在 RTMP 服务器上连接的应用名称。

**-v**, **--live**
> 指定媒体为直播流。此时无法续传或定位播放位置。

**-W** _URL_, **--swfVfy** _URL_
> SWF 播放器的 URL。哈希值和大小会自动计算。

**-s** _URL_, **--swfUrl** _URL_
> 该媒体对应的 SWF 播放器 URL。某些服务器验证时需要此参数。

**--resume**
> 恢复未完成的下载。

**-T** _TOKEN_, **--token** _TOKEN_
> SecureToken 响应所用的密钥。

**--timeout** _SECS_
> 在 SECS 秒内未收到数据则使会话超时。

**-n** _HOST_, **--host** _HOST_
> 覆盖 RTMP URL 中的主机名。

**-c** _PORT_, **--port** _PORT_
> 覆盖 RTMP URL 中的端口号。

**--hashes**
> 每完成 1% 的进度显示一个井号标记。

**-q**, **--quiet**
> 抑制所有命令输出。

**-V**, **--verbose**
> 详细输出。

**-z**, **--debug**
> 调试级输出，包含所有数据包数据的十六进制转储。

# DESCRIPTION

**rtmpdump** 使用实时消息协议（Real-Time Messaging Protocol，RTMP）下载媒体流，该协议最初由 Adobe 为基于 Flash 的流媒体开发。它会连接 RTMP 服务器并将流数据保存到本地文件，同时支持直播广播和点播视频内容。

该工具负责完整的 RTMP 握手与协议协商，包括在服务器要求时进行的 SWF（Shockwave Flash）验证。RTMP URL 由服务器地址、应用路径和 playpath 组成，后者可能需要单独指定。对于直播流，**-v** 标志可启用直播模式，录制会持续到流结束或用户中断为止。

中断的下载可以使用 **--resume** 标志恢复，这在不可靠网络环境下进行长时间录制时尤其有用。默认输出为 FLV（Flash Video）格式，可使用 ffmpeg 等工具转换为其他格式。

# CAVEATS

随着 HLS 和 DASH 等现代流媒体协议取代 RTMP，它的使用正在减少。某些服务器要求 SWF 验证或令牌认证。输出始终为 FLV 格式。

# HISTORY

**rtmpdump** 是作为一个开源 RTMP 客户端而诞生的。在现代流媒体协议普及之前，它让下载 Adobe Flash 视频流成为可能。

# INSTALL

```apt: sudo apt install rtmpdump```

```dnf: sudo dnf install rtmpdump```

```pacman: sudo pacman -S rtmpdump```

```apk: sudo apk add rtmpdump```

```brew: brew install rtmpdump```

```nix: nix profile install nixpkgs#rtmpdump```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1), [streamlink](/man/streamlink)(1), [youtube-dl](/man/youtube-dl)(1), [curl](/man/curl)(1)
