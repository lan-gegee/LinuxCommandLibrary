# TAGLINE

Deezer 音乐流媒体服务下载工具

# TLDR

按 URL **下载单曲**

```deemix [https://www.deezer.com/track/12345]```

**下载专辑**

```deemix [https://www.deezer.com/album/12345]```

**下载播放列表**

```deemix [https://www.deezer.com/playlist/12345]```

**指定输出目录**

```deemix -p [/path/to/music] [url]```

**以指定音质下载**

```deemix -b [flac] [url]```

**同时下载多个 URL**

```deemix [url1] [url2]```

在当前目录**使用便携式配置文件夹**

```deemix --portable [url]```

# SYNOPSIS

**deemix** [_options_] _url_...

# PARAMETERS

_URL_
> 单曲、专辑、播放列表或艺人的 Deezer URL。可以提供多个 URL。

**-p**, **--path** _DIR_
> 下载内容的输出目录。

**-b**, **--bitrate** _QUALITY_
> 音频音质：128、320、flac。

**--portable**
> 在当前目录而不是用户配置目录中创建配置文件夹。

**--help**
> 显示帮助信息。

# CONFIGURATION

**~/.config/deemix/.arl**
> 存储 Deezer ARL 身份验证令牌。

**~/.config/deemix/config.json**
> 配置文件，用于设置下载音质、文件夹结构等。

# DESCRIPTION

**deemix** 是面向 Deezer 音乐流媒体服务的下载工具。它可以从 Deezer 下载单曲、专辑、播放列表和艺人全集，音频质量最高支持 FLAC 无损格式。

该工具需要通过 Deezer 账户的 ARL 令牌完成身份验证；首次运行时会提示输入令牌并将其保存到配置文件夹。下载的文件包含元数据和专辑封面。可通过 config.json 以可配置的文件夹结构组织输出文件。

配置可选的 Spotify 插件后，deemix 还能将 Spotify 链接解析为对应的 Deezer 链接。

# CAVEATS

需要有效订阅对应的 Deezer ARL 令牌。FLAC 音质需要 Deezer HiFi 订阅。下载受版权保护的内容可能违反服务条款。ARL 令牌会定期过期。

# HISTORY

deemix 由 **RemixDev** 开发，是 deezloader 等早期 Deezer 下载工具的延续。原作者于 **2022 年**停止开发；社区分支仍在继续维护代码库。

# INSTALL

```aur: yay -S deemix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[spotdl](/man/spotdl)(1), [youtube-dl](/man/youtube-dl)(1), [yt-dlp](/man/yt-dlp)(1)

# RESOURCES

```[Source code](https://gitlab.com/RemixDev/deemix-py)```

<!-- verified: 2026-07-11 -->
