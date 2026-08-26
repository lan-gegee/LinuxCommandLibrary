# TAGLINE

下载音乐并自动写入元数据标签

# TLDR

**连同元数据一起下载歌曲**

```ytmdl [song name]```

**从 YouTube URL 下载**

```ytmdl [https://youtube.com/watch?v=VIDEO_ID]```

**指定输出目录**

```ytmdl -o [~/Music] [song name]```

**跳过确认提示**

```ytmdl --skip-meta [song name]```

**下载为 MP3**

```ytmdl --format mp3 [song name]```

# SYNOPSIS

**ytmdl** [_options_] [_song_|_URL_]

# PARAMETERS

**-o**, **--output-dir** _DIR_
> 设置下载的输出目录

**--format** _FORMAT_
> 音频格式（mp3、m4a、opus 等）

**--skip-meta**
> 跳过查询元数据，直接使用默认值

**-q**, **--quiet**
> 不显示输出

**--proxy** _URL_
> 使用代理下载

**--level** _LEVEL_
> 日志级别（DEBUG、INFO、WARNING、ERROR）

**--disable-metaadd**
> 禁止为歌曲添加元数据

**--trim**, **-t**
> 去除开头和结尾的静音

# DESCRIPTION

**ytmdl** 是一款从 YouTube 下载音乐的工具，会自动从 iTunes、Spotify、Deezer 和 Gaana 等来源添加元数据（艺术家、专辑、封面、歌词）。它搜索歌曲，以音频形式下载，并写入正确的标签。

该工具既可接受歌名（会在 YouTube 上搜索），也可接受直接的 YouTube URL。它会展示来自多个来源的元数据选项，让你选择最匹配的一项。

配置保存在 **~/.config/ytmdl/config** 中，可设置默认行为、输出目录和首选的元数据来源。

# CAVEATS

元数据的准确性取决于搜索结果。冷门或拼错的歌可能得到错误的元数据。

音频转换和格式处理需要 **ffmpeg**。

部分元数据源可能有地区限制或限流。

下载的内容可能受版权保护。请尊重内容创作者的权利。

# INSTALL

```nix: nix profile install nixpkgs#ytmdl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[yt-dlp](/man/yt-dlp)(1), [ffmpeg](/man/ffmpeg)(1), [youtube-dl](/man/youtube-dl)(1), [spotdl](/man/spotdl)(1)
