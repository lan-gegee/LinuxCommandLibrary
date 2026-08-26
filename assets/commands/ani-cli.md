# TAGLINE

从终端搜索并观看动漫

# TLDR

**搜索**并观看动漫

```ani-cli [anime_name]```

从历史记录**继续**观看

```ani-cli -c```

**下载**而不是在线播放

```ani-cli -d [anime_name]```

选择特定**画质**

```ani-cli -q [720] [anime_name]```

使用 **VLC** 播放器

```ani-cli -v [anime_name]```

观看**配音版**

```ani-cli --dub [anime_name]```

观看指定的**剧集**范围

```ani-cli -e [1-5] [anime_name]```

# SYNOPSIS

**ani-cli** [_-cdevN_] [_-q quality_] [_-e episodes_] [_--dub_] [_search_query_]

# DESCRIPTION

**ani-cli** 是一个从多个来源搜索和播放动漫的命令行工具。它提供基于终端的界面，可用于选择动漫、挑选剧集，并在你偏好的视频播放器中播放。

该工具抓取动漫流媒体站点以查找可用内容，并以交互式菜单形式呈现选项。

# PARAMETERS

**-c**, **--continue**
> 从历史记录继续观看

**-d**, **--download**
> 下载而不是在线播放

**-e**, **--episode** _range_
> 指定集数或范围（如 1-5）

**-q** _quality_
> 指定视频画质（best、worst、360、480、720、1080）。默认为 best。

**-v**, **--vlc**
> 使用 VLC 播放器而不是 mpv

**-D**, **--delete**
> 删除观看历史

**-s**, **--syncplay**
> 使用 Syncplay 与朋友一起观看（仅限 mpv）

**-N**, **--non-interactive**
> 禁用交互式菜单

**-S** _index_, **--select-nth** _index_
> 直接选择第 n 个搜索结果而不询问

**--dub**
> 播放配音版而不是字幕版

**--skip**
> 使用 ani-skip 跳过片头（仅限 mpv）

**--no-detach**
> 不分离播放器（适合在终端内播放）

**--rofi**
> 交互式菜单使用 rofi 而不是 fzf

**-U**, **--update**
> 更新 ani-cli

**-h**, **--help**
> 显示帮助信息

# CONFIGURATION

**ANI_CLI_MODE**
> 控制媒体模式：sub 或 dub。默认为 sub。

**ANI_CLI_QUALITY**
> 控制视频画质（best、worst、360、480、720、1080）。默认为 best。

**ANI_CLI_DOWNLOAD_DIR**
> 下载目录。默认为当前目录。

**ANI_CLI_EXTERNAL_MENU**
> 设为 1 时使用 rofi dmenu 而不是 fzf。默认为 0。

**ANI_CLI_SKIP_INTRO**
> 设为 1 时使用 ani-skip 跳过片头（仅限 mpv）。默认为 0。

# CAVEATS

依赖可能变化或失效的外部流媒体来源。画质和可用性因作品而异。需要 mpv 或 vlc 进行播放。可能并非在所有地区都可用。依赖 curl、sed、grep 和 fzf 作为前置组件。

# HISTORY

**ani-cli** 作为社区项目而创建，服务于偏爱命令行工具的动漫爱好者。项目一直得到积极维护，持续更新以适应不断变化的流媒体来源。

# INSTALL

```aur: yay -S ani-cli```

```nix: nix profile install nixpkgs#ani-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[mpv](/man/mpv)(1), [vlc](/man/vlc)(1), [yt-dlp](/man/yt-dlp)(1), [fzf](/man/fzf)(1)
