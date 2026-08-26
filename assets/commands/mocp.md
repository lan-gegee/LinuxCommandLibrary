# TAGLINE

基于控制台、带 ncurses 界面的音频播放器

# TLDR

**启动** MOC 终端界面

```mocp```

在**指定目录**中启动 MOC

```mocp [path/to/directory]```

**在后台启动服务器**而不显示界面

```mocp -S```

在后台把**歌曲加入播放队列**

```mocp -q [path/to/audio_file]```

**递归地把歌曲加入**播放队列

```mocp -a [path/to/directory]```

**清空**播放队列

```mocp -c```

**播放或停止**当前歌曲

```mocp --play```
```mocp --stop```

**停止服务器**

```mocp -x```

# SYNOPSIS

**mocp** [**-S**] [**-x**] [**-p**] [**-s**] [**-q**] [**-a**] [**-c**] [**-f**] [**-r**] [_file_|_dir_...]

# PARAMETERS

**-S, --server**
> 只在后台运行服务器并退出

**-F, --foreground**
> 在前台运行服务器并将日志输出到 stdout

**-x, --exit**
> 关闭 MOC 服务器

**-p, --play**
> 从播放列表第一项开始播放

**-s, --stop**
> 停止播放

**-P, --pause**
> 暂停播放

**-U, --unpause**
> 从暂停中恢复

**-G, --toggle-pause**
> 在播放和暂停状态之间切换

**-f, --next**
> 播放下一首

**-r, --previous**
> 播放上一首

**-q, --enqueue**
> 将文件加入队列，不启动界面

**-a, --append**
> 追加文件、目录或播放列表

**-c, --clear**
> 清空播放列表

**-k _N_, --seek _N_**
> 向前/向后跳转 N 秒（使用 +/- 前缀）

**-v _N_, --volume _N_**
> 设置或调整混音器音量

**-i, --info**
> 显示当前正在播放文件的信息

**-T _theme_, --theme**
> 加载指定的主题文件

**-C _file_, --config**
> 使用备用配置文件

**-m, --music-dir**
> 从配置的 MusicDir 启动

# DESCRIPTION

**MOC**（Music On Console）是一个基于控制台、带 ncurses 界面的音频播放器。它通过各种解码器插件支持 OGG、WAV、MP3、FLAC 等音频格式。

播放器采用客户端-服务器架构：服务器负责播放，客户端提供界面。这样即使关闭界面，音乐也能继续播放。用方向键浏览目录，按 Enter 播放文件。

# CAVEATS

如果服务器已在运行，影响服务器行为的命令行选项（如 --sound-driver）会被静默忽略。必须重启服务器才能应用这些更改。配置保存在 ~/.moc/ 目录中。

# HISTORY

**MOC** 最初由 **Damian Pietras** 开发。该项目为图形化音乐播放器提供了一个轻量的终端替代方案，遵循把一件事做好的 Unix 哲学。

# INSTALL

```apt: sudo apt install moc```

```zypper: sudo zypper install moc```

```brew: brew install moc```

```nix: nix profile install nixpkgs#moc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cmus](/man/cmus)(1), [mpd](/man/mpd)(1), [ncmpcpp](/man/ncmpcpp)(1)
