# TAGLINE

从 YouTube 及其他网站下载视频

# TLDR

**下载视频**

```youtube-dl "[url]"```

**仅下载音频**（最佳画质）

```youtube-dl -x --audio-format mp3 "[url]"```

**列出视频可用格式**

```youtube-dl -F "[url]"```

**下载指定格式**

```youtube-dl -f [format_code] "[url]"```

**下载播放列表**

```youtube-dl "[playlist_url]"```

**使用自定义文件名模板**下载

```youtube-dl -o "%(title)s.%(ext)s" "[url]"```

**下载字幕**

```youtube-dl --write-sub --sub-lang [en] "[url]"```

**续传未完成的下载**

```youtube-dl -c "[url]"```

# SYNOPSIS

**youtube-dl** [_options_] _url_ [_url ..._]

# PARAMETERS

**-f**, **--format** _format_
> 视频格式代码。用 **-F** 列出可用格式。

**-F**, **--list-formats**
> 列出该视频所有可用格式。

**-o**, **--output** _template_
> 输出文件名模板，可使用 %(title)s、%(ext)s 等变量。

**-x**, **--extract-audio**
> 仅提取音频轨。

**--audio-format** _format_
> 提取的音频格式：mp3、aac、flac、wav 等。

**--audio-quality** _quality_
> 音频质量：0（最佳）到 9（最差），或指定位率。

**-a**, **--batch-file** _file_
> 从文件读取 URL（每行一个）。

**-c**, **--continue**
> 续传部分下载的文件。

**-i**, **--ignore-errors**
> 遇错继续（对播放列表有用）。

**--playlist-start** _num_
> 从播放列表的第几个视频开始。

**--playlist-end** _num_
> 下载到播放列表的第几个视频为止。

**--write-sub**
> 下载字幕。

**--sub-lang** _langs_
> 要下载的字幕语言。

**-j**, **--dump-json**
> 以 JSON 打印视频信息而不下载。

**--cookies** _FILE_
> 从 Netscape 格式的 Cookie 文件读取 Cookie，用于需要认证的访问。

**--proxy** _URL_
> 使用指定的 HTTP/HTTPS/SOCKS 代理。

**--geo-bypass**
> 通过伪造 X-Forwarded-For 头绕过地域限制。

**-u** _USER_, **--username** _USER_
> 使用账户用户名登录。

**-p** _PASS_, **--password** _PASS_
> 使用账户密码登录。

**-v**, **--verbose**
> 打印调试信息。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**youtube-dl** 是一款命令行程序，用于从 YouTube 和数百个其他视频平台下载视频。它支持播放列表、频道和单个视频，并提供格式选择、音频提取和字幕下载等选项。

输出文件名可以通过包含元数据变量的模板自定义。配置选项可保存在 **~/.config/youtube-dl/config** 或 **/etc/youtube-dl.conf** 中以实现持久设置。

该工具需要 Python，可在 Linux、macOS 和 Windows 上运行。

# CAVEATS

youtube-dl 的开发已明显放缓。建议改用 **yt-dlp**——一个积极维护的分支，功能更多、性能更好且支持更多网站。某些网站可能会屏蔽 youtube-dl，或要求提供 Cookie/认证才能访问。

# HISTORY

youtube-dl 由 Ricardo Garcia 创建于 **2006 年**，此后成为最受欢迎的命令行视频下载工具之一。项目迁移到 GitHub 后得到广泛采用。由于 **2020 年 10 月**遭 DMCA 下架（后已恢复）以及开发进度缓慢，社区分支 **yt-dlp** 于 **2021 年**出现，并成为推荐的替代品。

# INSTALL

```dnf: sudo dnf install youtube-dl```

```apk: sudo apk add yt-dlp-core```

```nix: nix profile install nixpkgs#youtube-dl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[yt-dlp](/man/yt-dlp)(1), [ffmpeg](/man/ffmpeg)(1), [streamlink](/man/streamlink)(1)
