# TAGLINE

从流媒体网站下载视频

# TLDR

**下载视频**

```you-get [https://example.com/video]```

**显示视频信息**

```you-get -i [https://example.com/video]```

**下载指定格式**

```you-get --format [dash-flv720] [url]```

**下载到目录**

```you-get -o [/output/dir] [url]```

**下载播放列表**

```you-get --playlist [url]```

**设置输出文件名**

```you-get -O [filename] [url]```

**使用代理**

```you-get -x [127.0.0.1:1080] [url]```

**携带 Cookie 下载**

```you-get -c [cookies.txt] [url]```

# SYNOPSIS

**you-get** [_-i_] [_-o dir_] [_-O name_] [_--format fmt_] [_options_] _url_

# PARAMETERS

**-i**, **--info**
> 仅显示视频信息。

**-o** _DIR_
> 输出目录。

**-O** _NAME_
> 输出文件名。

**--format** _FMT_
> 指定格式。

**--playlist**
> 下载播放列表。

**-c** _FILE_
> Cookie 文件。

**-x** _PROXY_
> HTTP 代理。

**-s** _PROXY_
> SOCKS5 代理。

**-u**
> 出错时自动重试。

**-n**
> 不合并（保留分片）。

**-F**
> 强制下载。

**--json**
> JSON 输出。

# DESCRIPTION

**you-get** 用于从网站下载视频，支持 YouTube、Bilibili、Vimeo 等众多视频平台。

信息模式（-i）在不下载的情况下显示可用格式，方便选择最佳画质或格式。

通过格式选择可下载特定画质。可用格式用 -i 查看，用 --format 选择。

播放列表支持可下载整个播放列表或频道，单个视频在输出中会编号。

Cookie 支持用于访问私有或年龄限制内容，Cookie 可从浏览器导出。

代理支持可通过防火墙访问，支持 HTTP 和 SOCKS5 代理。

# CAVEATS

网站支持可能因网站改版而失效。部分站点需要登录。下载速度因站点而异。使用时请考虑服务条款。

# HISTORY

**you-get** 由 **Mort Yao** 于 **2012 年**前后创建。它以 Python 编写，除国际平台外还重点支持中文视频网站。

# INSTALL

```apk: sudo apk add you-get```

```zypper: sudo zypper install you-get```

```brew: brew install you-get```

```nix: nix profile install nixpkgs#you-get```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[youtube-dl](/man/youtube-dl)(1), [yt-dlp](/man/yt-dlp)(1), [streamlink](/man/streamlink)(1), [ffmpeg](/man/ffmpeg)(1)
