# TAGLINE

终端中的 TUI 播客客户端

# TLDR

**交互式启动**播客客户端

```castero```

**从 OPML 文件导入**播客订阅

```castero --import [path/to/subscriptions.opml]```

**将当前订阅导出**到 OPML 文件

```castero --export [path/to/feeds.opml]```

**显示版本**信息

```castero --version```

# SYNOPSIS

**castero** [**-h**] [**-V**] [**--import** _PATH_] [**--export** _PATH_]

# PARAMETERS

**-h**, **--help**
> 显示帮助信息并退出。

**-V**, **--version**
> 显示版本信息并退出。

**--import** _PATH_
> 要导入的 OPML 订阅源文件路径；添加订阅后退出。

**--export** _PATH_
> 将当前订阅源保存为 OPML 文件的路径；导出后退出。

# DESCRIPTION

**castero** 是一个基于终端的播客客户端，用户可以订阅 RSS 播客源、浏览节目、下载以便离线播放，并直接在终端中播放。它使用基于 curses 的 TUI，提供多种可切换的布局。播放委托给 **VLC** 或 **mpv** 作为外部媒体播放器后端。

主要功能包括添加、删除和刷新播客源，将节目加入播放队列，调节音量和播放速度，在节目中跳转进度，标记节目为已播/未播，以及在订阅源内过滤或搜索。订阅可以通过 OPML 导入导出，便于在不同播客客户端之间迁移。

# KEY BINDINGS

```
h    Help              a    Add feed
q    Exit              d    Delete feed
r    Reload all        R    Reload selected
Enter  Play episode    Space  Add to queue
c    Clear queue       n    Next in queue
p/k  Pause/play        f/l  Seek forward
b/j  Seek backward     =/−  Volume up/down
]/[  Speed up/down     m    Mark played
s    Save offline      x    Delete download
/    Filter/search     1-5  Switch layout
```

# CONFIGURATION

配置存储于 **~/.config/castero/castero.conf**（首次运行时创建）。用户数据和下载内容存储于 **~/.local/share/castero/**。

值得注意的选项包括 **player**（mpv 或 vlc）、**default_layout**（1-5）、**default_playback_speed**、**default_volume**（0-100）、以秒为单位的 **seek_distance_forward/backward**、**reload_on_start**、**custom_download_dir**，以及代理设置（**proxy_http**、**proxy_https**）。所有按键绑定和颜色均可自定义。

# CAVEATS

需要安装外部媒体播放器（**VLC** 或 **mpv**）才能播放音频。需要 Python 3.5+ 和 SQLite3。该项目自 2022 年起没有新版本发布，可能已不再积极维护。

# HISTORY

**castero** 由 **Jake Robertson** 创建，于 **2018 年 4 月**首次发布。主要里程碑包括节目下载（v0.2.0，2018）、mpv 后端支持（v0.4.0，2019）、SQLite 数据库及已播/未播跟踪（v0.5.0，2019），以及 OPML 导入/导出（v0.6.0，2019）。最新版本为 v0.9.5。

# INSTALL

```nix: nix profile install nixpkgs#castero```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mpv](/man/mpv)(1), [vlc](/man/vlc)(1), [newsboat](/man/newsboat)(1), [cmus](/man/cmus)(1)
