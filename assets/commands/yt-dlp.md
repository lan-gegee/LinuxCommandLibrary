# TAGLINE

功能丰富的视频下载器分支

# TLDR

**下载视频**

```yt-dlp [https://youtube.com/watch?v=VIDEO_ID]```

**仅下载音频**（最佳质量）

```yt-dlp -x [url]```

**下载为 MP3 音频**

```yt-dlp -x --audio-format mp3 [url]```

**列出可用格式**

```yt-dlp -F [url]```

**下载指定格式**

```yt-dlp -f [format_code] [url]```

**下载最佳视频 + 音频**

```yt-dlp -f "bestvideo+bestaudio" [url]```

**下载整个播放列表**

```yt-dlp [playlist_url]```

**连同字幕下载**

```yt-dlp --write-subs --sub-lang en [url]```

**使用自定义文件名下载**

```yt-dlp -o "%(title)s.%(ext)s" [url]```

# SYNOPSIS

**yt-dlp** [_options_] _URL_...

# PARAMETERS

**-F**, **--list-formats**
> 列出可用格式

**-f** _FORMAT_
> 按格式代码或质量选择器选择格式

**-x**, **--extract-audio**
> 仅提取音频

**--audio-format** _FORMAT_
> 将音频转换为指定格式（mp3、aac、wav 等）

**--audio-quality** _QUALITY_
> 音频质量（0=最佳，9=最差）

**-o** _TEMPLATE_
> 输出文件名模板

**--write-subs**
> 下载字幕

**--sub-lang** _LANGS_
> 字幕语言（逗号分隔）

**--embed-subs**
> 将字幕嵌入视频

**--embed-thumbnail**
> 将缩略图嵌入音频

**-P** _PATH_
> 下载到指定目录

**--no-playlist**
> 当 URL 指向播放列表时仅下载单个视频

**--playlist-items** _ITEMS_
> 要下载的播放列表条目（例如 1,3,5-10）

**--cookies-from-browser** _BROWSER_
> 从浏览器提取 Cookie（chrome、firefox、edge、safari 等）

**--limit-rate** _RATE_
> 限制下载速度（例如 50K、4.2M）

**--sponsorblock-mark** _CATS_
> 在视频章节中标记 SponsorBlock 类别（sponsor、intro、outro 等）

**-U**, **--update**
> 更新 yt-dlp

# FILENAME TEMPLATE

**%(title)s**：视频标题
**%(id)s**：视频 ID
**%(ext)s**：文件扩展名
**%(uploader)s**：频道名称
**%(upload_date)s**：上传日期（YYYYMMDD）
**%(playlist_index)s**：播放列表中的位置

# DESCRIPTION

**yt-dlp** 是一款功能丰富的命令行程序，用于从 YouTube 和众多其他网站下载视频。它是 youtube-dl 的分支，具有更多功能并保持活跃维护。

该工具支持数千个网站，不限于 YouTube。使用 **--list-extractors** 可查看所有支持的站点。

格式选择非常强大：**bestvideo+bestaudio** 合并分离的流，**best[height<=720]** 限制画质，而 **-F** 得到的具体格式代码可选择确切的流。

配置可保存在 **~/.config/yt-dlp/config** 中作为默认选项。

# CAVEATS

站点支持依赖提取器的更新。网站改版后，提取器在更新前可能失效。请定期运行 **yt-dlp -U**。

部分站点需要身份验证。使用 **--cookies-from-browser** 或 **--cookies** 提供登录 Cookie。

下载的内容可能受版权保护。请尊重内容创作者的权利和服务条款。

合并格式需要安装 **ffmpeg** 才能正确组合视频/音频。

# INSTALL

```dnf: sudo dnf install yt-dlp```

```pacman: sudo pacman -S yt-dlp```

```apk: sudo apk add yt-dlp-core```

```zypper: sudo zypper install yt-dlp```

```brew: brew install yt-dlp```

```nix: nix profile install nixpkgs#yt-dlp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1), [youtube-dl](/man/youtube-dl)(1), [aria2c](/man/aria2c)(1), [wget](/man/wget)(1)
