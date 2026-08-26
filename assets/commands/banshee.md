# TAGLINE

音乐播放器与媒体管理器

# TLDR

**启动** Banshee 音乐播放器

```banshee```

**播放**指定文件

```banshee [music.mp3]```

**导入**媒体

```banshee --import [/path/to/music]```

# SYNOPSIS

**banshee** [_options_] [_files_]

# DESCRIPTION

**banshee** 是一款跨平台音乐播放器与媒体管理应用。它支持音频和视频播放、媒体库管理、播客、网络电台，以及与便携式媒体设备同步。

该应用基于 Mono 和 GTK+ 构建，提供功能丰富的媒体体验。

# PARAMETERS

**--import** _path_
> 从目录导入媒体

**--play**
> 开始播放

**--pause**
> 暂停播放

**--next**
> 跳到下一曲

**--previous**
> 上一曲

**--volume** _level_
> 设置音量（0-100）

**--show-import-media**
> 显示导入对话框

# FEATURES

- 音乐库管理
- 智能播放列表
- 播客订阅
- 网络电台
- iPod/Android 同步
- 专辑封面
- Last.fm 记录（scrobbling）
- 扩展支持

# CAVEATS

开发已大幅放缓。许多发行版不再打包此软件。Mono 依赖可能体积较大。部分硬件同步功能可能无法使用。可以考虑 Rhythmbox 或 Clementine 等替代品。

# HISTORY

**Banshee** 由 Aaron Bockover 于 **2005** 年创建，曾连续数年担任 GNOME 的默认音乐播放器，后被 GNOME Music 取代。

# SEE ALSO

[clementine](/man/clementine)(1), [audacious](/man/audacious)(1)
