# TAGLINE

终端下的流式下载 BitTorrent 客户端

# TLDR

**下载种子**

```webtorrent download "[magnet:?xt=...]"```

**下载到目录**

```webtorrent download [file.torrent] -o [./downloads]```

**串流到播放器**

```webtorrent download [magnet] --vlc```

**投屏到 Chromecast**

```webtorrent download [magnet] --chromecast```

**做种文件**

```webtorrent seed [file.mp4]```

**显示种子信息**

```webtorrent info [file.torrent]```

**创建种子**

```webtorrent create [file.mp4]```

# SYNOPSIS

**webtorrent** _command_ [_--vlc_|_--mpv_] [_-o dir_] [_options_] _torrent_

# PARAMETERS

**download** _TORRENT_
> 下载种子。

**seed** _FILE_
> 为文件做种。

**info** _TORRENT_
> 显示信息。

**create** _FILE_
> 创建种子。

**-o**, **--out** _DIR_
> 输出目录。

**--vlc**
> 在 VLC 中打开。

**--mpv**
> 在 mpv 中打开。

**--chromecast**
> 投屏到 Chromecast。

**--airplay**
> 投屏到 AirPlay。

**-s**, **--select** _N_
> 选择文件索引。

# DESCRIPTION

**webtorrent** 是一款可以在下载仍在进行时将文件直接串流到 VLC、mpv 等媒体播放器，也可以将文件下载到磁盘的种子客户端。它同时支持传统 BitTorrent 节点以及基于 WebRTC 的浏览器节点。

download 命令将种子内容保存到指定目录，而 --vlc 或 --mpv 等串流选项会在数据到达时在对应播放器中打开媒体内容。它还支持投屏到 Chromecast 和 AirPlay 设备，以便在电视屏幕上观看。

seed 命令通过 BitTorrent 网络分享本地文件，create 命令生成新的 .torrent 文件。该工具接受磁力链接、种子文件和 info hash 作为输入。

# CAVEATS

不支持某些 tracker。串流需要足够的带宽。浏览器版本是不同的产品。

# HISTORY

**WebTorrent** 由 **Feross Aboukhadijeh** 创建，旨在把种子下载带入浏览器。CLI 版本将其功能扩展到了 Node.js。

# SEE ALSO

[transmission-cli](/man/transmission-cli)(1), [aria2c](/man/aria2c)(1), [vlc](/man/vlc)(1)
