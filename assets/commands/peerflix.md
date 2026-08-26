# TAGLINE

直接流式播放种子

# TLDR

**将种子流式播放到默认播放器**

```peerflix "[magnet_link]"```

**流式播放到 VLC**

```peerflix "[torrent_file]" --vlc```

**流式播放到 mpv**

```peerflix "[magnet_link]" --mpv```

**按索引选择特定文件**

```peerflix "[magnet_link]" -i [1]```

**列出种子中的文件**

```peerflix "[magnet_link]" -l```

**带字幕流式播放**

```peerflix "[magnet_link]" --vlc -t [subtitles.srt]```

# SYNOPSIS

**peerflix** [_options_] _torrent_

# PARAMETERS

_TORRENT_
> 种子文件或磁力链接。

**--vlc**
> 在 VLC 中打开流。

**--mplayer**
> 在 MPlayer 中打开流。

**--mpv**
> 在 mpv 中打开流。

**-i** _INDEX_, **--index** _INDEX_
> 要流式播放的文件索引。

**-l**, **--list**
> 列出种子中可用的文件。

**-t** _FILE_, **--subtitles** _FILE_
> 加载字幕文件。

**-a**
> 播放种子中的所有文件。

**-c** _NUM_, **--connections** _NUM_
> 最大连接节点数（默认：100）。

**-p** _PORT_, **--port** _PORT_
> HTTP 流式传输端口（默认：8888）。

**--remove**
> 流式播放结束后删除文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**peerflix** 是一个基于 Node.js 的流式种子客户端，无需等待完整下载即可立即播放。它会优先下载文件的起始部分，从而实现即时流式播放。

该工具会启动一个本地 HTTP 服务器，并可将流传送给 VLC、mpv 或 MPlayer 等媒体播放器。它支持多文件种子的文件选择和字幕加载。

# CAVEATS

需要 Node.js。通过 `npm install -g peerflix` 安装。播放时需要媒体播放器（VLC、mpv 或 MPlayer）。

# HISTORY

peerflix 的诞生是为了在**不必完整下载的情况下流式播放种子内容**。

# INSTALL

```aur: yay -S peerflix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[webtorrent](/man/webtorrent)(1), [vlc](/man/vlc)(1), [mpv](/man/mpv)(1), [mplayer](/man/mplayer)(1)
