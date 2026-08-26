# TAGLINE

快速的多站点视频和媒体下载器

# TLDR

从 URL **下载**视频

```lux "[url]"```

只**列出可用流**而不下载

```lux -i "[url]"```

按格式 ID **下载指定的流**

```lux -f [stream_id] "[url]"```

**下载整个播放列表**

```lux -p "[playlist_url]"```

**设置输出目录和文件名**

```lux -o [path/to/dir] -O [name] "[url]"```

**带 cookies 下载**（例如需要登录的网站）

```lux -c "[cookie_string]" "[url]"```

# SYNOPSIS

**lux** [*OPTIONS*] *URL*...

# DESCRIPTION

**lux** 是一个用 Go 编写的快速视频和媒体下载器。它可以从许多热门网站（YouTube、Bilibili、抖音等）提取可播放的流并下载，还可以选择用 FFmpeg 合并音频/视频。当给定的是不属于已知网站的直接资源 URL 时，它会回退为普通下载。

先用 **-i** 查看可用的画质和流 ID，再用 **-f** 选择其一。播放列表模式（**-p**）、多线程分片下载、代理、cookies 以及 aria2 RPC 都受支持，可用于大型任务或需要身份验证的任务。

# PARAMETERS

**-i**

> 仅获取信息：列出可用流和元数据而不下载。

**-f** *stream*

> 选择要下载的特定流 ID（来自 **-i** 输出）。

**-p**

> 下载播放列表而非单个条目。

**-n** *int*

> 用于分片视频的下载线程数（默认：10）。

**-c** *cookie*

> 用于身份验证或区域限制内容的 cookie 字符串。

**-r** *referrer*

> 要发送的 HTTP Referer 头。

**-o** *path*

> 输出目录。

**-O** *name*

> 输出文件名。

**-C**

> 下载字幕（YouTube 及支持的网站）。可与 **-items** 组合指定语言代码。

**-retry** *int*

> 下载失败时的重试次数（默认：10）。

**-start** *n*, **-end** *n*, **-items** *list*

> 播放列表的范围或条目选择（例如 **1,5,8-10**）。

**-aria2**

> 将下载转交给 aria2 RPC 端点处理（**-aria2addr**、**-aria2token** 等）。

**-d**

> 调试模式。

**-j**

> 以 JSON 格式打印提取的数据。

**-v**

> 显示版本号。

# CAVEATS

将分离的音频/视频流合并为最终文件需要 FFmpeg；没有它下载仍然可以工作。网站支持和流 ID 会随着上游网站 API 的变化而变化。当某个站点失效时，优先使用官方软件包或发布二进制文件，而不是过时的发行版构建。

# INSTALL

```zypper: sudo zypper install lux```

```brew: brew install lux```

```nix: nix profile install nixpkgs#lux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[yt-dlp](/man/yt-dlp)(1), [youtube-dl](/man/youtube-dl)(1), [ffmpeg](/man/ffmpeg)(1), [aria2c](/man/aria2c)(1)

# RESOURCES

```[Source code](https://github.com/iawia002/lux)```

<!-- verified: 2026-07-19 -->
