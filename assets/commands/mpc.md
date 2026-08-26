# TAGLINE

MPD 的命令行客户端

# TLDR

**显示当前歌曲**

```mpc```

**播放/暂停切换**

```mpc toggle```

**下一曲**

```mpc next```

**上一曲**

```mpc prev```

**向播放列表添加文件**

```mpc add [path/to/song.mp3]```

**清空播放列表**

```mpc clear```

**设置音量**

```mpc volume [80]```

**更新数据库**

```mpc update```

**在当前歌曲内跳转**

```mpc seek [+10]```

**切换重复模式**

```mpc repeat```

# SYNOPSIS

**mpc** [_options_] [_command_] [_arguments_]

# PARAMETERS

**-f**, **--format** _FORMAT_
> 使用元数据定界符配置歌曲显示格式，如 %artist%、%album%、%title%、%track%、%time%、%file%。

**-h**, **--host** _HOST_
> 要连接的主机。认证可用 password@host 形式。绝对路径表示通过 Unix Domain Socket 连接。

**-p**, **--port** _PORT_
> 要连接的端口（默认：MPD_PORT 环境变量或 6600）。

**-q**, **--quiet**, **--no-status**
> 命令执行后不显示当前歌曲状态。

**-v**, **--verbose**
> 详细输出。

**--wait**
> 等待操作完成（例如数据库更新）。

# COMMANDS

**play** [_position_]
> 开始播放，可选从播放列表的某个位置开始。

**pause**
> 暂停播放。

**toggle**
> 切换播放/暂停。

**stop**
> 停止播放。

**next**
> 跳到下一曲。

**prev**
> 回到上一曲。

**seek** _value_
> 在当前歌曲内跳转（如 +10、-5、50%）。

**volume** _LEVEL_
> 设置音量百分比（0-100），或相对调整（+5、-5）。

**repeat** [_on|off_]
> 切换或设置重复模式。

**random** [_on|off_]
> 切换或设置随机模式。

**shuffle**
> 打乱当前播放列表。

**crossfade** [_seconds_]
> 获取或设置歌曲间的淡入淡出（0 表示禁用）。

**add** _URI_
> 向播放列表添加歌曲。

**clear**
> 清空播放列表。

**playlist**
> 打印当前播放列表。

**search** _type_ _query_
> 在数据库中搜索歌曲。

**update** [_path_]
> 扫描音乐目录中的更新文件。

**status**
> 显示当前播放状态。

# DESCRIPTION

**mpc** 是 MPD（Music Player Daemon，音乐播放守护进程）的命令行客户端。它连接到正在运行的 MPD 实例，根据传入的命令和参数控制播放、播放列表、音量和播放状态。

如果不指定命令，则打印当前状态（等同于 **mpc status**）。

# CAVEATS

需要有一个正在运行的 MPD 实例。该客户端本身不播放音频。连接参数默认为 localhost:6600，也可通过 MPD_HOST 和 MPD_PORT 环境变量设置。

# HISTORY

mpc 作为 Music Player Daemon 项目的参考**命令行客户端**而创建。

# INSTALL

```apt: sudo apt install mpc```

```dnf: sudo dnf install mpc```

```pacman: sudo pacman -S mpc```

```apk: sudo apk add mpc```

```brew: brew install mpc```

```nix: nix profile install nixpkgs#mpc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mpd](/man/mpd)(1), [ncmpcpp](/man/ncmpcpp)(1), [mpv](/man/mpv)(1)
