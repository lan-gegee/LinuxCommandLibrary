# TAGLINE

通过 YouTube 下载 Spotify 曲目

# TLDR

**下载曲目**

```spotdl "[song name]"```

**从 URL 下载**

```spotdl [https://open.spotify.com/track/...]```

**下载播放列表**

```spotdl [https://open.spotify.com/playlist/...]```

**下载专辑**

```spotdl [https://open.spotify.com/album/...]```

**指定输出格式模板**

```spotdl --output "[{artist} - {title}]" [url]```

**下载为 MP3**

```spotdl --format mp3 [url]```

# SYNOPSIS

**spotdl** [_options_] _query_or_url_

# DESCRIPTION

**spotdl** 通过在 YouTube Music 上查找并下载匹配的曲目来下载 Spotify 歌曲。它使用 Spotify 的元数据打标签。

该工具下载音频、添加元数据和封面图，从 Spotify 链接生成标签完整的音乐文件。

# PARAMETERS

**--output** _template_
> 输出文件名模板。

**--format** _fmt_
> 音频格式（mp3, flac, ogg, m4a）。

**--bitrate** _rate_
> 音频比特率。

**-o** _dir_, **--output-dir** _dir_
> 输出目录。

**--threads** _n_
> 下载线程数。

**--no-cache**
> 不使用缓存。

**--sponsor-block**
> 移除赞助片段。

**--sync** _file_
> 与保存的文件同步。

**--cookie-file** _file_
> YouTube cookies 文件。

# CAVEATS

取决于 YouTube Music 的可用性。音质参差不齐。可能遇到限速。请尊重版权法律。

# HISTORY

**spotdl** 为连接 Spotify 曲库与可下载音频而创建。它由更早的工具演变而来，使用 yt-dlp 进行下载，并加入 Spotify 集成以获取元数据。

# INSTALL

```nix: nix profile install nixpkgs#spotdl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[yt-dlp](/man/yt-dlp)(1), [youtube-dl](/man/youtube-dl)(1), [ffmpeg](/man/ffmpeg)(1)
