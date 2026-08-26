# TAGLINE

用 fzf 搜索并播放 YouTube 视频

# TLDR

带缩略图**搜索**

```ytfzf -t [search_pattern]```

循环播放**音频**

```ytfzf -m -a -l [search_pattern]```

从历史记录中**下载**

```ytfzf -d --choose-from-history```

播放**所有**音频结果

```ytfzf -m -A [search_pattern]```

显示**热门**视频

```ytfzf --trending --ext-menu [search_pattern]```

搜索 **PeerTube**

```ytfzf --peertube [search_pattern]```

# SYNOPSIS

**ytfzf** [_OPTIONS_] [_SEARCH_]

# PARAMETERS

**-t, --show-thumbnails**
> 显示缩略图预览

**-m, --audio-only**
> 仅播放音频

**-a, --auto-select**
> 自动选择第一个结果

**-l, --loop**
> 循环播放

**-d, --download**
> 下载而非播放

**-A, --select-all**
> 选择全部结果

**--trending**
> 显示热门视频

**--peertube**
> 搜索 PeerTube 而非 YouTube

**--ext-menu**
> 使用外部菜单程序

# DESCRIPTION

**ytfzf** 是一个 POSIX Shell 脚本，用于查找和播放 YouTube 及其他平台的视频。它使用 fzf 进行选择，使用 mpv 进行播放。

该工具支持搜索、流式播放和下载视频，并提供缩略图预览。

# CAVEATS

需要 fzf、mpv 以及 yt-dlp 或 youtube-dl。缩略图预览需要 ueberzug 或类似工具。

# INSTALL

```pacman: sudo pacman -S ytfzf```

```apk: sudo apk add ytfzf```

```nix: nix profile install nixpkgs#ytfzf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[yt-dlp](/man/yt-dlp)(1), [youtube-dl](/man/youtube-dl)(1), [mpv](/man/mpv)(1)
