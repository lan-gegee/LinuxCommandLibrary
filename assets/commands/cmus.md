# TAGLINE

小巧快速的终端音乐播放器

# TLDR

在特定目录中**打开** cmus

```cmus [path/to/directory]```

将文件或目录**加入**曲库

```:add [path/to/file_or_directory]```

**刷新**曲库中歌曲的元数据

```:update-cache```

**搜索**歌曲、专辑或艺术家

```/[something]```

**暂停/继续播放**当前歌曲

```c```

切换**随机播放**模式

```s```

**退出** cmus

```q```

# SYNOPSIS

**cmus** [_options_] [_directory_]

# PARAMETERS

**--listen** _ADDR_
> 在 UNIX 套接字或 _host:port_ 上监听，而非 **cmus-remote** 的默认位置

**--plugins**
> 列出可用的输入/输出插件并退出

**--show-cursor**
> 始终显示光标（对屏幕阅读器有用）

**--help**
> 显示用法信息并退出

**--version**
> 显示版本信息并退出

# DESCRIPTION

**cmus** 是一款面向类 Unix 系统的小巧、快速且功能强大的终端音乐播放器。通过其基于插件的编解码系统，它支持多种音频格式，包括 Ogg Vorbis、MP3、FLAC、Opus、Musepack、WavPack、WAV、AAC 和 MP4。

界面提供七个视图，可通过数字键 1-7 访问：曲库（艺术家/专辑树）、排序曲库（扁平列表）、播放列表、播放队列、目录浏览器、过滤器和设置。使用方向键导航并用 Enter 选中，全程支持 vi 风格的按键绑定。

cmus 具有无间隙播放和 ReplayGain 支持，还可以通过 **cmus-remote** 命令或其套接字接口远程控制，适合与窗口管理器和状态栏集成。

# KEYBINDINGS

**c**
> 暂停/继续播放

**s**
> 切换随机播放

**r**
> 切换循环播放

**b**
> 下一曲

**z**
> 上一曲

**1-7**
> 切换视图（曲库、排序曲库、播放列表、队列、浏览器、过滤器、设置）

**q**
> 退出

**:add** _path_
> 将文件添加到曲库

**/**_query_
> 搜索

# CONFIGURATION

**~/.config/cmus/autosave**
> 退出时自动保存的设置、曲库状态和播放位置。

**~/.config/cmus/rc**
> cmus 启动时执行的启动命令（按键绑定、设置、颜色）。

# CAVEATS

基于终端，需要一个功能完善的终端模拟器。音频输出取决于可用的后端（ALSA、PulseAudio 等）。某些格式可能需要额外的编解码库。

# INSTALL

```apt: sudo apt install cmus```

```pacman: sudo pacman -S cmus```

```apk: sudo apk add cmus```

```zypper: sudo zypper install cmus```

```brew: brew install cmus```

```nix: nix profile install nixpkgs#cmus```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cmus-remote](/man/cmus-remote)(1), [ncmpcpp](/man/ncmpcpp)(1), [mpd](/man/mpd)(1)
