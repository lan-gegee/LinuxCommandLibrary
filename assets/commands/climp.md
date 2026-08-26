# TAGLINE

命令行界面音乐播放器

# TLDR

**播放**媒体文件

```climp --play [/path/to/song.mp3]```

**播放**网络电台流

```climp --play [http://example.com/stream]```

**创建**播放列表并开始播放

```climp --playlist [song1.mp3] [song2.mp3] --play```

向当前播放列表中**添加**文件

```climp --add [newsong.mp3] [myplaylist.m3u]```

将音量**设置**为 80

```climp --volume 80```

**定位**到 1 分 30 秒处

```climp --seek 1:30```

**显示**正在播放的曲目

```climp --current```

**退出**守护进程

```climp --quit```

# SYNOPSIS

**climp** **--**_cmd1_ [[_arg1_] ...] **--**_cmd2_ [[_arg1_] ...]

# PARAMETERS

**--play** [_args_]
> 开始播放。参数可以是媒体文件、.m3u/.txt 播放列表、URI 或播放列表索引（从 0 开始，支持负索引）。

**--add** [_files_]
> 将媒体文件或播放列表添加到当前播放列表。

**--playlist** [_args_]
> 不带参数：输出当前播放列表及其元数据。带参数：设置新的播放列表。

**--current**, **-c**
> 显示正在播放的曲目的位置、时长、标题、艺术家和专辑。

**--next**, **-n**
> 播放播放列表中的下一首曲目。

**--pause**
> 切换暂停/恢复。

**--stop**
> 停止播放。

**--volume** [_int_], **-v**
> 获取或设置音量级别。

**--seek** _time_
> 定位到指定位置。格式：m:ss、m.ss 或秒数。

**--speed** [_float_]
> 获取或设置播放速度。

**--pitch** [_float_]
> 获取或设置播放音调。

**--shuffle** [_bool_]
> 开启或关闭播放列表随机播放。

**--repeat** [_bool_]
> 开启或关闭播放列表循环。

**--mute** [_bool_], **-m**
> 切换静音，或直接设为开/关。

**--clear**
> 清空当前播放列表。

**--remove** [_indices_]
> 按索引从播放列表中移除曲目。

**--sort**
> 按文件路径的字母顺序对播放列表排序。

**--stdin**, **-i**
> 从 stdin 读取播放列表条目，便于管道使用。

**--quit**, **-q**
> 关闭 climpd 守护进程。

# DESCRIPTION

**climp** 是一个用 C 编写的轻量级终端音乐播放器，采用客户端-守护进程架构。**climp** 二进制文件是一个精简客户端，通过 Unix 域套接字向 **climpd** 发送命令；后者是后台守护进程，通过 GStreamer 处理实际的音频播放。发出命令时如果守护进程尚未运行，climp 会自动启动它。它支持本地媒体文件、网络流（网络电台）和播放列表管理（.m3u 和 .txt 格式）。

配套工具 **climp-discover** 可递归发现目录中的媒体文件，供管道传入 climp 使用。

# CONFIGURATION

配置存储在 **~/.config/climp/climpd.conf**。播放列表存储在 **~/.config/climp/playlists/**。设置项包括音量、音调、速度、循环、随机播放、列宽，以及是否在退出时保存更改。

# CAVEATS

不能以 root 身份运行。需要 GStreamer 及其插件以支持各种编解码器。该项目自 2016 年起未再更新。构建时需要作者自定义的 **libvci** 库。首次显示播放列表时解析元数据可能较慢。

# HISTORY

**climp** 由 **Steffen Nuessl** 于 **2014 年 2 月**创建。用 C 编写，基于 GPL-3.0 授权。该仓库累计 153 次提交，最后一次活跃大约在 2016 年 1 月。在 Arch Linux 和 Debian Jessie 上开发与测试。

# SEE ALSO

[cmus](/man/cmus)(1), [moc](/man/moc)(1), [mpd](/man/mpd)(1), [mpc](/man/mpc)(1), [mpv](/man/mpv)(1)
