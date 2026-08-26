# TAGLINE

从 LinkedIn Learning 下载视频

# TLDR

**下载 LinkedIn 视频**

```llvd [video_url]```

**指定输出文件**

```llvd -o [output.mp4] [video_url]```

**按画质下载**

```llvd -q [720] [video_url]```

**列出可用格式**

```llvd -F [video_url]```

**下载字幕**

```llvd --write-subs [video_url]```

# SYNOPSIS

**llvd** [_options_] _url_

# PARAMETERS

_URL_
> LinkedIn Learning 视频 URL。

**-o** _FILE_
> 输出文件名。

**-q** _QUALITY_
> 视频画质（360、480、720、1080）。

**-F**
> 列出可用格式。

**--write-subs**
> 下载字幕。

**--help**
> 显示帮助信息。

# DESCRIPTION

**llvd** 用于从 LinkedIn Learning 下载视频，支持多种画质级别和字幕提取。

该工具需要 LinkedIn 凭据才能通过身份验证访问学习内容。

# CAVEATS

需要 LinkedIn 账户。需考虑服务条款问题。需要身份验证。

# HISTORY

llvd 的创建目的是让获得授权的用户能够离线访问 LinkedIn Learning 的视频内容。

# SEE ALSO

[youtube-dl](/man/youtube-dl)(1), [yt-dlp](/man/yt-dlp)(1)
